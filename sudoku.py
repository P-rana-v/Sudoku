def convert(i,j):
    i2=((i//3)*3)+j//3
    j2=((i%3)*3)+j%3
    return i2


def solve(s):
    empty=[]
    for i in range(9):
        for j in range(9):
            if s[i][j]==0:
                empty.append([i,j,0])
    length = len(empty)
    ind=0
    while ind<length:
        f3=0
        k=empty[ind][2]
        i=empty[ind][0]
        j=empty[ind][1]
        while k!=10:
            x=((convert(i,j)//3)+1)*3
            y=((convert(i,j)%3)+1)*3
            f=0
            f1=0
            for m in range(x-3,x):
                for n in range(y-3,y):
                    if s[m][n]==k:
                        f=1
                        f1=1
                        break
                if f1==1:
                    break
            for m in range(9):
                if (s[i][m]==k and m!=j) or (s[m][j]==k and m!=i) or f==1:
                    k+=1
                    f=1
                    break
            if f==0:
                s[i][j]=k
                empty[ind][2]=k
                ind+=1
                break
            if k==10 and f==1:
                s[i][j]=0
                empty[ind][2]=0
                ind-=1
    return s




