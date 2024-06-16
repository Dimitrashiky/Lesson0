my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
d = 0
while d < len(my_list):
    if my_list[d] > 0:
        print(my_list[d])
        d += 1
        continue
    if my_list[d] < 0:
        break
    d +=1