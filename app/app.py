from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# create a connection to the postgres database
conn = psycopg2.connect(
    host="localhost",
    database="sreality",
    user="postgres",
    password="Jelenovgreben123"
)

# define a route to serve the apartments data
@app.route('/')
def apartments():
    # create a cursor object to execute SQL queries
    cur = conn.cursor()

    # execute a SELECT query to get the apartments data
    cur.execute("SELECT * FROM apartments")

    # fetch all rows of the query result
    rows = cur.fetchall()

    # create a list to store the apartments data
    apartments = []

    # iterate over each row and append a dictionary to the apartments list
    for row in rows:
        flat = {
            'title': row[1],
            'images': row[2],
        }
        apartments.append(flat)

    # close the cursor and database connection
    cur.close()
    conn.close()

    # return the apartments data as a JSON response
    return render_template('flats.html', flats=apartments)

# run the application
if __name__ == '__main__':
    app.run(debug=True, port=8080)