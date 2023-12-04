d=$<.map{_1}
s=d.size
n=[1]*s
p (0...s).sum{|i|(i+1..[i+(d[i].split("| ")[1].split&d[i].scan(/\d+(?=.*\|)/)[1..]).size,s-1].min).map{n[_1]+=n[i]};n[i]}