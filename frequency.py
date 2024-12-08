from rdkit import Chem
from rdkit.Chem import AllChem
import pubchempy
import psi4
import csv



# input chemical name
#chem_names = [input("Chemical name: ").lower()]
chem_names = ['water', 'benzene']
#chem_names = ['water', 'benzene', 'boron trifluoride', 'dopamine']

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
    #pubchem_mol = Chem.MolFromSmiles(smiles)
    #mol_filepath = f"mol_files/{chem_name}.mol"
    #Chem.MolToMolFile(pubchem_mol, mol_filepath)


    xyz = smiles_to_xyz(smiles)

    # configure psi4 settings
    psi4.set_options({
        'basis': '6-31G(d)',   # Basis set
        'scf_type': 'df',      # Density fitting to speed up calculations
        'reference': 'rhf'    # Restricted Hartree-Fock for closed-shell systems
    })


    # create psi4 molecule object
    psi4_mol = psi4.geometry(f"""
                            symmetry c1
                            {xyz}
                            """)
    psi4.optimize('scf/6-31G(d)', molecule=psi4_mol)

    # analyze vibrational energy
    energy, wfn = psi4.driver.frequency("scf/6-31G(d)", molecule=psi4_mol, return_wfn=True, NORMAL_MODES_WRITE=True)
    freq = wfn.frequencies().get(0,0)

    data.append({'molecule': chem_name, 'energy': energy, 'frequency': freq})



#molden_filepath = f'/molden/{chem_name}.molden'
#psi4.molden(psi4_mol, molden_filepath)


with open('data.csv', 'w', newline='') as file:
    cols = ['molecule', 'energy', 'frequency']
    writer = csv.DictWriter(file, fieldnames=cols)
    writer.writeheader()
    writer.writerows(data)
