# put your python code here
import math

side1 = int(input())
side2 = int(input())
side3 = int(input())
semi_perimeter = (side1 + side2 + side3) / 2
heron_formula = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
print(heron_formula)
