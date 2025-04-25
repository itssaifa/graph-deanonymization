import networkx as nx
import numpy as np
from scipy.spatial.distance import cosine
from gensim.models import Word2Vec

def generate_embeddings(G, dimensions=32):
    walks = []
    for _ in range(5):  # Fewer walks for speed
        for node in G.nodes():
            walk = [str(node)]  # Store nodes as strings in the walk
            for _ in range(10):
                try:
                    # Convert back to int for neighbor lookup, then to string for walk
                    neighbors = list(G.neighbors(int(walk[-1])))
                    if neighbors:
                        walk.append(str(np.random.choice(neighbors)))
                except (ValueError, KeyError):
                    break  # Skip if node conversion fails or node doesn't exist
            walks.append(walk)
    model = Word2Vec(walks, vector_size=dimensions, window=3, min_count=1)
    return {node: model.wv[str(node)] for node in G.nodes()}

def match_nodes(G1, G2):
    emb1 = generate_embeddings(G1)
    emb2 = generate_embeddings(G2)
    
    matches = {}
    for u in G1.nodes():
        best_match = None
        min_dist = float('inf')
        for v in G2.nodes():
            if v not in matches.values():
                dist = cosine(emb1[u], emb2[v])
                if dist < min_dist:
                    min_dist = dist
                    best_match = v
        if best_match:
            matches[u] = best_match
    return matches

if __name__ == "__main__":
    # Explicitly specify graph type and node type
    G1 = nx.read_edgelist("data/unseed_G1.edgelist", nodetype=int, create_using=nx.Graph())
    G2 = nx.read_edgelist("data/unseed_G2.edgelist", nodetype=int, create_using=nx.Graph())
    
    mappings = match_nodes(G1, G2)
    
    with open("results/LastnameSeedfree.txt", "w") as f:
        for g1, g2 in mappings.items():
            f.write(f"{g1} {g2}\n")