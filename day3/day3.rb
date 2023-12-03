a=$<.map{|x|x}
N=a.map{|l|i=-1;m=!1;l.chars.map{i+=1 if m!=(m=_1=~/\d/)&&m;m ?[l.scan(/\d+/).map(&:to_i)[i],i]:0}}
h=a.size-1
w=a[0].size-2
p (0..h).sum{|i|(0..w).sum{|j|r=[-1,0,1];n=r.product(r).map{|y,x|N[(i+y).clamp(0,h)][(j+x).clamp(0,w)]}.uniq-[0];n.size==2&&a[i][j]=='*'?(n.map{_1[0]}.inject(:*)):(0)}}
