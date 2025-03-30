import db

def add_chug(drink, total_time, amount, alcohollevel, carbonation, user_id):
    sql = """INSERT INTO chugs (drink, clock, amount, alcohol, carbonation, user_id)
            VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [drink, total_time, amount, alcohollevel, carbonation, user_id])
    