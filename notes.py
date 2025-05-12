# define what the next note will be
import random

class Notes:
    def __init__(self):
        self.seedNote = random.randrange(60, 70)
        print(f"seed note: {self.seedNote}")

        self.scale_patterns = {
            "major": [0, 2, 4, 5, 7, 9, 11],      # Major scale pattern (W-W-H-W-W-W-H)
            "minor": [0, 2, 3, 5, 7, 8, 10],      # Natural Minor scale (W-H-W-W-H-W-W)
            "pentatonic": [0, 2, 4, 7, 9],        # Pentatonic scale (W-W-m3-W-m3)
            "harmonic_minor": [0, 2, 3, 5, 7, 8, 11] # Harmonic Minor (with raised 7th)
        }


    def generateScale(self):
        scaleOptions = []
        for i in self.scale_patterns.keys():
            scaleOptions.append(i)
        scale = random.choice(scaleOptions)
        print(f"scale: {scale}")
        scaleArray = self.scale_patterns[scale]

        return scaleArray

    """
        notesArray: array of notes
        returns the next melody note to play
    """
    def nextNote(self, notesArray, scale):

        nextNoteInterval = random.choice(scale)

        # coin toss if the notes go up or down
        binary = random.choice([0,1])

        try:
            if binary: nextNote = notesArray[-1][0] + nextNoteInterval
            else: nextNote = notesArray[-1][0] - nextNoteInterval
        except:
            nextNote = self.seedNote

        if nextNote > 120 or nextNote < 10:
            nextNote = self.seedNote

        return nextNote