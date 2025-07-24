# Airline Flight Data Analysis Program

This is a terminal-based Python program that analyzes airline flight data from a CSV file. It allows users to perform a variety of queries, such as searching for flights, comparing prices, calculating durations, and exporting sorted flight information.

## Features

* Reads flight data from a CSV file
* Finds detailed information for a specific flight by airline name and flight number.
* Identifies flights shorter than a user-defined maximum duration
* Locates the cheapest flight offered by a specified airline
* Finds all flights departing after a given time
* Calculates the average price of all flights
* Generates a new CSV file with all flights sorted by their departure time
* User-Friendly interactive command-line menu for easy navigation

## How to Run

1.  The project source file and the data file must be downloaded into the same directory.

2.  Run the program:
    ```bash
    python airline.py
    ```

3. When prompted, enter the data file name: `flights.csv`
    ```
    Please enter a file name: flights.csv
    ```

4.  Follow the on-screen prompts to choose from the available options (1-7).
    ```
    Please choose one of the following options:
    1 -- Find flight information by airline and flight number
    2 -- Find flights shorter than a specified duration
    3 -- Find the cheapest flight by a given airline
    4 -- Find flight departing after a specified time
    5 -- Find the average price of all flights
    6 -- Write a file with flights sorted by departure time
    7 -- Quit
    Choice ==>
    ```
