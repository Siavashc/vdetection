class circle():
    def __init__(self , r : int):
        self.pi=3.14
        self.r = r
    def border(self):
        return 2*self.pi*self.r
    def area (self):
        return self.pi*self.r**2
it = circle(4)
print(it.area() , it.border())