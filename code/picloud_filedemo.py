import cloud
def savedata():
    f=open('data.txt','w')
    f.write('This is a line of text')
    f.close()
 
    cloud.files.put('data.txt')

# Interpreter session:
# In [7]: import cloud
# In [8]: cloud.files.list()
# Out[8]: []
# In [9]: from picloud_filedemo import *
# In [10]: cloud.call(savedata)
# Out[10]: 107
# In [11]: cloud.files.list()
# Out[11]: [u'data.txt']
