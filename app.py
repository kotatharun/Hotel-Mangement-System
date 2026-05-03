from flask import Flask
from routes.guests import guests_bp
from routes.reservations import reservations_bp
from routes.dashboard import dashboard_bp

app = Flask(__name__)

app.register_blueprint(guests_bp)
app.register_blueprint(reservations_bp)
app.register_blueprint(dashboard_bp)

@app.route("/")
def home():
    return """
    <h1>Hotel Management System</h1>
    <a href='/guests'>Guests</a><br>
    <a href='/reservations'>Reservations</a><br>
    <a href='/dashboard'>Dashboard</a>
    """

if __name__ == "__main__":
    app.run(debug=True)