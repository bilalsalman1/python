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