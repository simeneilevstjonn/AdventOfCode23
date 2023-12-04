d=$<.map{[_1,1]}
s=d.size
p (0...s).sum{|i|x,y=d[i];a,b=x.split ?|;(i+1..[i+(b.split&a.scan(/\d+/)[1..]).size,s-1].min).map{d[_1][1]+=y};y}