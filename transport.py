f=open('i.txt', 'r')
t=f.readline()[1:-2].split(",")
p=[]
for l in t:
 p.append(int(l))
t = f.readline()[1:-2].split(",")
r=[]
for i in range(0,len(t),2):
 a=[]
 a.append(int(t[i]))
 a.append(int(t[i+1]))
 r.append(a)
d=[]
for i in r:
 for j in p:
  if j>=i[0] and j<=i[1]:
   i.append(j) 
 d.append(i)
for i in d:
 i.pop(0)
 i.pop(0)
n=[]
for i in d:
    n+=i
print n
