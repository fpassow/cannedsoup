
# This is an example.
# Edit to:
#   1. Set a HUMAN_FRIENDLY_NAME for the app
#   1. Insert your own URL
#   2. Rewrite the extract_rows_from_soup(soup) function to extrat the data you want
#      and return it as a list of lists, which will become the rows in the output csv.

HUMAN_FRIENDLY_NAME = 'Cannedsoup Example Name'

URL = 'https://github.com/fpassow/cannedsoup'

def extract_rows_from_soup(soup):
    # soup is a BeautifulSoup object created with the HTML fetched from the above URL.
    # In this example we look for "Example Header" in a <th></th>.
    # Then move up to the <table> element, down to the <tbody>, and start processing <tr>'s
    # Please consult docs or tutorials on the python BeatifulSoup package to help you
    #    write your own code to extrat the date you want.
    # The function should then return a list of lists, where the inner lists will become rows
    #    in the outputted .csv
    table = soup.find(text='Example Header').parent.parent.parent.parent.find('tbody')
    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text)
        output_rows.append(output_row)
    return output_rows

