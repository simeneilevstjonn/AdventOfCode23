p $<.sum{|l|%w{r g b}.map{l.scan(eval("/\\d+(?= #{_1})/")).map(&:to_i).max}.inject(:*)}
