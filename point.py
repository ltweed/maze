

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

class Line:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas, color="black"):
        canvas.create_line(self.__p1.x, self.__p1.y, self.__p2.x, self.__p2.y, fill=color, width=2)

        