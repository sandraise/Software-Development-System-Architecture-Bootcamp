class Polygon:
    def __init__(self,no_of_sides):
        self.no_of_sides = no_of_sides
        # Create a list of numbers 
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " +str(i+1)+": ")) for i in range (self.no_of_sides)]

    def dispSides(self):
        for i in range(self.no_of_sides):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a,b,c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c) ** 0.5)
        return("The area of the triangle is {area}")


# poly = Polygon(6)
# poly.inputSides()
# poly.dispSides()

# tri = Triangle()
# tri.inputSides()
# tri.dispSides()
# tri.findArea()

class Quad(Polygon):
    def __init__(self):
        Polygon.__init__(self,4)

    def findPerimeter(self):
        a,b,c,d = self.sides
        perimeter = a + b + c + d
        return (f"The perimeter of the quad is {perimeter}")


q = Quad()
q.inputSides()
q.dispSides()
print(q.findPerimeter())