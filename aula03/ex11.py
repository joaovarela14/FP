def sec2hms(seg):
    h = seg // 3600 
    extra = seg % 3600
    m = (extra  // 60)
    s = extra % 60
    print("{:02d}:{:02d}:{:02d}".format(h, m, s))

seg=int(input("Segundos: "))
sec2hms(seg)