from flask import Flask, render_template
import json

app = Flask(__name__)
app.debug = True
resume_path = 'data/resume-fresh.json'


def read_resume(resume_path=resume_path):
    return json.load(open(resume_path))


@app.route('/')
def show_resume():
    return render_template('compact.html', r=read_resume())

app.run()
