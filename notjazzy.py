import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
import kallisto
import pubchempy
import jazzy
from jazzy.api import atomic_map_from_smiles

chem_name = input("Chemical name: ").lower()

smiles = pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles

print(atomic_map_from_smiles(smiles))
# atomic_tuples = atomic_tuples_from_smiles(glucose_smiles)
# print(atomic_tuples)