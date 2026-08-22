# variables
name = 'Bilal'
father_name = 'Salman'
age = 18
education = 'HSC 2'
city = 'Karachi'
country = 'Pakistan'
religion = 'Islam'

# print (f'My name is {name}.\nMy father name is {father_name}.\nI am {age} years old.\nI live in {city} {country}.\nMy education is {education}.\nI am {religion}.\nMy religion is {religion}.')

# String

pr_st = "teknoux software agency"

# print(pr_st.capitalize())
# print(pr_st.casefold())
# print(pr_st.center(50, '*'))
# print(pr_st.format("{'and'}"))

# # madlib game
# color = input('Enter a Color: ')
# plural_noun = input('Enter a Plural Noun: ')
# celebrity = input('Enter a Celebrity: ')

# print ('Roses are ' + color)
# print (plural_noun + ' are blue')
# print ('I love ' + celebrity)

favourite_car = ['Lx570', 'Lx600', "Mercedes C63", 'Revo GR', 'Lc300']
# print(favourite_car)
# print(favourite_car[0])
# print(favourite_car[4])
# print(favourite_car[::-1])
# favourite_car.append('Bmw M5')
# favourite_car.insert(1,'Bmw M5')
# print(favourite_car)
# favourite_car.remove('Bmw M5')
# favourite_car.sort()
favourite_car.reverse()
# print(favourite_car)


phone_number = ["0301-1234567", "0322-9876543", "0345-4567891", "0311-7654321", "0333-1122334"]
names = ['Bilal', 'Ali', 'Zia', 'TIm', "Bob"]

new_name = input('Enter your name: ')
new_phone_number = input('Enter your phone_number: ')

names.append(new_name)
phone_number.append(new_phone_number)

print("\nContact Book:")
for i in range(len(names)):
    print(names[i], "-", phone_number[i])