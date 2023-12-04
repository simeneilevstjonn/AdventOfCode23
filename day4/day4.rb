d=$<.map{[*_1.split(?|),1]}
s=d.size
p (0...s).sum{|i|a,b,y=d[i];(i+1..[i+(b.split&a.scan(/\d+/)[1..]).size,s-1].min).map{d[_1][2]+=y};y}