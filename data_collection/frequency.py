from rdkit import Chem
from rdkit.Chem import AllChem
import pubchempy
import psi4
import re
import csv
import os


chem_names = ['water', 'benzene', 'boron trifluoride', 'dopamine']

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

    atom_names = re.findall(r'^[A-Za-z]+', xyz, re.MULTILINE)
    n_atoms = len(atom_names)

    # configure psi4 settings
    psi4.set_options({
        'basis': '6-31G(d)',   # Basis set
        'scf_type': 'df',      # Density fitting to speed up calculations
        'guess': 'sad',
        'reference': 'rhf',   # Restricted Hartree-Fock for closed-shell systems
        'maxiter': 200,
        'print': 0
    })

    psi4.core.set_output_file('psi4_output.log') # or 'nul'

    # create psi4 molecule object
    psi4_mol = psi4.geometry(f"""
                            symmetry c1
                            {xyz}
                            """)

    energy, opt_wfn = psi4.optimize('scf/6-31G(d)', molecule=psi4_mol, return_wfn = True)

    # analyze vibrational energy
    energy, wfn = psi4.frequency('scf/6-31G(d)', molecule=psi4_mol, return_wfn = True)
    frequencies = wfn.frequencies().to_array() # in cm^-1

    for i, freq in enumerate(frequencies):
        atom = atom_names[i]
        data.append({'atom': atom, 'frequency': freq})

    with open(f'{chem_name}.csv', 'w', newline='') as file:
        cols = ['atom', 'frequency']
        writer = csv.DictWriter(file, fieldnames=cols)
        writer.writeheader()
        writer.writerows(data)


    #molden_filepath = f'/molden/{chem_name}.molden'
    #molden_filepath = f'{chem_name}.molden'
    molden_filepath = os.path.join(os.getcwd(), f'{chem_name}.molden')
    #psi4.molden(wfn, molden_filepath)
    wfn.write_molden(molden_filepath, use_natural = True)
