from pymongo import MongoClient
from scholarly import scholarly
from bson.json_util import dumps


client = MongoClient("mongodb+srv://admin:by6sutx4RltkEb8Y@cluster0.kc1e6.mongodb.net/?retryWrites=true&w=majority")
db = client.research_database
research_data = db.research_data

cursor = research_data.find()
list_cur = list(cursor)
json_data = dumps(list_cur)
with open('data.json','w') as file:
	file.write(json_data)