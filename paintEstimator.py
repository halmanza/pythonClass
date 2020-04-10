# Anthony Almanza
# Chapter 3

import math 

gallon_paint= 350.00

height_wall= (int(input('Enter wall height(feet):\n')))

width_wall= (int(input('Enter wall width(feet):\n')))


wall_area= height_wall * width_wall 
paint_needed= wall_area / gallon_paint
final_amount= math.ceil(paint_needed)

print('Wall area: {wall:.2f} feet'.format(wall=wall_area))
print('Paint needed:{needed:.2f} gallon(s)'.format(needed=paint_needed))
print('Cans needed: {paint:.2f} can(s)'.format(paint=final_amount))

