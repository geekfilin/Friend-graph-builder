import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
from collections import defaultdict

class SocialGraph:
    def __init__(self):
        self.graph = nx.Graph()
        self.user_map = {}
    
    def add_connections(self, connections, edge_threshold=3):
        main_user_id = connections['user_id']
        self.user_map[main_user_id] = connections['username']
        self.graph.add_node(main_user_id, label=connections['username'], type='main')
        
        connections_map = defaultdict(int)
        
        for follower in connections['followers']:
            follower_id = follower['id']
            self.user_map[follower_id] = follower['username']
            connections_map[follower_id] += 1
        
        for friend in connections['friends']:
            friend_id = friend['id']
            self.user_map[friend_id] = friend['username']
            connections_map[friend_id] += 1
        
        for user_id, weight in connections_map.items():
            if weight >= edge_threshold:
                self.graph.add_node(user_id, label=self.user_map[user_id], type='connection')
                self.graph.add_edge(main_user_id, user_id, weight=weight)
    
    def detect_communities(self):
        partition = community_louvain.best_partition(self.graph)
        for node, comm_id in partition.items():
            self.graph.nodes[node]['community'] = comm_id
        return partition
    
    def export_gexf(self, filename):
        nx.write_gexf(self.graph, filename)
    
    def visualize(self):
        plt.figure(figsize=(24, 16))
        pos = nx.spring_layout(self.graph, k=0.5)
        communities = self.detect_communities()
        
        nx.draw_networkx_nodes(
            self.graph, pos,
            node_size=120,
            node_color=list(communities.values()),
            cmap=plt.cm.tab20
        )
        
        nx.draw_networkx_edges(
            self.graph, pos,
            alpha=0.3,
            width=[d['weight']*0.3 for _,_,d in self.graph.edges(data=True)]
        )
        
        nx.draw_networkx_labels(
            self.graph, pos,
            labels={n: d['label'] for n,d in self.graph.nodes(data=True) if d['type']=='main'},
            font_size=14,
            font_weight='bold'
        )
        
        plt.axis('off')
        plt.savefig(f"{filename.split('.')[0]}.png", dpi=300, bbox_inches='tight')

def build_graph(connections, max_users=500, edge_threshold=3):
    graph = SocialGraph()
    graph.add_connections(connections, edge_threshold)
    return graph