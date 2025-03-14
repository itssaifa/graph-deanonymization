# Graph De-Anonymization
🔍 Seed-Based and Seed-Free Node Matching in Graphs

# Overview
This project focuses on graph de-anonymization, where nodes from two similar graphs are matched based on structure. The project includes:
- Seed-Based De-Anonymization: Using known seed node pairs to infer mappings.
- Seed-Free De-Anonymization: Matching nodes based purely on graph features.

# Installation
```bash
git clone https://github.com/itssaifa/graph-deanonymization.git
cd graph-deanonymization
pip install networkx
```

# Usage
Run Seed-Based De-Anonymization
```bash
python src/deanonymization.py --seeded
```

Run Seed-Free De-Anonymization
```bash
python src/deanonymization.py --seed-free
```

Run Both Methods
```bash
python src/deanonymization.py --all
```
