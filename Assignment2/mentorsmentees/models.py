from datetime import datetime
from django_neomodel import DjangoNode
from neomodel import StructuredNode, StringProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo, Relationship
from django import forms

class Person(DjangoNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    created = DateTimeProperty(default=datetime.utcnow)

    mentee = RelationshipTo('Person', 'IS_MENTOR_OF')

    def __str__(self):
        return "Name : "+self.name

    def getmentees(self):
        results, columns = self.cypher("MATCH (a)-[]-(b) WHERE id(b)={self} RETURN a")
        return [self.inflate(row[0]) for row in results]
