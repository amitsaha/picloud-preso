def square(x):
    return x*x

# demonstration of cloud.call()
import cloud
jid = cloud.call(square,3)

print 'Job Id::', jid
print 'Job status',cloud.status(jid)

print 'Result',cloud.result(jid)
