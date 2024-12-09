import pymol
from pymol import cmd
import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
import pubchempy
from pymol import preset
import imageio


# pymol.finish_launching(['pymol', '-q'])

# # molecule_name = input("input molecule name")
# smiles = pubchempy.("Glucose", "name")
# print(smiles)
# mol = Chem.MolFromSmiles
preset.ball_and_stick(selection='all', mode=1)

cmd.load("carbondioxide.mol", "co2")
cmd.show("sticks")
cmd.set("stick_ball", 1)
cmd.set("stick_ball_ratio", 1.5)
cmd.zoom()           
cmd.png("co2real.png")
