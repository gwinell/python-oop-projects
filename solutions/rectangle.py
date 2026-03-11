class Rectangle:

    def __init__(self, width, height):

        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("Ширина должна быть положительным числом.")
        if not isinstance(height, (int, float))  or height < 0:
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

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

