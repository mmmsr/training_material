from flask import Flask, render_template, request, redirect, url_for
from flask_sample.database import init_db
from flask_sample.models import Entry


def create_app():
    app = Flask(__name__)
    app.config.from_object('flask_sample.config.Config')
    init_db(app)
    return app


app = create_app()


@app.route('/')
def index():
    entries = Entry.query.all()
    return render_template(
        'index.html',
        entries=entries
    )


@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'GET':
        return render_template(
            'new-post.html'
        )
    elif request.method == 'POST':
        entry = Entry(
            request.form['title'],
            request.form['body'],
            request.form['posted_by']
        )
        entry.save()
        return redirect(url_for('index'))
