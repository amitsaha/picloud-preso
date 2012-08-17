import cloud
import numpy
 
def sort_num(num):
    sort_num = numpy.sort(num)
    return sort_num

if __name__ == '__main__':
    num=numpy.random.random_integers(10,10000,50000)
    jid=cloud.call(sort_num, num)
    print cloud.result(jid)
