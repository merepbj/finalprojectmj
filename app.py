# from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect
import pickle


app = Flask(__name__)

#mongo = PyMongo(app, uri='mongodb://localhost:27017/final_project_db')
pickle_model = None 
with open("predict_wins.sav", 'rb') as file:
    pickle_model = pickle.load(file)

    print(pickle_model)


@app.route('/')
def home():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)