import psycopg2
import sys
from datetime import datetime

CONNECTION = "postgres://tsdbadmin@fzb8kp9l0z.s6dj8lpbj9.tsdb.cloud.timescale.com:38959/tsdb?sslmode=require"

def get_connection():
    try:
        return psycopg2.connect(CONNECTION)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

def create_sensors_table(conn):
    query_create_sensors_table = """CREATE TABLE IF NOT EXISTS sensors (
                                        id SERIAL PRIMARY KEY,
                                        type VARCHAR(50),
                                        location VARCHAR(50)
                                    );
                                    """
    cursor = conn.cursor()
    cursor.execute(query_create_sensors_table)
    conn.commit()
    cursor.close()

def insert_sensor(conn):
    sensors = [('a', 'floor'), ('a', 'ceiling'), ('b', 'floor'), ('b', 'ceiling')]
    cursor = conn.cursor()
    for (type_, location) in sensors:
        try:
            cursor.execute("INSERT INTO sensors (type, location) VALUES (%s, %s);",
                        (type_, location))
        except (Exception, psycopg2.Error) as error:
            print(error.pgerror)
    conn.commit()
    cursor.close()

def select_sensors(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM sensors;"  # Changed from sensor_data to sensors
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row, file=sys.stdout)
    cursor.close()

def run_sample_test():
    conn = get_connection()
    if conn:
        print("Connecting to database...", file=sys.stdout)
        try:
            create_sensors_table(conn)
            insert_sensor(conn)
            select_sensors(conn)
        finally:
            conn.close()
            print("Connection closed.", file=sys.stdout)
    else:
        print("Failed to establish database connection.", file=sys.stdout)
