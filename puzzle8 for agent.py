"""
Puzzle8 Game
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
"""
from random import randrange
from assistantFun import possible_moves as get_actions
from assistantFun import aplly_move as get_state
from SearchAgent import solve

def print_puzzle(puzzle):
	p=''
	for i in puzzle:
		if i==0: p+=' '
		else: p+=str(i)
	print (
		'-'*13 + '\n' +
		'| ' + p[0] + ' | ' + p[1] + ' | ' + p[2] + ' |' + '\n' +
		'-'*13 + '\n' +
		'| ' + p[3] + ' | ' + p[4] + ' | ' + p[5] + ' |' + '\n' +
		'-'*13 + '\n' +
		'| ' + p[6] + ' | ' + p[7] + ' | ' + p[8] + ' |' + '\n' +
		'-'*13
		)

def shuffle_puzzle(n):
	puzzle=[0, 1, 2, 3, 4, 5, 6, 7, 8]
	for _ in range(n):
		actions=get_actions(puzzle)
		rand_index=randrange(0,len(actions))
		puzzle=get_state(actions[rand_index],puzzle)
	return puzzle

if __name__ == '__main__':
	puzzle=shuffle_puzzle(50)
	print("**************************************************************")
	print("using BFS Algorithm:")
	print(solve('BFS',puzzle))
	print("**************************************************************")
	print("using UCS Algorithm:")
	print(solve('UCS',[1, 0, 2, 6, 3, 5, 4, 7, 8]))
	print("**************************************************************")
	print("using DFS Algorithm:")
	print(solve('DFS',puzzle))
	print("**************************************************************")

	#use the implelemented search strategies (DFS,BFS,UCS) to solve the puzzle
	#print the final solution and the number of expanded nodes for each strategy
	#for DFS use this puzzle [1, 0, 2, 6, 3, 5, 4, 7, 8]
