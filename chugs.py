import db

def add_chug(drink, total_time, amount, alcohollevel, carbonation, user_id):
    sql = """INSERT INTO chugs (drink, clock, amount, alcohol, carbonation, user_id)
            VALUES (?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [drink, total_time, amount, alcohollevel, carbonation, user_id])

def get_chugs():
    sql = """SELECT id, drink FROM chugs ORDER BY id DESC"""

    return db.query(sql)

def get_chug(chug_id):
    sql = """SELECT chugs.drink,
                    chugs.id,
                    chugs.clock,
                    chugs.amount,
                    chugs.alcohol,
                    chugs.carbonation,
                    users.id user_id,
                    users.username
             FROM chugs
             JOIN users ON chugs.user_id = users.id
             WHERE chugs.id = ?"""
    return db.query(sql, [chug_id])[0]

def update_chug(chug_id, drink, total_time, amount, alcohollevel, carbonation):
    sql = """UPDATE chugs 
             SET drink = ?, 
                 clock = ?, 
                 amount = ?, 
                 alcohol = ?, 
                 carbonation = ? 
             WHERE id = ?"""
    db.execute(sql, [chug_id])

def remove_chug(chug_id):
    sql = "DELETE FROM chugs WHERE id = ?"
    db.execute(sql, [chug_id])

def find_chugs(query):
    sql = """SELECT id, drink
            FROM chugs
            WHERE drink LIKE ?
            ORDER BY id DESC"""
    return db.query(sql, ["%" + query + "%"])

