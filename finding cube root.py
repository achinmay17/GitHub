x=int(raw_input('Enter the number: '))
ans=0
while ans**3<abs(x):
    ans=ans+1
if ans**3!=abs(x):
    print x,'is not a perfect cube'
else:
    print 'Cube root of ' +str(x)+ ' is ' +str(ans)
    
    
