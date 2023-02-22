def gcd(a,b):
    if(a==0 or b==0):
        false
    if(a == b):
        return a
    if (a>b ):
        return gcd(a-b,b)
    return gcd(a,b-c)

    a=98
    b=56
    if(gcd(a,b)):
        print('GCD of ',a,'and',b,'is' ,gcd(a,b))
    else:
        print('not found')
