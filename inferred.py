import networkx as nx
import math

G1 = nx.read_edgelist('validation_G1.edgelist')
G2 = nx.read_edgelist('validation_G2.edgelist')

seed_mapping = {}
with open('seed_mapping.txt', 'r') as f:
    for line in f:
        g1_node, g2_node = line.strip().split()
        seed_mapping[g1_node] = g2_node

g1_seeded = set(seed_mapping.keys())
g2_seeded = set(seed_mapping.values())
g1_unseeded = [node for node in G1.nodes if node not in g1_seeded]
g2_unseeded = [node for node in G2.nodes if node not in g2_seeded]

def compute_similarity(g1_node, g2_node):
    g1_neighbors = set(G1.neighbors(g1_node))
    g2_neighbors = set(G2.neighbors(g2_node))
    mapped_neighbors = {seed_mapping[n] for n in g1_neighbors if n in seed_mapping}
    common = mapped_neighbors & g2_neighbors
    if not mapped_neighbors or not g2_neighbors:
        return 0
    return len(common) / math.sqrt(len(mapped_neighbors) * len(g2_neighbors))

new_mapping = {}
used_g2_nodes = set()

for g1_node in g1_unseeded:
    best_score = -1
    best_match = None
    for g2_node in g2_unseeded:
        if g2_node in used_g2_nodes:
            continue
        score = compute_similarity(g1_node, g2_node)
        if score > best_score:
            best_score = score
            best_match = g2_node
    if best_match:
        new_mapping[g1_node] = best_match
        used_g2_nodes.add(best_match)

full_mapping = {**seed_mapping, **new_mapping}

with open('inferred_mapping.txt', 'w') as f:
    for g1_node, g2_node in full_mapping.items():
        f.write(f"{g1_node} {g2_node}\n")

print(f"Seed pairs: {len(seed_mapping)}")
print(f"New inferred pairs: {len(new_mapping)}")
print(f"Total mapping saved to inferred_mapping.txt")
