times = 5
a, b  = 1, 1
month = 0

adult = 1
baby = 0
total = 0
for x in range(times):
    # print('Month ', month,':', b, ' pair(s) of rabbits')
    print('Month ', month,':', total, ' pair(s) of rabbits')
    # a, b = b, a + b
    baby = adult
    total = adult + baby

    adult = adult + baby
    month += 1
