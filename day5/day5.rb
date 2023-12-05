s,*m=`cat`.split("\n\n").map{_1.scan(/\d+/).map(&:to_i)}
def bigRangeToRanges(lo, length, maps)
    srcranges = [[lo, length]]
    destranges = []

    for dest, src, length in maps.each_slice(3) do
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

    return srcranges + destranges
end
ranges = s.each_slice(2).to_a

for map in m do
    nr = []
    for lo, le in ranges do
        nr += bigRangeToRanges(lo, le, map)
    end
    ranges = nr
end

p ranges.min{_1[0] <=> _2[0]}[0]
