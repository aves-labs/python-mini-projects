def tower_builder(n):
    n_list = []
    for i in range(n):
        spaces_num = n - i - 1
        stars_num  = 2*i + 1
        n_list.append(' '*spaces_num + '*'*stars_num +' '*spaces_num)
    return n_list
tower = tower_builder(int(input("Your Number: ")))
for row in tower:
    print(row)

