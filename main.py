list1 = list(map(int, input('первый список ').split()))
list2 = list(map(int, input('второй список').split()))
answer = []

for i in list1:
    if i % 2 == 0 and not i in list2:
        answer.append(i)
for i in list2:
    if not i % 2 == 0 and not i in list1:
        answer.append(i)
answer.sort()
print(answer)
