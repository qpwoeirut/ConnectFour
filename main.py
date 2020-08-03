ROWS = 6
COLUMNS = 7

EMPTY = '.'
PLAYER_ONE = 'B'
PLAYER_TWO = 'R'

board = [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]


def print_board():  # utility function to print the board to console
  print()
  print(' '.join([str(n) for n in range(COLUMNS)]))  # print column numbers
  for row in board:
    print(' '.join(row))  # use str.join to concatenate all the row chars


def get_input():
  while True:  # keep asking until we get valid input
    col = input("What column do you want to place in?\n> ")
    if col.isnumeric() is False:  # check if the input's a number
      print("Please input a number!")
      continue
    col = int(col)  # convert from string to number
    if not (0 <= col < COLUMNS):  # check if column is valid, using 0-index for now
      print(f"Please input a number between 0 and {COLUMNS-1}")
      continue
    if board[0][col] != EMPTY:  # check if column is already full (top cell will be taken)
      print(f"Column {col} is full already!")
      continue
    
    return col


def make_move(col, color):
  for r in reversed(range(ROWS)):  # start from the bottom and go up
    if board[r][col] == EMPTY:  # find the lowest empty cell
      board[r][col] = color
      return  # we only want to place once, so return once we're done

  raise ValueError(f"Unable to place {color} in column {col}")
  # this shouldn't ever happen since we've verified the top cell is empty in get_input, but let's make sure


def check_diag(row, col, player, inc):  # check column, always going down and either left or right
  cur_count = 0
  while row < ROWS and 0 <= col < COLUMNS:  # if we're out of bounds we can stop
    if board[row][col] == player:  # if player matches we count that cell
      cur_count += 1
      if cur_count == 4:  # check if 4 in a row has been reached
        return True
    else:  # if it's not the player, we have to restart
      cur_count = 0
    row += 1
    col += inc  # go either left or right
  return False


def check_winner(player):
  for row in range(ROWS):  # check all rows
    cur_count = 0
    for col in range(COLUMNS):
      if board[row][col] == player:
        cur_count += 1
        if cur_count == 4:
          return True
      else:
        cur_count = 0
  
  for col in range(COLUMNS):  # check all columns
    cur_count = 0
    for row in range(ROWS):
      if board[row][col] == player:
        cur_count += 1
        if cur_count == 4:
          return True
      else:
        cur_count = 0
  
  for row in range(ROWS):
    if check_diag(row, 0, player, 1) or check_diag(row, COLUMNS - 1, player, -1):
      return True
  
  for col in range(COLUMNS):
    if check_diag(0, col, player, 1) or check_diag(0, col, player, -1):
      return True

  return False


def main():
  print("Welcome to Connect Four!")

  for move in range(ROWS * COLUMNS):
    print_board()
    col = get_input()

    if move % 2 == 0:
      make_move(col, PLAYER_ONE)
      if check_winner(PLAYER_ONE):
        print("Player one wins!")
        break
    else:
      make_move(col, PLAYER_TWO)
      if check_winner(PLAYER_TWO):
        print("Player two wins!")
        break

  if not check_winner(PLAYER_ONE) and not check_winner(PLAYER_TWO):
    print("Draw.")

  print_board()
    
    
if __name__ == "__main__":
  main()