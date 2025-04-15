# pysmiles is a small package for reading and writing SMILES strings. Package is dependent on networkx.
# Molecules are depicted as networkx graphs.
# use environment pysmiles

from pysmiles import read_smiles

smiles = 'C1CC[13CH2]CC1C1CCCCC1'
mol = read_smiles(smiles)