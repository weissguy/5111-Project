import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
import kallisto
import pubchempy
import jazzy
from jazzy.api import atomic_map_from_smiles
from jazzy.api import deltag_from_smiles
from jazzy.api import molecular_vector_from_smiles
from rdkit.Chem import Descriptors


def create_atomic_map(chem_name):
    smiles = pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles
    return atomic_map_from_smiles(smiles)

def gibbs(chem_name):
    smiles = pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles
    return deltag_from_smiles(smiles)

def create_molecular_map(chem_name):
    smiles = pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles
    return molecular_vector_from_smiles(smiles)

def create_useful_dict(chem_name):
    mol_map = create_molecular_map(chem_name)
    useful_dict = {}
    useful_dict["mass"] = Descriptors.MolWt(Chem.MolFromSmiles(pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles))
    useful_dict["gibbs"] = gibbs(chem_name)
    useful_dict["acceptor_strength"] = mol_map["sa"]
    useful_dict["donor_strength"] = mol_map["sdc"] + mol_map["sdx"]
    return useful_dict

# molecule = input("type molecule nameejfijflsjfkl ")
# print(create_useful_dict(molecule))
        

# chem_name = input("TYPE YOUR CHEMICAL!! ")
# print(create_molecular_map(chem_name))

# chem_name = input("Chemical name: ").lower()

# smiles = pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles

# print(atomic_map_from_smiles(smiles))
# atomic_tuples = atomic_tuples_from_smiles(glucose_smiles)
# print(atomic_tuples)