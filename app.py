#!flask/bin/python
from flask import Flask
from flask import jsonify
import sys
from flask_script import Manager

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bye', methods=['GET'])
def good_bye():
    return jsonify({"comp_move": 'Good bye World!'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'})

@app.route('/tic_tac_toe/<user_moves>/<comp_moves>', methods=['GET'])
def retrieve_comp_move(user_moves = '0', comp_moves = '0'):
	database = populateDatabase()
	print('usermoves', user_moves.decode('utf-8'))
	print('compmoves', comp_moves.decode('utf-8'))
	board = createBoardGivenUserAndCompMoves(user_moves, comp_moves)
	print('board', board)
	try:
		comp_move_index = findProbableMove(database, board)
		print("this is the move I'm returning: {}".format(comp_move_index+1))
		return jsonify({"comp_move" : str(comp_move_index+1)})
	except:
	    return jsonify({"comp_move": "HI this didnt work!"})
#----------------------------------------------------------------------------------------
def createBoardGivenUserAndCompMoves(user_moves, comp_moves): 
	board = '---------'
	for x in user_moves: 
		if(x != '_' and int(x) > 0 and int(x) < 10): 
			index = int(x)-1
			board = board[:index] + 'X' + board[index+1:]
	for x in comp_moves: 
		if(x != '_' and int(x) > 0 and int(x) < 10): 
			index = int(x)-1
			board = board[:index] + 'O' + board[index+1:]
	return board
#----------------------------------------------------------------------------------------
def populateDatabase(): 
	db = getDictionaryFromOutfile()
	return db
# #----------------------------------------------------------------------------------------
def getDictionaryFromOutfile():
	outfile = open('database.txt', 'r')
	dict = eval(outfile.read())
	outfile.close()
	return dict
# #----------------------------------------------------------------------------------------
def findProbableMove(db, board):
	moves = db[board]
	print("here are the moves, i've found the board: ", moves)
	lst = [0]
	for x in range(len(moves)): 
		lst.append(float(moves[x])/sum(moves))
	print("probability list for this board:{}, is this:{} ".format(board, lst))
	rand = random()
	for x in range(1, len(lst)): 
		if sum(lst[0:x]) < rand < sum(lst[0:x+1]): return x-1
# #----------------------------------------------------------------------------------------
from random import random
#----------------------------------------------------------------------------------------
if __name__ == '__main__':
	app.run()


