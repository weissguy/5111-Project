import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
import kallisto
import pubchempy
import jazzy
from jazzy.api import atomic_map_from_smiles
from jazzy.api import deltag_from_smiles

def create_atomic_map(chem_name):
    smiles = pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles
    return atomic_map_from_smiles(smiles)

def gibbs(chem_name):
    smiles = pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles
    return deltag_from_smiles(smiles)

# chem_name = input("Chemical name: ").lower()

# smiles = pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles

# print(atomic_map_from_smiles(smiles))
# atomic_tuples = atomic_tuples_from_smiles(glucose_smiles)
# print(atomic_tuples)