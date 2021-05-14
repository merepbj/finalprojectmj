# from flask_pymongo import PyMongo
import flask
# import Flask, render_template, redirect
import pickle
import pandas as pd


# app = Flask(__name__)
app = flask.Flask(__name__, template_folder='templates')


#mongo = PyMongo(app, uri='mongodb://localhost:27017/final_project_db')
pickle_model = None 
with open("predict_wins.sav", 'rb') as file:
    pickle_model = pickle.load(file)

    print(pickle_model)


# @app.route('/')
# def home():
#     return render_template('index.html')

# Set up the main route
from sklearn.preprocessing import OrdinalEncoder
@app.route('/', methods=['GET', 'POST'])
def main():
    if  flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        weightClass = flask.request.form['weightClass']
        country = flask.request.form['country']
        age = flask.request.form['age']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[weightClass, country, age]],
                                       columns=['weightClass', 'country', 'age'],
                                       index=['input'])

        enc = OrdinalEncoder()
        m = enc.fit_transform(input_variables)
        # Get the model's prediction
        prediction = pickle_model.predict(m)[0]
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('index.html',
                                     original_input={'Weight Class':weightClass,
                                                     'Country':country,
                                                     'Age':age},
                                     result=prediction,
                                     )



if __name__=='__main__':
    app.run(debug=True)