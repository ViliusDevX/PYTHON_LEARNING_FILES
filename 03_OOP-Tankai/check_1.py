class Tank:
    def __init__(self, color):
        self.color = color


a = [(0, 255, 255),(0, 255, 0),(255,0,0)]

for i in range(3):
    tank = Tank(a[i])
    print(i)