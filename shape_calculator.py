
# RECTANGLE CLASS
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, new_value):
        self.width = new_value
    
    def set_height(self, new_value):
        self.height = new_value
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if max(self.width, self.height) > 50:
            return "Too big for picture."
        
        pic = "*"*self.width + "\n"
        pic *= self.height
        return pic
    
    def get_amount_inside(self, shape):
        x = int(self.width / shape.width)
        y = int(self.height / shape.height)

        return x * y
    
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, new_value):
        self.width = new_value
        self.height = new_value

    def set_width(self, new_value):
        self.set_side(new_value)
    
    def set_height(self, new_value):
        self.set_side(new_value)
    
    def __str__(self):
        return "Square(side={})".format(self.width)
