def get_numeric(prompt):
    while True:
        try:
            res = float(input(prompt))
            break
        except (ValueError, NameError):
            print("Numbers only please!")
    return res


class Point:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def input(self, prompt=""):
        if len(prompt) > 0:
            print(prompt)

        self.x = get_numeric("Entry x:")
        self.y = get_numeric("Entry y:")


class Rectangle:

    area = -1

    def __init__(self, point_a=Point(), point_b=Point(), point_c=Point(), point_d=Point()):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.point_d = point_d

    def input(self):
        self.point_a.input("==== Point A ====")
        self.point_b.input("==== Point B ====")
        self.point_c.input("==== Point C ====")
        self.point_d.input("==== Point D ====")

    def calc_area(self):
        if self.area < 0:

            side_ab = self.point_a.x * self.point_b.y - self.point_b.x * self.point_a.y
            side_bc = self.point_b.x * self.point_c.y - self.point_c.x * self.point_b.y
            side_cd = self.point_c.x * self.point_d.y - self.point_d.x * self.point_c.y
            side_da = self.point_d.x * self.point_a.y - self.point_a.x * self.point_d.y

            self.area = abs((side_ab + side_bc + side_cd + side_da) / 2)

        return self.area


rectangle = Rectangle()
rectangle.input()

print("Area is %.3f" % rectangle.calc_area())
