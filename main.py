import sqlite3
import os
import re
import gzip

# Connect to the database - sqlite3
conn = sqlite3.connect('logs.db')
c = conn.cursor()

# Create the table for storing the log data
c.execute('''CREATE TABLE IF NOT EXISTS logs
            (date text, uri text, count integer)''')  

# Go through all the files in the logs directory
for file_name in os.listdir('logs'):
    if file_name.endswith('.gz'):
        # Open and parse the gzipped file
        with gzip.open(os.path.join('logs', file_name), 'rt') as f:
            for line in f:
                # Split the line by tabs and extract the date and uri
                fields = re.split('\t', line)
                date = fields[0]
                uri = fields[1]

                # Insert the data into the database
                c.execute("INSERT INTO logs VALUES (?, ?, 1)", (date, uri))

# Commit changes and close DB
conn.commit()
conn.close()