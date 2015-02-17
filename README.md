Blender-DrawLattice
===================

A crude blender script that renders a single-layer of close-packed UV spheres

The motivation behind this Blender script is the lack of readily available tools to create accurate representations of crystalline surfaces in Blender for the modeling of surface features, catalytic reactions, etc. in journals and presentations. Current methods for modeling crystalline surfaces in blender include use of a third-party program to export a structure (e.g. a .pdb file) to be imported into Blender via an add-on.

The goal of this project is to create a series of scripts that render basic lattice structures (perovskite, fcc, hcp, etc.)

Currently, this script renders a three-dimensional lattice of a cubic or tetragonal crystal lattice. However, contents of the the unit cell (atoms and locations) as well as parameters must be inputed manually. An example using SrTiO3 can be found in the drawunitcell.py script

How to Use
==========

1. Copy the contents of drawunitcell.py into the Blender text editor.
2. Modify the atom dictionary to reflect the repeating atoms of the unit cell of the material to be rendered.
3. Modify xCellLength and other unit cell dimensions relative to the atomic radii in the atom dictionary to achieve a close-packed lattice.
4. Specify the dimensions of the lattice (in number of unit cells) for each edge by modifying "draw_lattice(1, 1, 1)".
  NOTE: It is highly recommended to start with 1x1x1 then 2x2x2 to check dimensions and gradually build up as rendering can be resource intensive.
3. Run Script.

Example
=======

![](/BrendanSweeny/path/to/img.jpg?raw=true "Optional Title")
