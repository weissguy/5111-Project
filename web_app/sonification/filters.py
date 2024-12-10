from pydub import AudioSegment
from pydub.scipy_effects import low_pass_filter

sound = AudioSegment.from_file("web_app/sonification/wav_files/methanol.wav")
filtered_sound = low_pass_filter(sound, 5000)  # Cutoff frequency in Hz
filtered_sound.export("methanol.mp3", format="mp3")

# available filters: low_pass_filter, high_pass_filter, band_pass_filter, and band_stop_filter.
