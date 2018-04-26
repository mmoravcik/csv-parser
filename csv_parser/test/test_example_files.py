import os
from csv_parser import CSVParser

CSV_FILES_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'csv_files')


def test_parse_csv_1():
    with open(os.path.join(CSV_FILES_DIR, '1.csv')) as f:
        expected = [
            {'day': 'mon', 'description': 'first_desc 1', 'square': 1, 'value': 1},
            {'day': 'tue', 'description': 'first_desc 25', 'square': 25, 'value': 5},
            {'day': 'wed', 'description': 'first_desc 4', 'square': 4, 'value': 2},
            {'day': 'thu', 'description': 'first_desc 6', 'double': 6, 'value': 3},
            {'day': 'fri', 'description': 'first_desc 6', 'double': 6, 'value': 3},
        ]
        assert CSVParser(f).parse() == expected


def test_parse_csv_2():
    with open(os.path.join(CSV_FILES_DIR, '2.csv')) as f:
        expected = [
            {'day': 'mon', 'description': 'second_desc 4', 'square': 4, 'value': 2},
            {'day': 'tue', 'description': 'second_desc 4', 'square': 4, 'value': 2},
            {'day': 'wed', 'description': 'second_desc 4', 'square': 4, 'value': 2},
            {'day': 'thu', 'description': 'second_desc 4', 'double': 4, 'value': 2},
            {'day': 'fri', 'description': 'second_desc 6', 'double': 6, 'value': 3},
        ]
        assert CSVParser(f).parse() == expected


def test_parse_csv_3():
    with open(os.path.join(CSV_FILES_DIR, '3.csv')) as f:
        expected = [
            {'day': 'mon', 'description': 'third_desc 9', 'square': 9, 'value': 3},
            {'day': 'tue', 'description': 'third_desc 9', 'square': 9, 'value': 3},
            {'day': 'wed', 'description': 'third_desc 4', 'square': 4, 'value': 2},
            {'day': 'thu', 'description': 'third_desc 4', 'double': 4, 'value': 2},
            {'day': 'fri', 'description': 'third_desc 2', 'double': 2, 'value': 1},
        ]
        assert CSVParser(f).parse() == expected
