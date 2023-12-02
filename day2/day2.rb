p $<.sum{|l|r,g,b=[],[],[];a,c=l.split ": ";c.split(/,|;/).map{|x|n,t=x.split;n=[n.to_i];(t<?c)?(b+=n):(t<?h)?(g+=n):(r+=n)};r.max*g.max*b.max}
