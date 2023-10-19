from random import sample

random_list = sample(range(1,100), 5)

for i in random_list:
    if i % 2 == 0:
        print (i, "ist eine gerade Zahl.")
    elif i % 2 != 0:
        print (i, "ist eine ungerade Zahl.")
