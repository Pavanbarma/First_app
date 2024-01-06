from fastapi import FastAPI, HTTPException
from typing import Dict, List
from model import Positions
from logics import calculate_knight_moves, calculate_queen_moves, calculate_rook_moves

app = FastAPI()

@app.post("/chess/knight")
def knight_moves(positions: Positions):
    knight_pos = positions.positions.get("Knight")
    if not knight_pos or len(knight_pos) != 2 or not knight_pos[0].isalpha() or not knight_pos[1].isdigit():
        raise HTTPException(status_code=400, detail="Invalid Knight position")

    valid_moves = calculate_knight_moves(knight_pos)
    return {"valid_moves": valid_moves}

@app.post("/chess/queen")
def queen_moves(positions: Positions):
    queen_pos = positions.positions.get("Queen")
    if not queen_pos or len(queen_pos) != 2 or not queen_pos[0].isalpha() or not queen_pos[1].isdigit():
        raise HTTPException(status_code=400, detail="Invalid Queen position")

    valid_moves = calculate_queen_moves(queen_pos, positions.positions)
    return {"valid_moves": valid_moves}

@app.post("/chess/rook")
def rook_moves(positions: Positions):
    rook_pos = positions.positions.get("Rook")
    if not rook_pos or len(rook_pos) != 2 or not rook_pos[0].isalpha() or not rook_pos[1].isdigit():
        raise HTTPException(status_code=400, detail="Invalid Rook position")

    valid_moves = calculate_rook_moves(rook_pos, positions.positions)
    return {"valid_moves": valid_moves}

