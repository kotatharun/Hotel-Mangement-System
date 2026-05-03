from flask import Flask, render_template
from routes.guests import guests_bp
from routes.reservations import reservations_bp
from routes.dashboard import dashboard_bp

app = Flask(__name__)

# Needed for flash messages
app.secret_key = "hotel_management_secret_key"

# Register route files
app.register_blueprint(guests_bp)
app.register_blueprint(reservations_bp)
app.register_blueprint(dashboard_bp)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)