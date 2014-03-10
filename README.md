vizTreed3
=========

A small python script to visualize easily instances in RDF datasets using treemap in d3.

We suppose you copy the content to this location {HOME_INSTALL}
{HOME_PYTHON27} your home install of python2.7. 
To be sure, open a terminal an type python --version. 
c:\python27> python makeJSONd3.py [-f] [-e] endpointURI 
	copy/Y (mv) classesd3.json {HOME_INSTALL}
	cd {HOME_INSTALL}
	python -m http.server  (3x) | python -m SimpleHTTPServer
	open your browser at localhost:8000 or 127.0.0.0:80

=========
Dependencies:
	python 2.7
	SPARQLWrapper
	JSON 

=========
Visualization based on d3 Treemap
"Right view" shows the top first classes with a large number of instances
"Left view" shows the classes with fewer instances.

What can vizTreed3 con do for you?
=========
Instant treemap-like view of an endpoint
Filter by language tag "en", "fr" (-e, -f)
Example: dbpedia fr instances at a glance
Issue #1: Don't work for lod.openlinksw.com/sparql

Why might you need viz-tree-d3 ?
=========
Check you converted all your raw/legacy dataset
Quick view of instances in a given endpoint for further analysis
screen scraping of RDF datasets for instance matching
Dataset instance monitoring and quality checking

How it works
=========
input for makeJSON: endpoint URL, SPARQL query for counting instances per classes.
output for makeJSON: classesd3.json (d3 alike for viewing using d3.js TreeMap)
input for treemap: classesd3.json
