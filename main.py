from flask import Flask, jsonify, json, redirect, url_for, render_template, request, flash
import requests
import task

app = Flask(__name__)
app.secret_key = "Hassaan"


@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        batchSize = request.form['batchSize']
        latency = request.form['latency']
        output=task.getCrimesCategories(batchSize,latency)
        output2=task.dropdown()

        return render_template('frontend.html', data2={'value':output,'latency':latency,'batchSize':batchSize, 'drop':output2})
        #return requeoutputst.form
    else:
        output=task.dropdown()
        return render_template('frontend.html',data2={'drop':output})
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
