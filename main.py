import requests
import os
from flask import Flask, render_template
from math import ceil
from datetime import datetime
from faker import Faker
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

url = 'https://api.chucknorris.io/jokes/random'
fake = Faker()

messages = [{'username': fake.name(), 'text': requests.get(url).json()['value'], 'timestamp': datetime.now()} for i in range(1,101)]
# messages = [{'username': fake.name(), 'text': i, 'timestamp': datetime.now()} for i in range(1,101)]
messages.reverse()

class MessageForm(FlaskForm):
    text_message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

def list_cutter(messages_list, page_number):
    return messages_list[5*(page_number - 1):5*page_number]

@app.route("/", methods=['GET', 'POST'])
def home(messages_list=messages, page_count=ceil(len(messages)/5)):
    joke = requests.get(url).json()['value']
    form = MessageForm()
    if form.validate_on_submit():
            messages.insert(0, {'username': fake.name(), 'text': form.text_message.data, 'timestamp': datetime.now()})
    return render_template('home.html', messages_list=list_cutter(messages_list, 1), page_count=ceil(len(messages)/5), chuck_norris_joke=joke, form=form)

@app.route("/<int:page_number>", methods=['GET', 'POST'])
def chat(page_number, messages_list=messages, page_count=ceil(len(messages)/5)):
    joke = requests.get(url).json()['value']
    form = MessageForm()
    if form.validate_on_submit():
        messages.insert(0, {'username': fake.name(), 'text': form.text_message.data, 'timestamp': datetime.now()})
    return render_template('home.html', messages_list=list_cutter(messages_list, page_number), page_count=ceil(len(messages)/5), chuck_norris_joke=joke, form=form)

if __name__ == "__main__":
    app.run(debug=True)
