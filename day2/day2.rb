p $<.sum{|l|v=[[],[],[]];l.split(?:)[1].split(/,|;/).map{|x|n,t=x.split;v[(t<=>?c).+t<=>?h]+=[n.to_i]};v.map(&:max).inject :*}
