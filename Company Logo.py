if __name__ == '__main__':
    s = input()
    k=[]
    for i in s:
        k.append(i)
    l=list(set(k))
    c=[]
    for i in range(len(l)):
        c.append(0)
    d=dict(zip(l,c))
    for i,j in d.items():
        while i in k:
            d[i]+=1
            k.remove(i)
    r=sorted(d.items(), key=lambda x: (-x[1], x[0]))
    for i in range(0,3):
        print(r[i][0]+" "+str(r[i][1]))
