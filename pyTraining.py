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
# my_dict = {'day': 'A period of twenty-four hours, mostly misspent',
# 'positive': "Mistaken at the top of one's voice",
# 'misfortune': 'The kind of fortune that never misses'}
# my_dict['ahmed'] = 'man'
# pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry',
# 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}
# others = { 'Marx': 'Groucho', 'Howard': 'Moe' }
# pythons.update(others)
# names = {item: f'!<{item.upper()}>!' for item in pythons.keys() }
# empty_set = set('letters')
# drinks = {
# 'martini': {'vodka', 'vermouth'},
# 'black russian': {'vodka', 'kahlua'},
# 'white russian': {'cream', 'kahlua', 'vodka'},
# 'manhattan': {'rye', 'vermouth', 'bitters'},
# 'screwdriver': {'orange juice', 'vodka'}
# }

# for names, contents in drinks.items():
#     if contents & {'vermouth', 'orange juice'}:
#         print(names)
# def nonbuggy(args, result = None):
#     if result is None:
#         result = []
#         result.append(args)
#         print(result)
# nonbuggy('d', nonbuggy('sd'))
# def print_args(*args):
#     print('positional tuple ', args)
# print_args('a', 'Ahmed', {'animal': 'Rat'}, 332)
# def print_kwargs(**kwargs):
#     print("keyward agrs: ", kwargs)
# print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
# def print_data(data, *, start = 0, end = 100):
#     for value in data[start: end]:
#         print(value)
# data = ['a', 'b', 'c', 'd', 'e', 'f']
# print_data(data, start=5, end=100)
# def edit_data(args):
#     data[0]=args
#     print(data)
# edit_data(6)
# def answer():
#     print('answer')
# def run_something(func):
#     func()
# run_something(answer)
# def sum_args(*args):
#     return sum(args)
# def run_positional_args(func, *args):
#     return func(*args)
# s= run_positional_args(sum_args, 2, 4, 6)
# print(s)
# def outer(a, b):
#     def inner(c,d):
#         return c+d
#     return inner(a,b)
# print(outer(5,3))
# def knights(saying):
#     def inner(quote):
#         return "We are the kninghts who say: '%s' " % quote
#     return inner(saying)
# print(knights('No')) 
# def knights2(saying):
#     def inner2():
#         return "We are the knights who say: '%s'" % saying
#     return inner2()
# a = knights2('help')
# b = knights2('dd')
# print(a)
# print(b)
# def edit_story(words, func):
#     for word in words:
#         print(func(word))
#
#
# stairs = ['thud', 'meow', 'thud', 'hiss']
# # def enliven(word):
# #     return word.capitalize() + '!!!'
# # edit_story(words= stairs, func= enliven)
# edit_story(words=stairs, func=lambda word: word.capitalize() + '!')
# def my_range(start=0, end=10, step=1):
#     number = start
#     while number < end:
#         yield number
#         number += step
#
#
# ranger = my_range(1, 5)
# for x in ranger:
#     print(x)
#
# pair: int
# genobj = (pair for pair in range(1, 6))
# for z in genobj:
#     print(z)
# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Running function:', func.__name__)
#         print('Positional arguments:', args)
#         print('Keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('Result:', result)
#         return result
#     return new_function
#
# @document_it
# def add_ints(a=3, b=6):
#     return a + b
# print(add_ints())

# id_1 = '15'
# def print_id():
#     id_1 = '20'
#     print('locals: ', locals())
# print_id()
#
# print(id_1)
# print('globals:', globals())
# def flatten(lol):
#     for item in lol:
#         if isinstance(item, list):
#             yield from flatten(item)
#         else:
#             yield item
#
# lol = [1, 2, [3,4,5], [6,[7,8,9], []]]
# print(flatten(lol))
# print(list(flatten(lol)))

short_list = [1, 2, 3]
position = 5


# try:
#     short_list[position]
# except:
#     print('Need a position between 0 and', len(short_list)-1, 'but got',
#           position)
# while True:
#     value = input('Position [q to quit]: ')
#     if value == 'q':
#         break
#     try:
#         position = int(value)
#         print(short_list[position])
#     except IndexError as err:
#         print('Bad Index:', err)
#     except Exception as other:
#         print('Error happened: ', other)
#
#
# class UppercaseException(Exception):
#     pass
# words = ['eenie', 'meenie', 'miny', 'MO']
# for word in words:
#     if word.isupper():
#         raise UppercaseException(word)
# try:
#     raise UppercaseException('panic')
# except UppercaseException as exc:
#     print(exc)
# def good():
#     return ['Harry', 'Ron','Hermione']
# print(good())
# def test(func):
#     def new_function(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return new_function()
# @test
# def greeting():
#     print('Greetings')
# greeting()

# class Cat:
#     def __init__(self, name):
#         self.name = name + ' cat'
#
#
# def dump(ff):
#     import pprint
#     pprint.pprint(vars(ff))
#
#
#
#
#
# class Meo(Cat):
#     def __init__(self, name, sound):
#         super().__init__(name)
#         self.sound = sound
#     def printHi(self):
#         print('hi', self.name)
#
#
# cat = Meo( 'a', 'd')
# dump(cat)
# cat2 = Cat('mohamed')
# print(cat.printHi())
# print(cat2)
# class Duck():
#     def __init__(self, input_name):
#         self.__name = input_name
#
#     @property
#     def name(self):
#         print('inside the getter')
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         print('inside the setter')
#         self.__name = value
#
#
# don = Duck('Donald')
# print(don._Duck__name)
# print(don.name)

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def diameter(self):
#         return 2 * self.radius
#
#
# c = Circle(5)
# print(c.radius)
# c.diameter = 20
# print(c.diameter)
# class A:
#     count = 0
#
#     def __init__(self):
#         A.count += 1
#
#     def exclaim(self):
#         print("I'm an A!")
#
#     @classmethod
#     def kids(cls):
#         print("A has", cls.count, "little objects.")
#
#
# a1 = A()
# a2 = A()
# a3 = A()
# A.kids()

# class BabblingBrook:
#     def who(self):
#         return 'Brook'
#
#     def says(self):
#         return 'Babble'
#
#
# brook = BabblingBrook()
#
#
# def who_says(obj):
#     print(obj.who(), 'says', obj.says())
#
# who_says(brook)
# class Word:
#     def __init__(self, word):
#         self.word = word
#
#     def __eq__(self, other):
#         return self.word.lower() == other.word.lower()
#
#     def __str__(self):
#         return self.word
#
#     def __repr__(self):
#         return 'Word("' + self.word + '")'
#
#
# first = Word('ha')
# class Bill:
#     def __init__(self, description):
#         self.description = description
#
#
# class Tail():
#     def __init__(self, length):
#         self.length = length
#
#
# class Duck():
#
#     def __init__(self, bill, tail):
#         self.bill = bill
#         self.tail = tail
#
#     def about(self):
#         print('This duck has a ', self.bill.description,
#               'bill and a', self.tail.length, 'tail')
#
#
# a_tail = Tail('long')
# a_bill = Bill('wide orange')
# duck = Duck(a_bill, a_tail)
# from collections import namedtuple
# Duck = namedtuple('Duck', 'bill tails')
# duck = Duck('wide orange', 'long')
# print(duck)
# parts = {'bill': 'wide orange', 'tails': 'long'}
# duck2 = Duck(**parts)
# duck3 = Duck(bill='wide orange', tails='long')
# print(duck2)
# print(duck3.bill)
# from dataclasses import dataclass
# @dataclass
# class AnimalClass:
#     name: str
#     habitat: str
#     teeth: int = 0
#
# snowman = AnimalClass('yeti', 'Himalayas', 46)
# duck = AnimalClass(habitat='lake', name='duck')
# print(snowman)
# print(duck)
# from attrs import *
#
#
# @define
# class Point3D(object):
#     x: int
#     y: int
#     z: int
#
#
# point1 = Point3D(1, 2, 3)
# point2 = Point3D(1, 2, 1+2)
# print(point2.__repr__())
# class Thing():
#     pass
#
#
# print(Thing)
# example = Thing()
# example2 = Thing()
# print(example)
#
#
# class Thing2():
#     letters: str = 'abc'
# print(Thing2.letters)
#
# class Thing3():
#     def __init__(self):
#         self.letters = 'xyz'
#
# print(Thing3().letters)
#
# from attrs import *
#
#
# @define
# class Element:
#     __name: str
#     __symbol: str
#     __number: int
#
#
# hydrogen1 = Element('Hydrogen', 'H', 1)
#
# mydict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
# print(hydrogen1)
#
# class Bear:
#     def eats(self):
#         return 'berris'
#
# bear = Bear()
# print(bear.eats())
# import sys
# for f in sys.path:
#     print(f.lower())
# from collections import defaultdict
# periodic_table = defaultdict(lambda : 'f')
# periodic_table = {"Hydrodgen": 1, "Helium": 2}
# print(periodic_table)
# carbon = periodic_table.setdefault("Carbon", 12)
# print(periodic_table)
# helium = periodic_table.setdefault("Helium", 947)
# print(periodic_table)
# food_counter = defaultdict(int)
# for food in ['spam', 'spam', 'eggs', 'spam']:
#     food_counter[food] += 1
key = 'my_var'
value = 1.234
formatted = f'{key!r:<10} = {value:.2f}'

print(formatted)
