f_list = [1, 1]

answer = f_list[-1] + f_list[-2]
while answer <= 1000:
    answer = f_list[-1] + f_list[-2]
    f_list.append(answer)

print(int(f_list))





