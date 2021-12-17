# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

# def calculate_area(x,y):
#     area = (x*y)/2
#     return area
#
# base = int(input("base = "))
# height= int(input("height = "))
#
# # print("Area = ", calculate_area(int(base),int(height)))
# print("Area = ", calculate_area(base,height))

# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def cal_area(a,b,shape='triangle'):
    if shape == 'triangle':
        area = (a*b)/2
    elif shape == 'rectangle':
        area = a*b
    else:
        print("different shape")
        area=None
    return area


a = int(input("a = "))
b = int(input("b = "))
# shape = input(" shape type : ")
print("AREA = ", cal_area(a,b,'rectangle'))







