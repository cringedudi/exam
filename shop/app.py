from flask import Flask, jsonify
import sqlite3 
app = Flask(__name__)
@app.route("/orders")
def get_orders():
    db = sqlite3.connect("shop.db")
    rows = db.execute("""SELECT o.id, o.status, u.last_name, u.first_name, u.middle_name FROM orders o JOIN users u ON u.id = o.users_id Order BY o.id""").fetchall()
    db.close()
    result = []
    for r in rows:
        parts = [r[2]. r[3], r[4]]
        customer = " ".join(p for p in parts if p)
        result.append({
            "order_id": r[0], 
            "customer": customer, 
            "status": r[1]
            })
    return jsonify(result)
app.run(port=8080)