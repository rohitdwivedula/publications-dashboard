#!/usr/bin/env python
# coding: utf-8

# In[25]:


from pymongo import MongoClient
from scholarly import scholarly


# In[26]:


GET_ALL_PUBLICATION_DATA = True
basic_attr =  ['affiliation', 'citedby','citedby5y', 'email','i10index5y', 'hindex','hindex5y', 'i10index','id','interests','name','url_picture']

client = MongoClient("mongodb+srv://admin:by6sutx4RltkEb8Y@cluster0.kc1e6.mongodb.net/?retryWrites=true&w=majority")
db = client.research_database
research_data = db.research_data


# In[27]:


search_query = "hyderabad.bits-pilani.ac.in" # Find everything from specific college
results = scholarly.search_author(search_query)


# In[ ]:


try:
    while True:
        author_info = next(results).fill()
        print("Processing", author_info.name, " with ID:", author_info.id)
        if research_data.find_one({'id': author_info.id}) is not None:
            print("Data for", author_info.name, "with ID", author_info.id, "already exists in MongoDB")
        else:
            author_dict = dict()
            for attr in basic_attr:
                if attr in dir(author_info):
                    author_dict[attr] = getattr(author_info, attr)
            attr = 'cites_per_year'
            author_dict[attr] = dict()
            for element in getattr(author_info, attr):
                author_dict[attr][str(element)] = getattr(author_info, attr)[element]
            pub_num = 1
            author_dict['publications'] = []
            if GET_ALL_PUBLICATION_DATA:
                for publication in author_info.publications:
                    if pub_num%10 == 1:
                        print("Processing publication #", pub_num,"of", len(author_info.publications) ,"for author", author_info.name)
                    if publication is not None and not publication.filled:
                        pub = dict()
                        try:
                            tmp = publication.fill()
                        except AttributeError:
                            print(publication.id_citations, "could not be filled.")
                        pub['bib'] = publication.bib
                        if 'cites_per_year' in dir(publication):
                            pub['cites_per_year'] = dict()
                            for element in publication.cites_per_year:
                                pub['cites_per_year'][str(element)] = publication.cites_per_year[element]
                            author_dict['publications'].append(pub)
                    pub_num += 1
            research_data.insert_one(author_dict)
            print("Data for", author_info.name, "(ID:", author_info.id,")")
except StopIteration:
    print("Done processing all authors")

