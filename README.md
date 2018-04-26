# CSV Parser

## Installation
1. Clone the repository and cd into the `csv-parser` folder
2. Create new virtual env (python 2.7):
`mkvirtualenv csv-parser`
3. Activate it: `workon csv-parser`
4. Install dependencies: `pip install -r requirements.txt`

## Running
1. cd into `csv-parser` folder
2. Activate virtual env: `workon csv-parser`
3. Run it: `python parser.py`

## Tests
1. cd into `csv-parser` folder
2. Activate virtual env: `workon csv-parser`
3. Run: `pytest`


## About

This parser will print to the console result of parsing of 3 provided CSV files 
stored in `csv_files` directory

In the csv files you can find a data for 5 days of a week: mon, tue, wed, thu, fri. Days may be provided in range format: `mon-thu`.
For each day you should store a value, description and some day's specific data:
1. For mon, tue and wed it is a `square` field.
2. For thu, fri it is a `double` field.

In csv there is also some additional data which should be skipped.

`description` field contains day's specific data.


### Assumptions

We assume that the source CSV will only have a 1 row of data and the day value 
is always a number.
Supported day headers are `mon`, `tue`, `wed`, `thu`, `fri`
Date range is supported only via `<day_header>-<day_header>` format