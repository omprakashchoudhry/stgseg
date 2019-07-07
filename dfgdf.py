N=int(input())
a=list(map(int,input().split()))[:N]
a1=sum(a[0:N:2])
a2=sum(a[1:N:2])
if a1>a2:
  print(a1)
else:
  print(a2)
