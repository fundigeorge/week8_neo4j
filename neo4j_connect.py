# rWZy4F1mL-nWoxiRviwQCaGYNE0WiQWtQ57XYYnFcmU

# (m:Movie[])-->(p:person)

# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth
import pandas as pd


driver = GraphDatabase.driver(
  "bolt://44.200.158.245:7687",
  auth=basic_auth("neo4j", "correlation-documentation-swimmers"))

cypher_query = '''
MATCH (movie:Movie {title:$favorite})<-[:ACTED_IN]-(actor)-[:ACTED_IN]->(rec:Movie)
 RETURN distinct rec.title as title LIMIT 20
'''
tom_hanks = "MATCH (p:Person) - [a:ACTED_IN] -> (m:Movie ) where m.born >1950 return p, m, a"

#transaction function that does  the actual query of data
def get_actor_movies(tx, actor_name):
    actor_query ="MATCH (p:Person {name:$name})-[:ACTED_IN]-> (m:Movie) return count(p) as movie_number, p.name, m"
    results = tx.run(actor_query, name=actor_name).data()
    #results has to be processed, atleast by returning list(results). Results methods like data(), value(key=name,), fetch(n)
    #single(strict=false), consume()
    return results
    
#create a session, the with as session will close at the end of with clause
actor_name = 'Tom Hanks'
with driver.session(database="neo4j") as session:
    reconds = session.execute_read(get_actor_movies, actor_name)
    print(type(reconds), 'query results records', reconds)
    for record in reconds:
        print(record)
        break





# driver = GraphDatabase.driver(
#     "bolt://44.200.158.245:7687",
#     auth = basic_auth("neo4j", "correlation-documentation-swimmers")
# )
# cypher_query = """
# """
# with driver.session(database="neo4j") as session:
#     results = session.read_transaction(lambda tx: tx.run(cypher_query, favorite="The Matrix").data())
    
#     for records in results:
#         print(records['title'])
# driver.close()

