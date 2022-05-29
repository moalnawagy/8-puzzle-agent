"""
search(intial_state):
	#node{ state , path , ..... }
	initialize fringe with intital state
	while fringe is not empty :
		pick a node from the fringe according to a strategy
		--if visited : continue
		if goal : return solution
		from state get possible actions
		from actions generate next states
		append successors to the fringe
	return failure 
"""

from assistantFun import check_for_winning as isgoal
from assistantFun import possible_moves as get_actions
from assistantFun import aplly_move as get_state
from assistantFun import compute_cost


def solve(strategy,intial_state):
	fringe=[]; visited=[]
	initial_node=init_node(strategy,intial_state)
	fringe.append(initial_node)
	
	while len(fringe)>0:
		current_node=fringe.pop(select_node(strategy,fringe))
		if current_node['state'] in visited : continue
		visited.append(current_node['state'])
		if isgoal(current_node['state']):
			return get_solution(strategy,current_node,len(visited))
		possible_actions=get_actions(current_node['state'])
		for action in possible_actions:
			next_state=get_state(action,current_node['state'])
			next_node=add_node(strategy,current_node,action,next_state)
			fringe.append(next_node)
	return None

def select_node(strategy,fringe):
	if strategy == 'DFS': return -1
	if strategy == 'BFS': return 0
	if strategy == 'UCS': return get_min('cost',fringe)

def get_min(key,fringe):
	idx_min= 0
	for i in range(1,len(fringe)):
		if fringe[i][key] < fringe[idx_min][key] :
			idx_min=i
	return idx_min

def init_node(strategy,intial_state):
	initial_node = {}
	initial_node['state']=intial_state
	initial_node['path']=[]
	if strategy=='UCS': initial_node['cost']=0
	return initial_node

def add_node(strategy,current_node,action,next_state):
	next_node = {}
	next_node['state']=next_state
	next_node['path']=current_node['path'][:]; next_node['path'].append(action)
	if strategy=='UCS':
		next_node['cost']=current_node['cost']+compute_cost(action,current_node['state'])
	return next_node

def get_solution(strategy,current_node,complexity):
	solution={}
	solution['solution']=current_node['path']
	solution['complexity']=complexity
	if strategy=='UCS':
		solution['cost']=current_node['cost']
	return solution

