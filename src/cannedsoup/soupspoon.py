
# This is an example.
# Edit to:
#   1. Insert your own URL
#   2. Rewrite extract_rows_from_soup(soup) to extrat the data you want in your CSV

URL = 'https://github.com/fpassow/cannedsoup'

def extract_rows_from_soup(soup):
    table = soup.find(text='Example Header').parent.parent.parent.parent
    output_rows = []
    for table_row in table.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text)
        output_rows.append(output_row)
    return output_rows

