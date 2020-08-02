ROWS = 6
COLUMNS = 8

EMPTY = '.'
PLAYER_ONE = 'B'
PLAYER_TWO = 'R'

board = [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]


def col_full(col):
  return board[0][col] != EMPTY


def get_input():
  while True:
    col = input("Type the column you want to place in: ")
    if col.isnumeric() is False:
      print("Please input a number!")
      continue
    col = int(col)
    if not (0 <= col < ROWS):  # using 0-index for now
      print(f"Please input a number between 0 and {ROWS-1}")
      continue
    if col_full(col):
      print(f"Column {col} is full already!")
      continue
    
    return int(col)


def make_move(col, color):
  for r in reversed(range(ROWS)):
    if board[r][col] == EMPTY:
      board[r][col] = color
      return
  assert False, f"{col} {color}"


def main():
  print("Welcome to Connect Four!")

  for move in range(ROWS * COLUMNS):
    for row in board:
      print(' '.join(row))
    col = get_input()

    if move % 2 == 0:
      make_move(col, PLAYER_ONE)
    else:
      make_move(col, PLAYER_TWO)
    

    

    
if __name__ == "__main__":
  main()