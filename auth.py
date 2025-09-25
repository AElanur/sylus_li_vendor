import os

from flask import Flask, request, redirect, url_for
from flask_discord import DiscordOAuth2Session, requires_authorization
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)
port: int = int(os.getenv('DISCORD_BOT_PORT', 5000))

app.config["DISCORD_CLIENT_ID"] = os.getenv('DISCORD_CLIENT_ID')
app.config["DISCORD_CLIENT_SECRET"] = os.getenv('DISCORD_CLIENT_SECRET')
app.config["DISCORD_REDIRECT_URI"] = os.getenv('DISCORD_REDIRECT_URI')

discord = DiscordOAuth2Session(app)

@app.route('/')
def home():
    return 'Discord bot OAuth app home.'

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route('/login/')
def login():
    return discord.create_session()

@app.errorhandler(404)
def not_found(e):
    return '404 Not Found: The requested URL was not found on the server.', 404

@app.route('/callback/')
def callback():
    discord.callback()
    return redirect(url_for('me'))

@app.route('/me/')
@requires_authorization
def me():
    user = discord.fetch_user()
    return user.name

@app.route('/auth/discord')
def discord_auth():
    code = request.args.get('code')
    state = request.args.get('state')
    return f"{state}?{code}"

if __name__ == '__main__':
    app.run(port=port, debug=True)