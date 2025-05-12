from midiutil import MIDIFile
import random

# Define musical scales using interval math
scale_patterns = {
    "major": [0, 2, 4, 5, 7, 9, 11],      # Major scale pattern (W-W-H-W-W-W-H)
    "minor": [0, 2, 3, 5, 7, 8, 10],      # Natural Minor scale (W-H-W-W-H-W-W)
    "pentatonic": [0, 2, 4, 7, 9],        # Pentatonic scale (W-W-m3-W-m3)
    "harmonic_minor": [0, 2, 3, 5, 7, 8, 11] # Harmonic Minor (with raised 7th)
}

def generate_scale(root_note, scale_type):
    """Generates a scale dynamically based on the root note and interval math"""
    if scale_type in scale_patterns:
        return [root_note + step for step in scale_patterns[scale_type]]
    else:
        return "Invalid scale type"

# Define chords mathematically using intervals
chord_intervals = {
    "major": [0, 4, 7],    # Root, Major Third, Perfect Fifth
    "minor": [0, 3, 7],    # Root, Minor Third, Perfect Fifth
    "diminished": [0, 3, 6],
    "augmented": [0, 4, 8]
}

def generate_chord(root_note, chord_type):
    """Constructs chords mathematically"""
    return [root_note + step for step in chord_intervals.get(chord_type, [])]

# Implement Markov Chain for melody probability-based transitions
def generate_melody(scale, length=16):
    """Generates a melody sequence probabilistically"""
    melody = []
    current_note = random.choice(scale)

    for _ in range(length):
        next_note = random.choice(scale)
        melody.append(next_note)
        current_note = next_note  # Move to new note
    return melody

# Create a MIDI file to store generated music
def create_midi_file(melody, chords, filename="generated_music.mid"):
    midi = MIDIFile(2)  # Two tracks: melody & chords
    midi.addTempo(0, 0, 120)
    midi.addTempo(1, 0, 120)

    # Add melody to track 0
    time = 0
    for note in melody:
        midi.addNote(0, 0, note, time, 1, 100)  # Note lasts one beat
        time += 1

    # Add chord progression to track 1
    time = 0
    for chord in chords:
        for note in chord:
            midi.addNote(1, 0, note, time, 2, 80)  # Chords last 2 beats
        time += 2

    # Save MIDI file
    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)
    print(f"MIDI file '{filename}' created successfully!")

# Example usage
root = 60  # Middle C (MIDI Note)
scale_type = "major"
chord_type = "major"

scale = generate_scale(root, scale_type)
melody = generate_melody(scale)
chords = [generate_chord(root + i * 5, chord_type) for i in range(4)]  # Simple progression

create_midi_file(melody, chords)