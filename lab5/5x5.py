import random

#Alunos:
#Caique de Paula Figueiredo Coelho
#Lucas Queiroz

def getBoardCopy(board):
	#Faz uma copia do quadro e retrona esta copia

	dupeBoard = []

	for i in board:
		dupeBoard.append(i)

	return dupeBoard

def drawBoard(board):

	#Esta funcao imprime o quadro do jogo
	#O quadro eh uma lista de 9 strings representando o qaudro
	copyBoard = getBoardCopy(board)

	for i in range(1,26):
		if(board[i] == ''):
			copyBoard[i] = str(i)
		else:
			copyBoard[i] = board[i]

	print(' ' + copyBoard[21] + ' | ' + copyBoard[22] + ' | ' + copyBoard[23]+ '  | '  + copyBoard[24]+ ' | ' + copyBoard[25])
	print('-------------------------')
	print(' ' + copyBoard[16] + ' | ' + copyBoard[17] + ' | ' + copyBoard[18]+ '  | ' + copyBoard[19]+ ' | ' + copyBoard[20])
	#print(' | |')
	print('-------------------------')
	print(' ' + copyBoard[11] + ' | ' + copyBoard[12] + ' | ' + copyBoard[13]+ '  | ' + copyBoard[14]+ ' | ' + copyBoard[15])
	#print(' | |')
	print('-------------------------')
	#print(' | |')
	print(' '+ copyBoard[6] + '  | ' + copyBoard[7] + '  |  ' + copyBoard[8]+ '  |  ' + copyBoard[9] + ' | ' + copyBoard[10])
	#print(' | |')
	print('-------------------------')
	#print(' | |')
	print(' '+ copyBoard[1] + '  | ' + copyBoard[2] + '  |  ' + copyBoard[3]+ '  |  ' + copyBoard[4]+ ' | ' + copyBoard[5])
	print(' ')
	#print(' | |')
	print('***************************************************')
	#print(' | |')
	print(' ')

def inputPlayerLetter():
	#O jogador escolumnahe com qual letra ele quer jogar "X" ou "O"
	#Retorna uma lista com a letra do jogador e a letra do computador
	letter = ''
	while not(letter == 'X' or letter == 'O'):
		print('Voce quer ser X ou O?')
		letter = input().upper()
		if(letter != 'X' and letter != 'O'):
			print("Entre apenas com a letra X(xis) se voce quer ser X ou com a letra O(oh) se voce quer ser O!")

	#O primeiro elemento na lista eh o do jogador e o segundo do computador
	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

def whoGoesFirts():
	#Escolumnahe aleatoriamente o jogador que jogara primeiro
	if random.randint(0, 1) == 0:
		return 'computador'
	else:
		return 'jogador'

def makeMove(board, letter, move,nro):
	#Faz o movimento do computador ou do jogador a depender do letter no quadro



	board[move] = letter

def isWinner(brd, let ,nro):

	#Dado un marco y una letra, esta función devuelve True si la letra se da en el juego.
	#-----------izquierda a derecha
	return((brd[1] == let and brd[2] == let and brd[3] == let) or #linha de cima
		    ((brd[6] == let and brd[7] == let and brd[8] == let) and nro>19) or #linha do meio
		    ((brd[11] == let and brd[12] == let and brd[13] == let) and nro>19)  or #linha de baixo
		    (brd[16] == let and brd[17] == let and brd[18] == let) or #columnauna da esquerda
		    (brd[21] == let and brd[22] == let and brd[23] == let) or #columnauna do meio
		    (brd[3] == let and brd[4] == let and brd[5] == let) or #columnauna da direito
		  	((brd[8] == let and brd[9] == let and brd[10] == let)  and nro>19)  or #diagonal principal
		    ((brd[13] == let and brd[14] == let and brd[15] == let) and nro>19)  or
		    (brd[18] == let and brd[19] == let and brd[20] == let) or
		    (brd[23] == let and brd[24] == let and brd[25] == let)or
			(brd[2] == let and brd[3] == let and brd[4] == let)or
			((brd[7] == let and brd[8] == let and brd[9] == let)  and nro>19) or
			((brd[12] == let and brd[13] == let and brd[14] == let) and nro>19) or
			(brd[17] == let and brd[18] == let and brd[19] == let)or
			(brd[22] == let and brd[23] == let and brd[24] == let)or
			#de abajo a arriba
 			(brd[1] == let and brd[6] == let and brd[11] == let)or
			((brd[2] == let and brd[7] == let and brd[12] == let)  and nro>19) or
			((brd[3] == let and brd[8] == let and brd[13] == let)  and nro>19) or
			(brd[4] == let and brd[9] == let and brd[14] == let)or
			(brd[5] == let and brd[10] == let and brd[15] == let)or
			(brd[6] == let and brd[11] == let and brd[16] == let)or
			((brd[7] == let and brd[12] == let and brd[17] == let)  and nro>19) or
			((brd[8] == let and brd[13] == let and brd[18] == let)  and nro>19) or
			(brd[9] == let and brd[14] == let and brd[19] == let)or
			(brd[10] == let and brd[15] == let and brd[20] == let)or
			(brd[11] == let and brd[16] == let and brd[21] == let)or
			((brd[12] == let and brd[17] == let and brd[22] == let)  and nro>19) or
			((brd[13] == let and brd[18] == let and brd[23] == let)  and nro>19) or
			(brd[14] == let and brd[19] == let and brd[24] == let)or
			(brd[15] == let and brd[20] == let and brd[25] == let)or
			 #diagonal 1
			((brd[11] == let and brd[7] == let and brd[3] == let)  and nro>19) or
			((brd[16] == let and brd[12] == let and brd[8] == let)  and nro>19) or
			((brd[12] == let and brd[8] == let and brd[4] == let)  and nro>19) or
			((brd[21] == let and brd[17] == let and brd[13] == let)  and nro>19) or
			((brd[17] == let and brd[13] == let and brd[9] == let)  and nro>19) or
			((brd[13] == let and brd[9] == let and brd[5] == let)  and nro>19) or
			(brd[22] == let and brd[18] == let and brd[14] == let)or
			(brd[18] == let and brd[14] == let and brd[10] == let)or
			(brd[23] == let and brd[19] == let and brd[15] == let)or
			 #diagonal 2
			(brd[15] == let and brd[9] == let and brd[3] == let)or
			((brd[20] == let and brd[14] == let and brd[8] == let) and nro>19) or
			((brd[14] == let and brd[8] == let and brd[2] == let) and nro>19) or
			((brd[25] == let and brd[19] == let and brd[13] == let)  and nro>19) or
			((brd[19] == let and brd[13] == let and brd[7] == let)  and nro>19) or
			((brd[13] == let and brd[7] == let and brd[1] == let)  and nro>19) or
			((brd[24] == let and brd[18] == let and brd[12] == let)  and nro>19) or
			((brd[18] == let and brd[12] == let and brd[6] == let)  and nro>19) or
			(brd[23] == let and brd[17] == let and brd[11] == let))  #diagonal secundaria

def isSpaceFree(board, move):
	#Retorna true se o espaco solicitado esta livre no quadro
	if(board[move] == ''):
		return True
	else:
		return False

def getPlayerMove(board,nrot):
	#Recebe o movimento do jogador
	move = ''
	while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'.split() or not isSpaceFree(board, int(move)):
		print('Qual eh o seu proximo movimento? (1-25)')
		move = input();
		if(move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'):
			print("MOVIMENTO INVALIDO! INSIRA UM NUMERO ENTRE 1 E 9!")

		if nrot<20 and move=='7' or move=='8' or move=='12' or move=='13':
			
			print("¡cambie de numero!")
			move = input(); #se ingresa un movimiento
		
		if(move in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'):
			if(not isSpaceFree(board, int(move))):
				print("ESPACO INSDISPONIVEL! ESCOLHA OUTRO ESPACO ENTRE 1 E 9 O QUAL O NUMERO ESTA DISPONIVEL NO QUADRO!")

	return int(move)

def chooseRandomMoveFromList(board, movesList):
	#Retorna um movimento valido aleatorio
	#Retorna None se nao possui movimentos validos

	possiveisMovimentos = []
	for i in movesList:
		if isSpaceFree(board, i):
			possiveisMovimentos.append(i)

	if len(possiveisMovimentos) != 0:
		return random.choice(possiveisMovimentos)
	else:
		return None


def isBoardFull(board):
	#Devuelve True si todos los espacios de marco no están disponibles
	for i in range(1,26):
		if isSpaceFree(board, i):
			return False
	return True

def possiveisOpcoes(board,inicio,final,nrot):
	#Devuelve una lista de todos los espacios en el marco que están disponibles

	opcoes = []

	for i in range(inicio, final):
		if nrot<20 and (i==7 or i==8 or i==12 or i == 13):
			continue
		elif isSpaceFree(board, i):
			opcoes.append(i)

	return opcoes

def finishGame(board, computerLetter):
	#Verifica se o jogo chegou ao final
	#Retorna -1 se o jogador ganha
	#Retorna 1 se o computador ganha
	#Retorna 0 se o jogo termina empatado
	#Retorna None se o jogo nao terminou

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if(isWinner(board, computerLetter,nro)):
		return 1

	elif(isWinner(board, playerLetter,nro)):
		return -1

	elif(isBoardFull(board)):
		return 0

	else:
		return None


def alphabeta(board, computerLetter, turn, alpha, beta,nro,inicio,final):
	#Fazemos aqui a poda alphabeta

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if turn == computerLetter:
		nextTurn = playerLetter
	else:
		nextTurn = computerLetter

	finish = finishGame(board, computerLetter)

	if (finish != None):
		return finish

	possiveis = possiveisOpcoes(board,inicio,final,nro)

	if turn == computerLetter:
		for move in possiveis:
			makeMove(board, turn, move,nro)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta,nro,inicio,final)
			makeMove(board, '', move,nro)
			if val > alpha:
				alpha = val

			if alpha >= beta:
				return alpha
		return alpha

	else:
		for move in possiveis:
			makeMove(board, turn, move,nro)
			val = alphabeta(board, computerLetter, nextTurn, alpha, beta,nro,inicio,final)
			makeMove(board, '', move,nro)
			if val < beta:
				beta = val

			if alpha >= beta:
				return beta
		return beta



def getComputerMove(board, turn, computerLetter,nro,move2):
	#Definimos aqui qual sera o movimento do computador
	inicio = 0
	final = 25
	a = -2
	opcoes = []

	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	if nro>8:
		inicio = 1
		final = 26

	if move2>=1 and move2 <= 10 and nro>4:
		inicio = 1
		final = 20
	
	if move2>=11 and move2 <= 15 and nro>4:
		inicio = 1
		final = 22
	if move2>=16 and move2 <= 26 and nro>4:
		inicio = 6
		final = 25

	if move2 <=10 and nro<=4:
		inicio = 1
		final = 16
	if move2 >= 11 and move2 <=15 and nro<=4:
		inicio = 6
		final = 20
	if move2 >= 16 and move2 <=26 and nro<=4:
		inicio = 11
		final = 25

	#if len(possiveisOpcoes(board)) == 9:
	#	return 5

	#Comecamos aqui o MiniMax
	#Primeiro chechamos se podemos ganhar no proximo movimento
	for i in range(inicio, final):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i,nro)
			if isWinner(copy, computerLetter,nro):
				return i

	#Checa se o jogador pode vencer no proximo movimento e bloqueia
	for i in range(inicio, final):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i,nro)
			if isWinner(copy, playerLetter,nro):
				return i

	possiveisOpcoesOn = possiveisOpcoes(board,inicio,final,nro)

	for move in possiveisOpcoesOn:

		makeMove(board, computerLetter, move,nro)
		val = alphabeta(board, computerLetter, playerLetter, -2, 2,nro,inicio,final)		
		makeMove(board, '', move,nro)

		if val > a:
			a = val
			opcoes = [move]

		elif val == a:
			opcoes.append(move)

	return random.choice(opcoes)

print('Vamos a jugar el juego del gato!')
print('las casillas 7 8 12 14 se habilitaran faltando 6 movimientos ')


jogar = True

while jogar:
	#Reseta o jogo
	theBoard = [''] * 26
	print(theBoard)
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirts()
	nro=0
	
	if turn == 'jogador':
		print('X ' + turn +' Juega primero,')
	else:
		print('O ' + turn +' Juega primero,')
		


	gameisPlaying = True
    

	while gameisPlaying:
		if turn == 'jogador':
			#Vez do Jogador
			drawBoard(theBoard)
			nro=nro+1
			move = getPlayerMove(theBoard,nro)
			makeMove(theBoard, playerLetter, move,nro)
			move2=move

			if isWinner(theBoard, playerLetter,nro):
				drawBoard(theBoard)
				print('Woooow! Voce venceu o jogo!')
				gameisPlaying = False
			
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('O jogo terminou empatado')
					break
				else:
					turn = 'computador'

		else:
			#Vez do computador
			drawBoard(theBoard)
			nro=nro+1
			if nro==1:
				rand=random.randint(0,20)
				makeMove(theBoard, computerLetter, rand,nro)
			else:
				move = getComputerMove(theBoard, playerLetter, computerLetter,nro,move2)
				makeMove(theBoard, computerLetter, move,nro)

			if isWinner(theBoard, computerLetter,nro):
				drawBoard(theBoard)
				print("O computador venceu :(")
				gameisPlaying = False

			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('O jogo terminou empatado')
					break
				else:
					turn = 'jogador'

	letterNew = ''
	while not(letterNew == 'S' or letterNew == 'N'):
		print("Voce quer jogar novamente? Digite S(para sim) ou N(para nao)")
		letterNew = input().upper()
		if (letterNew != 'S' and letterNew != 'N'):
			print("Entrada invalida! Digite S(para sim) ou N(para nao)!")
		if(letterNew == 'N'):
			print("Foi bom jogar com voce! Ate mais!")
			jogar = False