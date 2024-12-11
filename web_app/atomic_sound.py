from atomic_data import *
from miditoaudio import to_audio
import pretty_midi
import csv
from pydub import AudioSegment
from pydub.scipy_effects import low_pass_filter


mol_name = input("enter molecule name:")
def make_sound(mol_name, index):
    # getting the frequency
    scaling_factor = 1
    with open(f"{mol_name}.csv", newline='') as f:
        reader = csv.reader(f)
        freq_dict = {}
        for row in reader:
            freq_dict[row[1]] = row[2]
    mol_sound = pretty_midi.PrettyMIDI()
    properties_map = create_useful_dict(mol_name)
    # mapping properties to sound
    vib_freq = 440
    molecule_instr = pretty_midi.Instrument(program = 63)
    atom_note = pretty_midi.Note(velocity = 100, pitch = int(pretty_midi.hz_to_note_number(vib_freq)), start =0, end=1)
    # adding sound to molecule (lowkey need to fix this)
    note_2 = pretty_midi.Note(velocity = 100, pitch = 61, start =0, end=1)
    note_3 = pretty_midi.Note(velocity = 100, pitch = 64, start =0, end=1)
    molecule_instr.notes.extend([atom_note, note_2, note_3])
    mol_sound.instruments.append(molecule_instr)

    #converting the midi file to wav and saving it
    mol_sound.write(f"web_app/sonification/mid_files/{mol_name}_{index}.mid")
    to_audio("web_app/sonification/allinone.sf2", f"web_app/sonification/mid_files/{mol_name}_{index}.mid", "web_app/sonification/wav_files")

    # #applying filters
    # sound = AudioSegment.from_file(f"web_app/sonification/wav_files/{mol_name}_{index}.wav")
    # filtered_sound = low_pass_filter(sound, 5000)  # Cutoff frequency in Hz
    # filtered_sound.export(f"web_app/sonification/mp3_files/{mol_name}_{index}.mp3", format="mp3") 
make_sound(mol_name, 1)

