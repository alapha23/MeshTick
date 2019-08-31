## Report on the Second Phase in August

Objective
---

This project aims at designing a program to add supporters for 3D models automatically.
In the second phase, I will use numpy-stl to support island detection in 3D models.


What I have done
---

I wrote [python scripts](https://github.com/alapha23/MeshTick/blob/master/FindIsland/main.py) that try to find islands in 3d models. I am using a straight forward algorithm -- to detect points that above the lowest point in model, filter the points above to specify the points on the surface, and cut those suface points into grids. Every grid would need a supporter. 

I am debuging on how to filter the points to find the surface points, and I think there should be APIs in numpy-stl to make things easier. Currently I am not aware of it.

What I am going to do
---

I will finish the island finder in September, and I have to start supporter design in September too. There are plenty of optimization on supporter design, I will first make sure the functionality has no problem, then move on to optimizations.

I understand current progress is left behind. I plan to communicate more with my mentor. I will make weekly simple text reports to him, and in case there are something that I find difficult, he can know immediately that I might need some help.
