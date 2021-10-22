from neo4j import GraphDatabase


uri = 'neo4j://localhost:7687'
username = 'neo4j'
password = 'amir'

class Company:
	def __init__(self, uri, username, password):
		self.driver = GraphDatabase.driver(uri, auth=(username, password))

	def close(self):
		self.driver.close()

	def get_all(self, tx):
		result = tx.run("MATCH(n) RETURN n")
		return result.data()

	def get_person(self, tx, name):
		result = tx.run("MATCH (n:devops) WHERE n.name=$name RETURN n", name=name)
		return result.data()

	def create_person(self, tx, name, age):
		tx.run("CREATE (n:devops{name:$name, age:$age})", name=name, age=age)

	def read_execute(self, func, *args, **kwargs):
		with self.driver.session() as session:
			result = session.read_transaction(func, *args, **kwargs)
			return result

	def write_execute(self, func, *args, **kwargs):
		with self.driver.session() as session:
			session.write_transaction(func, *args, **kwargs)


a = Company(uri, username, password)
result = a.read_execute(a.get_person, 'kevin')
print(result)
