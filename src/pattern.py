class Pattern:

    def __init__(self, name):
        self.name = name
        self.stitch_map = [[]]
        self.multiples_of = 0
        self.multiples_change = 0
        self.max_row = 0

    def is_correct_stitch_count(self, count):
        return True if ((count % self.multiples_of) - self.multiples_change == 0) else False

    def add_row(self, row):
        self.stitch_map.append(row)
        self.max_row += 1

    def get_row(self, rowNumber):
        index = rowNumber % self.max_row
        return self.stitch_map[index]

    def set_multiples(self, multipleOf, multipleChange):
        self.multiples_of = multipleOf
        self.multiples_change = multipleChange