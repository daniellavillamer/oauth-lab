from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "your_random_secret_key_here"

oauth = OAuth(app)

github = oauth.register(
    name='github',
    client_id='Ov23liZgQYax3efxIEAA',
    client_secret='1a20d693ae0a29b4dbbe00c94e94b052789afcf3',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@app.route('/login')
def login():
    return github.authorize_redirect(url_for('callback', _external=True))

@app.route('/')
def home():
    return """
    <h1>Welcome</h1>
    <a href="/login">Login with GitHub</a>
    """

@app.route('/callback')
def callback():
    token = github.authorize_access_token()
    user = github.get('user').json()
    session['user'] = user
    return redirect('/profile')

@app.route('/profile')
def profile():
    if 'user' not in session:
        return "Unauthorized: Please log in first.", 401
    
    user = session['user']
    
    return f"""
    <h1>Welcome, {user['login']}!</h1>
    <img src="{user['avatar_url']}" width="100">
    <p><b>Name:</b> {user.get('name', 'Not provided')}</p>
    <p><b>Username:</b> {user['login']}</p>
    <p><b>Email:</b> {user.get('email', 'Not provided')}</p>
    <p><b>Public Repos:</b> {user['public_repos']}</p>
    <p><b>Followers:</b> {user['followers']}</p>
    <a href="/logout">Logout</a>
    """

@app.route('/logout')
def logout():
    session.pop('user', None)
    return "You have been logged out. <a href='/login'>Login again</a>"

if __name__ == '__main__':
    app.run(debug=True)