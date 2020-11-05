"""
Base project for Beautiful Soup scrapers packaged as native apps
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import requests
from bs4 import BeautifulSoup
import csv

import cannedsoup.soupspoon as soupspoon


class CannedSoup(toga.App):

    def startup(self):
        self.data = []
        main_box = toga.Box()
        textbox = toga.MultilineTextInput(id='view1')
        def get_data(butt):
            page = requests.get(soupspoon.URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            output_rows = soupspoon.extract_rows_from_soup(soup)
            self.data = output_rows
            textbox.value = str(output_rows)
        get_data_button = toga.Button('Get Data', on_press=get_data)

        def save_data(butt):
            file_name = self.main_window.save_file_dialog('Save Data', 'web_data.csv', file_types=['csv'])
            print(file_name)
            with open(file_name, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(self.data)
        save_data_button = toga.Button("Save Data", on_press=save_data)

        main_box.add(get_data_button)
        main_box.add(save_data_button)
        main_box.add(textbox)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return CannedSoup()

# Example to scrape https://github.com/fpassow/cannedsoup
# Look for "Example Header" in a <th></th>

