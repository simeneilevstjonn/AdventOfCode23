p $<.sum{|l|v=[[],[],[]];l.scan(/\d+ \w/).map{|x|n,t=x.split;v[t<=>?g]+=[n.to_i]};v.map(&:max).inject :*}
