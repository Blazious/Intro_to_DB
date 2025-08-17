import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Blaze@12236.395xzg",
    database="alx_book_store"
)

if conn.is_connected():
    print("✅ Successfully connected to MySQL database!")

# Close connection
conn.close()
