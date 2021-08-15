# print 0-150
for i in range(0,151):
    print(i)
# print multiple of 5    
for i in range(5,1001,5):
    print(i)
# counting the dojo way
for i in range(101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("coding")
    elif i < 101:
        print(i)
# sum large number
sum = 0
for i in range(1,500000,2):
    sum = sum + i
    print(sum)
# countdown by 4
for i in range(2018,0,-4):
    print(i)
# flexible counter
def flexible_counter(low_num, high_num, mult):
    for i in range(low_num, high_num + 1):
        if i % mult == 0:
            print(i)
flexible_counter(2,9,3)