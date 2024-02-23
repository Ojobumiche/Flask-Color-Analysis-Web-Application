import psycopg2
from collections import Counter
from colour import all_colors

# Connect to PostgreSQL
conn = psycopg2.connect(database="bincodb",
                        user="joshua",
                        password="chenemi",
                        host="localhost", port="5432")  # Assuming the default port for PostgreSQL is 5432
cursor = conn.cursor()

# Create the color_frequencies table if it does not exist
cursor.execute("CREATE TABLE IF NOT EXISTS color_frequencies (color VARCHAR(255), frequency INT)")

# Insert color frequencies into the database 
for color, frequency in Counter(all_colors).items():
    cursor.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)", (color, frequency))

# Commit and close the connection
conn.commit()
conn.close()
