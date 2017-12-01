import random
import sys
import os

board = []

space = []

rows = 4
rowprint = rows
rowrand = rows
cols = 4
colrand = cols
bombs = 2
r = 0

if rows <= 0 or cols <= 0:
	print("How did you mess this up...")
	sys.exit()

for x in range(rows):
	row = [0] * cols
	board.append(row)


while bombs > 0:
	bombcol = int(random.uniform(0,colrand))
	bombrow = int(random.uniform(0,rowrand))
	while board[bombcol-1][bombrow-1] == '*':
		bombcol = int(random.uniform(0,colrand))
		bombrow = int(random.uniform(0,rowrand))
	board[bombcol][bombrow] = '*'
	bombs -= 1

	try:
		board[bombcol-1][bombrow-1] += 1
	except:
		ValueError or IndexError
	try:
		board[bombcol-1][bombrow] += 1
	except:
		ValueError or IndexError
	try:
		board[bombcol-1][bombrow+1] += 1
	except:
		ValueError or IndexError

	try:
		board[bombcol][bombrow-1] += 1
	except:
		ValueError or IndexError
	try:
		board[bombcol][bombrow+1] += 1
	except:
		ValueError or IndexError

	try:
		board[bombcol+1][bombrow-1] += 1
	except:
		ValueError or IndexError
	try:
		board[bombcol+1][bombrow] += 1
	except:
		ValueError or IndexError
	try:
		board[bombcol+1][bombrow+1] += 1
	except:
		ValueError or IndexError


print(board)	
while rowprint > 0:
	print(board[rowprint-1])
	rowprint -= 1

