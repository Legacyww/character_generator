import random
list = ["Kate","Nick","Den","Alex","Tom"]
new_list = []
while len(new_list) != len(list):
    i = random.randrange(0,len(list))
    if list[i] not in new_list:
        new_list.append(list[i])
print(new_list)

