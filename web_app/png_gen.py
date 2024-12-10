# import pymol
# from pymol import cmd
# import rdkit
# from rdkit import Chem
# from rdkit.Chem import Draw
# import pubchempy
# from pymol import preset
# import imageio
# import pubchempy as pcp
# import allchem

from rdkit import Chem
from rdkit.Chem import AllChem
import pubchempy as pcp
import os

# TO GENERATE A PNG:
# just run this file and type in the molecule name!

# Import PyMOL (ensure PyMOL is installed and configured)
from pymol import cmd

# molecule_name = input("Input molecule name: ")

# Fetch SMILES from PubChem
def create_visualisation(molecule_name):
    compound = pcp.get_compounds(molecule_name, 'name')
    if not compound:
        print(f"Compound '{molecule_name}' not found.")
        exit()

    # Get the first result's SMILES
    smiles = compound[0].canonical_smiles
    print(f"SMILES for {molecule_name}: {smiles}")

    # Generate RDKit molecule object
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)  # Add hydrogens
    AllChem.EmbedMolecule(mol)  # Generate 3D coordinates
    AllChem.UFFOptimizeMolecule(mol)  # Optimize structure

    # Save as an SDF file for PyMOL
    sdf_file = f"{molecule_name}.sdf"
    with Chem.SDWriter(sdf_file) as writer:
        writer.write(mol)

    # Visualize in PyMOL
    cmd.load(sdf_file, molecule_name)
    cmd.show("sticks")
    cmd.set("stick_ball", 1)
    cmd.set("stick_ball_ratio", 2)
    cmd.zoom()

    # Save an image
    output_image = f"visualization/png_files/{molecule_name}.png"
    cmd.png(output_image)

    print(f"Visualization saved to {output_image}")

    # Cleanup
    os.remove(sdf_file)


# pymol.finish_launching(['pymol', '-q'])

# # molecule_name = input("input molecule name")
# smiles = pubchempy.("Glucose", "name")
# print(smiles)
# mol = Chem.MolFromSmiles
# preset.ball_and_stick(selection='all', mode=1)

# cmd.load("carbondioxide.mol", "co2")
# cmd.show("sticks")
# cmd.set("stick_ball", 1)
# cmd.set("stick_ball_ratio", 1.5)
# cmd.zoom()           
# cmd.png("co2real.png")
