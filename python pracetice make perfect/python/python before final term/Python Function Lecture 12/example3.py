def display_info(a,b,*args, instructor='Mock', **kwargs):
    print(a)
    print(b)
    print(args)
    print(instructor)
    print(kwargs)
    return [a,b,args, instructor, kwargs] #return a list

print(display_info(1,2,3,4,last_name='Yo', job='instructor'))