










# string = "1 - 2 + 5 * 7"
# print(string)
# list = string.split()
# print(list)
# for i in range(len(list)):
#     if list[i].isdigit():
#         list[i] = int(list[i])
# print(list)
#
# result = 0
#
# while len(list) != 1:
#     i = 0
#     while ('*' in list or '/' in list) and i < len(list):
#         if list[i] == '*':
#             result = list[i-1] * list[i+1]
#             list.pop(i)
#             list.pop(i)
#             list[i-1] = result
#             i -= 1
#         elif list[i] == '/':
#             result = list[i-1] / list[i+1]
#             list.pop(i)
#             list.pop(i)
#             list[i-1] = result
#             i -= 1
#         i += 1
#
#     while ('+' in list or '-' in list) and i < len(list):
#         if list[i] == '+':
#             result = list[i-1] + list[i+1]
#             list.pop(i)
#             list.pop(i)
#             list[i-1] = result
#             i -= 1
#         elif list[i] == '-':
#             result = list[i-1] - list[i+1]
#             list.pop(i)
#             list.pop(i)
#             list[i-1] = result
#             i -= 1
#         i += 1
#
# print(list)