# config.py
# ------------------------------------
# This file holds all configurations
# like Secret Key, Database connection
# details, Email settings, Razorpay keys etc.
# ------------------------------------


# Stores all configuration settings
# ------------------------------------------
import os
SECRET_KEY = "your_secret_key"

# MySQL Database


# MySQL Database
DB_HOST = os.environ.get('DB_HOST')
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Teja@1610")
DB_NAME = os.getenv("DB_NAME", "smartcart_db")
# Email SMTP Settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'tejayepuri350@gmail.com'
MAIL_PASSWORD = 'hufyduedziggcvke'   # Gmail App Password

RAZORPAY_KEY_ID = "rzp_test_T8hXeb5Ihbm9l8"
RAZORPAY_KEY_SECRET = "ozU09rsClILVMcLfJ1xmNGj5"

