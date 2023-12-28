'''for i in range(1,6):
    print('* '*i)
print('--------------------')
for i in range(5,0,-1):
    print('* '*i)
print('--------------------')
n=4
for i in range(1,6):
    print('  '*n,'* '*i)
    n -= 1
print('--------------------')
n=0
for i in range(5,0,-1):
    print('  '*n,'* '*i)
    n +=1
print('--------------------')
for i in range(1,6):
    print(str(i)*i)
print('--------------------')
for i in range(5,0,-1):
    print(str(i)*i)
print('--------------------')
n=5
for i in range(1,6):
    print(str(i)*n)
    n -=1
print('--------------------')
n=1
for i in range(5,0,-1):
    print(str(i)*n)
    n +=1
print('--------------------')
n=4
for i in range(1,6):
    print(' '*n,str(i)*i)
    n -=1
print('--------------------')
n=4
k=1
for i in range(5,0,-1):
    print(' '*n,str(i)*k)
    n -= 1
    k += 1
print('--------------------')
n=5
k=0
for i in range(1,6):
    print(' '*k,str(i)*n)
    n -= 1
    k +=1
print('--------------------')
n=0
for i in range(5,0,-1):
    print(' '*n,str(i)*i)
    n += 1
print('--------------------')
n=1
for i in range(4,-1,-1):
    print('  '*i,'* '*n)
    n += 2
print('--------------------')
n=9
for i in range(5):
    print(' '*i,'*'*n)
    n -= 2
print('--------------------')
n=5
for i in range(1,10,2):
    print(' '*n,'*'*i)
    n -= 1
for i in range(2,7):
    for j in range(1,i):
        print(j,end=' ')
    print()
print('---------------------')
for i in range(6,1,-1):
    for j in range(1,i):
        print(j,end=' ')
    print()
print('---------1-----------')
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
print('----------2----------')
for i in range(2,7):
    for j in range(1,i):
        print(j,end=' ')
    print()
print('-----------3---------')
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
print('------------4--------')
for i in range(1,6):
    for j in range(i,6):
        print(j,end=' ')
    print()
print('-------------5-------')
for i in range(0,5):
    for j in range(5,i,-1):
        print(j,end=' ')
    print()
print('--------------6------')
for i in range(4,-1,-1):
    for j in range(5,i,-1):
        print(j,end=' ')
    print()
print('---------------7-----')
for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end=' ')
    print()
print('----------------8----')
'''
s='python'

'''for i in range(1,len(s)+1):
    print(s[0:i])'''
'''
print('---------------------')
for i in range(-1,-len(s)-1,-1):
    print(s[i:-len(s)-1:-1])
print('---------------------')
for i in range(len(s),0,-1):
    print(s[0:i])

print('---------------------')
for i in range(-len(s)-1,0):
    print(s[-1:i:-1])


num=123
rev=0
while(num!=0):
    rem = num%10
    rev = rev*10+rem
    num//=10
print(rev)

'''

def out(fun):
    print('fun',fun)
    def inn():
        fun()
        print('hello')
    return inn
@out
def ss():
    print('hi')
print('ss',ss)
ss()

































    
