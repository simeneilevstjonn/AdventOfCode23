d=$<.map{[*_1.split(?|),1]}
s=d.size-1
p (0..s).sum{|i|a,b,y=d[i];(i+1..[i+(b.split&a.scan(/\d+/)[1..]).size,s].min).map{d[_1][2]+=y};y}