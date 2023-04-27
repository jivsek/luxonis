#!/bin/bash

# Set database name and credentials
DB_NAME="postgres"
DB_USER="postgres"
DB_HOST="localhost"
DB_PORT="5432"

# Create sreality database
psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -c "CREATE DATABASE sreality;"

# Set database name to sreality
DB_NAME="sreality"

# Create apartments table
psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -c "
    CREATE TABLE IF NOT EXISTS apartments (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        images JSONB
    );"

echo "Database created successfully!"