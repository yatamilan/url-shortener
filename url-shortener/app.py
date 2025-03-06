from flask import Flask, request, redirect, render_template, session, url_for
from flask_mysqldb import MySQL
import random, string
import config
import qrcode
import os

app = Flask(__name__)
app.config.from_object(config)

# Secret key for session management
app.secret_key = 'your_secret_key'  # Change this to a strong, random string

mysql = MySQL(app)

# Function to generate a random short code
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Function to generate QR codes
def generate_qr(short_code):
    qr = qrcode.make(f"http://127.0.0.1:5000/{short_code}")
    qr_path = f"static/qr/{short_code}.png"
    
    # Ensure the directory exists
    os.makedirs("static/qr", exist_ok=True)

    qr.save(qr_path)
    return qr_path

# Home route - URL shortening
@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    qr_code_path = None

    if request.method == 'POST':
        long_url = request.form['long_url']
        custom_code = request.form.get('custom_code', '').strip()

        cur = mysql.connection.cursor()

        if custom_code:
            cur.execute("SELECT short_code FROM urls WHERE short_code = %s", (custom_code,))
            if cur.fetchone():
                cur.close()
                return "Error: Short code already taken. Choose another one.", 400
            short_code = custom_code
        else:
            short_code = generate_short_code()

        cur.execute("INSERT INTO urls (long_url, short_code) VALUES (%s, %s)", (long_url, short_code))
        mysql.connection.commit()
        cur.close()

        # Generate QR Code
        qr_code_path = generate_qr(short_code)
        short_url = f"http://127.0.0.1:5000/{short_code}"

    return render_template('index.html', short_url=short_url, qr_code=qr_code_path)

# Redirect users based on short code & track clicks
@app.route('/<short_code>')
def redirect_url(short_code):
    cur = mysql.connection.cursor()
    cur.execute("SELECT long_url, clicks FROM urls WHERE short_code = %s", (short_code,))
    result = cur.fetchone()

    if result:
        long_url, clicks = result
        cur.execute("UPDATE urls SET clicks = clicks + 1 WHERE short_code = %s", (short_code,))
        mysql.connection.commit()
        cur.close()
        return redirect(long_url)
    else:
        cur.close()
        return "URL not found", 404

# Admin login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'Yukesh' and password == '12345':  # Updated credentials
            session['admin'] = True
            return redirect('/admin')
        else:
            return "Invalid credentials, try again."

    return render_template('login.html')

# Admin dashboard (View all URLs)
@app.route('/admin')
def admin_dashboard():
    if not session.get('admin'):
        return redirect('/login')

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, long_url, short_code, clicks, created_at FROM urls")
    urls = cur.fetchall()
    cur.close()
    return render_template('admin.html', urls=urls)

# Delete URL (Admin only) & Reset ID Order
@app.route('/delete/<int:url_id>', methods=['POST'])
def delete_url(url_id):
    if not session.get('admin'):
        return redirect('/login')

    cur = mysql.connection.cursor()
    
    # Delete the URL entry
    cur.execute("DELETE FROM urls WHERE id = %s", (url_id,))
    mysql.connection.commit()
    
    # Reset ID sequence
    cur.execute("SET @num = 0;")
    cur.execute("UPDATE urls SET id = @num := (@num+1);")
    cur.execute("ALTER TABLE urls AUTO_INCREMENT = 1;")
    mysql.connection.commit()

    cur.close()
    return redirect('/admin')

# Logout admin
@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
