import csv
import re


# Regular expression which matches the possible day range,
# for example `mon-tue` or `wed-fri`.
RANGE_REGEX = '\\b(mon|tue|wed|thu|fri)\\b-\\b(mon|tue|wed|thu|fri)\\b'


class CSVParser:
    week_days = ('mon', 'tue', 'wed', 'thu', 'fri')

    def __init__(self, csv_file):
        self.file = csv_file

    def _get_day_header_mapping(self, row):
        """
        For a row, lets create a week_day <-> header mapping dict so we
        know which header to use for a certain day

        Example output

        ```
            {
                'tue': 'tue-wed',
            },
            {
                'wed': 'tue-wed',
            },
            {
                'mon': 'mon',
            },

            ....

        :param row <array>
        :return: <dict>
        """
        day_header_mapping = {}

        for header in row:
            if header in self.week_days:
                # In this case, `header` is the header for the day
                day_header_mapping[header] = header
            else:
                # Lets see if we are dealing with the day range
                range_match = re.search(RANGE_REGEX, header)
                if range_match:
                    # If we are, then start_day and end_day are our matches
                    start_day = range_match.group(1)
                    end_day = range_match.group(2)
                    start_day_index = self.week_days.index(start_day)
                    end_day_index = self.week_days.index(end_day)
                    for day in self.week_days[start_day_index:end_day_index+1]:
                        day_header_mapping[day] = header
        return day_header_mapping

    def _get_day_data(self, day, row, day_header_mapping):
        """
        Constructs a dict which hold data about the specific day read from
        the given row

        Example output

        ```
            {
                'day': 'mon',
                'description: 'desc 1',
                'value: 1,
                'square': 1
            },
            ...
        """
        # Only consider the day if we have a data for it
        if day_header_mapping.get(day):

            # For now, assuming numbers only
            value = int(row[day_header_mapping[day]])

            # We could tweak this to make sure we handle no
            # `description` column properly
            description = row.get('description', 'N/A')

            day_data = dict(
                day=day,
                value=value,
            )

            # Lets workout the day specific data
            if day in ['mon', 'tue', 'wed']:
                day_data['square'] = value * value
                day_data['description'] = "{} {}".format(
                    description, day_data['square']
                )
            elif day in ['thu', 'fri']:
                day_data['double'] = value * 2
                day_data['description'] = "{} {}".format(
                    description, day_data['double']
                )
            return day_data

    def parse(self):
        reader = csv.DictReader(self.file)
        results = []  # This is where we hold the final list of day data

        # We are assuming only 1 row of data for now
        row = next(reader)

        # Lets get the mapping so we know which day is which header
        day_header_mapping = self._get_day_header_mapping(row)

        # Lets get data for days, if present. This will also make
        # sure the order of day data is correct
        for day in self.week_days:
            day_data = self._get_day_data(day, row, day_header_mapping)
            if day_data:
                results.append(day_data)

        return results
