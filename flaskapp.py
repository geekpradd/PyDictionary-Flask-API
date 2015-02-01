from flask import Flask
import json
from PyDictionary import PyDictionary
app=Flask(__name__)
d=PyDictionary()
@app.route('/')
def index():
	return "PyDictionary API: Check out the docs for usage."
@app.route('/api/meaning/<name>',methods=['GET'])
def meaning(name):
	value=d.meaning(name)
	if value is None:
		return json.dumps({'error':'Word has no meaning in API'})
	return json.dumps(value)
	

@app.route('/api/synonym/<name>',methods=['GET'])
def synonym(name):
	value=d.synonym(name)
	if value is None:
		return json.dumps({'error':'Word has no synonym in API'})
	return json.dumps(value)
@app.route('/api/antonym/<name>',methods=['GET'])
def antonym(name):
	value=d.antonym(name)
	if value is None:
		return json.dumps({'error':'Word has no antonym in API'})
	return json.dumps(value)
@app.route('/api/translate/<lang>/<word>',methods=['GET'])
def translate(lang,word):
	return d.translate(word,lang)
if __name__=='__main__':
	app.run(debug=True)