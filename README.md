# ETL and Data Analysis Project

## Project Overview

This project involves extracting data from a SQLite database, transforming it into a suitable format, and loading it into a pandas DataFrame for analysis. The analysis includes generating various visualizations to gain insights into the data.

## Project Structure

- `movies.ipynb`: Jupyter notebook containing the ETL process and data analysis.
- `movies.sqlite`: SQLite database containing the raw data.
- `README.md`: This file.

## Requirements

- Python 3.11.7
- pandas
- numpy
- sqlite3
- matplotlib
- seaborn

## Setup

1. Clone the repository.
2. Install the required libraries:
    ```sh
    pip install pandas numpy sqlite3 matplotlib seaborn
    ```

## ETL Process

1. **Extract**: Connect to the SQLite database and extract the data using SQL queries.
2. **Transform**: Clean and transform the data into a suitable format for analysis.
3. **Load**: Load the transformed data into a pandas DataFrame.

## Data Analysis

The analysis includes:
- Displaying the first few rows of the DataFrame.
- Generating summary statistics.
- Creating visualizations such as histograms and scatter plots.

## Usage

Open the [movies.ipynb](http://_vscodecontentref_/3) notebook in Jupyter and run the cells to execute the ETL process and perform the data analysis.

## License

This project is licensed under the MIT License.
