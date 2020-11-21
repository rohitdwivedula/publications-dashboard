import json
import mysql.connector 
import re

def sanitize(raw_str):
	if raw_str is None:
		return None
	else:
		return re.sub('[^A-Za-z0-9 ]+', '', raw_str)[:700]

db = mysql.connector.connect(
	host="localhost",
	user="research",
	password="123",
	database="research"
)
cursor = db.cursor()
print("[UPDATE] Database connection establishment. Done.")

with open("all_data.json", "r") as datafile:
	data = datafile.read()

data = json.loads(data)
print("[UPDATE] Data read from JSON file. Done.")

'''
Foreign Keys for organisation
+--------+----------------+------------------------------+
| org_id | name           | domain                       |
+--------+----------------+------------------------------+
|      1 | BITS Pilani    | @pilani.bits-pilani.ac.in    |
|      2 | BITS Goa       | @goa.bits-pilani.ac.in       |
|      3 | BITS Hyderabad | @hyderabad.bits-pilani.ac.in |
|      4 | BITS Dubai     | @dubai.bits-pilani.ac.in     |
+--------+----------------+------------------------------+
'''

colleges = dict()
colleges["@pilani.bits-pilani.ac.in"] = 1
colleges["@goa.bits-pilani.ac.in"] = 2
colleges["@hyderabad.bits-pilani.ac.in"] = 3
colleges["@dubai.bits-pilani.ac.in"] = 4

researcher_id = 0
pub_id = 0

names = []
for researcher in data["authors"]:
	print("Processing Researcher:", researcher["name"], "with", len(researcher["publications"]), "publications")
	if researcher["email"] not in ["@pilani.bits-pilani.ac.in", "@goa.bits-pilani.ac.in", "@hyderabad.bits-pilani.ac.in", "@dubai.bits-pilani.ac.in "]:
		continue
	researcher_id += 1
	cursor.execute("SELECT * FROM Researcher WHERE name = '{name}';".format(name=researcher["name"]))
	found = False
	for x in cursor:
		found  = True
	if not found:
		# ADD NEW RESEARCHER
		query = """INSERT into Researcher (researcher_id, org_id, name, h5_index, h5_index_ten, i10_index, i10_index_ten, citations) VALUE ({researcher_id}, {org_id}, '{name}', {h}, {h_10}, {i10}, {i10_10}, {citations});"""		
		citations = researcher.get("citedby")
		if citations is None:
			citations = -1
		query = query.format(researcher_id = researcher_id, org_id = colleges[researcher["email"]], name=researcher["name"].strip(), h = researcher["hindex"], 
			h_10 = researcher["hindex5y"], i10 = researcher['i10index'], i10_10 = researcher["i10index5y"], citations = citations)
		cursor.execute(query)

		# ADD Researcher Interests
		values = []
		for interest in researcher["interests"]:
			values.append((researcher_id, interest))
		query = "INSERT into Interests (researcher_id, interest) VALUE (%s, %s);"
		
		if len(values):
			cursor.executemany(query, values)

		count = 1
		# Add Publications and Citations
		for pub in researcher["publications"]:
			if count%20 == 0:
				print("[PROGRESS] Processed", count, "publications so far...")
			pub_id += 1
			query = "INSERT into Publication (publication_id, title, year, publisher, citations) VALUE ({pid}, '{title}', {year}, '{publisher}', {citations});"
			publisher = pub["bib"].get("publisher")
			year = pub["bib"].get('year')
			if year is not None:
				year = int(year)
			else:
				year = 0
			query = query.format(pid = pub_id, title = sanitize(pub["bib"]['title']), year = year, publisher = sanitize(publisher), citations = int(pub['bib']['cites']))
			cursor.execute(query)
			query = "INSERT INTO Authors (publication_id, author_id) VALUE ({pub_id}, {author_id});".format(pub_id = pub_id, author_id = researcher_id)
			cursor.execute(query);

			## Add citations of current publication
			if 'cites_per_year' in pub:
				entries = []
				for year, cites in pub['cites_per_year'].items():
					entries.append((pub_id, int(year), int(cites)))
				query = "INSERT into Citations (publication_id, year, citation_count) VALUE (%s, %s, %s);"
				cursor.executemany(query, entries)
			count+=1
		db.commit()
names = set(names)
print(len(names))
print(len(data["authors"]))
