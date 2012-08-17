>>> def square(x):
        return x*x
>>> import cloud
>>> uri=cloud.rest.publish(square, "square_func")
>>> print uri
https://api.picloud.com/r/3222/square_func
