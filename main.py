import requests
from bs4 import BeautifulSoup
import sqlite3
import config
from scraper import scrape_data
from database import create_table, insert_data

def main():
    # Create a database connection
    conn = sqlite3.connect(config.DATABASE_NAME)

    # Create table
    create_table(conn, config.TABLE_NAME, config.TABLE_SCHEMA)

    # Scrape data
    for index in config.INDICES:
        response = requests.get(config.BASE_URL + index)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = scrape_data(soup, config.DOM_IDS[index])

        # Insert data into database
        insert_data(conn, config.TABLE_NAME, data)

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()