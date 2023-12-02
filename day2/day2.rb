p $<.sum{|l|[?r,?g,?b].map{|x|l.scan(eval("/\\d+(?= #{x})/")).map(&:to_i).max}.inject(:*)}
