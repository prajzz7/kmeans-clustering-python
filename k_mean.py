from statistics import mean
import math
t=[]
def kmeans(cst,avg1):
    l=[[] for Null in range(k)]
    navg=avg1
    print("k-means iteration:")
    for i in range(k):
        for j in range(len(cst[i])):
            h=cst[i][j]
            p = []
            for f in range(k):
                m=navg[f]
                dif=abs(m-h)
                p.append(dif)
            g=p.index(min(p))
            l[g].append(h)
            for x in range(len(l)):
                if(len(l[x])==0):
                    navg.append(0)
                else:
                    navg.append(mean(l[x]))
    t=l
    for p in range(k):
        t[p].sort(reverse=True)
    avg=[]
    for i in range(len(l)):
        if(len(l[i])==0):
            avg.append(0)
        else:
            avg.append(mean(l[i]))
    for e in range(len(t)):
        print("k{}:{}={}".format(e+1,t[e],avg[e]))
    if(cst==t):
        navg1=[]
        for i in range(k):
            if(len(t[i])==0):
                kmeans(t,avg)
        print("Since both the above clusters are same,the final cluster is:")
        for v in range(len(t)):
            navg1.append(mean(t[v]))
        for i in range(len(t)):
            print("k{}:{}={}".format(i+1,t[i],navg1[i]))
        exit()
    else:
        kmeans(l,avg)

avg,emt=[],[]
k=int(input("Enter the no. of clusters that you want(k):"))
a=int(input("Enter the number of elements you require:"))

if(a<k):
    print("Cluster Cannnot be formed.")
    exit()
print("Enter the numbers:")
for i in range(a):
    emt.append(int(input()))
if(a/k ==1):
    c=emt
    for j in range(k):
        print("k{}:{}={}".format(j+1,c[j],avg[j]))
if(k+1==a):
    c=[[] for Null in range(k)]
    avg=[]
    for i in range(k):
        c[i].append(emt.pop())
    c[0].append(emt.pop())
    for j in range(k):
        avg.append(mean(c[j]))
    for m in range(k):
        c[m].sort(reverse=True)
    kmeans(c,avg)
c=[[] for Null in range(k)]
i=0
for o in range(k):
    c[o].append(emt.pop())

#print(c,"stop")		#extra
while(len(emt)!=0):
    if(i==k):
        i=0
    c[i].append(emt.pop())
    i+=1
#print(c,"stop")		#extra
for j in range(len(c)):
	avg.append(mean(c[j]))
for j in range(k):
    print("k{}:{}={}".format(j+1,c[j],avg[j]))
for m in range(k):
    c[m].sort(reverse=True)
#print(c)		#extra
kmeans(c,avg)		
