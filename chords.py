# work with chords

import random


class Chords:
    def __init__(self):
        # Chord formulas (intervals in semitones from the root)
        self.chords = {
            "Major": [0, 4, 7],
            "Minor": [0, 3, 7],
            "Diminished": [0, 3, 6],
            "Augmented": [0, 4, 8],
            "Major 7th": [0, 4, 7, 11],
            "Minor 7th": [0, 3, 7, 10],
            "Dominant 7th": [0, 4, 7, 10],
            "Suspended 2nd": [0, 2, 7],
            "Suspended 4th": [0, 5, 7],
            "Minor 6th": [0, 3, 7, 9],
            "Major 6th": [0, 4, 7, 9],
            "Diminished 7th": [0, 3, 6, 9],
        }

    '''
        notesArray: array of notes
        returns the type of chord to generate for this note
    '''
    def generateChord(self, notesArray, thisNote):
        type_of_chord = "Major"

        chord_choices = []
        for i in self.chords.keys():
            chord_choices.append(i)
        type_of_chord = random.choice(chord_choices)
        print(f"type of chord: {type_of_chord}")

        return type_of_chord


    """
        return the note offsets for a chord
    """
    def generateChordNotes(self, type_of_chord):
        return self.chords[type_of_chord]