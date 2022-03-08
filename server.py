from flask import Flask, render_template, redirect, request 
from user import User

app = Flask(__name__)

@app.route('/')
def create_user():
    return render_template('newuser.html')

@app.route('/users', methods=["POST"])
def home():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.save(data)
    return redirect ('/show_users')

@app.route('/show_users')
def show_users():
    users = User.get_all()
    print(users)
    return render_template ('index.html', all_users = users)


@app.route('/users/<int:id>')
def view_one(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    return render_template('oneuser.html', one_user = user )


@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    return render_template('edituser.html', edit_user = user)


@app.route('/users/<int:id>/edit', methods=['POST'])
def process_edit(id):
    data = {
        'id' : id,
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.update(data)
    return redirect (f'/users/{id}')


@app.route('/users/<int:id>/delete')
def delete(id):
    data = {
        'id' : id
    }
    User.delete(data)
    return redirect('/show_users')


if __name__ == "__main__":
    app.run(debug=True)