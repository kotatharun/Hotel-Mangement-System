from flask import Blueprint, render_template
from db import get_db

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM Guests")
    guests = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM Reservations")
    reservations = cursor.fetchone()["total"]

    cursor.execute("""
        SELECT COALESCE(SUM(payment_amount), 0) AS total
        FROM Payments
        WHERE payment_status = 'Paid'
    """)
    revenue = cursor.fetchone()["total"]

    cursor.execute("SELECT AVG(nightly_rate) AS avg_rate FROM Rooms")
    avg_rate = cursor.fetchone()["avg_rate"]

    db.close()

    return render_template(
        "dashboard.html",
        guests=guests,
        reservations=reservations,
        revenue=revenue,
        avg_rate=avg_rate
    )