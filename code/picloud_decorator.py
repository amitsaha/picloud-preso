# Demo code: decorator wrapping a call to PiCloud
# See: https://github.com/amitsaha/picloud-preso

def cloudcall(func):
    def sendtocloud(*args, **kwargs):
        import cloud
        jid = cloud.call(func,*args,**kwargs)
        cloud.join(jid)
        print 'Result:: ', cloud.result(jid)

    return sendtocloud

# simply decorate a method you want to be executed
# in PiCloud
@cloudcall
def anexpensivefunction(x,y):
    return x**3 + y**3

if __name__=='__main__':
    anexpensivefunction(3,3)
