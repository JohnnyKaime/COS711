import textwrap

#Modified 
#https://github.com/hrshtpurohit/8-puzzle-solver/blob/master/bfs%20solver.py
#
#Good Read:
#https://sandipanweb.wordpress.com/2017/03/16/using-uninformed-informed-search-algorithms-to-solve-8-puzzle-n-puzzle/
#https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288
#Breadth First Search 8-puzzle solver...
#I have used technique similar to BFS, except for I haven't used tree

def visualGraph(board):
	#Use textwrap to split board into 3 equal parts
	row = textwrap.wrap(str(board),3)
	print("---------")
	for i in row:
		#Each row is a list object
		#Visualizing graph of the board
		#quite visual, much wow
	    print("|",*i,"|",sep=' ')
	print("---------")
#Takes in the entire board
#Find 0, the empty space on the 3x3 board
#
def find_index_0(num):
	if len(str(num))==8:
		#Board length is only 8 
		#Return the blank space
		return 0
	#Loop through all elements on the board
	#From Top Left -> Top Mid -> etc
	for i in range(9):
		#Checks the last position on the board
		#Bottom Right
		x = num % 10
		num = int(num/10)
		#If its the blank space
		#Searching from the backwards
		if x==0:
			break
	#Return the position on the blank space
	return 8-i

#Converts String into a list
#Swaps the 2 puzzles or numbers
#Converts list back to String
def swap(strr, a, b):
	t = list(strr)
	temp = t[a]
	t[a] = t[b]
	t[b] = temp
	
	return ''.join(t)

def make_move(num):
	#Find 0, blank space
	ind = find_index_0(num)
	#String wrapper
	operate = str(num)
	#My queue
	#For generating children
	moved_list = []
	
	if len(operate)==8:
		#Add 0 to first position
		#Top Left of the board
		operate = '0' + operate
		
	if ind==0:
		#If Top Left is blank space
		#Swop with Top Mid
		#Push it on our queue
		final = swap(operate, ind, 1)
		moved_list.append([int(final),num])
		#Swop with Mid Left
		#Push it on our queue
		final = swap(operate, ind, 3)
		moved_list.append([int(final),num])
		
	elif ind==1:
		#If Top Mid is blank space
		#Swop with Top Left
		#Push it on our queue
		final = swap(operate, ind, 0)
		#Since we came from Top Left, we push the other children nodes to the queue
		#Ignore that one
		final = final[1:]
		moved_list.append([int(final),num])
		#Swop with Top Right
		#Push it on our queue
		final = swap(operate, ind, 2)
		moved_list.append([int(final),num])
		#Swop with Mid Mid
		#Push it on our queue
		final = swap(operate, ind, 4)
		moved_list.append([int(final),num])
	
	elif ind==2:
		#Swop with Top Mid
		#Push it on our queue
		final = swap(operate, ind, 1)
		moved_list.append([int(final),num])
		#Swop with Mid Right
		#Push it on our queue
		final = swap(operate, ind, 5)
		moved_list.append([int(final),num])
		
	elif ind==3:
		#Swop with Top Left
		#Push it on our queue
		final = swap(operate, ind, 0)
		#Since we came from Top Left, we push the other children nodes to the queue
		#Ignore that one
		final = final[1:]
		moved_list.append([int(final),num])
		#Swop with Mid Mid
		#Push it on our queue
		final = swap(operate, ind, 4)
		moved_list.append([int(final),num])
		#Swop with Bot Left
		#Push it on our queue
		final = swap(operate, ind, 6)
		moved_list.append([int(final),num])
		
	elif ind==4:
		#Swop with Top Mid
		#Push it on our queue
		final = swap(operate, ind, 1)
		moved_list.append([int(final),num])
		#Swop with Mid Left
		#Push it on our queue
		final = swap(operate, ind, 3)
		moved_list.append([int(final),num])
		#Swop with Mid Right
		#Push it on our queue
		final = swap(operate, ind, 5)
		moved_list.append([int(final),num])
		#Swop with Bot Mid
		#Push it on our queue
		final = swap(operate, ind, 7)
		moved_list.append([int(final),num])
	
	elif ind==5:
		#Swop with Top Right
		#Push it on our queue
		final = swap(operate, ind, 2)
		moved_list.append([int(final),num])
		#Swop with Mid Left
		#Push it on our queue
		final = swap(operate, ind, 4)
		moved_list.append([int(final),num])
		#Swop with Bot Right
		#Push it on our queue
		final = swap(operate, ind, 8)
		moved_list.append([int(final),num])
	
	elif ind==6:
		#Swop with Mid Left
		#Push it on our queue
		final = swap(operate, ind, 3)
		moved_list.append([int(final),num])
		#Swop with Bot Mid
		#Push it on our queue
		final = swap(operate, ind, 7)
		moved_list.append([int(final),num])
		
	
	elif ind==7:
		#Swop with Mid Mid
		#Push it on our queue
		final = swap(operate, ind, 4)
		moved_list.append([int(final),num])
		#Swop with Bot Left
		#Push it on our queue
		final = swap(operate, ind, 6)
		moved_list.append([int(final),num])
		#Swop with Bot Right
		#Push it on our queue
		final = swap(operate, ind, 8)
		moved_list.append([int(final),num])
		
	
	elif ind==8:
		#Swop with Mid Right
		#Push it on our queue
		final = swap(operate, ind, 5)
		moved_list.append([int(final),num])
		#Swop with Bot Mid
		#Push it on our queue
		final = swap(operate, ind, 7)
		moved_list.append([int(final),num])

	return moved_list

#Input board
print("Enter Start State of board\n")
number = int(input())
solution = 123804765
#number = 321804965
#Create Queue
Q = []
#Queue contains (node, last node of level)
Q.append([number,111111111])		
#No. of moves
moves = 0
#No. of nodes
nodes = 0
last = number

while Q:
	#Dequeue
	x = Q.pop(0)
	nodes+=1
	
	if x[0]==last:
		moves+=1
	#Generate child of the node
	listing = make_move(x[0])
	
	#Remove previous move
	#Ones we visted and next move
	#Will be the same
	for i in listing:
		if i[0]==x[1]:
			listing.remove(i)
			break
	#Update last element of the current Board
	if listing[len(listing)-1][1]==last:
		last = 	listing[len(listing)-1][0]	
	#Loop through all possible states of the Board
	for i in listing:
		#Visualization of the Board
		visualGraph(i[0])
		#Find solution
		if i[0] == solution:
			print("Number of moves - " + str(moves+1))
			print("Number of nodes - " + str(nodes))
			print("Solution Found!")
			exit(0)
		Q.append(i)	
