s,*M=`cat`.split("\n\n").map{_1.scan(/\d+/).map(&:to_i)}
r=s.each_slice(2).to_a
M.map{|m|r=r.flat_map{|a|
srcranges = [a]
destranges = []

for dest, src, length in m.each_slice(3) do
    nsr = []
    for l, le in srcranges do
        h = le + l

        if (src <= l && l < length + src) and (src <= h - 1 && h - 1< length + src)
            destranges.append([l + dest - src, le])
        elsif (src <= l && l< length + src)
            destranges.append([l + dest - src, length + src - l])
            if h - length - src > 0
                nsr.append([length + src, h - length - src])
            end
        elsif (src <= h && h< length + src)
            destranges.append([dest, h - src])
            if src - l > 0
                nsr.append([l, src - l])
            end
        else
            nsr.append([l, le])
        end
    end
    srcranges = nsr
end

srcranges + destranges
}}
p r.min[0]
