from flask import Flask, render_template, redirect, request, session
from user import User

app = Flask(__name__)

@app.route('/')
def create_user():
    return render_template('newuser.html')

@app.route('/users', methods=["POST"])
def users():
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



if __name__ == "__main__":
    app.run(debug=True)