class LeClass:
    marks = list()
    name = str()

    def __init__(self, marks, name):
        self.marks = marks
        self.name = name
        self.avr_mark = float()
        for i in marks:
            self.avr_mark += i
        self.avr_mark /= len(marks)

    def print_marks(self):
        print("You're dumb\n", self.marks)


Andrew = LeClass([1, 2, 3, 10, 9, 12, 8], "Andrew")
print(f"Andrew.name, {Andrew.avr_mark:.3}")
