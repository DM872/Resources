#-----------------------------------------------------------------------------------------------------------------------
import networkx as nx
#-----------------------------------------------------------------------------------------------------------------------
def main():
    # directed graphs
    G = nx.DiGraph()
    G.add_edge("0", "A", capacity=4)
    G.add_edge("A", "D", capacity=3)
    G.add_edge("0", "B", capacity=7)
    G.add_edge("A", "B", capacity=1)
    G.add_edge("B", "D", capacity=4)
    G.add_edge("B", "E", capacity=4)
    G.add_edge("0", "C", capacity=3)
    G.add_edge("C", "E", capacity=4)
    G.add_edge("E", "D", capacity=1)
    G.add_edge("D", "T", capacity=8)
    G.add_edge("E", "T", capacity=6)
    cut_value, partition = nx.minimum_cut(G, "0", "T")
    reachable, non_reachable = partition
    print(cut_value, reachable, non_reachable)

    max_flow, flow_dict = nx.maximum_flow(G, "0", "T")
    print(max_flow)
    print(flow_dict)

    # undirected graphs
    G = nx.Graph()
    G.add_edge("0", "A", capacity=4)
    G.add_edge("A", "D", capacity=3)
    G.add_edge("0", "B", capacity=7)
    G.add_edge("A", "B", capacity=1)
    G.add_edge("B", "D", capacity=4)
    G.add_edge("B", "E", capacity=4)
    G.add_edge("0", "C", capacity=3)
    G.add_edge("C", "E", capacity=4)
    G.add_edge("E", "D", capacity=1)
    G.add_edge("D", "T", capacity=8)
    G.add_edge("E", "T", capacity=6)
    for tour in nx.connected_components(G):
        print(tour)
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
