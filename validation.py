inferred = {}
with open('inferred_mapping.txt', 'r') as f:
    for line in f:
        g1, g2 = line.strip().split()
        inferred[g1] = g2

ground_truth = {}
with open('validation_seed_mapping.txt', 'r') as f:
    for line in f:
        g1, g2 = line.strip().split()
        ground_truth[g1] = g2

correct = 0
total = 0

for g1_node, g2_node in inferred.items():
    if g1_node in ground_truth:
        total += 1
        if ground_truth[g1_node] == g2_node:
            correct += 1

accuracy = correct / total if total else 0

print(f"Validation accuracy: {accuracy:.4f} ({correct}/{total} correct matches)")
