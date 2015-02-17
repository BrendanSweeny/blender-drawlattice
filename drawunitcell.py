import bpy

#An example using strontium titanate (SrTiO3) and the perovskite crystal lattice
atoms = {
            "Sr": {"color": [0, 1, 0], "radius": 1.142855, "location": [0.0, 0.0, 0.0]},
            "Ti": {"color": [0.74902, 0.760784, 0.780392], "radius": 0.8, "location": [0.5714275, 0.5714275, 0.5714275]},
            "O": {"color": [1, 0.0509804, 0.0509804], "radius": 0.342857, "location": [[0.5714275, 0.5714275, 0.0], [0.5714275, 0.0, 0.5714275], [0.0, 0.5714275, 0.5714275]]}
        }

xCellLength = 1.142855
yCellLength = 1.142855
zCellLength = 1.142855

def draw_atom(atom, radius, x, y, z):
  #Draws the specific UV sphere
  bpy.ops.mesh.primitive_uv_sphere_add(size = radius, location = (x, y, z))
  bpy.ops.object.shade_smooth()

  #Creates a new material with the element name if none already exists
  if atom not in bpy.data.materials:
    bpy.data.materials.new(name = atom)
    bpy.data.materials[atom].diffuse_color = atoms[atom]["color"]
    bpy.data.materials[atom].specular_intensity = 0.2

  #Applies correct material to the new mesh
  bpy.context.active_object.data.materials.append(bpy.data.materials[atom])

#Draws a row of unit cells in the x-direction at a given y-value and z-value
def draw_row(xUnits, yFactor, zFactor):
  xLength = xUnits * xCellLength
  xFactor = 0

  #Draws atoms by element in a specific unit cell before moving on to the next unit cell
  #The radius of the atoms from atoms.json is divided by two for a more reasonable scale
  while (xFactor * xCellLength) < xLength:
    for atom in atoms:
      if isinstance(atoms[atom]["location"][0], list): #Checks to see if element is present in unit cell more than once
        for location in atoms[atom]["location"]:
          draw_atom(atom, atoms[atom]["radius"] / 2, location[0] + xCellLength * xFactor, location[1] + yCellLength * yFactor, location[2] + zCellLength * zFactor)
      else:
        draw_atom(atom, atoms[atom]["radius"] / 2, atoms[atom]["location"][0] + xCellLength * xFactor, atoms[atom]["location"][1] + yCellLength * yFactor, atoms[atom]["location"][2] + zCellLength * zFactor)
    xFactor += 1

#Uses the draw_row function to render rows of unit cells at given y-intervals
def draw_surface(xUnits, yUnits, zFactor):
  yLength = yUnits * yCellLength
  yFactor = 0
  while (yFactor * yCellLength) < yLength:
    draw_row(xUnits, yFactor, zFactor)
    yFactor += 1

#Uses the draw_surface function to render rows of unit cells at given z-intervals
def draw_lattice(xUnits, yUnits, zUnits):
  zLength = zUnits * zCellLength
  zFactor = 0
  while (zFactor * zCellLength) < zLength:
    draw_surface(xUnits, yUnits, zFactor)
    zFactor += 1

#Enter the number of repeating units in the x, y and z directions
draw_lattice(1, 1, 1)
