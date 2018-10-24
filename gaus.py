# -*- coding: utf-8 -*-

from PIL import Image
from math import pi, log, exp
import numpy as np
import sys

def process(filename, r):
    # должна обрабатывать файл filename гауссовым размытием в квадрате [-r, +r] x [-r, +r] 
    # и записывать результат в <filename>.gaussblurred.png
    img = Image.open('darwin.png')
    img.load()

    A=np.array(img.getdata())
    A=A.reshape(3000,3667)
    B=np.zeros((3000,3667))

    dx, dy = np.meshgrid(np.arange(-r, +r+1, 1.), np.arange(-r, +r+1, 1.0))
    sigma = 0.38*r
    gauss_dist = np.exp( -(dx*dx+dy*dy)/(2*sigma**2) ) / (2*pi*sigma**2)
    coeff = gauss_dist / np.sum(gauss_dist)

    # код сюда ....
    for i in range(3000):
    	for j in range(3667):
    		for in range(-r,r+1):
    			for m in range(-r,r+1):
    				B[i,j]+=coeff[ , ]*A[i+l,j+m]
    				
    			
    	
    newimg = img
    newimg.show()
    newimg.save(filename+'.gaussblurred.png')



if __name__=='__main__':
    # Запускать с командной строки с аргументом <имя файла>, например: python gauss.py darwin.png
    if len(sys.argv) > 1:
        main(sys.argv[1], 3)
    else:
        print("Must give filename.\n")