t,d=$<.map{_1.scan(/\d/).join.to_i}
p (0..t).sum{_1*(t-_1)>d ?1:0}
