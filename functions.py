def greet():                          #####function
    print('good morning, khushpreet')


greet()
greet()
greet() 


###passing value

def greeting(name):
    print('hi how r u',name)


greeting('khushpreet')
greeting('ashmeet')



####
def sum_of_list(a):
    print('calculating...')
    return sum(a)

marks=[45,22,13]
sum_of_marks=sum_of_list(marks)

print('my sum of',sum_of_marks)