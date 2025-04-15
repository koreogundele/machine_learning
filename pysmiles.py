# pysmiles is a small package for reading and writing SMILES strings. Package is dependent on networkx.
# Molecules are depicted as networkx graphs.
# use environment pysmiles

from pysmiles import read_smiles

# READING SMILES
smiles = 'C1CC[13CH2]CC1C1CCCCC1'
mol = read_smiles(smiles)

# molecule is a networkx graph, so nodes are elements, bonds are edges
print(f"Elements (excluding hydrogen) in the molecule are: {mol.nodes(data='element')}")
print(f"Bonds in molecule are: {mol.nodes(data='hcount')}")

mol_with_H = read_smiles(smiles, explicit_hydrogen=True)
print(f"Elements (including hydrogen) in the molecule are: {mol_with_H.nodes(data='element')}")

# WRITING SMILES
