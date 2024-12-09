from notjazzy import *
import pretty_midi

mol_name = input("enter molecule name:")
for atom in create_atomic_map(mol_name):
    ##map z number to name/letter in a dictionary??

molecule = pretty_midi.PrettyMIDI()
molecule_instr = pretty_midi.Instrument(program = 4)
print(pretty_midi.hz_to_note_number(440))
a_note = pretty_midi.Note(velocity = 10, pitch = int(pretty_midi.hz_to_note_number(440)), start =0, end=1)
molecule_instr.notes.append(a_note)
molecule.instruments.append(molecule_instr)
molecule.write("sonification/mid_files/instr4.mid")