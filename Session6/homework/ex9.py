def get_even_list(l):
    even_list = []
    for i in l:
        if i % 2 == 0:
            print('{0} is an even number.'.format(i))
            even_list.append(i)
        else:
            print('{0} is not an even number.'.format(i))
    return(even_list)
