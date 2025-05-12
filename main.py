import random

from midiutil import MIDIFile

from notes import Notes
from chords import Chords

midi_notes = {
        -1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        0: [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        1: [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
        2: [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
        3: [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
        4: [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71],
        5: [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
        6: [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95],
        7: [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107],
        8: [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119],
        9: [120, 121, 122, 123, 124, 125, 126, 127]
    }



note_names = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]



def main():
    notesClass = Notes()
    chordsClass = Chords()

    number_of_notes = 200


    ''' build tracks '''
    # assemble empty array
    notesArray = []

    # generate scale
    scale = notesClass.generateScale()

    # run for every note
    for note in range(number_of_notes):
        timeSlice = []

        # generate melody
        melodyNote = notesClass.nextNote(notesArray, scale)
        timeSlice.append(melodyNote)

        # generate chords
        chordArray = []
        type_of_chord = chordsClass.generateChord(notesArray, melodyNote)
        chordNotes = chordsClass.generateChordNotes(type_of_chord)

        binary = random.choice([0,0,0,1])
        if binary:
            for chordNote in chordNotes:
                chordArray.append(melodyNote + chordNote)
        else:
            chordArray=[melodyNote, melodyNote, melodyNote]

        timeSlice.append(chordArray)

        # bring it all together
        notesArray.append(timeSlice)
        print(f"note # {note}")

    print(f"note array: ")
    for note in range(number_of_notes):
        print(f"{note} {notesArray[note]}")


    """ build midi file """
    tracks = 2
    midi = MIDIFile(tracks)

    tempo = 120

    # Define tempo for each track
    for track in range(tracks):
        midi.addTempo(track, 0, tempo)

    # load melody track
    time = 0
    for note in range(number_of_notes):
        noteToPlay = notesArray[note][0]
        midi.addNote(0, 0, noteToPlay, time, 1, 100)
        time += 1
        print(f'melody t={time} note={noteToPlay}')

    # load chords track
    time = 0
    for note in range(int(number_of_notes/2)):

        for chordNote in notesArray[note][1]:
            midi.addNote(1, 0, chordNote, time, 2, 90)
            print(f'chord t={time} note={chordNote}')
        time += 2


    print('tracks finished')

    # Save the MIDI file
    with open("song.mid", "wb") as output_file:
        midi.writeFile(output_file)

    print("MIDI file created successfully!")


if __name__ == "__main__":
    main()