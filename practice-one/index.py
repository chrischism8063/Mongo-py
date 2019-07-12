import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')


db = client['second_test']

posts = db.posts

post_1 = {
    'title': 'Title One',
    'content': 'One content',
    'author': 'One author'
}

post_2 = {
    'title': 'Title Two',
    'content': 'Two content',
    'author': 'Two author'
}

post_3 = {
    'title': 'Title Three',
    'content': 'Three content',
    'author': 'Three author'
}

post_4 = {
    'title': 'Title Four',
    'content': 'Four content',
    'author': 'Four author'
}

post_5 = {
    'title': 'Title Five',
    'content': 'Five content',
    'author': 'Five author'
}

result_one = posts.insert_one(post_1)
print(result_one)

result_two = posts.insert_one(post_2)
print(result_two)

result_three = posts.insert_one(post_3)
print(result_three)

result_four = posts.insert_one(post_4)
print(result_four)

result_five = posts.insert_one(post_5)
print(result_five)
