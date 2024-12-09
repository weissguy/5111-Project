
import mido
from fluidsynth import Synth
import numpy as np
import soundfile as sf

def midi_to_wav(midi_file, sf2_file, wav_file, sample_rate=44100):
    # Initialize FluidSynth
    synth = Synth(samplerate=sample_rate)
    synth.start(driver="file")  # Use 'file' driver for offline rendering

    # Load the SoundFont
    sfid = synth.sfload(sf2_file)
    synth.program_select(0, sfid, 0, 0)

    # Create an audio buffer
    audio = []

    # Load MIDI file
    midi = mido.MidiFile(midi_file)

    # Process MIDI messages
    for msg in midi.play():
        if not msg.is_meta:
            if msg.type == "note_on":
                synth.noteon(0, msg.note, msg.velocity)
            elif msg.type == "note_off":
                synth.noteoff(0, msg.note)

        # Render audio block (size can be adjusted for performance)
        samples = np.array(synth.get_samples(512), dtype=np.float32)
        audio.extend(samples)

    # Save audio to WAV file
    sf.write(wav_file, np.array(audio), sample_rate)

    # Clean up
    synth.delete()

# Example usage
midi_to_wav("piano.mid", "creativelabs.sf2", "output.wav")