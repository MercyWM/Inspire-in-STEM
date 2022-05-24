#!usr/bin/python

# assignment on operations

# area of a circle

radius = input('Enter the radius of the circle')
PI = 3.142
area_of_a_circle = PI * int(radius) * int(radius)
print(' The area of the circle is ' + str(area_of_a_circle))

# volume of a cylinder

height = input('Enter the height of the cylinder')
volume_of_a_cylinder = area_of_a_circle * int(height)
print('The volume of the cylinder is ' + str(volume_of_a_cylinder))

#  surface area of a cylinder

surface_area_of_a_cylinder = 2 * PI * int(radius) * int(radius) + PI * 2 * int(radius) * int(height)
print(' The surface area of this cylinder is ' + str(surface_area_of_a_cylinder))

#  volume of a cube

side = input( 'Enter the side of the cube')
volume_of_a_cube = int(side) * int(side) * int(side)
print('The volume of this cube is ' + str(volume_of_a_cube))
print("Thats it")