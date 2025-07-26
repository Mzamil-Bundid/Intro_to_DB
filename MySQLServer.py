#!/usr/bin/env python3
"""
MySQLServer.py - Script to create alx_book_store database
Author: Student
Task: Create MySQL database with proper error handling
"""

import mysql.connector
from mysql.connector import Error


def create_database():
    """
    Creates the alx_book_store database in MySQL server
    Handles connection, creation, and proper cleanup
    """
    connection = None
    cursor = None
    
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password=''   # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            # Print success message
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        # Handle and print database connection/creation errors
        print(f"Error: Failed to connect to MySQL server or create database - {e}")
        
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error: An unexpected error occurred - {e}")
        
    finally:
        # Ensure proper cleanup of resources
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()