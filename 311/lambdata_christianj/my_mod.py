# Single function to take a list, turn it into a series and add
# it to a dataframe as a new column
def add_column(data, new_col, col_name):
    # makes sure the column being added is a list
    new_col = list(new_col)

    data[str(col_name)] = new_col

    return data

# State abbreviation: Florida -> FL


def state_abbr(arg):
    arg = str(arg).upper()
    switcher = {
        'ALABAMA': 'AL',
        'ALASKA': 'AK',
        'AMERICAN SAMOA': 'AS',
        'ARIZONA': 'AZ',
        'ARKANSAS': 'AR',
        'CALIFORNIA': 'CA',
        'COLORADO': 'CO',
        'CONNECTICUT': 'CT',
        'DELAWARE': 'DE',
        'DISTRICT OF COLUMBIA': 'DC',
        'FEDERATED STATES OF MICRONESIA': 'FM',
        'FLORIDA': 'FL',
        'GEORGIA': 'GA',
        'GUAM': 'GU',
        'HAWAII': 'HI',
        'IDAHO': 'ID',
        'ILLINOIS': 'IL',
        'INDIANA': 'IN',
        'IOWA': 'IA',
        'KANSAS': 'KS',
        'KENTUCKY': 'KY',
        'LOUISIANA': 'LA',
        'MAINE': 'ME',
        'MARSHALL ISLANDS': 'MH',
        'MARYLAND': 'HD',
        'MASSACHUSETTS': 'MA',
        'MICHIGAN': 'MI',
        'MINNESOTA': 'MN',
        'MISSISSIPPI': 'MS',
        'MISSOURI': 'MO',
        'MONTANA': 'MT',
        'NEBRASKA': 'NE',
        'NEVADA': 'NV',
        'NEW HAMPSHIRE': 'NH',
        'NEW JERSEY': 'NJ',
        'NEW MEXICO': 'NM',
        'NEW YORK': 'NY',
        'NORTH CAROLINA': 'NC',
        'NORTH DAKOTA': 'ND',
        'NORTHERN MARIANA ISLANDS': 'MP',
        'OHIO': 'OH',
        'OKLAHOMA': 'OK',
        'OREGON': 'OR',
        'PALAU': 'PW',
        'PENNSYLVANIA': 'PA',
        'PUERTO RICO': 'PR',
        'RHODE ISLAND': 'RI',
        'SOUTH CAROLINA': 'SC',
        'SOUTH DAKOTA': 'SD',
        'TENNESSEE': 'TN',
        'TEXAS': 'TX',
        'UTAH': 'UT',
        'VERMONT': 'VT',
        'VIRGIN ISLANDS': 'VI',
        'VIRGINIA': 'VA',
        'WASHINGTON': 'WA',
        'WEST VIRGINIA': 'WV',
        'WISCONSIN': 'WI',
        'WYOMING': 'WY',
    }

    return switcher.get(arg, "Not Valid State")
