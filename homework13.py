class Building:
    total = 0
    id = 0

    def __init__(self):
        self.id = Building.total
        Building.total += 1



for i in range(1, 41):
    a = Building()

print(a.total)