n="ø|one|two|three|four|five|six|seven|eight|nine"
p $<.map{|l|m=l.scan(eval "/(?=(\\d|#{n}))/").map{|y|x,a=y;x=~/\d/?x.to_i: n.split(?|).index(x)};m[0]*10+m[-1]}.sum
