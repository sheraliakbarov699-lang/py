def juft_sonlar(royxat):
    return [son for son in royxat if son % 2 == 0]

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Juft sonlar:", juft_sonlar(sonlar))
