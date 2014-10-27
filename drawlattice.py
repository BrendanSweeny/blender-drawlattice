import bpy
import math

# Draw Lattice is a crude script that creates a single-layer

def make_row(x, y, z, largerRadius, smallerRadius, size, total):
    while x < (largerRadius * 2 * total):
        bpy.ops.mesh.primitive_uv_sphere_add(size = size, location = (x, y, z))
        bpy.ops.object.shade_smooth()
        x += largerRadius * 2

def draw_lattice(atom1, atom2, total):
    if atom1 > atom2:
        largerRadius = atom1
        smallerRadius = atom2
    else:
        largerRadius = atom2
        smallerRadius = atom1
    yOffset = math.sqrt(((largerRadius + smallerRadius)**2) - largerRadius**2)

    #Renders rows with larger atom
    make_row(0, 0, 0, largerRadius, smallerRadius, largerRadius, total)
    if yOffset > largerRadius:
        factor = 2
        iteration = 1
        while iteration < total:
            make_row(0, yOffset * factor, 0, largerRadius, smallerRadius, largerRadius, total)
            factor += 2
            iteration += 1
    else:
        factor = 2
        iteration = 1
        while iteration < total:
            make_row(0, largerRadius * factor, 0, largerRadius, smallerRadius, largerRadius, total)
            factor += 2
            iteration += 1

    #Renders rows with smaller atom
    if yOffset > largerRadius:
        make_row(largerRadius, yOffset, 0, largerRadius, smallerRadius, smallerRadius, total)
        factor = 3
        iteration = 1
        while iteration < total:
            make_row(largerRadius, yOffset * factor, 0, largerRadius, smallerRadius, smallerRadius, total)
            factor += 2
            iteration += 1
    else:
        make_row(largerRadius, largerRadius, 0, largerRadius, smallerRadius, smallerRadius, total)
        factor = 3
        iteration = 1
        while iteration < total:
            make_row(largerRadius, largerRadius * factor, 0, largerRadius, smallerRadius, smallerRadius, total)
            factor += 2
            iteration += 1

# To draw a surface, enter parameters: radius of atom 1, radius of atom 2,
# and total number of each atom per row (e.g. draw_lattice(0.3, 0.2, 6))
draw_lattice()
