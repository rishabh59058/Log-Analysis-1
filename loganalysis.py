#!/usr/bin/env python3
import psycopg2

# Top 3 popular authors
query1 = """select title, count(title) as total_views from articles, log
where path like concat('%', articles.slug) group by title
order by total_views desc limit 3"""

# Top popular articles
query2 = """select name, count(title) as page_views from authors, articles, log
where authors.id = author and path like concat('%', articles.slug)
group by name order by page_views desc"""

# More than 1% of requests lead to errors
query3 = """select to_char(date,'Mon DD,YYYY') as date,error from view3 where
error>1.0"""

print("LIST OF TOP THREE POPULAR ARTICLES ARE:")
db = psycopg2.connect("dbname = news")
c1 = db.cursor()
c1.execute(query1)
data = c1.fetchall()
for i in range(0, len(data)):
    title = data[i][0]
    total_views = data[i][1]
    print("%s -- %d" % (title, total_views)+" views")
db.close()
print("")
print("THE LIST OF POPULAR AUTHORS ARE:")
db = psycopg2.connect("dbname = news")
c2 = db.cursor()
c2.execute(query2)
data = c2.fetchall()
for i in range(0, len(data)):
    name = data[i][0]
    page_views = data[i][1]
    print("%s -- %d" % (name, page_views)+" views")
db.close()
print("")
print("PERCENTAGE ERROR MORE THAN 1.0:")
db = psycopg2.connect("dbname = news")
c3 = db.cursor()
c3.execute(query3)
data = c3.fetchall()
for i in range(0, len(data)):
    date = data[i][0]
    error = data[i][1]
    print("%s -- %.1f" % (date, error)+"% errors")
db.close()
