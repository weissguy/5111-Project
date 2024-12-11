import pretty_midi

import numpy as np

import pydub
from midi2audio import FluidSynth
from pydub import AudioSegment
import itertools

import os
import os, sys, getopt, glob, random, re, subprocess
    
def is_fsynth_installed():
    """ Check to make sure fluidsynth exists in the PATH """
    for path in os.environ['PATH'].split(os.pathsep):
        f = os.path.join(path, 'fluidsynth')
        if os.path.exists(f) and os.access(f, os.X_OK):
            return True
        
    return False

print(is_fsynth_installed())

def to_audio(sf2, midi_file, out_dir, out_type='wav', txt_file=None, append=True):
    """ 
    Convert a single midi file to an audio file.  If a text file is specified,
    the first line of text in the file will be used in the name of the output
    audio file.  For example, with a MIDI file named '01.mid' and a text file
    with 'A    major', the output audio file would be 'A_major_01.wav'.  If
    append is false, the output name will just use the text (e.g. 'A_major.wav')
    
    Args:
        sf2 (str):        the file path for a .sf2 soundfont file
        midi_file (str):  the file path for the .mid midi file to convert
        out_dir (str):    the directory path for where to write the audio out
        out_type (str):   the output audio type (see 'fluidsynth -T help' for options)
        txt_file (str):   optional text file with additional information of how to name 
                          the output file
        append (bool):    whether or not to append the optional text to the original
                          .mid file name or replace it
    """
    fbase = os.path.splitext(os.path.basename(midi_file))[0]
    if not txt_file:
        out_file = out_dir + '/' + fbase + '.' + out_type
    else:
        line = 'out'
        with open(txt_file, 'r') as f:
            line = re.sub(r'\s', '_', f.readline().strip())
            
        if append:
            out_file = out_dir + '/' + line + '_' + fbase + '.' + out_type
        else:
            out_file = out_dir + '/' + line + '.' + out_type

    subprocess.call(['fluidsynth', '-T', out_type, '-F', out_file, '-ni', sf2, midi_file])

# import IPython.display
# import matplotlib.pyplot as plt
# import numpy as np
# import pretty_midi
# from pymixer.project import MidiTrackSpec, Project
# from pymixer.sound_makers import FluidsynthSoundMaker
# from sinethesizer.synth.core import Event
# from sinethesizer.effects.reverb import apply_room_reverb
# from sinethesizer.effects.stereo import apply_stereo_to_mono_conversion
# from sinethesizer.io.events_to_wav import write_timeline_to_wav

# from fluidsynth import Synth

# synth = Synth()
# synth.start(driver="file")  # Output to file instead of audio device

# # Load a SoundFont
# sfid = synth.sfload("creativelabs.sf2")
# synth.program_select(0, sfid, 0, 0)

# # Render MIDI file to WAV
# synth.midi_file_to_audio("piano.mid", "output.wav")

# # Clean up
# synth.delete()

# def play_frequency(frequency, duration, velocity=100, instrument=0):
#     """Plays a frequency on MIDI using pitch bends."""

#     # Create a PrettyMIDI object
#     midi = pretty_midi.PrettyMIDI()
#     instrument = pretty_midi.Instrument(program=instrument)

#     # Calculate the MIDI note number closest to the desired frequency
#     note_number = int(round(pretty_midi.hz_to_note_number(frequency)))

#     # Add the note to the instrument
#     note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=0, end=duration)
#     instrument.notes.append(note)

#     # Calculate the pitch bend required to match the exact frequency
#     pitch_bend = int(8192 * (frequency - pretty_midi.note_number_to_hz(note_number)) /
#                       (pretty_midi.note_number_to_hz(note_number + 0.5) -
#                        pretty_midi.note_number_to_hz(note_number - 0.5)))

#     # Add the pitch bend to the instrument
#     instrument.pitch_bends.append(pretty_midi.PitchBend(pitch=pitch_bend, time=0))

#     # Add the instrument to the MIDI object
#     midi.instruments.append(instrument)

#     # Write the MIDI file
#     midi.write('frequency.mid')

# # Example usage
# play_frequency(440, 2)  # Play 440 Hz for 2 seconds


# # Create a PrettyMIDI object
# cello_c_chord = pretty_midi.PrettyMIDI()
# # Create an Instrument instance for a cello instrument
# cello_program = pretty_midi.instrument_name_to_program('Cello')
# cello = pretty_midi.Instrument(program=cello_program)
# # Iterate over note names, which will be converted to note number later
# for frequency in [440]:
#     # Create a Note instance, starting at 0s and ending at .5s
#     note_number = pretty_midi.hz_to_note_number(frequency)
#     print(note_number)
#     note = pretty_midi.Note(
#         velocity=100, pitch=note_number, start=0, end=.5)
#     # Add it to our cello instrument
#     cello.notes.append(note)
# # Add the cello instrument to the PrettyMIDI object
# cello_c_chord.instruments.append(cello)
# # Write out the MIDI data
# cello_c_chord.write('cello-C-chord.mid')

# data = pd.read_csv("data.csv")

molecule = pretty_midi.PrettyMIDI()
molecule_instr = pretty_midi.Instrument(program = 94)
a_note = pretty_midi.Note(velocity = 100, pitch = int(pretty_midi.hz_to_note_number(440)), start =0, end=1)
# note_2 = pretty_midi.Note(velocity = 100, pitch = 61, start =0, end=1)
# note_3 = pretty_midi.Note(velocity = 100, pitch = 64, start =0, end=1)
# molecule_instr.notes.extend([a_note, note_2, note_3])
molecule_instr.notes.append(a_note)
molecule.instruments.append(molecule_instr)
molecule.write("web_app/sonification/mid_files/metallic.mid")
to_audio("web_app/sonification/arachno.sf2", f"web_app/sonification/mid_files/metallic.mid", "web_app/sonification/wav_files")


# # Initialize the synthesizer (you need a soundfont file, e.g., a .sf2 file)
# soundfont = "path/to/your/soundfont.sf2"
# synth = fluidsynth.Synth()
# synth.sfload(soundfont)
# synth.start()

# # Load and play MIDI file
# midi_file = "input_file.mid"
# synth.midi_file_to_audio(midi_file, "output_audio.wav")

# synth = FluidSynth("creativelabs.sf2")

# synth.midi_to_audio('goblin.mid', 'goblin2.wav')


# # Load the generated audio
# audio = AudioSegment.from_file("output_audio.wav")

# # Apply a low-pass filter (example)
# filtered_audio = audio.low_pass_filter(1000)

# # Export the filtered audio
# filtered_audio.export("filtered_audio.wav", format="wav")

# timidity piano.mid -Ow -o out.wav

# tracks_specs = [
#     MidiTrackSpec(
#         FluidsynthSoundMaker(
#             "mid_files/track_1.mid",
#             "creativelabs.sf2",
#             {'1': 15},
#         ),
#             '02.mid',
#         '03.mid'
#     )]

# project = Project(
#     "mid_files",
#     tracks_specs,
# )

# gains = [1.0, 1.0, 1.0, 1.0, 1.2, 1.2]
# opening_silence = 0.5
# trailing_silence = 0.5

# timeline = project.mix(gains, opening_silence, trailing_silence)
# timeline /= np.max(np.abs(timeline))
# IPython.display.Audio(timeline, rate=project.frame_rate)

# write_timeline_to_wav("result.wav", timeline, project.frame_rate)
