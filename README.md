# Largest Banks ETL Pipeline

This project is an ETL (Extract, Transform, Load) pipeline that extracts data about the world's largest banks from Wikipedia, processes it, and stores it in multiple formats.

## Features

- Extracts bank data (rank, name, market capitalization) from Wikipedia
- Transforms currency values to GBP, EUR, and INR
- Stores data in CSV and SQLite database formats
- Includes logging functionality
- Provides example SQL queries for data analysis

## Prerequisites

- Python 3.x
- Required Python packages:
  - requests
  - pandas
  - numpy
  - beautifulsoup4
  - sqlite3

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mahmoud-keno/largest-banks-etl.git
   cd largest-banks-etl


## Data Sources

- **Bank data**: [Wikipedia - List of Largest Banks](https://en.wikipedia.org/wiki/List_of_largest_banks)  
  (Archived version used: [2023-09-08 snapshot](https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks))

- **Exchange rates**: Local `exchange_rate.csv` file  
  (Sample format:)
  ```csv
  Currency,Rate
  GBP,0.81
  EUR,0.93

## File Structure
```markdown

largest-banks-etl/
├── datasets/
│   ├── exchange_rate.csv       # Currency exchange rates
│   ├── banks.csv               # Output CSV file
│   └── Banks.db                # SQLite database
├── main.py                     # Main ETL script
├── log.txt                     # Log file generated during execution
└── README.md                   # This file


  INR,82.95
