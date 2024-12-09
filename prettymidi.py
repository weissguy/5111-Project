import pretty_midi

import numpy as np
import pandas as pd

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

data = pd.read_csv("data.csv")

molecule = pretty_midi.PrettyMIDI()

molecule_instr = pretty_midi.Instrument(program = 102)

note_num = pretty_midi.hz_to_note_number(440)
note_num = int(note_num)

note = pretty_midi.Note(velocity = 10, pitch = note_num, start=0, end=100)
molecule_instr.notes.append(note)
molecule.instruments.append(molecule_instr)
molecule.write("GOBLIn.mid")
