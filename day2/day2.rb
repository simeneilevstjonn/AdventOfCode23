p $<.sum{|l|r,g,b=0,0,0;a,c=l.split ": ";c.split(/,|;/).map{|x|n,t=x.split;n=n.to_i;(t<?c)?(b=[b,n].max):(t<?h)?(g=[g,n].max):(r=[r,n].max)};r*g*b}
