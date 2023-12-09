e=->(a){d=a.each_cons(2).map{_2-_1};a[0]-((a-[0]).any?? e.(d):0)}
p $<.sum{e.(_1.split.map(&:to_i))}
