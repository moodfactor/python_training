# guess_me = 7
# number = 1
# while True:
#     if number < guess_me:
#         print('too low')
#     elif number == guess_me:
#         print('found it')
#         break
#     else:
#         print('oops')
#         break
#     number +=1
# guess_me = 5
# for number in range(10):
#     if number < guess_me:
#         print('too low')
#     elif number == guess_me:
#         print('found it!')
#         break
#     else:
#         print('oops')
#         break
# years_list = [1980, 1981, 1982, 1983, 1984, 1985]
# things = ["mozzarella","cinderella", "salmonella"]
# names = things[1]
# cheesy = things[0]+ things[2]
# for name in things:
#     if name in names:
#         print(name.capitalize())
#     elif name in cheesy:
#         print(name.upper())
# print(things.remove("salmonella"))
# surprise = ["Groucho", "Chico", "Harpo"]
# print(surprise[-1].lower())
# print(surprise.sort(reverse=True))
# for n in surprise:
#      print(n.capitalize())
# even = [n for n in range(10) if n % 2 == 0]
# print(even)

# start1 = ["fee", "fie", "foe"]
# rhymes = [
# ("flop", "get a mop"),
# ("fope", "turn the rope"),
# ("fa", "get your ma"),
# ("fudge", "call the judge"),
# ("fat", "pet the cat"),
# ("fog", "walk the dog"),
# ("fun", "say we're done"),
# ]
# start2 = "Someone better"
# for (a, b) in zip(start1, 'first'):
#     print(a.capitalize() + "! ", "first".capitalize() + "!")
my_dict = {'day': 'A period of twenty-four hours, mostly misspent',
'positive': "Mistaken at the top of one's voice",
'misfortune': 'The kind of fortune that never misses'}
my_dict['ahmed'] = 'man'
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry',
'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}
others = { 'Marx': 'Groucho', 'Howard': 'Moe' }
pythons.update(others)
names = {item: f'!<{item.upper()}>!' for item in pythons.keys() }
print(names)
