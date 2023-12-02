p $<.sum{|l|v={};l.scan(/(\d+) (\w)/).map{|n,t|v[t]=[n.to_i,v[t]||0].max};v.values.inject(:*)}
