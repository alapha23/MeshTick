import math
import stl
from stl import mesh
import numpy

INPUT1 = "3d-models/Rabbit_baby_one.stl"
OUTPUT = "3d-models/Rabbit_one_rotated.stl"

# Using an existing stl file:
main_body = mesh.Mesh.from_file(INPUT1)

# rotate along Y
main_body.rotate([0.0, 0.5, 0.0], math.radians(90))

main_body.save(OUTPUT, mode=stl.Mode.ASCII)  # save as ASCII
