import librosa 
import librosa.display
import matplotlib.pyplot as plt 

def plot_waveform(audio_path):
    # Load audio file
    audio, sr = librosa.load(audio_path)

    # Plot waveform 
    plt.figure(figsize=(14, 5))
    librosa.display.waveshow(audio, sr=sr)
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Amplitude")
    plt.show()

plot_waveform("")
