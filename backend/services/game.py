# /backend/routers/api.py
# Made by shivrsdev or shiv.rs.dev@gmail.com
# Game services (Such as making moves from the client side)

from random import randint

def make_move(move):
    bot_move = randint(0, 2)

    match bot_move:
        case 0:
            if move == 'paper': return True
            else: return False
        case 1:
            if move == 'scissors': return True
            else: return False
        case 2:
            if move == 'rock': return True
            else: return False
    
    return False # There is no possible way this happens, but if so then just let the player lose as if it lets them win then they could exploit this to get infinite wins