from atomic_data import *
from miditoaudio import to_audio
import pretty_midi
import csv
from pydub import AudioSegment
from pydub.scipy_effects import low_pass_filter
from pydub.scipy_effects import high_pass_filter
import ast

with open(f"data_collection/data.csv", newline='') as f:
    reader = csv.reader(f)
    freq_dict = {}
    i = 0
    for row in reader:
        if i > 0:
            string_list = row[1]
            actual_list = ast.literal_eval(string_list)
            freq_dict[row[0]] = actual_list
        i += 1

def calc_filter(val, str):
    if str == "low":
        return 10000 - 2500*val
    elif str == "high":
        return 100 + 300*val

mol_name = input("enter molecule name:")
index = int(input("type your index!!!!!!! "))
def make_sound(mol_name, index):
    # getting the frequency
    frequencies = freq_dict[mol_name]
    print(frequencies)
    vib_freq = frequencies[index]
    mol_sound = pretty_midi.PrettyMIDI()
    properties_map = create_useful_dict(mol_name)
    if properties_map["mass"] < 5:
        instr = 4
    elif properties_map["mass"] < 15:
        instr = 89
    elif properties_map["mass"] < 25:
        instr = 94
    else:
        instr = 95
    # mapping properties to sound
    molecule_instr = pretty_midi.Instrument(program = instr)
    atom_note = pretty_midi.Note(velocity = 100, pitch = int(pretty_midi.hz_to_note_number(vib_freq/17.72+178)), start =0, end=1)
    # adding sound to molecule (lowkey need to fix this)
    molecule_instr.notes.append(atom_note)
    mol_sound.instruments.append(molecule_instr)
    #converting the midi file to wav and saving it
    mol_sound.write(f"web_app/sonification/mid_files/{mol_name}_{index}.mid")
    to_audio("web_app/sonification/allinone.sf2", f"web_app/sonification/mid_files/{mol_name}_{index}.mid", "web_app/sonification/wav_files")

    #applying filters
    low_pass = calc_filter(properties_map["donor_strength"], "low")
    high_pass = calc_filter(properties_map["acceptor_strength"], "high")
    print("high", high_pass, "low", low_pass)
    sound = AudioSegment.from_file(f"web_app/sonification/wav_files/{mol_name}_{index}.wav")
    filtered_sound = low_pass_filter(sound, low_pass)  # Cutoff frequency in Hz
    filtered_sound = high_pass_filter(filtered_sound, high_pass)
    filtered_sound.export(f"web_app/sonification/mp3_files/{mol_name}_{index}.mp3", format="mp3") 
make_sound(mol_name, index)

# 1 - honkytonk
# 2 - fantasia
# 3 - metallic
# 4 - poly (rmove?)
# 5 - halo

# freq max = 4643
# freq min = 745
# 220-440
# / 17.72 + 178