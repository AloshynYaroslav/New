a = int(input())


def mu_func3():
    b = int(a / 86400)
    c = int((a - 86400) / 3600)
    d = int((a - (86400 + c * 3600)) / 60)
    e = int(a - (b * 86400) - (c * 3600) - (d * 60))
    print(b, "d,", c, "h,", d, "m,", e, "s")


mu_func3()
