from rdkit import Chem
from rdkit.Chem import AllChem
import pubchempy
import psi4
import numpy as np
import csv


chem_names = ['water', 'hydrogen', 'carbon dioxide', 'ethene']

atomic_nums = {'H': 1, 'C': 6, 'O': 8}

c = 2.99792458e10

# convert to xyz
def smiles_to_xyz(smiles):
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)  # Add hydrogens
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())  # 3D conformation
    AllChem.UFFOptimizeMolecule(mol)  # Geometry optimization
    atoms = mol.GetAtoms()
    conformer = mol.GetConformer()
    xyz = ""
    for i, atom in enumerate(atoms):
        pos = conformer.GetAtomPosition(i)
        xyz += f"{atom.GetSymbol()} {pos.x:.6f} {pos.y:.6f} {pos.z:.6f}\n"
    return xyz


data = []

for chem_name in chem_names:

    # get smiles id
    smiles = pubchempy.get_compounds(chem_name, "name")[0].isomeric_smiles

    # convert to mol
    pubchem_mol = Chem.MolFromSmiles(smiles)
    mol_filepath = f"mol_files/{chem_name}.mol"
    Chem.MolToMolFile(pubchem_mol, mol_filepath)

    # convert to xyz
    xyz = smiles_to_xyz(smiles)

    # configure psi4 settings
    psi4.set_options({
        'basis': '6-31G(d)',   # Basis set
        'scf_type': 'df',      # Density fitting to speed up calculations
        'guess': 'sad',
        'reference': 'rhf',   # Restricted Hartree-Fock for closed-shell systems
        'maxiter': 200,
        'print': 0
    })

    psi4.core.set_output_file('nul')

    # create psi4 molecule object
    psi4_mol = psi4.geometry(f"""
                            symmetry c1
                            {xyz}
                            """)

    energy, opt_wfn = psi4.optimize('scf/6-31G(d)', molecule=psi4_mol, return_wfn = True)

    # analyze vibrational energy
    energy, wfn = psi4.frequency('scf/6-31G(d)', molecule=psi4_mol, return_wfn = True)
    frequencies = wfn.frequencies().to_array() # in cm^-1
    #frequencies *= c # in Hz
    frequencies = frequencies.tolist()

    print(frequencies)

    data.append({'molecule': chem_name, 'frequencies': frequencies})


with open('data.csv', 'w', newline='') as file:
    cols = ['molecule', 'frequencies']
    writer = csv.DictWriter(file, fieldnames=cols)
    writer.writeheader()
    writer.writerows(data)
