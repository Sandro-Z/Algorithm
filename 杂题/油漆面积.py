#本题采用骗分方法做
vis=set()
n=eval(input())
sum=0
for k in range(n):
	x1,x2,y1,y2=map(int,input().split())
	if x1>x2:x1,x2=x2,x1
	if y1>y2:y1,y2=y2,y1
	for i in range(x1,x2):
		for j in range(y1,y2):
			if (i,j) not in vis:
				sum+=1
				vis.add((i,j))
