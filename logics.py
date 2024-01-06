from typing import Dict, List

def calculate_knight_moves(position: str) -> List[str]:
    # {"postions": {"Queen": "E7", "Bishop": "B7", "Rook":"G5", "Knight": "C3""}}
    board = 'ABCDEFGH'
    valid_moves = []
    row, col = board.index(position[0]), int(position[1])

    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 8 and 1 <= new_col <= 8:
            valid_moves.append(board[new_row] + str(new_col))

    return valid_moves

def calculate_queen_moves(position: str, other_positions: Dict[str, str]) -> List[str]:
    board = 'ABCDEFGH'
    valid_moves = []
    row, col = board.index(position[0]), int(position[1])
    
    # Directions: horizontal, vertical, and diagonal
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for d in directions:
        for i in range(1, 8):
            new_row, new_col = row + d[0] * i, col + d[1] * i
            if 0 <= new_row < 8 and 1 <= new_col <= 8:
                new_pos = board[new_row] + str(new_col)
                if new_pos in other_positions.values():  # stop if another piece is found
                    break
                valid_moves.append(new_pos)
            else:
                break

    return valid_moves

def calculate_rook_moves(position: str, other_positions: Dict[str, str]) -> List[str]:
    board = 'ABCDEFGH'
    valid_moves = []
    row, col = board.index(position[0]), int(position[1])
    
    # Directions: horizontal and vertical
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for d in directions:
        for i in range(1, 8):
            new_row, new_col = row + d[0] * i, col + d[1] * i
            if 0 <= new_row < 8 and 1 <= new_col <= 8:
                new_pos = board[new_row] + str(new_col)
                if new_pos in other_positions.values():  # stop if another piece is found
                    break
                valid_moves.append(new_pos)
            else:
                break

    return valid_moves
