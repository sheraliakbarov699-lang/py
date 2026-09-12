def juft_sonlar(sonlar):
    yangi_list = []

    for son in sonlar:
        if son % 2 == 0:
            yangi_list.append(son)

    return yangi_list


sonlar = [1, 2, 3, 4, 5, 6, 7, 8]

print(juft_sonlar(sonlar))
