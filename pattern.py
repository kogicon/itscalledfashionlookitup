class Motif:
    """
    Represents a "motif", a repeating element that is part of a pattern. Has a color, size, and parameters for how it
    tiles / repeats over an area.
    """
    def __init__(self, color="#FFFFFF", width=0, height=0, repeat_x=1, repeat_y=1, space_x=0, space_y=0):
        # the color of the motif
        self.color = color
        # the width of the motif
        self.width = width
        # the height of the motif
        self.height = height
        # the number of times a motif repeats horizontally
        self.repeat_x = repeat_x
        # the number of times a motif repeats vertically
        self.repeat_y = repeat_y
        # the space between each horizontal instance of the motif
        self.space_x = space_x
        # the space between each horizontal instance of the motif
        self.space_y = space_y

    @staticmethod
    def random_motif():
        return Motif()


class Pattern:
    """
    Represents a "pattern", containing a series of motifs and a background color.
    """
    def __init__(self, bgcol="#FFFFFF", motifs=[]):
        # the background color
        self.bgcol = bgcol
        # the list of motifs
        self.motifs = motifs

    @staticmethod
    def random_pattern():
        return Pattern()
