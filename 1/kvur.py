import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
x1, x2 = 0, 0

D = b * b - 4 * a * c
if D >= 0:
	x1 = (int)((-b - D ** 0.5) / (2 * a))
	x2 = (int)((-b + D ** 0.5) / (2 * a))
	print(x1)
	print(x2)
else:
	print("Корней на множестве действительных чисел нет")
	
sys.exit(0)
