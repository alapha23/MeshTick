import numpy
from stl import mesh

INPUT_FILENAME = "3d-models/Rabbit_baby_one.stl"
OUTPUT_FILENAME = "3d-models/Rabbit_new.stl"

# Using an existing stl file:
#MeshObj = mesh.Mesh.from_file(INPUT_FILENAME)

# Or creating a new mesh (make sure not to overwrite the `mesh` import by
# naming it `mesh`):
#VERTICE_COUNT = 100
#data = numpy.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
#MeshObj = mesh.Mesh(data, remove_empty_areas=False)

# The mesh normals (calculated automatically)
#MeshObj.normals

# The mesh vectors
#MeshObj.v0, MeshObj.v1, MeshObj.v2

# Accessing individual points (concatenation of v0, v1 and v2 in triplets)
#assert (MeshObj.points[0][0:3] == MeshObj.v0[0]).all()
#assert (MeshObj.points[0][3:6] == MeshObj.v1[0]).all()
#assert (MeshObj.points[0][6:9] == MeshObj.v2[0]).all()
#assert (MeshObj.points[1][0:3] == MeshObj.v0[1]).all()

# Create 3 faces of a cube
data = numpy.zeros(6, dtype=mesh.Mesh.dtype)

# Top of the cube
data['vectors'][0] = numpy.array([[0, 1, 1],
                                  [1, 0, 1],
                                  [0, 0, 1]])
data['vectors'][1] = numpy.array([[1, 0, 1],
                                  [0, 1, 1],
                                  [1, 1, 1]])
# Front face
data['vectors'][2] = numpy.array([[1, 0, 0],
                                  [1, 0, 1],
                                  [1, 1, 0]])
data['vectors'][3] = numpy.array([[1, 1, 1],
                                  [1, 0, 1],
                                  [1, 1, 0]])
# Left face
data['vectors'][4] = numpy.array([[0, 0, 0],
                                  [1, 0, 0],
                                  [1, 0, 1]])
data['vectors'][5] = numpy.array([[0, 0, 0],
                                  [0, 0, 1],
                                  [1, 0, 1]])

MeshObj = mesh.Mesh(data, remove_empty_areas=False)

MeshObj.save(OUTPUT_FILENAME)
