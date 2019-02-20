#Create merge conflict
print("Merge conflict")
print("i want to make conflict too.")

#message = "Hello Python world"
name = "eric Norling"
print(name.title()+"\n"+name.upper()+"\n"+name.lower())
print("\n\t"+name.title()+' once said,"A person who bever made a \n\tmistake never tried anything new."')
name = " Albert Einstein "
#print(name.strip())
#print(0.2 + 0.1)
print(5+3)
favorite_num = 8
msg = "This is my favorite number: " + str(favorite_num)
print(msg);

name = ['mali','wei','qian','yikai','azalea']
print(name[0])
print(name[2] + "can't make the dinner")
name.pop(2)
name.insert(2,"liJing")
person = name.pop()
print(person + "sorry can't invite you to dinner.")
print(name)
del name[-1]
del name[-1]
print(name)

locations = ['xian','kunshan','newyork','paris','london','anhui']
print("the original order: ")
print(locations)
print(sorted(locations,reverse=True))

locations.reverse()
print(locations)
locations.sort()
print(locations)

num = len(locations)
print(num)

for location in locations:
	print(location)
	print("i like "+location)
print("i really love travel")
numbers = list(range(2,19,3))
print(numbers)

nums = list(range(1,20))
print(nums)
one_to_million = list(range(1,1000000))

print(min(one_to_million))
print(max(one_to_million))
print(sum(one_to_million))

odd_num = list(range(1,20,2))
print(odd_num)

mul_3 = [value * 3 for value in range(3,30)]
print(mul_3)

cube = [value**3 for value in range(1,10)]
print(cube)

cube2 = []
for value in range(1,10):
	cube2.append(value**3)
print(cube2)
#copy　
print(cube[ : ])
# first three items
print(nums[0:3])
# last three items
print(nums[-3:])

copy_name = name[:]
copy_name.append("cuiheng")
name.append("david")
print(copy_name)
print(name)
foods = ("beef","lamp","chicken","pork","duck","appale","pear","banana","orange","kivi")
for value in foods:
	print(value)

car = "Subari"
if car.lower() == "subari":
	print("i predict true.")
alien_color = ['green','yellow','red']
for value in alien_color:
	if value == 'green':
		print("the player just earned 5 points")
	elif value == 'yellow' :
		print("the player just earned 10 points")
	elif value == 'red' :
		print("the player just earned 15 points")

if alien_color:
	print("alien_color is not an empty list")
else:
	print("alien_color is an empty list")

usernames = ['azalea','cui','mali','jing','admin']
for name in usernames:
	if name == 'admin':
		print(name+' This is a special greeting!')
	else:
		print(name+' This is a generic greeting!')

usernames = []
if usernames == []:
	print("We need to find some users.")
current_users = ['azalea','CUi','mali','jing','admin']
new_users = ['qian','wei','cui','mali']
tem_users = []
for cuser in current_users:
	tem_users.append(cuser.lower())
print(tem_users)
for user in new_users:
	#user should compare with all lowercase of current_users
	if user in tem_users:
		print(user+" the person should need to enter a new username")
	else:
		print(user+ " is available.")
ordinal_num = list(range(1,10))
for num in ordinal_num:
	if num == 1:
		print("1st")
	elif num == 2:
		print('2nd')
	elif num == 3:
		print('3rd')
	elif num == 4:
		print('4th')
	else:
		print('none')
dic_person = {
	'first_name':'qian',
	'last_name':'wei',
	'age': '23',
	'city':'China',
	'location':'UK',
}
for key,value in dic_person.items():
	print(key.title() + value.title())
glossary = {
	'azalea' : 'java',
	'ivy' : 'html',
	'jing' : 'Python',
	'david' : 'python',
	'cui' : 'css',
	'job' : 'c',
	'heng' : 'python',
	'yikai' : 'python',
}
for name,language in glossary.items():
	print('name: '+ 
		name.title() + 
		' likes ' + 
		language.title() + 
		' language.'
		)
rivers = {
	'jiang' : 'china',
	'saina' : 'paris',
	'nile' : 'egypt',
}
for river, country in rivers.items():
	print('The '+river.title() + ' runs through ' + country.title() )
for river in rivers.keys():
	print(river.title())
names = ['huang', 'azalea', 'ivy', 'job', 'heng']
for name in glossary.keys():
	if name in names :
		print(name + ', thanking for responding!')
	else:
		print(name + ', please take the poll.')

aliens = []
for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['point'] = 10
for alien in aliens[:5]:
	print(alien)
people =[dic_person, glossary]
print(people)
dog = {
	'kind' : 'dog',
	'name' : 'ivy',
}
cat = {
	'kind' : 'cat',
	'name' : 'qian',
}
pets = [dog, cat]
print(pets)

favorite_places = {
	'ivy' : ['xian','chongqing','beijing'],
	'qian' : ['hebei','paris','sheffield'],
	'wei' : ['leeds','york','london','livepool'],
}
for name,places in favorite_places.items():
	print(name + ' , the favorite places are : ')
	for place in places:
		print('\t' + place)
cities = {
	'paris':{
		'country' : 'france',
		'population' : 1264532,
		'fact' : 'it is beautiful.'
	},
	'london':{
		'country' : 'UK',
		'population' : 2764582,
		'fact' : 'it is beautiful.'
	},
	'sheffield':{
		'country' : 'UK',
		'population' : 45728945,
		'fact' : 'it is beautiful.'
	},
}
for city, city_info in cities.items():
	print('This is some information about the '+city+
		':\t'+ city +' is in '+ city_info['country'])


print("YH - Test changingTest")