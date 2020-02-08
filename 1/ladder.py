import sys


num_steps = int(sys.argv[1])
space = " "
hashtag = "#"
num_space = num_steps - 1
num_hashtag = 1

while(num_steps > 0):
	print(space * num_space + hashtag * num_hashtag)
	if not num_space:
		break
	num_space -= 1
	num_hashtag += 1

sys.exit(0)
