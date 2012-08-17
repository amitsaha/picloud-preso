import sys
import cloud

def success(jid):
    print 'Job Completed Successfully'
    print 'Result::',cloud.result(jid)

def failure(jid):
    print 'Job Completed with Errors'
    print cloud.info(jid, ['stderr', 'stdout'] )

def reciprocal(x):
    try:
        return 1.0/x
    except Exception as e:
        print >> sys.stderr, "Attempted division by",x
        return 'Error'


if __name__=='__main__':
    jid1 = cloud.call(reciprocal,3,_callback=[success], _callback_on_error=[failure])
    jid2 = cloud.call(reciprocal,0,_callback=[success], _callback_on_error=[failure])

