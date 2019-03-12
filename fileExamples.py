# with open('input_Day01.txt') as file:
#     # result = 0
#     # for number in file:
#     #     result += int(number)
#     # print(result)
#     print (sum(int(n) for n in file))

# Part two:
uniquenumbers = []
with open('input_Day01.txt') as file:
    result = 0
    # for number in file:
    #     result += int(number)
    # print(result)
    frequencyFound = False
    while not frequencyFound:
        for number in file:
            result += int(number)
            if result not in uniquenumbers:
                uniquenumbers.append(result)
            else:
                frequencyFound = True
                print "First frequency reached twice: " + str(result)
                break

# Tuples and more lists
# my_list = list(range(5))
# print my_list

