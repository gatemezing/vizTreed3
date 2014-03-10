#! /usr/bin/python
# -*- coding: utf-8 -*-

use_sparql = True

from SPARQLWrapper import SPARQLWrapper, JSON
import json
import sys
import argparse

# --- liste des classes et individus - requete 1 ---

def makeJSON(endpoint): 
	if use_sparql:
		sparql = SPARQLWrapper(endpoint) #"http://dbpedia.org/sparql"
		sparql.setQuery("""	
	select ?classe ?label (count(?x) as ?nombre) where
	{ ?x a ?classe.
	 ?classe a ?class.
	 ?classe rdfs:label ?label.
	 filter(lang(?label)="en")
	 #filter (regex(str(?classe), "http://dbpedia.org/ontology", "i" )) 
	filter(?class=owl:Class || ?class=rdfs:Class)
	}order by asc(?classe)
	 

		""")
		sparql.setReturnFormat(JSON)
		classesd3 = sparql.query().convert()
	else:
			classesd3 = json.load(open("classesd3.json"))

	new_classes = {"name":"Class-Resources",
			'children': []
		  
			}

	for classes in classesd3["results"]["bindings"]:
		item = {}
		item['uri'] = classes['classe']['value']
		item['name'] = classes['label']['value'] 
		item['size'] = classes['nombre']['value']
		
		new_classes['children'].append(item)

	with open("classesd3.json", "w") as f:
			f.write(json.dumps(new_classes, sort_keys=True, indent=4))

def makeJSONfr(endpoint): 
	if use_sparql:
		sparql = SPARQLWrapper(endpoint) #"http://dbpedia.org/sparql"
		sparql.setQuery("""	
	select ?classe ?label (count(?x) as ?nombre) where
	{ ?x a ?classe.
	 ?classe a ?class.
	 ?classe rdfs:label ?label.
	 filter(lang(?label)="fr")
	 #filter (regex(str(?classe), "http://dbpedia.org/ontology", "i" )) 
	filter(?class=owl:Class || ?class=rdfs:Class)
	}order by asc(?classe)
	 

		""")
		sparql.setReturnFormat(JSON)
		classesd3 = sparql.query().convert()
	else:
			classesd3 = json.load(open("classesd3.json"))

	new_classes = {"name":"Class-Resources",
			'children': []
		  
			}

	for classes in classesd3["results"]["bindings"]:
		item = {}
		item['uri'] = classes['classe']['value']
		item['name'] = classes['label']['value'] 
		item['size'] = classes['nombre']['value']
		
		new_classes['children'].append(item)

	with open("classesd3.json", "w") as f:
			f.write(json.dumps(new_classes, sort_keys=True, indent=4))
			
def main():
    # parse command line options
	parser = argparse.ArgumentParser(description='Process and endpoint and get list of classes with number of instances.') 
	parser.add_argument('-e', metavar='URL', help='the enpoint to query')
	parser.add_argument('-f', metavar='lang', help='the language to retrieve the label classes in "fr"')
	args= parser.parse_args() 
	#for arg in args:
	if (args.e) :
		makeJSON(args.e) # makeJSON() is defined elsewhere
	if (args.f) :
		makeJSONfr(args.f)
		
if __name__ == "__main__":
    main()
			