from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail


# with open("config.json",'r') as c:
#     params = json.loads(c)["params"]

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MIL_USE_SSL=True,
    MAIL_USERNSME='', #use paams from config.json entries
    MIL_PASSWORD='' #use paams from config.json entries
)
mail=MAIL(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pythondb'
# app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
data = SQLAlchemy(app)
print(data)
print("\n\n")


class Contact(data.Table):
    sno = data.Column(data.Integer, primary_key=True)
    name = data.Column(data.String(80), unique=False, nullable=False)
    phone = data.Column(data.String(12), nullable=False)
    message = data.Column(data.String(120), nullable=False)
    mail = data.Column(data.String(20), nullable=False)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        message = request.form.get('message')
        mail = request.form.get("mail")
        # entry = Contact(name=name, phone=phone, message=message, mail=mail)
        entry = Contact(name=name)
        data.session.add(entry)
        data.session.commit()
        mail.send_message('New message from' + name,
                          sender=mail,
                          recipients=['savardekarrohit@gmail.com'],
                          body=message + '\n' + phone
# S.no name phone message mail
    return render_template('contact.html')


@app.route("/post")
def post():
    return render_template('post.html')


app.run(debug=True)
