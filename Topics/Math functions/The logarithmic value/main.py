import math

positive_value = abs(int(input()))
base = int(input())
if base > 1:
    print(round(math.log(positive_value, base), 2))
else:
    print(round(math.log(positive_value), 2))
