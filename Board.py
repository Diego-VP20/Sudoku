import Utilities


class Board(Utilities.Utilities):

	def __init__(self):

		super(Board, self).__init__()

		self.field = [[(), (), (), (), (), (), (), (), ()],
		              [(), (), (), (), (), (), (), (), ()],
		              [(), (), (), (), (), (), (), (), ()],
		              [(), (), (), (), (), (), (), (), ()],
		              [(), (), (), (), (), (), (), (), ()],
		              [(), (), (), (), (), (), (), (), ()],
		              [(), (), (), (), (), (), (), (), ()],
		              [(), (), (), (), (), (), (), (), ()],
		              [(), (), (), (), (), (), (), (), ()]]

		# Sample

		self.field = [[("7", False), ("2", False), ("6", False), ("4", False), ("9", False), ("3", False), ("8", False), ("1", False), ("5", False)],
		              [("3", False), ("1", False), ("5", False), ("7", False), ("2", False), ("8", False), ("9", False), ("4", False), ("6", False)],
		              [("4", False), ("8", False), ("9", False), ("6", False), ("5", False), ("1", False), ("2", False), ("3", False), ("7", False)],
		              [("8", False), ("5", False), ("2", False), ("1", False), ("4", False), ("7", False), ("6", False), ("9", False), ("3", False)],
		              [("6", False), ("7", False), ("3", False), ("9", False), ("8", False), ("5", False), ("1", False), ("2", False), ("4", False)],
		              [("9", False), ("4", False), ("1", False), ("3", False), ("6", False), ("2", False), ("7", False), ("5", False), ("8", False)],
		              [("1", False), ("9", False), ("4", False), ("8", False), ("3", False), ("6", False), ("5", False), ("7", False), ("2", False)],
		              [("5", False), ("6", False), ("7", False), ("2", False), ("1", False), ("4", False), ("3", False), ("8", False), ("9", False)],
		              [("2", False), ("3", False), ("8", False), ("5", False), ("7", False), ("9", False), ("4", False), ("6", False), ("1", False)]]

		self.drawBoard()

	def drawBoard(self):

		super().clear()

		fields = self.field
		header = Utilities.CYAN + "   ┌───┬───┬───┐║┌───┬───┬───┐║┌───┬───┬───┐"
		intersection = Utilities.CYAN + "   ├───┼───┼───┤║├───┼───┼───┤║├───┼───┼───┤"
		separator = Utilities.CYAN + "   ═════════════╬═════════════╬═════════════"
		footer = Utilities.CYAN + "   └───┴───┴───┘║└───┴───┴───┘║└───┴───┴───┘"
		numerationHorizontal = Utilities.CYAN + "     1   2   3     4   5   6     7   8   9\n"

		print(numerationHorizontal)

		print(header)
		print(f"1  │ {fields[0][0][0]} │ {fields[0][1][0]} │ {fields[0][2][0]} │║│ {fields[0][3][0]} │ {fields[0][4][0]} │ {fields[0][5][0]} │║│ {fields[0][6][0]} │ {fields[0][7][0]} │ {fields[0][8][0]} │".replace("0", " "))
		print(intersection)

		print(f"2  │ {fields[1][0][0]} │ {fields[1][1][0]} │ {fields[1][2][0]} │║│ {fields[1][3][0]} │ {fields[1][4][0]} │ {fields[1][5][0]} │║│ {fields[1][6][0]} │ {fields[1][7][0]} │ {fields[1][8][0]} │".replace("0", " "))
		print(intersection)

		print(f"3  │ {fields[2][0][0]} │ {fields[2][1][0]} │ {fields[2][2][0]} │║│ {fields[2][3][0]} │ {fields[2][4][0]} │ {fields[2][5][0]} │║│ {fields[2][6][0]} │ {fields[2][7][0]} │ {fields[2][8][0]} │".replace("0", " "))
		print(footer)

		print(separator)

		print(header)
		print(f"4  │ {fields[3][0][0]} │ {fields[3][1][0]} │ {fields[3][2][0]} │║│ {fields[3][3][0]} │ {fields[3][4][0]} │ {fields[3][5][0]} │║│ {fields[3][6][0]} │ {fields[3][7][0]} │ {fields[3][8][0]} │".replace("0", " "))
		print(intersection)

		print(f"5  │ {fields[4][0][0]} │ {fields[4][1][0]} │ {fields[4][2][0]} │║│ {fields[4][3][0]} │ {fields[4][4][0]} │ {fields[4][5][0]} │║│ {fields[5][6][0]} │ {fields[5][7][0]} │ {fields[5][8][0]} │".replace("0", " "))
		print(intersection)

		print(f"6  │ {fields[5][0][0]} │ {fields[5][1][0]} │ {fields[5][2][0]} │║│ {fields[5][3][0]} │ {fields[5][4][0]} │ {fields[5][5][0]} │║│ {fields[5][6][0]} │ {fields[5][7][0]} │ {fields[5][8][0]} │".replace("0", " "))
		print(footer)

		print(separator)

		print(header)
		print(f"7  │ {fields[6][0][0]} │ {fields[6][1][0]} │ {fields[6][2][0]} │║│ {fields[6][3][0]} │ {fields[6][4][0]} │ {fields[6][5][0]} │║│ {fields[6][6][0]} │ {fields[6][7][0]} │ {fields[6][8][0]} │".replace("0", " "))
		print(intersection)

		print(f"8  │ {fields[7][0][0]} │ {fields[7][1][0]} │ {fields[7][2][0]} │║│ {fields[7][3][0]} │ {fields[7][4][0]} │ {fields[7][5][0]} │║│ {fields[7][6][0]} │ {fields[7][7][0]} │ {fields[7][8][0]} │".replace("0", " "))
		print(intersection)

		print(f"9  │ {fields[8][0][0]} │ {fields[8][1][0]} │ {fields[8][2][0]} │║│ {fields[8][3][0]} │ {fields[8][4][0]} │ {fields[8][5][0]} │║│ {fields[8][6][0]} │ {fields[8][7][0]} │ {fields[8][8][0]} │".replace("0", " "))
		print(footer)


board = Board()
