d=$<.map{_1}
s=d.size
n=[1]*s
(0...s).map{|i|w=d[i].scan(/\d+(?=.*\|)/)[1..];c=d[i].split("| ")[1].split;c=(c&w).size;(i+1..[i+c,s-1].min).map{n[_1]+=n[i]}}
p n.sum