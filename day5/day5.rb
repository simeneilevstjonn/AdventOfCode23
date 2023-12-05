S,*M=`cat`.split("\n\n").map{_1.scan(/\d+/).map(&:to_i)}
r=S.each_slice(2).to_a
M.map{|m|r=r.flat_map{|a|s=[a];d=[];m.each_slice(3){|t,c,g|n = []
for l, le in s do
    h = le + l

    if (c <= l && l < g + c) and (c <= h - 1 && h - 1< g + c)
        d<<[l + t - c, le]
    elsif (c <= l && l< g + c)
        d<<[l + t - c, g + c - l]
        if h - g - c > 0
            n<<[g + c, h - g - c]
        end
    elsif (c <= h && h< g + c)
        d<<[t, h - c]
        if c - l > 0
            n<<[l, c - l]
        end
    else
        n<<[l, le]
    end
end
s = n}

s + d
}}
p r.min[0]
