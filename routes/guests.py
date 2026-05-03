from flask import Blueprint, render_template
from db import get_db

guests_bp = Blueprint("guests", __name__)

@guests_bp.route("/guests")
def guests():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Guests")
    data = cursor.fetchall()
    db.close()

    return render_template("guests.html", guests=data)