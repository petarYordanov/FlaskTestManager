#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, render_template

from face_detect.face_detection_tests import *
from ui_pom.end_to_end_tests import EndToEndTests

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/faceResults")
def GetData():
    test1 = test_four_faces()
    test2 = test_one_face()
    test3 = test_three_children_faces()
    test4 = test_one_face()
    return render_template("face_detection_results.html", test1=test1, test2=test2, test3=test3, test4=test4)

@app.route('/e2eResults')
def e2e():
    e2e = EndToEndTests()
    test1 = e2e.test_get_student_details()
    return render_template("e2e_results.html", test1=test1)



app.run()
if __name__ == '__main__':
	app.run(debug = False)
