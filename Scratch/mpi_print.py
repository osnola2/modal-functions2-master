from Scratch.pi2 import *
from Scratch.mpi_draw import *

place_x = 600
place_y = 600
step_matrices = step_m*2

func = easy_end_pi23


mpi_draw(func, mpi[0], (place_x, place_y))
mpi_draw(func, mpi[1], (place_x + step_matrices*2, place_y ))
mpi_draw(func, mpi[2], (place_x + step_matrices*4, place_y))
mpi_draw(func, mpi[3], (place_x + step_matrices*6, place_y))
mpi_draw(func, mpi[4], (place_x + step_matrices*8 , place_y))
mpi_draw(func, mpi[5], (place_x + step_matrices*10, place_y))
mpi_draw(func, mpi[6], (place_x + step_matrices*12, place_y))
