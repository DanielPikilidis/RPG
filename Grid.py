class Board:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.board = []

    def createGrid(self):   # list of lists magic
        for i in range(1, 24):
            line = []
            if i % 2 == 0:
                for n in range(1, 17):
                    line.append("|")
                    line.append("   ")
                line.append("|")
            else:
                for n in range(1, 17):
                    line.append("+")
                    line.append("---")
                line.append("+")
            self.board.append(line)

        self.board[1][1] = " H "    # Starting location, could be any open block
        # Markets
        self.board[7][1] = " M "
        self.board[21][23] = " M "
        self.board[19][1] = " M "
        self.board[9][19] = " M "

        # Blocked
        long = [19, 19, 19, 19, 21, 9, 11, 13, 15, 17, 13, 15, 17, 19, 19, 13, 1, 1, 3, 3, 3, 9, 9, 11, 9, 11, 11, 11, 11,
             13, 13, 13, 1, 1, 1, 3]
        lat = [25, 23, 21, 19, 25, 1, 1, 1, 1, 1, 3, 3, 3, 3, 5, 5, 31, 29, 27, 29, 31, 15, 13, 13, 17, 19, 21, 15, 17,
             15, 17, 19, 9, 11, 13, 13]
        for i in range(len(long)):
            self.board[long[i]][lat[i]] = " X "


    def printGrid(self):
        ind = 0
        print("     1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16")
        for lst in self.board:
            if ind % 2 == 0:
                print("  ", "".join(lst))
            else:
                if ind < 19:
                    print("{} ".format(int((ind+1)/2)), "".join(lst))
                else:
                    print("{}".format(int((ind+1)/2)), "".join(lst))
            ind += 1

    def move(self, direction):
        # Target is the block the hero wants to move to.
        # Checking is target is available, unavailable or market and returning appropriate number
        if direction == "U":
            target = self.x - 2
            if target <= 0:
                print("You are at the top border, you can't go any higher!")
            elif self.board[target][self.y] == " X ":
                print("You cannot go there, that location is unavailable.")
            elif self.board[target][self.y] == " M ":
                print("Welcome to the Market.")
                return 1
            else:
                self.board[self.x][self.y] = "   "
                self.x -= 2
                self.board[self.x][self.y] = " H "
                return 2

        elif direction == "D":
            target = self.x + 2
            if target >= 22:
                print("You are at the bottom border, you can't go any lower!")
            elif self.board[target][self.y] == " X ":
                print("You cannot go there, that location is unavailable.")
            elif self.board[target][self.y] == " M ":
                print("Welcome to the Market.")
                return 1
            else:
                self.board[self.x][self.y] = "   "
                self.x += 2
                self.board[self.x][self.y] = " H "
                return 2

        elif direction == "R":
            target = self.y + 2
            if target >= 32:
                print("You are at the right border, you can't go any more right!")
            elif self.board[self.x][target] == " X ":
                print("You cannot go there, that location is unavailable.")
            elif self.board[self.x][target] == " M ":
                print("Welcome to the Market.")
                return 1
            else:
                self.board[self.x][self.y] = "   "
                self.y += 2
                self.board[self.x][self.y] = " H "
                return 2

        elif direction == "L":
            target = self.y - 2
            if target <= 0:
                print("You are at the left border, you can't go any more left!")
            elif self.board[self.x][target] == " X ":
                print("You cannot go there, that location is unavailable.")
            elif self.board[self.x][target] == " M ":
                print("Welcome to the Market.")
                return 1
            else:
                self.board[self.x][self.y] = "   "
                self.y -= 2
                self.board[self.x][self.y] = " H "
                return 2

