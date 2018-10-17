#!/usr/bin/env python
# coding: utf-8

# In[22]:


from PIL import Image
from math import pi, log, exp
import numpy as np

img = Image.open('darwin.png')
img.load()
img


# In[23]:


print(img.size)
print(img.mode)

data = img.getdata()
print(data[1])
a = np.array(img, dtype=np.uint8).reshape(img.size[::-1])
print(a[0,1])


# In[24]:


b = a[900:1350, 900:1500]
pic = Image.fromarray(b) # создаем новый объект Image из массива фрагмента
pic


# In[ ]:





# In[ ]:





# In[33]:


def average_blur(img,r):
    w, h = img.size
    a = np.array(img.getdata(), dtype=np.uint8)                .reshape(h, w)
    b = np.zeros((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            s = 0.
            up, bt = max(i-r,0), min(i+r+1,h)
            lf, rt = max(j-r,0), min(j+r+1,w)
            n = (bt-up)*(rt-lf)
            for y in range(up,bt):
                for x in range(lf,rt):
                    s += a[y,x]
            b[i,j] = s / n
    return Image.fromarray(b)


# In[32]:


average_blur(Image.fromarray(b),7)


# In[21]:


import cv2
img = cv2.imread('darwin.png', cv2.IMREAD_GRAYSCALE)
Image.fromarray(img[900:1350, 900:1500])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




