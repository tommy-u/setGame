import itertools
import copy
import random

set_sz = 0 #Num elements in set.
num_players = 1
S = [] #The starting set.
P = S  #The updated set.
K = P #copied set.
go_first = False

def rules():
	'''The rules.'''
	print('=================RULES=================')
	print('You will give a set size, N.')
	print('I will generate the powerset, S, of the N integers in [1, N].')
	print('P initially is equal to S.')
	print('Players take turns picking a set, s, in P that is neither S,')
	print('nor the empty set.') 
	print('P is updated by removing all sets that contain s (including s)')
	print('The loser is the one who has no set left to remove.')
	print('=======================================')

def welcome():
	'''Introduce player to game.'''
	print('****************************************')
	print('Welcome to the set game.')
	print('****************************************')

	while True:
		ch = input('s to start, r for rules, q to quit: ')
		if ch == 'q':
			exit()
		elif ch == 'r':
			rules()
		elif ch == 's':
			return

def get_num_players():
	'''Determine number players.'''
	global num_players
	while True:
		ch = input('1 for 1 player, 2 for 2 player: ')
		if ch == '1':
			return
		elif ch == '2':
			num_players = 2
			return

def get_player_order():
	'''Determine if player goes 1st or 2nd.'''
	global go_first
	while True:
		ch = input('1 for play 1st, 2 for play 2nd: ')
		if ch == '1':
			go_first = True
			return
		elif ch == '2':
			return

def get_size():
	'''Determine set start size.'''
	global set_sz
	while True:
		try:
			set_sz = int(input('Give a positive int set start size: '))
		except:
			print('Try again.')
			continue

		if set_sz > 0:
			print('Set size is:', set_sz) 
			return

		print('Try again.')

def powerset():
	'''Set of all subsets of [1, ..., N]'''
	'''https://gist.github.com/codemaniac/3005522'''
	global set_sz
	global S
	tmp = list(range(1,set_sz+1))
	S = [[tmp[j] for j in range(set_sz) if (i&(1<<j))] for i in range(1<<set_sz)]
	A = S[-1]
	S.remove(A)
	S.remove([])
	

def move_help():
	'''Specify input form.'''
	print('+++++++++++++++++HELP+++++++++++++++++')
	print('Say P is [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],')
	print('and you want to select [1,2]')
	print('just type the elements separated by spaces: 1 2')
	print('and hit return.')
	print('++++++++++++++++++++++++++++++++++++++')

def player_move():
	'''Removes all sets containing subset'''
	'''Todo: add error checking.'''
	# if set in s and set is not s and set not empty
	# remove all subsets that contain all it's elements 
	# else error
	while True:
		ch = input('Enter subset you would like to select, h for help: ')
		if ch == 'h':
			move_help()
		else:
			player_set = sorted([int(i) for i in ch.split()]) 
			if player_set == []:
				print('That set is empty, try again')
				continue
			break
	print('Player chose', player_set)
	delete_sets(player_set)

def strategy():
#'''goes through the powerset list and for each element it sees whether it will leave an even or odd number fo sets left'''
#'''if none of the sets leave an odd number of sets left then pick a random one'''
	global P
	i = 0
	for i in range(0, 2**set_sz):
		comp_set = P[i]
		delete_setsK(comp_set)
		if (i != 2**(set_sz) or len(KC) % 2 == 0):
			KC = copy.deepcopy(P)
		else: comp_set = P[random.randrange(1, len(P))]

def tu_strategy():
	#Comments need to be indented.
	'''goes through the powerset list and for each element it sees whether it will 
	leave an even or odd number fo sets left.if none of the sets leave an odd number 
	of sets left then pick a random one'''
	global P
        #No need to initialize i in python
        #i = 0 
        #for i in range(0, 2**set_sz):

	#Skip the 0th element, the empty set by starting the range at 1.
	#P changes in size, so can't always go up to 2**set_sz
	for i in range(1, len(P)):
		trial_set = P[i]
		#Copy P into local variable, KC
		KC = copy.deepcopy(P) 
		#Update KC by removing ith element.
		KC = tu_delete_setsK(KC, trial_set)
		#The strategy is to leave the other player with an odd # of non empty elements.
		#This happens when len(KC) % 2 == 0 because you have to count the empty set.
		if len(KC) % 2 == 0:
			#The current index of P results in an odd num of non empty elements.
			#Return P[i] to computer_move to make use of this information.
			return P[i]
	#If we exit the loop, no subset of P results in an odd # non empty set.
	#Return an impossible index (-1) to signal that we failed to find an index.
	return P[random.randrange(1,len(p))]


def computer_move():
	'''Computer removes a subset depending on strategy.'''
	global P
	'''Assuming [] is always 0th element'''
	comp_set = tu_strategy()
	assert comp_set != []
	print('computer chooses set', comp_set )
	delete_sets(comp_set)

def delete_setsK(player_set):
	'''Remove from copy'''
	global KC
	KC = [i for i in K if not (set(player_set) <= set(i)) ]

def tu_delete_setsK(KC, trial_set):
       '''Remove from copy'''
       return [i for i in K if not (set(player_set) <= set(i)) ]

def delete_sets(player_set):
	'''Remove from P'''
	global P
	P = [i for i in P if not (set(player_set) <= set(i)) ]

def game_loop():
	'''Keep game running.'''
	global P
	p1_turn = True

	while True:

		print('Currently available sets:')
		print(P)
		print(len(P))
		

		# If set is empty, you are the loser.
		if len(P) == 1:
			if p1_turn:
				print('player 1 loses')
				return
			else:
				print('player 2 loses')
				return

		if p1_turn:
			print('Player 1 is up.')
			if num_players == 2 or go_first == True:
				player_move()
			else:
				computer_move()

		else:
			print('Player 2 is up.')
			if num_players == 2 or not go_first:
				player_move()
			else:	
				computer_move()

		p1_turn = not p1_turn


def run():
	global P
	global S
	welcome()
	get_num_players()
	if num_players == 1:
		get_player_order()
	get_size()
	powerset()
	P = copy.deepcopy(S)
	game_loop()


run()
