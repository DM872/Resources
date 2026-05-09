
import sys
import json
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------
BUNKER_PRICE = 500          # USD per metric ton of bunker fuel
INSTANCE = sys.argv[1] if len(sys.argv) > 1 else "Baltic"

# ---------------------------------------------------------------------------
# Load distilled data
# ---------------------------------------------------------------------------
data_file = Path(__file__).parent / f"distilled_{INSTANCE}.json"
if not data_file.exists():
    sys.exit(f"File not found: {data_file}\nRun: python build_data.py {INSTANCE}")

with open(data_file) as f:
    raw = json.load(f)

nodes   = set(raw["nodes"])
vessels = raw["vessels"]   # cls -> {capacity, design_speed, bunker_per_day, tc_rate_daily}
ports   = raw["ports"]     # code -> {cost_load, cost_transship}

# Restore tuple keys from "A,B" strings
arcs        = {tuple(k.split(",")): v for k, v in raw["arcs"].items()}
demands = {tuple(k.split(",")): v for k, v in raw["demands"].items()}

# ---------------------------------------------------------------------------
# Arc transit cost per FFE and capacity
# Uses cheapest feasible vessel for cost, largest for capacity.
# ---------------------------------------------------------------------------

def transit_cost_per_ffe(arc_info):
    best = float("inf")
    for cls in arc_info["feasible_vessels"]:
        v = vessels[cls]
        days = arc_info["distance"] / (v["design_speed"] * 24)
        c = (v["bunker_per_day"] * BUNKER_PRICE + v["tc_rate_daily"]) * days / v["capacity"]
        best = min(best, c)
    return best if best < float("inf") else 0.0


transit = {(i, j): transit_cost_per_ffe(info) for (i, j), info in arcs.items()}
cap     = {
    (i, j): max((vessels[cls]["capacity"] for cls in info["feasible_vessels"]), default=0)
    for (i, j), info in arcs.items()
}

real_arcs = [(i, j) for (i, j) in arcs if cap[i, j] > 0]

# Adjacency lists 
out_arcs = defaultdict(list)
in_arcs  = defaultdict(list)
for (i, j) in real_arcs:
    out_arcs[i].append((i, j))
    in_arcs[j].append((i, j))

# ---------------------------------------------------------------------------
# Port handling costs (per FFE), falling back to 0 for NULL
# ---------------------------------------------------------------------------

def load_cost(port):
    v = ports.get(port, {}).get("cost_load")
    return v if v is not None else 0.0


def transship_cost(port):
    v = ports.get(port, {}).get("cost_transship")
    return v if v is not None else 0.0


def arc_cost(o, d, i, j):
    c = transit[i, j]
    if i == o:
        c += load_cost(i)
    elif i != d:
        c += transship_cost(i)
    if j == d:
        c += load_cost(j)
    return c


# ---------------------------------------------------------------------------
# Build your model
# ---------------------------------------------------------------------------
