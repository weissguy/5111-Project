from atomic_data import *
from miditoaudio import to_audio
import pretty_midi


mol_name = input("enter molecule name:")
def make_sound(mol_name):
    mol_sound = pretty_midi.PrettyMIDI()
    print("start")
    atomic_map = create_atomic_map(mol_name)
    print(atomic_map)
    for atom_dict in atomic_map:
        # getting all the properties
        atom_num = atom_dict["z"]
        vib_freq = 441
        partial_charge = atom_dict["eeq"]
        lone_pairs = atom_dict["num_lp"]
        donor_strength = atom_dict["sdx"] + atom_dict["sdc"]
        # mapping properties to sound
        molecule_instr = pretty_midi.Instrument(program = atom_num)
        atom_note = pretty_midi.Note(velocity = 100, pitch = int(pretty_midi.hz_to_note_number(vib_freq)), start =0, end=lone_pairs)
        # adding sound to molecule (lowkey need to fix this)
        molecule_instr.notes.append(atom_note)
        mol_sound.instruments.append(molecule_instr)
    print(gibbs(mol_name))

    mol_sound.write(f"web_app/sonification/mid_files/{mol_name}.mid")
    print("done")
    to_audio("web_app/sonification/allinone.sf2", f"web_app/sonification/mid_files/{mol_name}.mid", "web_app/sonification/wav_files")

make_sound(mol_name)