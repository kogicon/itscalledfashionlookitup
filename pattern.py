class Motif():
    def __init__(self, color, width, height, repeat_x, repeat_y, space_x, space_y):
        self.color = color;
        self.width = width;
        self.height = height;
        pass

class Pattern():

    def __init__(self, bgcol, motifs):
        self.bgcol = bgcol
        self.motifs = motifs

    @staticmethod
    def random_pattern():
        return Pattern()
    pass

# - bgcolor
# - motifs...
#    - color
#    - width
#    - height
#    - repeat-x
#    - repeat-y
#    - space-x
#    - space-y

def generate_pattern():
    pass
