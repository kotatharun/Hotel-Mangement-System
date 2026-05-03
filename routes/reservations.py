from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import get_db

reservations_bp = Blueprint("reservations", __name__)

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
            DATEDIFF(r.check_out_date, r.check_in_date) AS total_nights,
            r.reservation_status
        FROM Reservations r
        JOIN Guests g ON r.guest_id = g.guest_id
        JOIN Rooms rm ON r.room_id = rm.room_id
    """)
    reservations_data = cursor.fetchall()

    cursor.execute("SELECT * FROM Guests")
    guests = cursor.fetchall()

    cursor.execute("SELECT * FROM Rooms")
    rooms = cursor.fetchall()

    db.close()

    return render_template(
        "reservations.html",
        reservations=reservations_data,
        guests=guests,
        rooms=rooms
    )


@reservations_bp.route("/reservations/add", methods=["POST"])
def add_reservation():
    guest_id = request.form["guest_id"]
    room_id = request.form["room_id"]
    check_in = request.form["check_in_date"]
    check_out = request.form["check_out_date"]
    status = request.form["reservation_status"]

    if not guest_id or not room_id or not check_in or not check_out:
        flash("All reservation fields are required.")
        return redirect(url_for("reservations.reservations"))

    if check_out <= check_in:
        flash("Check-out date must be after check-in date.")
        return redirect(url_for("reservations.reservations"))

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO Reservations
        (guest_id, room_id, check_in_date, check_out_date, reservation_date, reservation_status)
        VALUES (%s, %s, %s, %s, CURDATE(), %s)
    """, (guest_id, room_id, check_in, check_out, status))

    db.commit()
    db.close()

    flash("Reservation added successfully.")
    return redirect(url_for("reservations.reservations"))


@reservations_bp.route("/reservations/update/<int:reservation_id>", methods=["POST"])
def update_reservation(reservation_id):
    status = request.form["reservation_status"]

    allowed_status = ["Booked", "Checked-In", "Checked-Out", "Cancelled"]
    if status not in allowed_status:
        flash("Invalid reservation status.")
        return redirect(url_for("reservations.reservations"))

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        UPDATE Reservations
        SET reservation_status=%s
        WHERE reservation_id=%s
    """, (status, reservation_id))

    db.commit()
    db.close()

    flash("Reservation updated successfully.")
    return redirect(url_for("reservations.reservations"))


@reservations_bp.route("/reservations/delete/<int:reservation_id>")
def delete_reservation(reservation_id):
    try:
        db = get_db()
        cursor = db.cursor()

        cursor.execute("DELETE FROM Payments WHERE reservation_id=%s", (reservation_id,))
        cursor.execute("DELETE FROM Reservations WHERE reservation_id=%s", (reservation_id,))

        db.commit()
        db.close()

        flash("Reservation and related payment deleted successfully.")

    except Exception as e:
        flash(f"Error deleting reservation: {e}")

    return redirect(url_for("reservations.reservations"))


@reservations_bp.route("/reservations/book-with-payment", methods=["POST"])
def book_with_payment():
    db = get_db()

    try:
        guest_id = request.form["guest_id"]
        room_id = request.form["room_id"]
        check_in = request.form["check_in_date"]
        check_out = request.form["check_out_date"]
        payment_amount = float(request.form["payment_amount"])
        payment_method = request.form["payment_method"]

        if not guest_id or not room_id or not check_in or not check_out:
            flash("All booking fields are required.")
            return redirect(url_for("reservations.reservations"))

        if check_out <= check_in:
            flash("Check-out date must be after check-in date.")
            return redirect(url_for("reservations.reservations"))

        if payment_amount <= 0:
            flash("Payment amount must be greater than 0.")
            return redirect(url_for("reservations.reservations"))

        cursor = db.cursor()
        db.begin()

        # Insert reservation (NO total_nights)
        cursor.execute("""
            INSERT INTO Reservations
            (guest_id, room_id, check_in_date, check_out_date, reservation_date, reservation_status)
            VALUES (%s, %s, %s, %s, CURDATE(), 'Booked')
        """, (guest_id, room_id, check_in, check_out))

        reservation_id = cursor.lastrowid

        # Insert payment
        cursor.execute("""
            INSERT INTO Payments
            (reservation_id, payment_date, payment_amount, payment_method, payment_status)
            VALUES (%s, CURDATE(), %s, %s, 'Paid')
        """, (reservation_id, payment_amount, payment_method))

        # Update room
        cursor.execute("""
            UPDATE Rooms
            SET room_status='Occupied'
            WHERE room_id=%s
        """, (room_id,))

        db.commit()
        flash("Transaction successful.")

    except Exception as e:
        db.rollback()
        flash(f"Transaction failed: {e}")

    finally:
        db.close()

    return redirect(url_for("reservations.reservations"))