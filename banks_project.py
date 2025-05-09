import requests
import pandas as pd
import numpy as np
from datetime import datetime
from bs4 import BeautifulSoup
import sqlite3
# Constants
BASE_URL = "https://web.archive.org/web/20230908091635%20/https://en.wikipedia.org/wiki/List_of_largest_banks"
# Function to log messages
def log(message):
    """Logs messages to a file with the current timestamp."""  
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as log_file:
        log_file.write(f"{timestamp} - {message}\n")
dictionary = {
    'Rank': [],
    'Bank_name': [],
    'MC_USD_Billion': []
}
def extract(Base_url):
    response = requests.get(Base_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table',{'class':'wikitable sortable mw-collapsible'})
    rows = table.find_all('tr')[9].text.strip().split('\n')[2].strip()

    for i,row in enumerate(rows):
        if 11 > i > 0:
            
            dictionary['Rank'].append(table.find_all('tr')[i].text.strip().split('\n')[0].strip())
            dictionary['Bank_name'].append(table.find_all('tr')[i].text.strip().split('\n')[2].strip())
            dictionary['MC_USD_Billion'].append(table.find_all('tr')[i].text.strip().split('\n')[4].strip())
            
def transform():
    df = pd.DataFrame(dictionary)
    exchange_csv = pd.read_csv('datasets\\exchange_rate.csv')
    df['MC_USD_Billion'] = df['MC_USD_Billion'].astype(float)
    exchange_rate = exchange_csv.set_index('Currency').to_dict()['Rate']
    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]

    return df

def load_to_csv(df):
    df.to_csv('datasets\\banks.csv', index=False)

def load_to_db(df):
    conn = sqlite3.connect('datasets\\Banks.db')
    df.to_sql('Largest_banks', conn, if_exists='replace', index=False)
    conn.close()


def run_query(query):
    conn = sqlite3.connect('datasets\\Banks.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
def main():
    log("ETL process started")
    extract(BASE_URL)
    log("Data extracted")
    transformed_df = transform()
    log("Data transformed")
    load_to_csv(transformed_df)
    log("Data loaded to CSV")
    load_to_db(transformed_df)
    log("Data loaded to SQLite database")
    log("ETL process completed")
if __name__ == "__main__":
    main()
    # Example query
    query1 = "SELECT * FROM Largest_banks"
    query2 = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
    query3 = "SELECT Bank_name from Largest_banks LIMIT 5"
    print("Example Queries:")
    print("Query 1: Select all data from the table")
    result_df = run_query(query1)
    print(result_df)
    print("=================================================================================================================================")
    print("Query 2: Select average market capitalization in GBP")
    result_df2 = run_query(query2)
    print(result_df2)
    print("=================================================================================================================================")
    print("Query 3: Select first 5 bank names")
    result_df3 = run_query(query3)
    print(result_df3)
    print("=================================================================================================================================")
    log("Example queries executed")
'''The code above is a complete ETL pipeline that extracts data from a Wikipedia page, 
transforms it, and loads it into both a CSV file and a SQLite database.'''