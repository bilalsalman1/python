# if statement
# is_male = True
# is_tall = True

# if is_male or is_tall:
#     print ('You\'re a male or tall both')
# else:
#     print ('You\'re neither a male nor a tall')

is_female = True
is_taller = False

if is_female and is_taller:
    print ('You\'re a tall female')
elif is_female and not(is_taller):
    print ('You\'re a short female')
elif not(is_female) and is_taller:
    print ('You\'re a tall male')
else:
    print ('You neither  male nor tall')


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print (max_num(3, 4, 5))




