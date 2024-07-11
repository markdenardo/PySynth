import math
import numpy as np
import sounddevice as sd
from pynput import keyboard

# Constants
SAMPLE_RATE = 44100  # Sample rate in Hz
DURATION = 1.0  # Duration in seconds
AMPLITUDE = 0.5  # Amplitude for the sound

# Frequency map for keyboard keys (assuming a basic layout for simplicity)
NOTE_FREQUENCIES = {
    'a': 261.63,  # C4
    'w': 277.18,  # C#4/Db4
    's': 293.66,  # D4
    'e': 311.13,  # D#4/Eb4
    'd': 329.63,  # E4
    'f': 349.23,  # F4
    't': 369.99,  # F#4/Gb4
    'g': 392.00,  # G4
    'y': 415.30,  # G#4/Ab4
    'h': 440.00,  # A4
    'u': 466.16,  # A#4/Bb4
    'j': 493.88,  # B4
    'k': 523.25   # C5
}

def generate_sine_wave(frequency, sample_rate, duration):
    num_samples = int(sample_rate * duration)
    x = np.linspace(0, duration, num_samples, endpoint=False)
    frequencies = x * frequency
    y = AMPLITUDE * np.sin((2 * np.pi) * frequencies)
    return y

def play_sound(frequency):
    # Generate sine wave
    samples = generate_sine_wave(frequency, SAMPLE_RATE, DURATION).astype(np.float32)

    # Play sound using sounddevice
    sd.play(samples, SAMPLE_RATE)
    sd.wait()

def on_press(key):
    try:
        if key.char in NOTE_FREQUENCIES:
            frequency = NOTE_FREQUENCIES[key.char]
            play_sound(frequency)
    except AttributeError:
        pass

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
