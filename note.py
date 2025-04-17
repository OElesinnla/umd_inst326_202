# Global dictionaries provided in the assignment.
POSITIONS = {
    "A": 0,
    "A#": 1,
    "Bb": 1,
    "B": 2,
    "C": 3,
    "C#": 4,
    "Db": 4,
    "D": 5,
    "D#": 6,
    "Eb": 6,
    "E": 7,
    "F": 8,
    "F#": 9,
    "Gb": 9,
    "G": 10,
    "G#": 11,
    "Ab": 11
}

PITCHES = {
    0: ["A"],
    1: ["A#", "Bb"],
    2: ["B"],
    3: ["C"],
    4: ["C#", "Db"],
    5: ["D"],
    6: ["D#", "Eb"],
    7: ["E"],
    8: ["F"],
    9: ["F#", "Gb"],
    10: ["G"],
    11: ["G#", "Ab"]
}


class Note:
    """
    Represents a musical note from the twelve-tone chromatic scale.

    Attributes:
        position (int): The position on the chromatic scale (0 for A, 1 for A#/Bb, ..., 11 for G#/Ab).
        perspective (str or None): The accidental perspective of the note; possible values:
            "#"  - represents a sharp view.
            "b"  - represents a flat view.
            None - no specific perspective (used for naturals or displaying both names for accidentals).
    
    Initialization:
        The first parameter may be either:
          - A note name (string) e.g., "C", "C#", "Gb". The position is determined using the POSITIONS dict.
          - An integer (0-11) indicating the note's position directly.
          
        The second, optional parameter is the perspective ("#" or "b"). If it is provided and not None, 
        it overrides any accidental indication in the note name. If not provided or is None:
            - and if the note name includes an accidental, the perspective is taken from that name.
            - otherwise, perspective is set to None.
    """
    
    def __init__(self, position, perspective=None):
        if isinstance(position, int):
            if position < 0 or position > 11:
                raise ValueError("Position must be an integer between 0 and 11 inclusive.")
            self.position = position
            self.perspective = perspective
        elif isinstance(position, str):
            if position not in POSITIONS:
                raise ValueError("Invalid note name: " + position)
            self.position = POSITIONS[position]
            # If the perspective parameter is provided (and not None), use that.
            if perspective is not None:
                self.perspective = perspective
            else:
                # If perspective is None, and the string contains an accidental, use that.
                if "#" in position:
                    self.perspective = "#"
                elif "b" in position:
                    self.perspective = "b"
                else:
                    self.perspective = None
        else:
            raise TypeError("First argument must be an integer or a string representing the note.")

    def __invert__(self):
        """
        Inversion: Return a new Note with the same position but with the opposite perspective.
        If the perspective is None, it remains None.
        """
        if self.perspective == "#":
            new_persp = "b"
        elif self.perspective == "b":
            new_persp = "#"
        else:
            new_persp = None
        return Note(self.position, new_persp)

    def __add__(self, steps):
        """
        Addition: Adding an integer to a Note returns a new Note that is a number of semitones
        above the original note (wrapping around with modulo 12).
        """
        if not isinstance(steps, int):
            return NotImplemented
        new_position = (self.position + steps) % 12
        return Note(new_position, self.perspective)

    def __sub__(self, steps):
        """
        Subtraction: Subtracting an integer from a Note returns a new Note that is a number of semitones
        below the original note (wrapping around with modulo 12).
        """
        if not isinstance(steps, int):
            return NotImplemented
        new_position = (self.position - steps) % 12
        return Note(new_position, self.perspective)

    def __rshift__(self, other):
        """
        Right shift (>>): Computes the distance (in semitones) from this note (assumed higher) to another note.
        The result is always between 0 and 11.
        For example, Note(position=8) >> Note(position=3) returns 5.
        """
        if not isinstance(other, Note):
            return NotImplemented
        return (self.position - other.position) % 12

    def __lshift__(self, other):
        """
        Left shift (<<): Computes the distance (in semitones) from this note (assumed lower) to another note.
        The result is always between 0 and 11.
        For example, Note(position=0) << Note(position=10) returns 10.
        """
        if not isinstance(other, Note):
            return NotImplemented
        return (other.position - self.position) % 12

    def __repr__(self):
        """
        Returns a string representation that can be used to recreate the Note object.
        For example: Note(2, 'b') or Note(4, None)
        """
        return "Note({}, {})".format(self.position, repr(self.perspective))

    def __str__(self):
        """
        Retup
        """
        names = PITCHES[self.position]
        if len(names) == 1:
            return names[0]
        
        if self.perspective == "#":
            for name in names:
                if "#" in name:
                    return name
        elif self.perspective == "b":
            for name in names:
                if "b" in name:
                    return name
        
        # If perspective is None, join both names with a slash.
        return "/".join(names)


# Example usage and testing (you can remove or modify this for your final assignment):
if __name__ == "__main__":
    # Testing Initialization
    n1 = Note("C", "#")      # C natural with sharp perspective: position 3, perspective "#"
    n2 = Note("C", "b")      # C natural with flat perspective: position 3, perspective "b"
    n3 = Note("Ab")          # Ab implies position 11 and flat perspective ("b")
    n4 = Note("C")           # C natural with no perspective: position 3, perspective None
    n5 = Note(6)             # Position 6 with no perspective

    print("Initialization tests:")
    print("n1:", repr(n1))   # Expected: Note(3, '#')
    print("n2:", repr(n2))   # Expected: Note(3, 'b')
    print("n3:", repr(n3))   # Expected: Note(11, 'b')
    print("n4:", repr(n4))   # Expected: Note(3, None)
    print("n5:", repr(n5))   # Expected: Note(6, None)
    
    # Testing Informal String Representation
    print("\nString representations:")
    n6 = Note("A#")         # Should have sharp perspective automatically (position 1, perspective "#")
    n8 = Note("A#", None)   # Position 1 with perspective deduced from accidental → "#"
    n9 = Note("A", None)    # Position 0, natural

    print("n6:", str(n6))   # Expected: "A#" (sharp)
    # For a note with position 1 and perspective None
    n10 = Note(1)
    print("n10:", str(n10))  # Expected: "A#/Bb"
    print("n9:", str(n9))    # Expected: "A"

    # Testing Inversion
    print("\nInversion tests:")
    # Inverting n1 which has perspective "#", should give perspective "b"
    inv_n1 = ~n1
    print("~n1:", repr(inv_n1))  # Expected: position 3, perspective "b"
    
    # Testing Addition and Subtraction
    print("\nAddition and Subtraction:")
    n11 = n1 + 1  # Should move C (position 3) one semitone up to C# (position 4) with sharp perspective
    n12 = n2 + 1  # Should move C (position 3) one semitone up to C# (position 4) but with flat perspective, printing as Db
    print("n11:", str(n11))  # Expected: "C#" (from sharp perspective)
    print("n12:", str(n12))  # Expected: "Db" (from flat perspective)
    
    n13 = n1 - 3  # Subtracting three semitones from C (position 3) gives position 0 (wrap-around), with sharp perspective
    print("n13:", repr(n13))  # Expected: Note(0, '#')

    # Testing Right Shift (>>)
    print("\nRight Shift (>>):")
    note1 = Note(8)  # F natural at position 8
    note2 = Note(3)  # C natural at position 3
    print("note1 >> note2:", note1 >> note2)  # Expected: (8 - 3) % 12 = 5

    note3 = Note(0)
    note4 = Note(10)
    print("note3 >> note4:", note3 >> note4)  # Expected: (0 - 10) % 12 = 2
    
    # Testing Left Shift (<<)
    print("\nLeft Shift (<<):")
    print("note3 << note4:", note3 << note4)  # Expected: (10 - 0) % 12 = 10
    print("note1 << note2:", note1 << note2)    # Expected: (3 - 8) % 12 = 7
