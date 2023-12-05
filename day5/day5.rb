S,*M=`cat`.split("\n\n").map{_1.scan(/\d+/).map(&:to_i)}
r=S.each_slice(2).to_a
M.map{|m|r=r.flat_map{|a|
s=[a]
d=[]

for dest, src, length in m.each_slice(3) do
    n = []
    for l, le in s do
        h = le + l

        if (src <= l && l < length + src) and (src <= h - 1 && h - 1< length + src)
            d<<[l + dest - src, le]
        elsif (src <= l && l< length + src)
            d<<[l + dest - src, length + src - l]
            if h - length - src > 0
                n<<[length + src, h - length - src]
            end
        elsif (src <= h && h< length + src)
            d<<[dest, h - src]
            if src - l > 0
                n<<[l, src - l]
            end
        else
            n<<[l, le]
        end
    end
    s = n
end

s + d
}}
p r.min[0]
