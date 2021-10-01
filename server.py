from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


def write_to_csv(data: dict):
    try:
        with open('database.csv', 'a', newline='') as csvfile:
            fieldnames = ['email', 'subject', 'message']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
    except:
        return 'Writing went wrong'


@app.route("/")
def run_default():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        else:
            return 'something went wrong, try again'
    except:
        return 'did not get POST data'


def write_to_database(data):    #not in use
    pass
    '''Writes the email, subject and message to the database and formats it.'''
    with open('database.txt', 'a') as database:
        database.write('____________________\n')
        for k,v in data.items():
            database.write(k)
            database.write(' : ')
            database.write(v)
            database.write('\n')