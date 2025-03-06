# README.md for Your URL Shortener Project
# 🔗 URL Shortener Project

A **Flask-based URL Shortener** that allows users to shorten long URLs with **custom short codes** and provides a **QR code** for each shortened link. It includes an **Admin Dashboard** for managing links, tracking clicks, and deleting URLs.

---

## 🚀 Features

✅ **Shorten Long URLs** – Convert long URLs into short links  
✅ **Custom Short Codes** – Users can create their own short links  
✅ **Click Tracking** – Tracks how many times a short link is clicked  
✅ **QR Code Generation** – Generates a scannable QR code for each URL  
✅ **Admin Dashboard** – View, manage, and delete short URLs  
✅ **Secure Admin Login** – Only admins can manage short URLs  
✅ **Mobile-Responsive UI** – Designed with **Tailwind CSS**  
✅ **Deployment on Railway** – Hosted online for global access  

---

## 📦 Technologies Used

| Technology     | Purpose                                   |
|---------------|-------------------------------------------|
| `Flask`       | Web framework for backend logic          |
| `Flask-MySQLdb` | Connects Flask with MySQL database     |
| `qrcode`      | Generates QR codes for short URLs        |
| `Tailwind CSS` | Frontend styling for a clean UI         |
| `os`          | Handles file directories for QR storage  |
| `random, string` | Generates unique short codes         |

---

## 🛠️ Installation Guide

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/YOUR-USERNAME/URL-Shortener.git
cd URL-Shortener

2️⃣ Install Dependencies
pip install flask flask-mysqldb qrcode

3️⃣ Set Up MySQL Database
Run these SQL commands in your MySQL database:

CREATE DATABASE yukesh;
USE yukesh;

CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    long_url TEXT NOT NULL,
    short_code VARCHAR(10) UNIQUE NOT NULL,
    clicks INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

4️⃣ Run the Flask Application

python app.py

5️⃣ Access the Application
Open your browser and go to: http://127.0.0.1:5000/
To access the Admin Panel, go to http://127.0.0.1:5000/login
Username: Yukesh
Password: 12345
🌐 Deployment on Railway
🚀 Steps to Deploy
Create a Railway account at railway.app
Create a New Project and select Deploy from GitHub
Set Environment Variables in Railway:

MYSQL_HOST = <your-railway-mysql-host>
MYSQL_USER = <your-railway-mysql-username>
MYSQL_PASSWORD = <your-railway-mysql-password>
MYSQL_DB = yukesh
Modify config.py to Use Environment Variables:

import os
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')
Deploy & Get Your Live URL!
⚠️ Common Mistakes & Fixes
❌ Error: Short code already exists
✔️ Fix: Ensure unique short codes before inserting into the database.

❌ Error: MySQL database not connected
✔️ Fix: Verify MySQL credentials in config.py and environment variables.

❌ QR Code Not Showing?
✔️ Fix: Ensure the static/qr/ directory exists and Flask serves static files properly.

🎯 Future Enhancements
🔹 User Authentication – Allow users to create accounts and manage their links
🔹 Custom Expiry Dates – Let users set expiration dates for short links
🔹 Analytics Dashboard – Show detailed insights on link clicks

📝 License
This project is open-source and available under the MIT License.

💬 Connect with Me
👤 Yukesh
📧 Email: your-email@example.com
🌍 LinkedIn: Your Profile
📂 GitHub: Your GitHub

⭐ If you like this project, don’t forget to star the repo! ⭐


---

### **✅ What’s Included in This README?**
✔ **Markdown Formatting** → Proper GitHub-style README  
✔ **Installation Steps** → How to set up and run the project  
✔ **Deployment Guide** → Steps for deploying on **Railway**  
✔ **Common Mistakes & Fixes** → To avoid errors  
✔ **Future Enhancements** → Features to add later  
✔ **Contact Info** → To connect with you  

---

### **🚀 Next Steps**
✅ **Copy & paste this into your `README.md` file in your GitHub repo.**  
Do you need **any changes or additions** before finalizing? 😊






