from toolz import curry 

@curry
def always(x):
    return lambda : x

