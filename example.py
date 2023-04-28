#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('run', './packer.ipynb')
packer = Packer()

#Bin(name, length, width, height, capacity)
#packer.add_bin(Bin('Conteneurs réfrigérés', 269.7, 1202.4, 235, 1000))
packer.add_bin(Bin('Conteneurs réfrigérés', 1200.1, 600.125, 25, 1000))
packer.add_bin(Bin('Conteneurs réfrigérés', 1200.1, 600.125, 25, 1000))

#Item(name, length, width, height, weight) in cm
for i in range(10):
    packer.add_item(Item('Carton de bananes', 30.9370, 20.0, 10.0, 1))
for i in range(10):
    packer.add_item(Item('Carton de bananes', 53.5, 40.0, 24.5, 1))

packer.pack()


# In[ ]:




