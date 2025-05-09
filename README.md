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
   git clone https://github.com/yourusername/largest-banks-etl.git
   cd largest-banks-etl
