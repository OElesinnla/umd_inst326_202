class Adder:
    def __init__(self):
        self.values = []

    def prompt(self):
        res = input()
        self.values.append(int(res.strip()))

    def get_sum(self):
        return sum(self.values)