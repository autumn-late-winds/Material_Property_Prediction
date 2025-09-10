import pandas as pd

# 仅用于管线联调的小样本（非权威数值），列名：smiles, logS
rows = [
    {"smiles": "CCO",          "logS": -0.3},   # ethanol
    {"smiles": "c1ccccc1",     "logS": -2.1},   # benzene
    {"smiles": "Cc1ccccc1",    "logS": -2.5},   # toluene
    {"smiles": "CC(=O)O",      "logS":  0.3},   # acetic acid
    {"smiles": "Oc1ccccc1",    "logS": -1.5},   # phenol
    {"smiles": "O=C(O)C(O)C(O)CO", "logS": 0.6},# glyceric acid (示意)
    {"smiles": "COC(=O)C1=CC=CC=C1C(=O)O", "logS": -1.8},  # aspirin
    {"smiles": "Cn1cnc2n(C)c(=O)n(C)c(=O)c12", "logS": -0.8}, # caffeine
    {"smiles": "CC(=O)NC1=CC=C(O)C=C1", "logS": -1.2},      # acetanilide
    {"smiles": "CCN(CC)CC",    "logS":  0.2}    # triethylamine
]
df = pd.DataFrame(rows, columns=["smiles", "logS"])
df.to_csv("data/sample/esol_small.csv", index=False)
print("Wrote data/sample/esol_small.csv with", len(df), "rows")
