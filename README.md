Blender-DrawLattice
===================

A crude blender script that renders a single-layer of close-packed UV spheres

The motivation behind this Blender script is the lack of readily available tools to create accurate representations of crystalline surfaces in Blender for the modeling of surface catalytic reactions. Current methods for modeling crystalline surfaces in blender include use of a third-party program to export a structure to be imported into Blender via an add-on.

The goal of this project is to create a series of scripts that render basic lattice structures (fcc, hcp, etc.)

Currently, this script renders a single-layer close-packed surface of one or two differently sized atoms.

How to Use
==========

1. Copy the contents of drawlattice.py into the Blender text editor.
2. Input the radius of atom 1, the radius of atom 2, and the total number per row into "draw_lattice(atom1, atom2, total)"
3. Run Script
