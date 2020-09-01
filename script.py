from pymongo import MongoClient
from scholarly import scholarly

'''
Sample author info fetched by the library

{
    'affiliation': 'IEEE Senior Member and Professor of Comp. Sc at BITS, '
                'Hyderabad',
    'citedby': 990,
    'email': '@hyderabad.bits-pilani.ac.in',
    'filled': False,
    'id': 'tFy6PS4AAAAJ',
    'interests': ['Information Security',
               'Artificial Intelligence',
               'Machine Learning',
               'Bigdata'],
    'name': 'Chittaranjan Hota',
    'url_picture': 'https://scholar.google.com/citations?view_op=medium_photo&user=tFy6PS4AAAAJ'
}
''' 

def getCleanDict(info):
    if str(type(info)) in ["<class 'scholarly.author.Author'>", "<class 'scholarly.publication.Publication'>", "<class 'dict'>"]:
        new_dict = dict()
        for key in list(filter(lambda x: x[0] != '_', dir(info))):
            if str(type(getattr(info, key))) != "<class 'builtin_function_or_method'>":
                new_dict[str(key)] = getCleanDict(getattr(info, key))
        return new_dict
    else:
        return info

GET_ALL_PUBLICATION_DATA = False    

client = MongoClient()
db = client.research_database
research_data = db.research_data

search_query = "Chittaranjan Hota" # Find everything from specific college
results = scholarly.search_author(search_query)
author_number = 1
try:
    while True:
        print("Processing author #", author_number)
        author_number += 1
        author_info = next(results).fill()
        num = 1
        if GET_ALL_PUBLICATION_DATA:
            for publication in author_info.publications:
                print("Processing publication #", num, "for author", author_info.name)
                num += 1
                tmp = publication.fill()
        author_dict = getCleanDict(author_info)
        research_data.insert_one(author_dict)
        break
except StopIteration:
    print("All authors completed on this run...")

