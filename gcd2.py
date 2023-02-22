d1=int(raw_input("Enter a number:"))
d2=int(raw_input("Enter another number:"))
rem=d1%d2
while rem!=0:
        d1=d2
        d2=rem
        rem=d1%d2
print "gcd of given numbers is : %d" %(d2)
                
