from flask import Flask, render_template, request, session, redirect, url_for
from datetime import date, time, datetime
import sqlite3 as sql
import os

# Create Database if it doesnt exist
if not os.path.isfile('database.db'):
    conn = sql.connect('database.db')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS Donors (Name TEXT NOT NULL, Amount INTEGER NOT NULL, Email TEXT NOT NULL, [timestamp] TIMESTAMP)')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS Users (Name TEXT NOT NULL, Email TEXT NOT NULL, Password TEXT NOT NULL, Contact INTEGER NOT NULL)')
    conn.close()

app = Flask(__name__, static_url_path='/assets',
            static_folder='assets',
            template_folder='./')


@app.route('/')
def root():
    session['logged_out'] = 1
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/header_page.html')
def header_page():
    return render_template('header_page.html')


@app.route('/menu-bar-charity.html')
def menu_bar_charity():
    return render_template('menu-bar-charity.html')


@app.route('/footer.html')
def footer():
    return render_template('footer.html')


@app.route('/sidebar.html')
def sidebar():
    return render_template('sidebar.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/our-causes.html')
def our_causes():
    return render_template('our-causes.html')


@app.route('/about-us.html')
def about_us():
    return render_template('about-us.html')


@app.route('/donate.html')
def donate():
    return render_template('donate.html')

if __name__ == '__main__':
    app.secret_key = ".."
    app.run()
