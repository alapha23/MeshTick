from stl import mesh
import stl
import math
import numpy as np
from matplotlib import pyplot
from mpl_toolkits import mplot3d

FILENAME = '/Users/zhiyuangao/Documents/python3/numpy-stl-practices/3d-models/ring.stl'
minz = None
maxz = None

def load_mesh():
	model = mesh.Mesh.from_file(FILENAME)
	global minz, maxz
	for p in model.points:
	# p contains (x, y, z)
		if minz is None:
			minz = p[stl.Dimension.Z]
			maxz = p[stl.Dimension.Z]
		else:
			maxz = max(p[stl.Dimension.Z], maxz)
			minz = min(p[stl.Dimension.Z], minz)
	print('minz = ' + str(minz) + '; maxz = ' + str(maxz))
	return model

def show_model(model):
	figure = pyplot.figure()
	axes = mplot3d.Axes3D(figure)
	axes.add_collection3d(mplot3d.art3d.Poly3DCollection(model.vectors))
	# Auto scale to the mesh size
	scale = model.points #.flatten('K')
	axes.auto_scale_xyz(scale, scale, scale)
	# Show the plot to the screen
	pyplot.show()

def print_point(p):
	x = str(p[stl.Dimension.X])
	y = str(p[stl.Dimension.Y])
	z = str(p[stl.Dimension.Z])
	print('(' + x + ', ' + y + ', ' + z + ')\n')

def on_surface(model, p):
	on_surface = True
	for point in model.v0:
		if p[2] > point[2]:
			on_surface = False
			return on_surface
	for point in model.v1:
		if p[2] > point[2]:
			on_surface = False
			return on_surface
	for point in model.v2:
		if p[2] > point[2]:
			on_surface = False
			return on_surface
	return on_surface

def find_islands(model):
	global minz, maxz
	unsupported_p = []
	for p in model.v0:
		# if above minz
		if p[stl.Dimension.Z] > minz:
			# if on the surface
			if on_surface(model, p):
			#print_point(p)
				unsupported_p.append(p)
	for p in model.v1:
		if p[stl.Dimension.Z] > minz:
			#print_point(p)
			if on_surface(model, p):
				unsupported_p.append(p)
	for p in model.v2:
		if p[stl.Dimension.Z] > minz:
			#print_point(p)
			if on_surface(model, p):
				unsupported_p.append(p)
	return unsupported_p

def stub(model):
	pin = model.points[0]
	print(pin[stl.Dimension.Z])
	for p in model.points:
		x = p[stl.Dimension.X]
		y = p[stl.Dimension.Y]
		z = p[stl.Dimension.Z]
		if abs(x - pin[stl.Dimension.X]) < 0.3 and abs(y - pin[stl.Dimension.Y]) < 0.3:
			print_point(p)

def relocate(model):
	global minz, maxz
	for p in model.points:
		print_point(p)
		if minz > 0:
			p[stl.Dimension.Z] -= minz
		else:
			p[stl.Dimension.Z] += minz
		print_point(p)

	return model

def moveup(model, delta):
	p = model.points[0]
	print(p)
	print('X: ' + str(p[stl.Dimension.X]))
	print('Y: ' + str(p[stl.Dimension.Y]))
	print('Z: ' + str(p[stl.Dimension.Z]))
	print('v0[0]' + str(model.v0[0]))
	print('v1[0]' + str(model.v1[0]))
	print('v2[0]' + str(model.v2[0]))
	for p in model.v0:
		p[2] += delta
	for p in model.v1:
		p[2] += delta
	for p in model.v2:
		p[2] += delta

if __name__ == '__main__':
	model = load_mesh()
	moveup(model, 30)
	# move model lower if it's floating in the sky
	#model = relocate(model)
	#stub(model)
	unsupported_points = find_islands(model)
	# a list of points that above the minz
	print(len(unsupported_points))
	for p in unsupported_points:
		print_point(p)
	print(len(model.points))
	show_model(model)
	model.save('/Users/zhiyuangao/Documents/python3/numpy-stl-practices/3d-models/test.stl')
