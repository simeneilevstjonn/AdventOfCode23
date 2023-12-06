w,d=$<.map{_1.scan(/\d/).join.to_i}
p ((w+(w*w-4*d-4)**0.5).to_i|1)-w
