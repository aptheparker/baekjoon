a,b,c = map(int,input().split())
d,e,f = map(int,input().split())

print(max(0,d-a)+max(0,e-b)+max(0,f-c))