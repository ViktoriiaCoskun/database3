
from . import app
from .models import Book
from flask import jsonify,abort,request,render_template
from . import db
import json
from forms import UpdateForm,GetBookByID,DeleteForm,CreateNew

@app.route("/", methods=["GET"])
def home():
    return render_template("Home.html")

@app.route("/searchbyid")
def searchbyid():
    form = GetBookByID()
    form.method.default="GET"
    return render_template("books.html", form=form)

@app.route("/update")
def update():
    form = UpdateForm()
    form.method.default="PUT"
    return render_template("books.html", form=form)

@app.route("/delete")
def delete():
    form = DeleteForm()
    form.method.default="DELETE"
    return render_template("books.html", form=form)

@app.route("/new")
def newBook():
    form = CreateNew()
    form.method.default="POST"
    return render_template("books.html", form=form)

@app.route("/allBooks", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_json() for book in books])

@app.route("/book/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.query.get(id)
    if book is None:
        abort(404)
    return jsonify(book.to_json())

@app.route("/book/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        abort(404)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'result': True})

@app.route('/book', methods=['POST'])
def create_book():
    if request.args:
        book = Book(
            author=request.args.get('author'),
            country=request.args.get('country'),
            imageLink=request.args.get('imageLink'),
            language=request.args.get('language'),
            pages=request.args.get('pages'),
            title=request.args.get('title'),
            link=request.args.get('link'),
            year=request.args.get('year')
        )
        db.session.add(book)
        db.session.commit()
        return jsonify(book.to_json())

    if not request.json:
        abort(400)
    book = Book(
        author=request.json.get('author'),
        country=request.json.get('country'),
        imageLink=request.json.get('imageLink'),
        language=request.json.get('language'),
        pages=request.json.get('pages'),
        title=request.json.get('title'),
        link=request.json.get('link'),
        year=request.json.get('year')
    )
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_json()), 201

@app.route('/book/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if book is None:
        abort(404)
    if request.args:
        book.author=request.args.get('author', book.author),
        book.country=request.args.get('country', book.country),
        book.imageLink=request.args.get('imageLink', book.imageLink),
        book.language=request.args.get('language', book.language),
        book.pages=request.args.get('pages', book.pages),
        book.title=request.args.get('title', book.title),
        book.link=request.args.get('link', book.link),
        book.year=request.args.get('year', book.year)
        db.session.commit()
        return jsonify(book.to_json())

    elif not request.json:
        abort(400)

    book.author=request.json.get('author', book.author),
    book.country=request.json.get('country', book.country),
    book.imageLink=request.json.get('imageLink', book.imageLink),
    book.language=request.json.get('language', book.language),
    book.pages=request.json.get('pages', book.pages),
    book.title=request.json.get('title', book.title),
    book.link=request.json.get('link', book.link),
    book.year=request.json.get('year', book.year)
    db.session.commit()
    return jsonify(book.to_json())


@app.route("/book/storeall", methods=["GET"])
def storeall():
    allbooks=[]
    with open("books.json", "r") as f:
        allbooks = json.load(f)
    
    if allbooks:
        for item in allbooks:
            book = Book(
                author=item.get('author'),
                country=item.get('country'),
                imageLink=item.get('imageLink'),
                language=item.get('language'),
                pages=item.get('pages'),
                title=item.get('title'),
                link=item.get('link'),
                year=item.get('year')
            )
            db.session.add(book)
            db.session.commit()
    books = Book.query.all()
    return jsonify([book.to_json() for book in books])


@app.route("/api/v1/booklibrary/", methods=["GET"])
def home_api():
  book_id = request.args.get("id")
  if book_id :
    if request.args.get("button") == 'delete':
      return delete_book(int(book_id))
    elif request.args.get("button") == 'update':
      return update_book(int(book_id))
    elif request.args.get("button") == 'search':
      return get_book(int(book_id))
  elif request.args.get("button") == 'create':
    return create_book()  
  else : return get_books()