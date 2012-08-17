def cloudcall(func):
    def sendtocloud(*args, **kwargs):
        import cloud
        jid = cloud.call(func,*args,**kwargs)
        cloud.join(jid)
        print 'Result:: ', cloud.result(jid)

    return sendtocloud
