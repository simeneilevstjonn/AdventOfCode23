import re,sys
g=[""]+sys.stdin.read().split()
w=re.finditer
def q(m,n):l,r=m.span();a,b=n.span();return b>=l<r>=a
print(sum(b[0]*b[1]for o in range(len(g))for m in w("\*",g[o])for b in[[int(n.group(0))for d in[-1,0,1]for n in w("\d+",g[o+d])if q(m,n)]]if len(b)==2))