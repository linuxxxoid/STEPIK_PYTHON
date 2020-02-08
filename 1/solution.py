import sys

digit_str = sys.argv[1]
ans = 0

if digit_str.isdigit():
	for element in digit_str:
		ans += int(element)
else:
	print("It's not a number!")
	sys.exit(1)

print(ans)
sys.exit(0)
