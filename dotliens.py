'''
    Problem Name: Dots and Lines
    Description:
        This problem is based off the game dots and lines. 
        In this game there are 2 players and a grid of dots.
        
        Players take it in turn to draw a single line between 2 dots.
        Player 1 starts.
        Lines can only be horizontal or vertical and of length 1. 

        If a player completes a square then they win a point and get another go.

    Technical Details:
        You're going to write a simulation of the above game.
        You will be given the following as input:
            width of board (#dots)
            height of board (#dots)
            moves...
        
        Run a
         simulation of the given game.
        After the simulation print:
            player 1 won X squares, player 2 won Y squares
        
        IF any player plays an invalid move (drawing a line that has already been drawn):
            print invalid

        Moves are given in the following form:
            x y direction
        
            Where x and y are the respective coordinates of the dot and direction is the direction
            you draw the line. Direction can be 'U', 'L', 'D', 'R' for Up, Left, Down, Right respectively.

            You can assume moves will:
                - Never try and draw outside the grid
                - Refer to points outside the board
'''

def get_affected_edges(w, h, x, y, dir):
    affected = []

    if dir == "L" and x > 0:
        if y < h-1: affected.append((x-1, y, "B"))
        if y > 0: affected.append((x-1, y-1, "T"))
    elif dir == "R" and x < w-1:
        if y > 0: affected.append((x, y-1, "T"))
        if y < h-1: affected.append((x, y, "B"))
    elif dir == "U" and y < h-1:
        if x > 0: affected.append((x-1, y, "R"))
        if x < w-1: affected.append(((x, y, "L")))
    elif dir == "D" and y > 0:
        if x > 0: affected.append((x-1, y-1, "R"))
        if x < w-1: affected.append((x, y-1, "L"))

    return affected 

EDGES = {
    "B": 0,
    "T": 1,
    "L": 2,
    "R": 3
}

def dots_and_lines(w, h, moves):
    board = [ [ [False, False, False, False] for _ in range(0, w) ] for _ in range(0, h) ]

    def get_edge(x, y, edge):
        return board[y][x][EDGES[edge]]

    def set_edge(x, y, edge):
        board[y][x][EDGES[edge]] = True

    p1Wins, p2Wins = 0, 0
    player1Turn = True 

    for move_str in moves:
        move = move_str.split(" ")
        move[0] = int(move[0])
        move[1] = int(move[1])

        affected_edges = get_affected_edges(w, h, *move)

        won_a_square = False

        for (x ,y, edge) in affected_edges:
            edge_state = get_edge(x, y, edge)

            if edge_state:
                return "invalid"

            set_edge(x, y, edge)

            if all(edge for edge in board[y][x]):
                if player1Turn:
                    p1Wins += 1
                else:
                    p2Wins += 1

                won_a_square = True

        if not won_a_square:
            player1Turn = not player1Turn

    return f"player 1 won {p1Wins} squares, player 2 won {p2Wins} squares" 


if __name__ == "__main__":
    test_cases = [

        # Test Case:
        # 2x2 board
        # Player 1 wins a square
        ((3, 3), [
            "0 0 U",
            "0 0 R",
            "1 1 D",
            "1 1 L"
        ], (0, 1)),

        # Test Case:
        # Invalid Move
        ((3, 3), [
            "0 0 U",
            "0 1 D"
        ], (-1, -1)),

        # Test Case:
        # No moves
        ((2, 2), [], (0, 0)),

        # Each player wins a square
        # Because when you win square you get another go
        # P1 should win the second square as shown in the moevs
        ((3, 3), [
            "0 0 U", # P1
            "0 0 R", # P2
            "1 1 D", # P1
            "1 1 L", # P2
            "2 2 D", # P2
            "2 2 L", # P1
            "1 2 D", # P2
            "2 1 L", # P1
        ], (1, 1))
    ]

    def compare_answers(answer, expected_answer, test_num, test_case):
        if answer == expected_answer:
            print(f"Passed test case {test_num}")
        else:
            print(f"Failed on test case {test_num}")
            (bounds, moves, _) = test_case 
            print(f"Board dimensions {bounds}")
            print('\n'.join(moves))
            print("Expected:", expected_answer)
            print("Got:", answer)
        print()

    for num, case in enumerate(test_cases):
        (board_bounds, moves, expected_wins) = case

        answer = dots_and_lines(*board_bounds, moves)

        (p1wins, p2wins) = expected_wins

        expected_answer = "invalid" if p1wins == -1 else f"player 1 won {p1wins} squares, player 2 won {p2wins} squares"
        
        compare_answers(answer, expected_answer, num, case)
