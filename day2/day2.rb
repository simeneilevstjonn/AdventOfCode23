p $<.sum{|l|v=[[],[],[]];a,c=l.split ": ";c.split(/,|;/).map{|x|n,t=x.split;v[(t<?c?0:1)+(t<?h?0:1)]+=[n.to_i]};v.map(&:max).inject(&:*)}
