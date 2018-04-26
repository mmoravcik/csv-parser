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

Please note that `description` field contains day's specific data.

Example output:
1.csv
[{'day': 'mon', 'description': 'first_desc 1', 'square': 1, 'value': 1},
 {'day': 'tue', 'description': 'first_desc 25', 'square': 25, 'value': 5},
 {'day': 'wed', 'description': 'first_desc 4', 'square': 4, 'value': 2},
 {'day': 'thu', 'description': 'first_desc 6', 'double': 6, 'value': 3},
 {'day': 'fri', 'description': 'first_desc 6', 'double': 6, 'value': 3}]

2.csv
[{'day': 'mon', 'description': 'second_desc 4', 'square': 4, 'value': 2},
 {'day': 'tue', 'description': 'second_desc 4', 'square': 4, 'value': 2},
 {'day': 'wed', 'description': 'second_desc 4', 'square': 4, 'value': 2},
 {'day': 'thu', 'description': 'second_desc 4', 'double': 4, 'value': 2},
 {'day': 'fri', 'description': 'second_desc 6', 'double': 6, 'value': 3}]

3.csv
[{'day': 'mon', 'description': 'third_desc 9', 'square': 9, 'value': 3},
 {'day': 'tue', 'description': 'third_desc 9', 'square': 9, 'value': 3},
 {'day': 'wed', 'description': 'third_desc 4', 'square': 4, 'value': 2},
 {'day': 'thu', 'description': 'third_desc 4', 'double': 4, 'value': 2},
 {'day': 'fri', 'description': 'third_desc 2', 'double': 2, 'value': 1}]


### Assumptions

We assume that the source CSV will only have a 1 row of data and the day value 
is always a number.
Supported day headers are `mon`, `tue`, `wed`, `thu`, `fri`
Date range is supported only via `<day_header>-<day_header>` format