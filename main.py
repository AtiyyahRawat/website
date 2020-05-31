# -*- coding: utf-8 -*-
"""
Created on Wed May 20 07:47:07 2020

@author: atiyy
"""

from flask import Flask, render_template
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "BY(7Mhc(ho?ypHQ"

@app.route('/')
@app.route('/home')
def homepage():
    return render_template("home.html")
@app.route('/posts')
def posts():
    return render_template("posts.html", posts_data=dat)
@app.route('/posts/Sunlight_&_Raindrops')
def p230220():
    return render_template("Sunlight_&_Raindrops.html")
@app.route('/posts/Cambridge')
def p010420():
    return render_template("Cambridge.html")
@app.route('/posts/Stress_Handling')
def p220220():
    return render_template("Stress.html")


if __name__ == '__main__':
    dat = {"num": 3,
         "pic": ["../static/website aesthetics/pink/Raindrops_tn.jpg", "../static/website aesthetics/pink/IMG-20200120-WA0000-01_tn.jpg", "../static/website aesthetics/mix/library_tn.jpg"],
         "title": ["Sunlight and Raindrops", "My Cambridge Rejection Story (yay)", "Dealing with the Stress of A Levels" ],
         "desc": ["A short fluff creative writing moment", "An imagined speech to my Mossbourne teachers and peers", "Some techniques I use to deal with all of this"],
         "link": ["p230220","p010420","p220220"]}
    app.run(host='0.0.0.0', port=5000)