p $<.sum{|l|v=[[],[],[]];a,c=l.split ": ";c.split(/,|;/).map{|x|n,t=x.split;v[(t<=>?c)+t<=>?h]+=[n.to_i]};v.map(&:max).inject(&:*)}
