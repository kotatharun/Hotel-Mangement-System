from flask import Blueprint, render_template, request, redirect, url_for, flash
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

@guests_bp.route("/guests/add", methods=["POST"])
def add_guest():
    name = request.form["guest_name"].strip()
    email = request.form["guest_email"].strip()
    phone = request.form["guest_phone"].strip()

    if not name or not email or not phone:
        flash("Guest name, email, and phone are required.")
        return redirect(url_for("guests.guests"))

    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO Guests (guest_name, guest_email, guest_phone)
            VALUES (%s, %s, %s)
        """, (name, email, phone))
        db.commit()
        db.close()
        flash("Guest added successfully.")
    except Exception as e:
        flash(f"Error adding guest: {e}")

    return redirect(url_for("guests.guests"))

@guests_bp.route("/guests/update/<int:guest_id>", methods=["POST"])
def update_guest(guest_id):
    name = request.form["guest_name"].strip()
    email = request.form["guest_email"].strip()
    phone = request.form["guest_phone"].strip()

    if not name or not email or not phone:
        flash("Guest name, email, and phone cannot be empty.")
        return redirect(url_for("guests.guests"))

    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        UPDATE Guests
        SET guest_name=%s, guest_email=%s, guest_phone=%s
        WHERE guest_id=%s
    """, (name, email, phone, guest_id))
    db.commit()
    db.close()

    flash("Guest updated successfully.")
    return redirect(url_for("guests.guests"))

@guests_bp.route("/guests/delete/<int:guest_id>")
def delete_guest(guest_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Guests WHERE guest_id=%s", (guest_id,))
        db.commit()
        db.close()
        flash("Guest deleted successfully.")
    except Exception as e:
        flash(f"Cannot delete guest because related reservations may exist: {e}")

    return redirect(url_for("guests.guests"))