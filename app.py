from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect

app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost:27017/final_project_db')

