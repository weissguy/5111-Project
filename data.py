from rdkit import Chem
import pubchempy


# input chemical name
chem_name = input("Chemical name: ").lower()

# convert to mol
smiles = pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles
mol = Chem.MolFromSmiles(smiles)

# export
Chem.MolToMolFile(mol, f'mol_files/{chem_name}.mol')
