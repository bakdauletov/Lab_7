# #1
# import random
# import re

# lists = []

# with open("OROMBO.txt", 'r') as files:
#     for line in files:
#         words = line.strip().split()
#         lists.extend(words)


# def task_1():
#     for x in lists:
#         print(x)
# task_1()

#2
# def task_2():
#     random_string = random.randint(1, len(lists) - 1)
#     print(f'{lists[random_string]}')
# task_2()

# #3
# def task_3():
#     count = 0
#     for i in lists:
#         if i.istitle():
#             count += 1
#     print(count)

# #4
# def task_4():
#     count = 0
#     with open('OROMBO.txt', 'r') as file:
#         for i in file:
#             i = i.strip().split()
#             for j in i:
#                 if j and j[0].lower() == 'd':
#                     count += 1
#                     print(f"{j}\n{count}")

# #5
# def task_5():
#     count = 0
#     with open('OROMBO.txt', 'r') as file:
#         for i in file:
#             i = i.strip().split()
#             for j in i:
#                 if j and j[-1].lower() == 'f':
#                     count += 1
#                     print(f"{j}")

#         print(count)
# #6
# def task_6():
#     count = 0
#     with open('OROMBO.txt', 'r') as file:
#         for i in file:
#             i = i.strip().split()
#             for j in i:
#                 if j == 'all' or j == 'none':
#                     count += 1
#         print(count)
# task_6()

# #7
# def task_7():
#     checked = set()
#     lists = []
#     with open('OROMBO.txt', 'r') as file:
#         for line in file:
#             words = line.strip().split()
#             lists.extend(words)

#     for i in lists:
#         i = i.strip()
#         count = lists.count(i)
#         if (i, count) not in checked:
#             checked.add((i, count))
#     print(checked)

#8
# def task_8():
#     max_length = 0
#     with open('OROMBO.txt', 'r') as file:
#         for i in file:
#             i = i.strip().split()
#             for j in i:
#                 if max_length < len(j):
#                     max_length = len(j)
#                     word = j
#     print(f"{word}")
# task_8()

# #9
# def task_9():
#     with open('OROMBO.txt', 'r+') as file:
#         content = file.read()
#         content = content.replace('b', 'j')
#         print(content)
# task_9()

# #10
# def task_10():
#     user_a = 0
#     user_b = 0
#     with open('task10.txt', 'r') as file:
#         lines = file.read()
#         for i in lines:
#             if i.lower() == 'a':
#                 user_a =+ 1
#             if i.lower() == 'b':
#                 user_b =+ 1
#     print(user_a, user_b)
# task_10()