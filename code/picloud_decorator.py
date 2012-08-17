# Demo code: decorator wrapping a call to PiCloud
# See: https://github.com/amitsaha/picloud-preso

def cloudcall(func):
    def sendtocloud(*args, **kwargs):
        import cloud
        jid = cloud.call(func,*args,**kwargs)
        
        while True:
            # blocking
            # You could just use a callback function here
            # http://docs.picloud.com/client_adv.html#callbacks
            status = cloud.status(jid)
            if status == 'done':
                print '{0:s} :: Done   '.format(func.__name__, str(jid))
                print '{0:s} :: Result {1:s}'.format(func.__name__, str(cloud.result(jid)))
                break
            else:
                print '{0:s} :: {1:s}'.format(func.__name__,status)

    return sendtocloud

# simply decorate a method you want to be executed
# in PiCloud
@cloudcall
def anexpensivefunction(x,y):
    return x**3 + y**3

if __name__=='__main__':
    anexpensivefunction(3,3)
