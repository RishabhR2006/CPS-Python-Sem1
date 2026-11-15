pos=-1
def search(L,n,i=0):
    global pos
    if i==len(L):
        return False
    if L[i]==n:
        pos=i
        return True
    return search(L,n,i+1)


L=[1,2,3,4,5,6,7,8,9]
n=6

if search(L,n):
    print("number found at ",pos+1)
else:
    print("not found")
