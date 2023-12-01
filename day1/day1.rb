n=[0,"one","two","three","four","five","six","seven","eight","nine"]
v=->(x){return x=~/\d/?x.to_i: n.index x}
p $<.map{|l|m=l.scan(eval("/(?=(\\d|"+n.join(?|)+"))/"));v.call(m[0][0])*10+v.call(m[-1][0])}.sum
