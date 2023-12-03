import re,sys
g=[""]+sys.stdin.read().split()
w=re.finditer
q=lambda m,n:n[1]>=m[0]<m[1]>=n[0]
print(sum(b[0]*b[1]for o,i in enumerate(g)for m in w("\*",g[o])for b in[[int(n.group(0))for d in[-1,0,1]for n in w("\d+",g[o+d])if q(m.span(),n.span())]]if len(b)==2))