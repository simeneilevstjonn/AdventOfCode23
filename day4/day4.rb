d=$<.map{_1}
s=d.size
n=[1]*s
p (0...s).sum{|i|a,b=d[i].split ?|;(i+1..[i+(b.split&a.scan(/\d+/)[1..]).size,s-1].min).map{n[_1]+=n[i]};n[i]}