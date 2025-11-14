def nb_year(p0, percent: float, aug, p):
    print(f"{p0}, {percent}, {aug}, {p}")
    count = 0
    percent = percent/100
    while p0 <= p:
        count +=1
        p0 = int(p0 + p0*percent + aug)
        if p0 >= p: 
             print(f"{p0} {p}")
             return count
    return count

print(nb_year(1000, 2.0, 50, 1214))