# Normalization Report

## 2.1. Original Functional Dependencies

### Guests
- guest_id → guest_name, guest_email, guest_phone, record_created_at
- guest_email → guest_id, guest_name, guest_phone, record_created_at
- guest_phone → guest_id, guest_name, guest_email, record_created_at

### Rooms
- room_id → room_number, room_type, nightly_rate, room_status
- room_number → room_id, room_type, nightly_rate, room_status

### Reservations
- reservation_id → guest_id, room_id, check_in_date, check_out_date, total_nights, reservation_date, reservation_status
- check_in_date, check_out_date → total_nights

### Payments
- payment_id → reservation_id, payment_date, payment_amount, payment_method, payment_status
- reservation_id → payment_id, payment_date, payment_amount, payment_method, payment_status

---

## 2.2 Anomaly Identification

The database is mostly normalized because guests, rooms, reservations, and payments are stored in separate tables.

The main normalization issue is in the `Reservations` table.

Before decomposition, the table included:

Reservations(
    reservation_id,
    guest_id,
    room_id,
    check_in_date,
    check_out_date,
    total_nights,
    reservation_date,
    reservation_status
)

## 2.3. Decomposition Steps:

  Step 1: Identify the Problem Table
  
      The table that needed decomposition was:
      
      Reservations(
          reservation_id,
          guest_id,
          room_id,
          check_in_date,
          check_out_date,
          total_nights,
          reservation_date,
          reservation_status
      )
  Step 2: Identify the Derived Dependency
  
      The dependency causing the issue is:
      
      check_in_date, check_out_date → total_nights
      
      This means total_nights depends on the reservation dates, not as an independent attribute.
  
  Step 3: Remove the Derived Attribute
  
      To satisfy strict 3NF, total_nights was removed from the stored table.
      
      Updated table:
      
      Reservations(
          reservation_id,
          guest_id,
          room_id,
          check_in_date,
          check_out_date,
          reservation_date,
          reservation_status
      )

## 2.4. Final Relational Schema
        Guests
        Guests(
            guest_id PRIMARY KEY,
            guest_name,
            guest_email UNIQUE,
            guest_phone UNIQUE,
            record_created_at
        )
        Rooms
        Rooms(
            room_id PRIMARY KEY,
            room_number UNIQUE,
            room_type,
            nightly_rate,
            room_status
        )
        Reservations
        Reservations(
            reservation_id PRIMARY KEY,
            guest_id FOREIGN KEY,
            room_id FOREIGN KEY,
            check_in_date,
            check_out_date,
            reservation_date,
            reservation_status
        )
        Payments
        Payments(
            payment_id PRIMARY KEY,
            reservation_id UNIQUE FOREIGN KEY,
            payment_date,
            payment_amount,
            payment_method,
            payment_status
        )
