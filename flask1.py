# INCREMENTAL PYTHON CODE - REMOVED ID ATTRIBUTE FROM THE __INIT__() & __REPR__() METHODS contd.,
# OF THE PUBLICATION TABLE TO ENABLE AUTO-POPULATION
# SECTION 5: LECTURE: 23

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.update(

    SECRET_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:Pythondb@localhost:5433/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask'


@app.route('/new/')
def query_string(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is: {0} </h1>'.format(query_val)


@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='mina'):
    return '<h1> hello there ! {} </>'.format(name)


# strings
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> here is a string: ' + name + '</h1>'


# numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: ' + str(num) + '</h1>'


# add numbers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1> the sum is : {}'.format(num1 + num2) + '</h1>'


# floats
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is : {}'.format(num1 * num2) + '</h1>'

# ================================================================

# rendering templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')


# JINJA TEMPLATES 1
@app.route('/watch')
def top_movies():
    movie_list = ['autopsy of jane doe',
                  'neon demon',
                  'ghost in a shell',
                  'kong: skull island',
                  'john wick 2',
                  'spiderman - homecoming']

    return render_template('movies.html',
                           movies=movie_list,
                           name='Harry')


# JINJA TEMPLATES 2
@app.route('/tables')
def movies_plus():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('table_data.html',
                           movies=movies_dict,
                           name='Sally')


# JINJA2 - FILTERS
@app.route('/filters')
def filter_data():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('filter_data.html',
                           movies=movies_dict,
                           name=None,
                           film='a christmas carol')


# JINJA2 - MACROS
@app.route('/macros')
def jinja_macros():
    movies_dict = {'autopsy of jane doe': 02.14,
                   'neon demon': 3.20,
                   'ghost in a shell': 1.50,
                   'kong: skull island': 3.50,
                   'john wick 2': 02.52,
                   'spiderman - homecoming': 1.48}

    return render_template('using_macros.html', movies=movies_dict)

# ===================================================================
# PUBLICATION TABLE
class Publication(db.Model):
    __tablename__ = 'publication'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'{self.id} --The Publisher is {self.name}'


# BOOKS TABLE
class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # ESTABLISH RELATIONSHIP
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return f'book name : {self.title} \n By :{self.author}\n'


p1 = Publication(1, "Oxford Publications")
p2 = Publication(2, "Paramount Press")
p3 = Publication(3, "Oracle Books Inc")
p4 = Publication(4, "Vintage Books and Comics")
p5 = Publication(5, "Trolls Press")
p6 = Publication(6, "Broadway Press")
p7 = Publication(7, "Downhill Publishers")
p8 = Publication(8, "Kingfisher Inc")

b1 = Book("Miky's Delivery Service", "William Dobelli", 3.9, "ePub", "broom-145379.svg", 123, 1)
b2 = Book("The Secret Life of Walter Kitty", "Kitty Stiller", 4.1, "Hardcover", "cat-150306.svg", 133, 1)
b3 = Book("The Empty Book of Life", "Roy Williamson", 4.2, "eBook", "book-life-34063.svg", 153, 1)
b4 = Book("Life After Dealth", "Nikita Kimmel", 3.8, "Paperback", "mummy-146868.svg", 175, 2)
b5 = Book("The Legend of Dracula", "Charles Rowling", 4.6, "Hardcover", "man-37603.svg", 253, 2)
b6 = Book("Taming Dragons", "James Vonnegut", 4.5, "MassMarket Paperback", "dragon-23164.svg", 229, 2)
b7 = Book("The Singing Magpie", "Oscar Steinbeck", 5, "Hardcover", "magpie-147852.svg", 188, 3)
b8 = Book("Mr. Incognito", "Amelia Funke", 4.2, "Hardcover", "incognito-160143.svg", 205, 3)
b9 = Book("A Dog without purpose", "Edgar Dahl", 4.8, "MassMarket Paperback", "dog-159271.svg", 300, 4)
b10 = Book("A Frog's Life", "Herman Capote", 3.9, "MassMarket Paperback", "amphibian-150342.svg", 190, 4)
b11 = Book("Logan Returns", "Margaret Elliot", 4.6, "Hardcover", "wolf-153648.svg", 279, 5)
b12 = Book("Thieves of Kaalapani", "Mohit Gustav", 4.1, "Paperback", "boat-1296201.svg", 270, 5)
b13 = Book("As Men Thinketh", "Edward McPhee", 4.5, "Paperback", "cranium-2028555.svg", 124, 6)
b14 = Book("Mathematics of Music", "Mary Turing", 4.5, "Hardcover", "music-306008.svg", 120, 6)
b15 = Book("The Mystery of Mandalas", "Jack Morrison", 4.2, "Paperback", "mandala-1817599.svg", 221, 6)
b16 = Book("The Sacred Book of Kairo", "Heidi Zimmerman", 3.8, "ePub", "book-1294676.svg", 134, 7)
b17 = Book("Love is forever, As Long as it lasts", "Kovi O'Hara", 4.5, "Hardcover", "love-2026554.svg", 279, 8)
b18 = Book("Order in Chaos", "Wendy Sherman", 3.5, "MassMarket Paperback", "chaos-1769656.svg", 140, 8)

if __name__ == '__main__':
    with app.app_context():
        # db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8])
        # db.session.commit()
        # db.session.add_all([b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18])
        # db.create_all()
        # db.session.commit()
        # all = Book.query.all()
        # print(all[0])
        # first = Book.query.first()
        # print("\nfirst book is",first)
        # cnt = Book.query.count()
        # print("\nTotal book count is",cnt)
        # filter_data = Book.query.filter_by(num_pages='200').all()
        # print("ePub list is -->\n", filter_data)
        # pk = Book.query.get(109)
        # print("query by get primary key",pk)
        # limit = Book.query.limit(4).all()
        # print("limiting entries to display --\n",limit)
        # order = Book.query.order_by(Book.title).all()
        # print("Ordering books \n", order)
        # bk = Book.query.filter_by(format='ePub').order_by(Book.title).all()
        # print("\nFilter_by & order_by together --",bk)
        # result = Publication.query.filter_by(name='Broadway Press').first()
        # print("\n",result)
        # bk = Book.query.filter_by(pub_id=result.id).all()
        # print("\n books of publisher BP are --\n",bk)
        # app.run(debug=True)
        # u.format = "Testing"
        # db.session.commit()
        # u = db.session.get(Book, 109)
        # print("new method for get is-->\n", u.title)
        # x = db.session.get(Book, 109)
        # db.session.delete(x)
        # print("entry deleted")
        # # Book.query.filter_by(pub_id=6).delete()
        # Publication.query.filter_by(id=6).delete()
        db.session.commit()

# git
