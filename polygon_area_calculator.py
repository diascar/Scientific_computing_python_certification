class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, newWidth):
        self.width = newWidth
    
    def set_height(self, newHeight):
        self.height = newHeight
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            line = ""
            for i in range(self.height):
                tmp = self.width*"*"
                line += f"{tmp}\n"
            return line
        else:
            return "Too big for picture."
    
    def get_amount_inside(self, another):
        amount = self.get_area()//another.get_area()
        if amount < 1:
            return 0
        else:
            return amount
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, newSide):
        super().set_height(newSide)
        super().set_width(newSide)
    
    def set_height(self, newHeight):
        self.set_side(newHeight)
    
    def set_width(self, newWidth):
        self.set_side(newWidth)
    
    def __str__(self):
        return f"Square(side={self.width})"


