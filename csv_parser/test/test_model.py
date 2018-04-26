import pytest
from io import StringIO

from csv_parser import CSVParser


def test_get_day_header_mapping():
    # Lets try with various 'malicious' data to make sure we end up
    # with a correct mapping
    row = [
        'mon',
        'wed',
        '^&*--&%$',
        'random',
        'monday-thursday',
        'nom-dew',
        'thu-fri',
        'fri-mon',
    ]
    csv_parser = CSVParser(StringIO())

    expected = {
        'mon': 'mon',
        'wed': 'wed',
        'thu': 'thu-fri',
        'fri': 'thu-fri',
    }

    assert csv_parser._get_day_header_mapping(row) == expected


def test_parse_only_days_we_provide_and_in_day_order():
    # Thursday is missing
    test_file = StringIO(
        u'fri,mon-tue,wed,ooops,description\n1,2,3,4,desc'
    )

    csv_parser = CSVParser(test_file)

    expected = [
        {'day': 'mon', 'description': 'desc 4', 'square': 4, 'value': 2},
        {'day': 'tue', 'description': 'desc 4', 'square': 4, 'value': 2},
        {'day': 'wed', 'description': 'desc 9', 'square': 9, 'value': 3},
        {'day': 'fri', 'description': 'desc 2', 'double': 2, 'value': 1},
    ]

    assert csv_parser.parse() == expected


def test_no_description_provided():
    test_file = StringIO(
        u'fri\n1'
    )

    csv_parser = CSVParser(test_file)

    expected = [
        {'day': 'fri', 'description': 'N/A 2', 'double': 2, 'value': 1},
    ]

    assert csv_parser.parse() == expected


def test_multiple_lines():
    """
    We assume 1 line of CSV data. Therefore, only return the first row parsed
    """

    # Multi-line file
    test_file = StringIO(
        u'fri,wed\n1,1\n2,2'
    )

    csv_parser = CSVParser(test_file)

    expected = [
        {'day': 'wed', 'description': 'N/A 1', 'square': 1, 'value': 1},
        {'day': 'fri', 'description': 'N/A 2', 'double': 2, 'value': 1},
    ]

    assert csv_parser.parse() == expected


def test_non_int_value_raises_an_exception():
    """
    We assume that value is always a number. Test the exception is raised if not
    """
    test_file = StringIO(
        u'fri,wed\na,6'
    )

    csv_parser = CSVParser(test_file)

    with pytest.raises(ValueError):
        csv_parser.parse()
