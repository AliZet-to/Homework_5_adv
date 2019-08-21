#Data input
while True:
    row = input("Input the row \n")
    if len(row) <= 0:
        continue
    new_row = ''
    first = row[0]

#Calculation workflow
    count_letters = 1
    for i in range(1, len(row)):
        if row[i] == first:
            count_letters += 1
        else:
            new_row = new_row + first + str(count_letters)
            first = row[i]
            count_letters = 1
    new_row = new_row + first + str(count_letters)
    print(new_row)

#Dialogue with an user
    request = input("If you want input one more row, please input 'Y'. Or input 'N' to exit the program. \n").upper()
    while not (request == 'Y' or request == 'N'):
        request = input("Please input 'Y' or 'N'. \n").upper()
    if request == "N":
        break
    else:
        continue