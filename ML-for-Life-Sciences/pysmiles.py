# pysmiles is a small package for reading and writing SMILES strings. Package is dependent on networkx.
# Molecules are depicted as networkx graphs.
# use environment pysmiles

import networkx as nx
from pysmiles import read_smiles
from pysmiles import write_smiles, fill_valence

# READING SMILES
smiles = 'C1CC[13CH2]CC1C1CCCCC1'
mol = read_smiles(smiles)

# molecule is a networkx graph, so nodes are elements, bonds are edges
print(f"Elements (excluding hydrogen) in the molecule are: {mol.nodes(data='element')}")
print(f"Bonds in molecule are: {mol.nodes(data='hcount')}")

mol_with_H = read_smiles(smiles, explicit_hydrogen=True)
print(f"Elements (including hydrogen) in the molecule are: {mol_with_H.nodes(data='element')}")

# WRITING SMILES
mol2 = nx.Graph()
mol2.add_edges_from([(0,1), (1,2), (1,3), (3,4), (1,5), (3,6)])

for idx, ele in enumerate('CCCCOCO'):
    mol.nodes[idx]['element'] = ele
# set charge, hydrogen count, and bond type
mol2.nodes[4]['charge'] = -1
mol2.nodes[4]['hcount'] = 0
mol2.edges[3,6]['order'] = 2

print(write_smiles(mol))

fill_valence(mol2, respect_hcount = True)
print(write_smiles(mol2))