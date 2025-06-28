numbers = [2,3,4,3,2,4,5,1]
uniques = []

for number in numbers :
    if number  not in uniques:
        uniques.append(number)
        uniques.sort()
print(uniques)