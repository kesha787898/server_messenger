from init import app
from init import db
import models
from flask import request, jsonify  # ,render_template
from email_module import send_email

unconfirmed_users = dict()

code_errors = {-1: 'Everything is OK', 0: 'unknown exseption', 1: 'Wrong confirm key', 2: 'Email aready confimed',
               3: 'Please try to confirm again', 4: '', 5: ''}


@app.route("/register", methods=['POST'])
def register():
    print('1')
    email = request.args.get('email')
    print(email)
    user = models.Users(
        username=request.args.get('username'),
        password=request.args.get('password'),
        phone=request.args.get('phone'),
        email=email,
        token=request.args.get('token'),
    )
    unconfirmed_users[email] = (send_email(request.args.get('email')), user)
    is_done = True
    code_error = -1
    if not is_done:
        code_error = 0

    return jsonify({'is_done': is_done,
                    'code_error': code_error})


@app.route("/confirm_user", methods=['POST'])
def confirm_user():
    is_done = False
    code_error = -1
    email = request.args.get('email')
    key = request.args.get('key')
    if email in unconfirmed_users.keys():
        if int(unconfirmed_users[email][0]) == int(key):
            db.session.add(unconfirmed_users[email][1])
            unconfirmed_users.pop(email)
            db.session.commit()
            is_done = True
        else:

            code_error = 1
    else:
        if 'Email aready confimed':
            code_error = 2
        else:
            code_error = 3
    return jsonify({'is_done': is_done,
                    'code_error': code_error})


if __name__ == "__main__":
    app.run()
