from flask import Blueprint, render_template
from db import get_db   # or db depending on your file name

reservations_bp = Blueprint("reservations", __name__)   # 👈 REQUIRED

@reservations_bp.route("/reservations")
def reservations():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT 
            r.reservation_id,
            g.guest_name,
            rm.room_number,
            r.check_in_date,
            r.check_out_date,
            r.total_nights,
            r.reservation_status
        FROM Reservations r
        JOIN Guests g ON r.guest_id = g.guest_id
        JOIN Rooms rm ON r.room_id = rm.room_id
    """)

    data = cursor.fetchall()
    db.close()

    return render_template("reservations.html", reservations=data)