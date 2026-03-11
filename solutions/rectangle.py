class Rectangle:

    def __init__(self, width, height):

        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина должна быть положительным числом.")
        if not isinstance(height, (int, float))  or height <= 0:
            raise ValueError("Длинна должна быть положительным числом.")

        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

    def scale(self, factor):
        if not isinstance(factor, (int, float)) or factor <= 0:
            raise ValueError("Необходимо положительное число.")
        self.width = self.width * factor
        self.height = self.height * factor

    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def can_contain(self, other):
        if not 'Rectangle' in str(type(other)):
            raise TypeError("Это не прямоугольник.")
        rect1 = (other.width, other.height)
        rect2 = (self.width, self.height)
        if (min(rect1) <= min(rect2)) and (max(rect1) <= max(rect2)):
            return True
        elif (max(rect1) <= min(rect2)) and (min(rect1) <= max(rect2)):
            return True
        else:
            return False

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


