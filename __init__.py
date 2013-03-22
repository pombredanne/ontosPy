VERSION = 1.0



"""
OntosPy.PY VERSION 1.0

Created	 on 2011-03-17
Modified on 2011-11-11

Copyright (c) 2010 __Michele Pasin__ <michelepasin.org>. All rights reserved.




****************
Dependencies: rdflib <http://www.rdflib.net/>
Tested on 2.4 and 3.0

Originally, I developed this in order to get the hang of the RdfLib library.

You can pass an OWL or RDFS ontology to the OntosPy class, and it'll give you a bunch of useful information about it. That's all!

The file can be used in standalone mode too.

****************





EXAMPLE: LOADING AND QUERYING the FOAF ONTOLOGY

In [1]: from OntosPy import *

In [2]: onto = OntosPy("http://xmlns.com/foaf/spec/20100809.rdf")

In [3]: onto.toplayer
Out[3]:
[rdflib.URIRef('http://xmlns.com/foaf/0.1/Agent'),
 rdflib.URIRef('http://www.w3.org/2000/01/rdf-schema#Class'),
 rdflib.URIRef('http://www.w3.org/2004/02/skos/core#Concept'),
 rdflib.URIRef('http://xmlns.com/foaf/0.1/Document'),
 rdflib.URIRef('http://xmlns.com/foaf/0.1/LabelProperty'),
 rdflib.URIRef('http://www.w3.org/2000/01/rdf-schema#Literal'),
 rdflib.URIRef('http://www.w3.org/2000/10/swap/pim/contact#Person'),
 rdflib.URIRef('http://xmlns.com/foaf/0.1/Project'),
 rdflib.URIRef('http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing'),
 rdflib.URIRef('http://www.w3.org/2002/07/owl#Thing')]

In [4]: onto.printTree()
foaf:Agent
----foaf:Group
----foaf:Organization
----foaf:Person
rdfs:Class
http://www.w3.org/2004/02/skos/core#Concept
foaf:Document
----foaf:Image
----foaf:PersonalProfileDocument
foaf:LabelProperty
rdfs:Literal
http://www.w3.org/2000/10/swap/pim/contact#Person
----foaf:Person
foaf:Project
http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing
----foaf:Person
owl:Thing
----foaf:OnlineAccount
--------foaf:OnlineChatAccount
--------foaf:OnlineEcommerceAccount
--------foaf:OnlineGamingAccount


In [5]: document = onto.find_class_byname("document")

In [6]: document
Out[6]:
[rdflib.URIRef('http://xmlns.com/foaf/0.1/Document'),
 rdflib.URIRef('http://xmlns.com/foaf/0.1/PersonalProfileDocument')]

In [7]: document = document[0]

In [8]: document
Out[8]: rdflib.URIRef('http://xmlns.com/foaf/0.1/Document')

In [9]: onto.get_classAllSubs(document)
Out[9]:
[rdflib.URIRef('http://xmlns.com/foaf/0.1/Image'),
 rdflib.URIRef('http://xmlns.com/foaf/0.1/PersonalProfileDocument')]

In [10]: onto.get_classAllSupers(document)
Out[10]: []

In [11]: onto.get_classComment(document)
Out[11]: rdflib.Literal('A document.', language=None, datatype=None)



"""