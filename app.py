from flask import Flask, request, render_template, send_from_directory #import main Flask class and request object
import csv

app = Flask(__name__, static_url_path='') #create the Flask app

@app.route('/')
@app.route('/<path:path>')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/form-receive', methods=['POST'])
def form_receive():
    name = request.form['name']
    email = request.form['email']
    fieldnames = ['name', 'email']
    with open('names.csv',"a")as inFile:
        writer = csv.DictWriter(inFile, fieldnames=fieldnames)
        writer.writerow({'name':name, 'email':email})
    return 'thanks'


if __name__ == '__main__':
    app.run(port=5000) #run app in debug mode on port 5000
