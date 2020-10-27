# -*- coding: utf-8 -*-
"""
Lego cube parametric calculations
"""

'---------main lego constants---------'
h = 3.2

H = 3*h
P = 2.5*h

'spacing 0,1 on each side, together = 0,2 mm'

print('h = %.2f'  %h)
print('H = %.2f'  %H)
print('P = %.2f'  %P)
'-------------------------------------'
'h = 3.2 H = 9.6 P = 8.0'
'-------------------------------------'

'----cube variables------'
Nx = 1
Ny = 1

l_x = Nx*P-0.2 
w_y = Ny*P-0.2
h_stand_z = H
h_flat_z = h

print('length_x = %.2f'  %l_x)
print('width_y = %.2f'   %w_y)
print('h_stand_z = %.2f' %h_stand_z)
print('h_flat_z = %.2f'  %h_flat_z)