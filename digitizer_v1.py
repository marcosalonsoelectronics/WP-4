# -*- coding: utf-8 -*-
"""
@author: Marcos Alonso - May 7, 2025
Digitizer_V1.py - Version 1.0
In this version the size of the image is obtained directly from
the image after loading it.
Thanks to Youtube viewer @jope4009 for suggestion this.
"""
import pygame
import numpy as np
# -------------------------------------------------------------------------
# Introduce the name of the input image file
image_file = "./panel-curves.png"
# Introduce window dimensions. Must be greater that image's dimensions
Xw = 1400; Yw = 700
# Introduce X and Y axis range of the characteristic
xmin=0;  ymin=0; xmax=40; ymax=12
# Introduce the name of the output data file
output_file="./data.txt"
#-------------------------------------------------------------------------
# Data array definition
Ndata=100
xp =   np.arange(0,Ndata,1, dtype=int) # pixel data arrays
yp =   np.arange(0,Ndata,1, dtype=int)
xd =   np.arange(0,Ndata,1, dtype=np.float) # actual data arrays
yd =   np.arange(0,Ndata,1, dtype=np.float)
# Activate the pygame library .
pygame.init()
# Create the display surface object of dimensions X,Y
imp = pygame.image.load(image_file)
h, w = imp.get_height(), imp.get_width()
window = pygame.display.set_mode((w, h))
# set the pygame window name
pygame.display.set_caption('image')
# create a surface object, image is drawn on it.
imp = pygame.image.load(image_file).convert()
# Using blit to copy content from one surface to other
window.blit(imp, (0, 0))
# paint window one time
pygame.display.flip()
# Read bottom-left point to get scales
read_min=True
print("Introduce (Xmin, Ymin) point")
while (read_min):
        # Note that y in pixels increases downwards
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                xminp=event.pos[0]; ymaxp=event.pos[1] # coordinates in pixels
                pygame.draw.circle(window, (0, 0, 255), [xminp, ymaxp], 3, 3)
                pygame.display.update()
                print("(xminp, ymaxp)=", xminp,ymaxp)
                read_min=False
            if event.type == pygame.QUIT:
                pygame.display.quit()        
# Read top-right point to get scales
read_max=True
print("Introduce (Xmax, Ymax) point")
while (read_max):
        # Note that y in pixels increases downwards
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                xmaxp=event.pos[0]; yminp=event.pos[1] # coordinates in pixels
                pygame.draw.circle(window, (0, 0, 255), [xmaxp, yminp], 3, 3)
                pygame.display.update()
                print("(xmaxp, yminp)= ", xmaxp, yminp)
                read_max=False
            if event.type == pygame.QUIT:
                pygame.display.quit()
# Calculates linear transformation slopes
mx =  (xmax - xmin)/(xmaxp - xminp)
my = -(ymax - ymin)/(ymaxp - yminp)                    
# Reads data points
read_points = True
print("Introduce data points")
i=0
while (read_points):
       for event in pygame.event.get():
           if event.type == pygame.MOUSEBUTTONDOWN:
               xp[i]=event.pos[0]; yp[i]=event.pos[1] # coordinates in pixels
               pygame.draw.circle(window, (255, 0, 0), [xp[i], yp[i]], 3, 3)
               pygame.display.update()
               # linear transformation to get data points
               xd[i]= xmin + mx*(xp[i]-xminp)
               yd[i]= ymax + my*(yp[i]-yminp)
               print("i= ", i, xp[i], yp[i])
               print("i= ", i, xd[i], yd[i])
               i=i+1
           if event.type == pygame.QUIT:
                   read_points=False
# Deactivates the pygame library
pygame.quit()
# Writes data to file
fh = open(output_file, "w")
for j in range(0, i):
    fh.write( str(xd[j]) + " " + str(yd[j]) + "\n") 
fh.close()








