def validNumber(displayText = 'Pick a location:', numberRange = [0, 2]):
	while True:
		inputNumber = raw_input(displayText)
		
		try:
			int(inputNumber)
			
		except:
			print 'Input must be a number.'
			
		try:
			if int(inputNumber) >= int(numberRange[0]) and int(inputNumber) <= int(numberRange[1]):
				return int(inputNumber)
			
			else:
				print 'The number must be between ' + str(numberRange[0]) + ' and ' + str(numberRange[1])
				
		except:
			print 'The number must be between ' + str(numberRange[0]) + ' and ' + str(numberRange[1])

def initBoard():
	board = [['  ', ' ', '  '],
			 ['  ', ' ', '  '],
			 ['  ', ' ', '  ']]
			 
	global board
	
def printBoard():
	for count0 in xrange(len(board)):
		for count1 in xrange(len(board[count0])):
			print board[count0][count1],
			
			if count1 < 2:
				print '|',
			
			if count1 >= 2:
				print

		if count0 < 2:
			print '---|---|---'
			
		else:
			print
			print '---------------'
			
def changeBoard(Xcoord, Ycoord, player = 1):
	if player == 0:
		character = characters[1]
			
	else:
		character = characters[0]
	
	if board[Ycoord][Xcoord] == ' ':
		board[Ycoord][Xcoord] = character
		
		return False
		
	elif board[Ycoord][Xcoord] == '  ':
		board[Ycoord][Xcoord] = ' ' + character
		
		return False
		
	else:
		return True
		
def testVictory():
	winnerChar = ''
	
	for count in xrange(len(board)):
		if board[count][0].strip() == board[count][1].strip() == board[count][2].strip():
			winnerChar = board[count][0].strip()
			
		if board[0][count].strip() == board[1][count].strip() == board[2][count].strip():
			winnerChar = board[0][count].strip()
			
	if board[0][0].strip() == board[1][1].strip() == board[2][2].strip():
		winnerChar = board[1][1].strip()
		
	if board[0][2].strip() == board[1][1].strip() == board[2][0].strip():
		winnerChar = board[1][1].strip()
		
	if winnerChar == characters[1]:
		print 'The winner is the player.'
		
		return 1
		
	elif winnerChar == characters[0]:
		print 'The winner is the computer.'
		
		return 2
	
	else:
		return 0
		
def computerPlay():
	for currentCheck in characters:
		for count in xrange(len(board)):
			if board[count][0].strip() == '' and currentCheck == board[count][1].strip() == board[count][2].strip():
				changeBoard(count, 0)
			
			elif board[count][1].strip() == '' and board[count][0].strip() == currentCheck == board[count][2].strip():
				changeBoard(count, 1)
				
			elif board[count][2].strip() == '' and board[count][0].strip() == board[count][1].strip() == currentCheck:
				changeBoard(count, 2)
				
			elif board[0][count].strip() == '' and currentCheck == board[1][count].strip() == board[2][count].strip():
				changeBoard(0, count)
				
			elif board[1][count].strip() == '' and board[0][count].strip() == currentCheck == board[2][count].strip():
				changeBoard(1, count)
				
			elif board[2][count].strip() == '' and board[0][count].strip() == board[1][count].strip() == currentCheck:
				changeBoard(1, count)
				
		if board[0][0].strip() == '' and currentCheck == board[1][1].strip() == board[2][2].strip():
			changeBoard(0, 0)
			
		elif board[1][1].strip() == '' and board[0][0].strip() == currentCheck == board[2][2].strip():
			changeBoard(1, 1)
			
		elif board[2][2].strip() == '' and board[0][0].strip() == board[1][1].strip() == currentCheck:
			changeBoard(2, 2)
			
		elif board[0][2].strip() == '' and currentCheck == board[1][1].strip() == board[2][0].strip():
			changeBoard(0, 2)
			
		elif board[1][1].strip() == '' and board[0][2].strip() == currentCheck == board[2][0].strip():
			changeBoard(1, 1)
			
		elif board[2][0].strip() == '' and board[0][2].strip() == board[1][1].strip() == currentCheck:
			changeBoard(2, 0)
			
	

characters = ['O', 'X']
initBoard()
printBoard()
victor = False
while not victor:
	while changeBoard(validNumber('"X" coordinate:'), validNumber('"Y" coordinate:'), 0):
		print 'That location has already been taken.'
		print '---------------'
	printBoard()
	
	computerPlay()
	
	victor = testVictory()
	
	
