# Write circle_calc() function that takes radius of a circle as an input from user
# and then it calculates and returns area, circumference and diameter.
# You should get these values in your main program by calling circle_calc function and then print them

radius = float(input("Enter radius = "))


def circle_calc(radius):
    Area = 3.14 * radius**2
    circumference = 2 * 3.14 * radius
    diameter = 2 * radius
    return Area,circumference,diameter


if __name__ == '__main__':
    a, c, d = circle_calc(radius)
    print('Area = {},circumference = {},diameter = {}'.format(a,c,d))
