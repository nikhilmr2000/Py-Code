p=input()
l=[]
for i in p:
    l.append(i)
n=len(p)
z=(n//2)-1
maxi=1000000000000000000
maxo=0

for i in range(n-1,z,-1):
  
    if(p[i]>p[z]):
        s=int(p[i])-int(p[z])
        if(s<maxi):
            maxi=s
            maxo=i

          

temp=l[z]
l[z]=l[maxo]
l[maxo]=temp


d=''
for i in range(0,z+1):
    d+=l[i]

for i in range(n-1,z,-1):
    d+=l[i]

print(d)
