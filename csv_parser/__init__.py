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
        value = int(row.get(day_header_mapping.get(day)))
        description = row.get('description', '')

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
        result = []
        for row in reader:
            day_header_mapping = self._get_day_header_mapping(row)

            for day in self.week_days:
                result.append(self._get_day_data(day, row, day_header_mapping))

        return result
