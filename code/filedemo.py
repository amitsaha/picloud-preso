import cloud
 
def savedata():
    f=open('data.txt','w')
    f.write('This is a line of text')
    f.close()
 
    cloud.files.put('data.txt')

# Interpreter session:

# >>> from filedemo import *
# >>> cloud.call(savedata)
# >>> cloud.files.list()
# [u'data.txt', u'stats_1.csv']
# >>> cloud.files.get('data.txt')
