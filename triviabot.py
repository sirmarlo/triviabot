#!/usr/bin/python

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
	return "<html><a href='http://gph.is/2w17nf7'/></html>"

@app.route('/scores', methods=['GET', 'POST'])
def scores():
	return "Dorville - 14, Dan - 8, Marlo - 7, Matt - 1, Achintya - 1"