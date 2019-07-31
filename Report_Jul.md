## Report on the First Phase

Objective
---

This project aims at designing a program to add supporters for 3D models automatically.
In the first phase, I will deploy my development environment including CURA and numpy-stl, and I will write simple programs in numpy-stl following the official guide.


What I have done
---

I installed CURA, numpy-stl and other python3 related packages. Related scripts reside in this repository on github.

I followed numpy-stl official tutorial to process STL files (Mesh objects) locally. The tutorials include how to load and create Mesh objects, how to find properties of the Mesh objects, and how to combine multiple Mesh objects.


#### A list of files and what they are supposed to do

* MeshIO.py	: It includes how to load a mesh object, how to create a mesh object from scratch, and to write the object to stl file.
* Cube.py 	: It creates a 
* EvaluateMesh.py: Emits utility of the mesh including volume, center of gravity(COG) and inertia matrix at COG.
* ModifyMesh.py	: 
* CombineMesh.py: It loads two mesh objects, manipulate their positions and combines them to a single mesh object.
* 3d-models	: A directory of stl files I used and created.

Those tutorials allow me to create supporters, change the position of the supporters and combine them with the original targeted mesh object.
As a consequence, I have the fundamental knowledge to manipulate supporters with the help of numpy-stl.

What I am going to do
---

Not only about completing the supporter generator, there are also a lot of optimizations we can do about supporters.

First, I will complete a basic supporter generator, which produces cuboid supporters of a fixed size. It detects the outstreching points in the mesh object, and adds a supporter accordingly. It should merge supporters if they overlap in the space.

Then, I plan to optimize the size and shape of the supporter the program generates. The size should be decided by the size of the target input mesh object, and also the space within the input mesh object, to make sure the supporter does not intervere other parts and can be detachedeasily. Furthermore, I will add options of shape of the supporter to generate. There are a lot of existing supporter models online, and I will import them in my implementation.

Third, I try to see if rotating the original input mesh object will save some supporters. Performance is more of a concern in this step, because we should not calculate supporters for all degreees.

All progress will be uploaded, documented on github.


