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

		self.field = [[("7", False), ("2", True), ("6", False), ("4", False), ("9", False), ("3", False), ("8", False),
		               ("1", False), ("5", False)],
		              [("3", False), ("1", False), ("5", False), ("7", False), ("2", False), ("8", False), ("9", False),
		               ("4", False), ("6", False)],
		              [("4", False), ("8", False), ("9", False), ("6", False), ("5", False), ("1", False), ("2", False),
		               ("3", False), ("7", False)],
		              [("8", False), ("5", False), ("2", False), ("1", False), ("4", False), ("7", False), ("6", False),
		               ("9", False), ("3", False)],
		              [("6", False), ("7", False), ("3", False), ("9", False), ("8", False), ("5", False), ("1", False),
		               ("2", False), ("4", False)],
		              [("9", False), ("4", False), ("1", False), ("3", False), ("6", False), ("2", False), ("7", False),
		               ("5", False), ("8", False)],
		              [("1", False), ("9", False), ("4", False), ("8", False), ("3", False), ("6", False), ("5", False),
		               ("7", False), ("2", False)],
		              [("5", False), ("6", False), ("7", False), ("2", False), ("1", False), ("4", False), ("3", False),
		               ("8", False), ("9", False)],
		              [("2", False), ("3", False), ("8", False), ("5", False), ("7", False), ("9", False), ("4", False),
		               ("6", False), ("1", False)]]

		#self.drawBoard()

	def drawBoard(self):
		super().clear()

		fields = self.field
		header = Utilities.CYAN + "   ┌───┬───┬───┐║┌───┬───┬───┐║┌───┬───┬───┐"
		intersection = Utilities.CYAN + "   ├───┼───┼───┤║├───┼───┼───┤║├───┼───┼───┤"
		separator = Utilities.CYAN + "   ═════════════╬═════════════╬═════════════"
		footer = Utilities.CYAN + "   └───┴───┴───┘║└───┴───┴───┘║└───┴───┴───┘"
		numerationHorizontal = Utilities.CYAN + "     A   B   C     D   E   F     G   H   J\n"

		print(numerationHorizontal)

		# s = "At least, that's what {pronoun} told me.".format(pronoun="he" if gender == "male" else "she")

		oneOne = "{field1}".format(field1=Utilities.RED + fields[0][0][0].replace("0", " ") + Utilities.CYAN if fields[0][0][1] else Utilities.BLUE + fields[0][0][0].replace("0", "") + Utilities.CYAN)
		oneTwo = "{field1}".format(field1=Utilities.RED + fields[0][1][0].replace("0", " ") + Utilities.CYAN if fields[0][1][1] else Utilities.BLUE + fields[0][1][0].replace("0", "") + Utilities.CYAN)
		oneThree = "{field1}".format(field1=Utilities.RED + fields[0][2][0].replace("0", " ") + Utilities.CYAN if fields[0][2][1] else Utilities.BLUE + fields[0][2][0].replace("0", "") + Utilities.CYAN)
		oneFour = "{field1}".format(field1=Utilities.RED + fields[0][3][0].replace("0", " ") + Utilities.CYAN if fields[0][3][1] else Utilities.BLUE + fields[0][3][0].replace("0", "") + Utilities.CYAN)
		oneFive = "{field1}".format(field1=Utilities.RED + fields[0][4][0].replace("0", " ") + Utilities.CYAN if fields[0][4][1] else Utilities.BLUE + fields[0][4][0].replace("0", "") + Utilities.CYAN)
		oneSix = "{field1}".format(field1=Utilities.RED + fields[0][5][0].replace("0", " ") + Utilities.CYAN if fields[0][5][1] else Utilities.BLUE + fields[0][5][0].replace("0", "") + Utilities.CYAN)
		oneSeven = "{field1}".format(field1=Utilities.RED + fields[0][6][0].replace("0", " ") + Utilities.CYAN if fields[0][6][1] else Utilities.BLUE + fields[0][6][0].replace("0", "") + Utilities.CYAN)
		oneEight = "{field1}".format(field1=Utilities.RED + fields[0][7][0].replace("0", " ") + Utilities.CYAN if fields[0][7][1] else Utilities.BLUE + fields[0][7][0].replace("0", "") + Utilities.CYAN)
		oneNine = "{field1}".format(field1=Utilities.RED + fields[0][8][0].replace("0", " ") + Utilities.CYAN if fields[0][8][1] else Utilities.BLUE + fields[0][8][0].replace("0", "") + Utilities.CYAN)

		twoOne = "{field1}".format(field1=Utilities.RED + fields[1][0][0].replace("0", " ") + Utilities.CYAN if fields[1][0][1] else Utilities.BLUE + fields[1][0][0].replace("0", "") + Utilities.CYAN)
		twoTwo = "{field1}".format(field1=Utilities.RED + fields[1][1][0].replace("0", " ") + Utilities.CYAN if fields[1][1][1] else Utilities.BLUE + fields[1][1][0].replace("0", "") + Utilities.CYAN)
		twoThree = "{field1}".format(field1=Utilities.RED + fields[1][2][0].replace("0", " ") + Utilities.CYAN if fields[1][2][1] else Utilities.BLUE + fields[1][2][0].replace("0", "") + Utilities.CYAN)
		twoFour = "{field1}".format(field1=Utilities.RED + fields[1][3][0].replace("0", " ") + Utilities.CYAN if fields[1][3][1] else Utilities.BLUE + fields[1][3][0].replace("0", "") + Utilities.CYAN)
		twoFive = "{field1}".format(field1=Utilities.RED + fields[1][4][0].replace("0", " ") + Utilities.CYAN if fields[1][4][1] else Utilities.BLUE + fields[1][4][0].replace("0", "") + Utilities.CYAN)
		twoSix = "{field1}".format(field1=Utilities.RED + fields[1][5][0].replace("0", " ") + Utilities.CYAN if fields[1][5][1] else Utilities.BLUE + fields[1][5][0].replace("0", "") + Utilities.CYAN)
		twoSeven = "{field1}".format(field1=Utilities.RED + fields[1][6][0].replace("0", " ") + Utilities.CYAN if fields[1][6][1] else Utilities.BLUE + fields[1][6][0].replace("0", "") + Utilities.CYAN)
		twoEight = "{field1}".format(field1=Utilities.RED + fields[1][7][0].replace("0", " ") + Utilities.CYAN if fields[1][7][1] else Utilities.BLUE + fields[1][7][0].replace("0", "") + Utilities.CYAN)
		twoNine = "{field1}".format(field1=Utilities.RED + fields[1][8][0].replace("0", " ") + Utilities.CYAN if fields[1][8][1] else Utilities.BLUE + fields[1][8][0].replace("0", "") + Utilities.CYAN)

		threeOne = "{field1}".format(field1=Utilities.RED + fields[2][0][0].replace("0", "") + Utilities.CYAN if fields[2][0][1] else Utilities.BLUE + fields[2][0][0].replace("0", "") + Utilities.CYAN)
		threeTwo = "{field1}".format(field1=Utilities.RED + fields[2][1][0].replace("0", "") + Utilities.CYAN if fields[2][1][1] else Utilities.BLUE + fields[2][1][0].replace("0", "") + Utilities.CYAN)
		threeThree = "{field1}".format(field1=Utilities.RED + fields[2][2][0].replace("0", "") + Utilities.CYAN if fields[2][2][1] else Utilities.BLUE + fields[2][2][0].replace("0", "") + Utilities.CYAN)
		threeFour = "{field1}".format(field1=Utilities.RED + fields[2][3][0].replace("0", "") + Utilities.CYAN if fields[2][3][1] else Utilities.BLUE + fields[2][3][0].replace("0", "") + Utilities.CYAN)
		threeFive = "{field1}".format(field1=Utilities.RED + fields[2][4][0].replace("0", "") + Utilities.CYAN if fields[2][4][1] else Utilities.BLUE + fields[2][4][0].replace("0", "") + Utilities.CYAN)
		threeSix = "{field1}".format(field1=Utilities.RED + fields[2][5][0].replace("0", "") + Utilities.CYAN if fields[2][5][1] else Utilities.BLUE + fields[2][5][0].replace("0", "") + Utilities.CYAN)
		threeSeven = "{field1}".format(field1=Utilities.RED + fields[2][6][0].replace("0", "") + Utilities.CYAN if fields[2][6][1] else Utilities.BLUE + fields[2][6][0].replace("0", "") + Utilities.CYAN)
		threeEight = "{field1}".format(field1=Utilities.RED + fields[2][7][0].replace("0", "") + Utilities.CYAN if fields[2][7][1] else Utilities.BLUE + fields[2][7][0].replace("0", "") + Utilities.CYAN)
		threeNine = "{field1}".format(field1=Utilities.RED + fields[2][8][0].replace("0", "") + Utilities.CYAN if fields[2][8][1] else Utilities.BLUE + fields[2][8][0].replace("0", "") + Utilities.CYAN)

		fourOne = "{field1}".format(field1=Utilities.RED + fields[3][0][0].replace("0", "") + Utilities.CYAN if fields[3][0][1] else Utilities.BLUE + fields[3][0][0] .replace("0", "") + Utilities.CYAN)
		fourTwo = "{field1}".format(field1=Utilities.RED + fields[3][1][0].replace("0", "") + Utilities.CYAN if fields[3][1][1] else Utilities.BLUE + fields[3][1][0].replace("0", "") + Utilities.CYAN)
		fourThree = "{field1}".format(field1=Utilities.RED + fields[3][2][0].replace("0", "") + Utilities.CYAN if fields[3][2][1] else Utilities.BLUE + fields[3][2][0].replace("0", "") + Utilities.CYAN)
		fourFour = "{field1}".format(field1=Utilities.RED + fields[3][3][0].replace("0", "") + Utilities.CYAN if fields[3][3][1] else Utilities.BLUE + fields[3][3][0].replace("0", "") + Utilities.CYAN)
		fourFive = "{field1}".format(field1=Utilities.RED + fields[3][4][0].replace("0", "") + Utilities.CYAN if fields[3][4][1] else Utilities.BLUE + fields[3][4][0].replace("0", "") + Utilities.CYAN)
		fourSix = "{field1}".format(field1=Utilities.RED + fields[3][5][0].replace("0", "") + Utilities.CYAN if fields[3][5][1] else Utilities.BLUE + fields[3][5][0].replace("0", "") + Utilities.CYAN)
		fourSeven = "{field1}".format(field1=Utilities.RED + fields[3][6][0].replace("0", "") + Utilities.CYAN if fields[3][6][1] else Utilities.BLUE + fields[3][6][0].replace("0", "") + Utilities.CYAN)
		fourEight = "{field1}".format(field1=Utilities.RED + fields[3][7][0].replace("0", "") + Utilities.CYAN if fields[3][7][1] else Utilities.BLUE + fields[3][7][0].replace("0", "") + Utilities.CYAN)
		fourNine = "{field1}".format(field1=Utilities.RED + fields[3][8][0].replace("0", "") + Utilities.CYAN if fields[3][8][1] else Utilities.BLUE + fields[3][8][0].replace("0", "") + Utilities.CYAN)

		fiveOne = "{field1}".format(field1=Utilities.RED + fields[4][0][0].replace("0", "") + Utilities.CYAN if fields[4][0][1] else Utilities.BLUE + fields[4][0][0].replace("0", "") + Utilities.CYAN)
		fiveTwo = "{field1}".format(field1=Utilities.RED + fields[4][1][0].replace("0", "") + Utilities.CYAN if fields[4][1][1] else Utilities.BLUE + fields[4][1][0].replace("0", "") + Utilities.CYAN)
		fiveThree = "{field1}".format(field1=Utilities.RED + fields[4][2][0].replace("0", "") + Utilities.CYAN if fields[4][2][1] else Utilities.BLUE + fields[4][2][0].replace("0", "") + Utilities.CYAN)
		fiveFour = "{field1}".format(field1=Utilities.RED + fields[4][3][0].replace("0", "") + Utilities.CYAN if fields[4][3][1] else Utilities.BLUE + fields[4][3][0].replace("0", "") + Utilities.CYAN)
		fiveFive = "{field1}".format(field1=Utilities.RED + fields[4][4][0].replace("0", "") + Utilities.CYAN if fields[4][4][1] else Utilities.BLUE + fields[4][4][0].replace("0", "") + Utilities.CYAN)
		fiveSix = "{field1}".format(field1=Utilities.RED + fields[4][5][0].replace("0", "") + Utilities.CYAN if fields[4][5][1] else Utilities.BLUE + fields[4][5][0].replace("0", "") + Utilities.CYAN)
		fiveSeven = "{field1}".format(field1=Utilities.RED + fields[4][6][0].replace("0", "") + Utilities.CYAN if fields[4][6][1] else Utilities.BLUE + fields[4][6][0].replace("0", "") + Utilities.CYAN)
		fiveEight = "{field1}".format(field1=Utilities.RED + fields[4][7][0].replace("0", "") + Utilities.CYAN if fields[4][7][1] else Utilities.BLUE + fields[4][7][0].replace("0", "") + Utilities.CYAN)
		fiveNine = "{field1}".format(field1=Utilities.RED + fields[4][8][0].replace("0", "") + Utilities.CYAN if fields[4][8][1] else Utilities.BLUE + fields[4][8][0].replace("0", "") + Utilities.CYAN)

		sixOne = "{field1}".format(field1=Utilities.RED + fields[5][0][0].replace("0", "") + Utilities.CYAN if fields[5][0][1] else Utilities.BLUE + fields[5][0][0] .replace("0", " ") + Utilities.CYAN)
		sixTwo = "{field1}".format(field1=Utilities.RED + fields[5][1][0].replace("0", "") + Utilities.CYAN if fields[5][1][1] else Utilities.BLUE + fields[5][1][0].replace("0", " ") + Utilities.CYAN)
		sixThree = "{field1}".format(field1=Utilities.RED + fields[5][2][0].replace("0", "") + Utilities.CYAN if fields[5][2][1] else Utilities.BLUE + fields[5][2][0].replace("0", " ") + Utilities.CYAN)
		sixFour = "{field1}".format(field1=Utilities.RED + fields[5][3][0].replace("0", "") + Utilities.CYAN if fields[5][3][1] else Utilities.BLUE + fields[5][3][0].replace("0", " ") + Utilities.CYAN)
		sixFive = "{field1}".format(field1=Utilities.RED + fields[5][4][0].replace("0", "") + Utilities.CYAN if fields[5][4][1] else Utilities.BLUE + fields[5][4][0].replace("0", " ") + Utilities.CYAN)
		sixSix = "{field1}".format(field1=Utilities.RED + fields[5][5][0].replace("0", "") + Utilities.CYAN if fields[5][5][1] else Utilities.BLUE + fields[5][5][0].replace("0", " ") + Utilities.CYAN)
		sixSeven = "{field1}".format(field1=Utilities.RED + fields[5][6][0].replace("0", "") + Utilities.CYAN if fields[5][6][1] else Utilities.BLUE + fields[5][6][0].replace("0", " ") + Utilities.CYAN)
		sixEight = "{field1}".format(field1=Utilities.RED + fields[5][7][0].replace("0", "") + Utilities.CYAN if fields[5][7][1] else Utilities.BLUE + fields[5][7][0].replace("0", " ") + Utilities.CYAN)
		sixNine = "{field1}".format(field1=Utilities.RED + fields[5][8][0].replace("0", " ") + Utilities.CYAN if fields[5][8][1] else Utilities.BLUE + fields[5][8][0].replace("0", " ") + Utilities.CYAN)

		sevenOne = "{field1}".format(field1=Utilities.RED + fields[6][0][0].replace("0", " ") + Utilities.CYAN if fields[6][0][1] else Utilities.BLUE + fields[6][0][0] .replace("0", " ") + Utilities.CYAN)
		sevenTwo = "{field1}".format(field1=Utilities.RED + fields[6][1][0].replace("0", " ") + Utilities.CYAN if fields[6][1][1] else Utilities.BLUE + fields[6][1][0].replace("0", " ") + Utilities.CYAN)
		sevenThree = "{field1}".format(field1=Utilities.RED + fields[6][2][0].replace("0", " ") + Utilities.CYAN if fields[6][2][1] else Utilities.BLUE + fields[6][2][0].replace("0", " ") + Utilities.CYAN)
		sevenFour = "{field1}".format(field1=Utilities.RED + fields[6][3][0].replace("0", " ") + Utilities.CYAN if fields[6][3][1] else Utilities.BLUE + fields[6][3][0].replace("0", " ") + Utilities.CYAN)
		sevenFive = "{field1}".format(field1=Utilities.RED + fields[6][4][0].replace("0", " ") + Utilities.CYAN if fields[6][4][1] else Utilities.BLUE + fields[6][4][0].replace("0", " ") + Utilities.CYAN)
		sevenSix = "{field1}".format(field1=Utilities.RED + fields[6][5][0].replace("0", " ") + Utilities.CYAN if fields[6][5][1] else Utilities.BLUE + fields[6][5][0].replace("0", " ") + Utilities.CYAN)
		sevenSeven = "{field1}".format(field1=Utilities.RED + fields[6][6][0].replace("0", " ") + Utilities.CYAN if fields[6][6][1] else Utilities.BLUE + fields[6][6][0].replace("0", " ") + Utilities.CYAN)
		sevenEight = "{field1}".format(field1=Utilities.RED + fields[6][7][0].replace("0", " ") + Utilities.CYAN if fields[6][7][1] else Utilities.BLUE + fields[6][7][0].replace("0", " ") + Utilities.CYAN)
		sevenNine = "{field1}".format(field1=Utilities.RED + fields[6][8][0].replace("0", " ") + Utilities.CYAN if fields[6][8][1] else Utilities.BLUE + fields[6][8][0].replace("0", " ") + Utilities.CYAN)

		eightOne = "{field1}".format(field1=Utilities.RED + fields[7][0][0].replace("0", " ") + Utilities.CYAN if fields[7][0][1] else Utilities.BLUE + fields[7][0][0].replace("0", " ") + Utilities.CYAN)
		eightTwo = "{field1}".format(field1=Utilities.RED + fields[7][1][0].replace("0", " ") + Utilities.CYAN if fields[7][1][1] else Utilities.BLUE + fields[7][1][0].replace("0", " ") + Utilities.CYAN)
		eightThree = "{field1}".format(field1=Utilities.RED + fields[7][2][0].replace("0", " ") + Utilities.CYAN if fields[7][2][1] else Utilities.BLUE + fields[7][2][0].replace("0", " ") + Utilities.CYAN)
		eightFour = "{field1}".format(field1=Utilities.RED + fields[7][3][0].replace("0", " ") + Utilities.CYAN if fields[7][3][1] else Utilities.BLUE + fields[7][3][0].replace("0", " ") + Utilities.CYAN)
		eightFive = "{field1}".format(field1=Utilities.RED + fields[7][4][0].replace("0", " ") + Utilities.CYAN if fields[7][4][1] else Utilities.BLUE + fields[7][4][0].replace("0", " ") + Utilities.CYAN)
		eightSix = "{field1}".format(field1=Utilities.RED + fields[7][5][0].replace("0", " ") + Utilities.CYAN if fields[7][5][1] else Utilities.BLUE + fields[7][5][0].replace("0", " ") + Utilities.CYAN)
		eightSeven = "{field1}".format(field1=Utilities.RED + fields[7][6][0].replace("0", " ") + Utilities.CYAN if fields[7][6][1] else Utilities.BLUE + fields[7][6][0].replace("0", " ") + Utilities.CYAN)
		eightEight = "{field1}".format(field1=Utilities.RED + fields[7][7][0].replace("0", " ") + Utilities.CYAN if fields[7][7][1] else Utilities.BLUE + fields[7][7][0].replace("0", " ") + Utilities.CYAN)
		eightNine = "{field1}".format(field1=Utilities.RED + fields[7][8][0].replace("0", " ") + Utilities.CYAN if fields[7][8][1] else Utilities.BLUE + fields[7][8][0].replace("0", " ") + Utilities.CYAN)

		nineOne = "{field1}".format(field1=Utilities.RED + fields[8][0][0].replace("0", " ") + Utilities.CYAN if fields[8][0][1] else Utilities.BLUE + fields[8][0][0] .replace("0", " ") + Utilities.CYAN)
		nineTwo = "{field1}".format(field1=Utilities.RED + fields[8][1][0].replace("0", " ") + Utilities.CYAN if fields[8][1][1] else Utilities.BLUE + fields[8][1][0].replace("0", " ") + Utilities.CYAN)
		nineThree = "{field1}".format(field1=Utilities.RED + fields[8][2][0].replace("0", " ") + Utilities.CYAN if fields[8][2][1] else Utilities.BLUE + fields[8][2][0].replace("0", " ") + Utilities.CYAN)
		nineFour = "{field1}".format(field1=Utilities.RED + fields[8][3][0].replace("0", " ") + Utilities.CYAN if fields[8][3][1] else Utilities.BLUE + fields[8][3][0].replace("0", " ") + Utilities.CYAN)
		nineFive = "{field1}".format(field1=Utilities.RED + fields[8][4][0].replace("0", " ") + Utilities.CYAN if fields[8][4][1] else Utilities.BLUE + fields[8][4][0].replace("0", " ") + Utilities.CYAN)
		nineSix = "{field1}".format(field1=Utilities.RED + fields[8][5][0].replace("0", " ") + Utilities.CYAN if fields[8][5][1] else Utilities.BLUE + fields[8][5][0].replace("0", " ") + Utilities.CYAN)
		nineSeven = "{field1}".format(field1=Utilities.RED + fields[8][6][0].replace("0", " ") + Utilities.CYAN if fields[8][6][1] else Utilities.BLUE + fields[8][6][0].replace("0", " ") + Utilities.CYAN)
		nineEight = "{field1}".format(field1=Utilities.RED + fields[8][7][0].replace("0", " ") + Utilities.CYAN if fields[8][7][1] else Utilities.BLUE + fields[8][7][0].replace("0", " ") + Utilities.CYAN)
		nineNine = "{field1}".format(field1=Utilities.RED + fields[8][8][0].replace("0", " ") + Utilities.CYAN if fields[8][8][1] else Utilities.BLUE + fields[8][8][0].replace("0", " ") + Utilities.CYAN)

		print(header)
		print("1  │ " + oneOne + " │ " + oneTwo + " │ " + oneThree + " │║│ " + oneFour + " │ " + oneFive + " │ " + oneSix + " │║│ " + oneSeven + " │ " + oneEight + " │ " + oneNine + " │")

		print(intersection)

		print("2  │ " + twoOne + " │ " + twoTwo + " │ " + twoThree + " │║│ " + twoFour + " │ " + twoFive + " │ " + twoSix + " │║│ " + twoSeven + " │ " + twoEight + " │ " + twoNine + " │")

		print(intersection)

		print("3  │ " + threeOne + " │ " + threeTwo + " │ " + threeThree + " │║│ " + threeFour + " │ " + threeFive + " │ " + threeSix + " │║│ " + threeSeven + " │ " + threeEight + " │ " + threeNine + " │")

		print(footer)

		print(separator)

		print(header)
		print("4  │ " + fourOne + " │ " + fourTwo + " │ " + fourThree + " │║│ " + fourFour + " │ " + fourFive + " │ " + fourSix + " │║│ " + fourSeven + " │ " + fourEight + " │ " + fourNine + " │")

		print(intersection)

		print("5  │ " + fiveOne + " │ " + fiveTwo + " │ " + fiveThree + " │║│ " + fiveFour + " │ " + fiveFive + " │ " + fiveSix + " │║│ " + fiveSeven + " │ " + fiveEight + " │ " + fiveNine + " │")

		print(intersection)

		print("6  │ " + sixOne + " │ " + sixTwo + " │ " + sixThree + " │║│ " + sixFour + " │ " + sixFive + " │ " + sixSix + " │║│ " + sixSeven + " │ " + sixEight + " │ " + sixNine + " │")

		print(footer)

		print(separator)

		print(header)
		print("7  │ " + sevenOne + " │ " + sevenTwo + " │ " + sevenThree + " │║│ " + sevenFour + " │ " + sevenFive + " │ " + sevenSix + " │║│ " + sevenSeven + " │ " + sevenEight + " │ " + sevenNine + " │")
		print(intersection)

		print("8  │ " + eightOne + " │ " + eightTwo + " │ " + eightThree + " │║│ " + eightFour + " │ " + eightFive + " │ " + eightSix + " │║│ " + eightSeven + " │ " + eightEight + " │ " + eightNine + " │")

		print(intersection)

		print("9  │ " + nineOne + " │ " + nineTwo + " │ " + nineThree + " │║│ " + nineFour + " │ " + nineFive + " │ " + nineSix + " │║│ " + nineSeven + " │ " + nineEight + " │ " + nineNine + " │")

		print(footer)


board = Board()
