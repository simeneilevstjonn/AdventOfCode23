import re,sys
g=[""]+sys.stdin.read().split()
t=0
w=re.finditer
def q(n):a,b=n.span();l,r=m.span();return b>=l<r>=a
for o in range(len(g)):
 for m in w("\*",g[o]):
  b=[int(n.group(0))for d in[-1,0,1]for n in w("\d+",g[o+d])if q(n)]
  if len(b)==2:t+=b[0]*b[1]
print(t)
