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
        main_box = toga.Box(style=Pack(direction=COLUMN))
        textbox = toga.MultilineTextInput(style=Pack(flex=1))
        def get_data(butt):
            page = requests.get(soupspoon.URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            output_rows = soupspoon.extract_rows_from_soup(soup)
            self.data = output_rows
            data_string = '';
            for row in output_rows:
                data_string += (', '.join(row))
                data_string += '\n'
            textbox.value = data_string
        get_data_button = toga.Button('Get Data', on_press=get_data)

        def save_data(butt):
            file_name = self.main_window.save_file_dialog('Save Data', 'web_data.csv', file_types=['csv'])
            print(file_name)
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(self.data)
        save_data_button = toga.Button("Save Data", on_press=save_data)
        controls_box = toga.Box(children=[get_data_button, save_data_button], style=Pack(padding=10))

        main_box.add(controls_box)
        main_box.add(textbox)

        title_string = 'Set HUMAN_FRIENDLY_NAME in soupspoon.py'
        if soupspoon.HUMAN_FRIENDLY_NAME:
            title_string = soupspoon.HUMAN_FRIENDLY_NAME
        self.main_window = toga.MainWindow(title=title_string)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return CannedSoup()

