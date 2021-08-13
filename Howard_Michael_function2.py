#Countdown
def countdown(num):
    num_list = []
    for val in range(num, -1, -1):
        num_list.append(val)
    return num_list
print(countdown(5))
#print and return
def print_and_retun(num_list):
    print(num_list[0])
    return num_list[1]
print(print_and_retun([1,2]))
#first plus length
def first_plus_length(num_list):
    return num_list[0] + len(num_list)
print(first_plus_length([1,2,3,4,5]))
#values greater than second

def values_greater_than_second(num_list):
    new_list = []
    second_value = num_list[1]
    for i in range(0, len(num_list), 1):
        if num_list[i] > second_value:
            new_list.append(num_list[i])

    print(len(new_list))
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
# this length, that value
def length_and_value(size,value):
    new_list = []
    for num_times in range(size):
        new_list.append(value)
    return new_list
print(length_and_value(4,7))

