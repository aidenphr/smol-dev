1. "requests" and "beautifulsoup4" Libraries: Both "main.py" and "scraper.py" will use these libraries for making HTTP requests to barcharts.com and parsing the HTML content.

2. "sqlite3" Library: "main.py" and "database.py" will use this library to interact with the SQLite database.

3. "config.py": This file will be imported by all other files to access shared configuration settings such as the base URL of barcharts.com, database connection details, and the specific indices (COR3M and COR1M).

4. Database Schema: The schema of the database will be shared between "database.py" (which will create the tables based on the schema) and "main.py" (which will insert data into the tables).

5. DOM Element IDs: The "scraper.py" will use the specific IDs of the DOM elements to extract the data for the COR3M and COR1M indices. These IDs will also be used in "main.py" to pass to the scraper functions.

6. Function Names: Functions for scraping (in "scraper.py") and database operations (in "database.py") will be called from "main.py". Therefore, the function names are shared between these files.

7. Message Names: Any logging or error messages will be shared across all files for consistency.

8. Indices Names: The names of the indices (COR3M and COR1M) will be shared across "main.py", "scraper.py", and "database.py" as these are the specific data points the user wants to scrape and store.