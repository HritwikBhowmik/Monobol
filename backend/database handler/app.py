import sqlite3
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Initialize database
def init_db():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect('data/data.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS health_events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                organizer TEXT NOT NULL,
                location TEXT NOT NULL,
                date DATETIME NOT NULL,
                time TEXT NOT NULL);""")
    
    c.execute("""CREATE TABLE IF NOT EXISTS health_worker_volunteer (
                v_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                service TEXT NOT NULL,
                contact TEXT NOT NULL);""")

    conn.commit()
    conn.close()

init_db()

# Create a single global connection for demo (not ideal for big apps)
conn = sqlite3.connect('data/data.db', check_same_thread=False)
c = conn.cursor()


# Get section
@app.route('/getAllHealthEvents', methods=['GET'])
def get_all_health_events():
    c.execute('SELECT * FROM health_events;')
    records = c.fetchall()
    if records:
        return jsonify(records)
    else:
        return jsonify({'message': 'No user found'})
    
@app.route('/getAllHealthWorkerVolunteer', methods=['GET'])
def get_all_health_worker_volunteer():
    c.execute('SELECT * FROM health_worker_volunteer;')
    records = c.fetchall()
    if records:
        return jsonify(records)
    else:
        return jsonify({'message': 'No user found'})


# post section
@app.route('/setHealthEvents', methods=['POST'])
def set_health_events():
    organizer = request.args.get('organizer', type=str)
    location = request.args.get('location', type=str)
    date = request.args.get('date', type=str)
    time = request.args.get('time', type=str)

    query = "INSERT INTO health_events (organizer, location, date, time) VALUES (?, ?, ?, ?)"
    c.execute(query, (organizer, location, date, time))
    conn.commit()

    return jsonify({
        'organizer': organizer,
        'location': location,
        'date': date,
        'time': time
    })

@app.route('/setHealthWorkerVolunteer', methods=['POST'])
def set_health_volunteer():
    name = request.args.get('name', type=str)
    service = request.args.get('service', type=str)
    contact = request.args.get('contact', type=str)

    query = "INSERT INTO health_worker_volunteer (name, service, contact) VALUES (?, ?, ?)"
    c.execute(query, (name, service, contact))
    conn.commit()

    return jsonify({
        'name': name,
        'service': service,
        'contact': contact
    })



@app.route('/deleteHealthEvents', methods=['POST'])
def del_health_events():
    event_id = request.args.get('event_id', type=int)
    c.execute("DELETE FROM health_events WHERE event_id = ?", (event_id,))
    conn.commit()
    return jsonify({'message': f'User {event_id} deleted successfully'})

@app.route('/deleteHealthWorkerVolunteer', methods=['POST'])
def del_health_worker_volunteer():
    v_id = request.args.get('v_id', type=int)
    c.execute("DELETE FROM health_worker_volunteer WHERE v_id = ?", (v_id,))
    conn.commit()
    return jsonify({'message': f'User {v_id} deleted successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=1212)
