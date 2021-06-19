# Define the board structure using a dictionary
the_board = {"1": " ", "2": " ", "3": " ",
             "4": " ", "5": " ", "6": " ",
             "7": " ", "8": " ", "9": " "}


# Create a function to print the current board state
def print_board(board):
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])


board_keys = []

for key in the_board:
    board_keys.append(key)


def play_game():
    # Assign the player to the "X" character and set the game turn count to 0
    turn = "X"
    count = 0

    # Set the game to a turn count of 10, print the board, and prompt the player to make the first move
    for i in range(10):
        print_board(the_board)
        move = input(f"It's your turn player {turn}. Enter a valid number between 1 and 9: ")

        # Check if the player's chosen square is already filled
        # If not, fill the square with an "X" and increase the turn count by 1
        if the_board[move] == " ":
            the_board[move] = turn
            count += 1
        # If so, let the user know the square is filled and prompt them to choose a valid square again
        else:
            print("That square is already filled.\nEnter a valid number between 1 and 9:")
            continue

        # Check if player X or player O has won after five or more moves
        if count >= 5:

            # Across the bottom row
            if the_board["1"] == the_board["2"] == the_board["3"] != " ":
                print_board(the_board)
                print("\nGame Over\n")
                print(f"{turn} won.")
                break

            # Across the middle row
            elif the_board["4"] == the_board["5"] == the_board["6"] != " ":
                print_board(the_board)
                print("\nGame Over\n")
                print(f"{turn} won.")
                break

            # Across the top row
            elif the_board["7"] == the_board["8"] == the_board["9"] != " ":
                print_board(the_board)
                print("\nGame Over\n")
                print(f"{turn} won.")
                break

            # Down the left column
            elif the_board["1"] == the_board["4"] == the_board["7"] != " ":
                print_board(the_board)
                print("\nGame Over\n")
                print(f"{turn} won.")
                break

            # Down the center column
            elif the_board["2"] == the_board["5"] == the_board["8"] != " ":
                print_board(the_board)
                print("\nGame Over\n")
                print(f"{turn} won.")
                break

            # Down the right column
            elif the_board["3"] == the_board["6"] == the_board["9"] != " ":
                print_board(the_board)
                print("\nGame Over\n")
                print(f"{turn} won.")
                break

            # First diagonal
            elif the_board["1"] == the_board["5"] == the_board["9"] != " ":
                print_board(the_board)
                print("\nGame Over\n")
                print(f"{turn} won.")
                break

            # Second diagonal
            elif the_board["3"] == the_board["5"] == the_board["7"] != " ":
                print_board(the_board)
                print("\nGame Over\n")
                print(f"{turn} won.")
                break

        # If neither player wins after nine moves, the games results in a tie
        if count == 9:
            print("\nGame Over\n")
            print("It's a draw.")

        # Alternate the player after each turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    # Ask if the player wants to play again
    restart = input("Do you want to play again? (y/n): ").lower()

    # If the player enters "y", restart the game, otherwise exit the program
    if restart == "y":
        for i in board_keys:
            the_board[i] = " "
        play_game()


if __name__ == "__main__":
    play_game()
