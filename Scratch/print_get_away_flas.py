from Scratch.get_away_matrices_flas import *
from Scratch.get_away_unary_flas import *
from Scratch.get_away_ternary_flas import *
from Scratch.get_away_quaternary_flas import *
from special_functions import *
from Scratch.pi2 import *


place_x = 600
place_y =50
step_matrices = step_m*1.9

sheffer = binary_supen

get_away_unary(sheffer, K[0], (place_x, place_y))
get_away_unary(sheffer, K[1], (place_x, place_y + step_matrices))
get_away_draw(sheffer, K[2], (place_x, place_y+ step_matrices*2))
get_away_draw(sheffer, K[3], (place_x, place_y+step_matrices*4 ))
get_away_quaternary(sheffer, K[4], (place_x, place_y+step_matrices*6 ))
get_away_unary(sheffer, K[5], (place_x, place_y + step_matrices*9))
get_away_unary(sheffer, K[6], (place_x, place_y + step_matrices*10))
get_away_unary(sheffer, K[7], (place_x, place_y + step_matrices*11))
get_away_draw(sheffer, K[8], (place_x, place_y + step_matrices*12))
get_away_draw(sheffer, K[9], (place_x, place_y + step_matrices*14))
get_away_draw(sheffer, K[10], (place_x, place_y + step_matrices*16))
get_away_draw(sheffer, K[11], (place_x, place_y + step_matrices*18))
get_away_draw(sheffer, K[12], (place_x, place_y + step_matrices*20))
get_away_draw(sheffer, K[13], (place_x, place_y + step_matrices*22))
get_away_draw(sheffer, K[14], (place_x, place_y + step_matrices*24))
get_away_draw(sheffer, K[15], (place_x, place_y + step_matrices*26))
get_away_draw(sheffer, K[16], (place_x, place_y + step_matrices*28))
get_away_draw(sheffer, K[17], (place_x, place_y + step_matrices*30))
get_away_ternary(sheffer, K[18], (place_x, place_y + step_matrices*32))
get_away_ternary(sheffer, K[19], (place_x, place_y + step_matrices*35))
get_away_unary(sheffer, K[20], (place_x, place_y + step_matrices*38))
get_away_draw(sheffer, K[21], (place_x, place_y + step_matrices*40))
get_away_draw(sheffer, K[22], (place_x, place_y + step_matrices*42))
get_away_draw(sheffer, K[23], (place_x, place_y + step_matrices*44))

