# /backend/routers/api.py
# Made by shivrsdev or shiv.rs.dev@gmail.com
# API router

from fastapi import APIRouter
import services.game as gameService

router = APIRouter()

@router.post('/move/{move}')
async def make_move(move: str):
    return { 'won': gameService.make_move(move) }