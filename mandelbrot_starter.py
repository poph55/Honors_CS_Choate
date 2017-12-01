''' fuzzy mandelbrot
xmin = -1.4112939
xmax = -1.3941601
ymin = -0.00873657
ymax = 0.008397216
'''
''' 8 STARFISH
xmin = -0.3739964458
xmax = -0.3739533212184
ymin = 0.6597450612386
ymax = 0.6597881858348846
'''
'''UPSIDE DOWN!
xmin = -.26014616507071026
xmax = -0.255196242155852
ymin = -0.6518695520471643
ymax = -0.6469196291323062
'''

import tkinter
from tkinter import *

def mandelbrot(z, c, count):
    z = z ** 2 + c
    count += 1
    if abs(z) > 2 or count > maxIt - 1:
        return count
    return mandelbrot(z,c,count)

WIDTH = 460 
HEIGHT = 460
xmin1 = -.26014616507071026
xmax1 = -0.255196242155852
ymin1 = -0.6518695520471643
ymax1 = -0.6469196291323062
maxIt = 255 

window1 = tkinter.Toplevel()

canvas1 = Canvas(window1, width = WIDTH, height = HEIGHT, bg = "#000000")

img1 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas1.create_image((0, 0), image = img1, state = "normal", anchor = tkinter.NW)

for row in range(HEIGHT):
    for col in range(WIDTH):
        c = complex((((xmax1-xmin1)/WIDTH)*col)+xmin1,(((ymax1-ymin1)/HEIGHT)*row)+ymin1)

        z = complex(0.0,0.0)

        r = mandelbrot(z,c,0)

        rd = hex(r)[2:].zfill(2)
        gr = hex(125)[2:].zfill(2)
        bl = hex(125)[2:].zfill(2)

        img1.put("#" + rd + gr + bl, (col, row))

canvas1.pack()


WIDTH = 460 
HEIGHT = 460
xmin2 = -0.3739964458
xmax2 = -0.3739533212184
ymin2 = 0.6597450612386
ymax2 = 0.6597881858348846
maxIt = 255 

window2 = tkinter.Toplevel()

canvas2 = Canvas(window2, width = WIDTH, height = HEIGHT, bg = "#000000")

img2 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas2.create_image((0, 0), image = img2, state = "normal", anchor = tkinter.NW)

for row in range(HEIGHT):
    for col in range(WIDTH):
        c = complex((((xmax2-xmin2)/WIDTH)*col)+xmin2,(((ymax2-ymin2)/HEIGHT)*row)+ymin2)

        z = complex(0.0,0.0)

        r = mandelbrot(z,c,0)

        rd = hex(r)[2:].zfill(2)
        gr = hex(80)[2:].zfill(2)
        bl = hex(40)[2:].zfill(2)

        img2.put("#" + rd + gr + bl, (col, row))

canvas2.pack()




WIDTH = 460 
HEIGHT = 460
xmin3 = -1.4112939
xmax3 = -1.3941601
ymin3 = -0.00873657
ymax3 = 0.008397216
maxIt = 255 

window3 = tkinter.Toplevel()

canvas3 = Canvas(window3, width = WIDTH, height = HEIGHT, bg = "#000000")

img3 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas3.create_image((0, 0), image = img3, state = "normal", anchor = tkinter.NW)

for row in range(HEIGHT):
    for col in range(WIDTH):
        c = complex((((xmax3-xmin3)/WIDTH)*col)+xmin3,(((ymax3-ymin3)/HEIGHT)*row)+ymin3)

        z = complex(0.0,0.0)

        r = mandelbrot(z,c,0)

        rd = hex(r)[2:].zfill(2)
        gr = hex(125)[2:].zfill(2)
        bl = hex(125)[2:].zfill(2)

        img3.put("#" + rd + gr + bl, (col, row))

canvas3.pack()
mainloop()