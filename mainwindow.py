import json
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QScrollArea, QStackedLayout, QLabel
from PyQt6.QtCore import QSize

CONFIG = {
    "json_file_path": "./reformatted_json_advanced.json",
    "command_prefix": "pm3 -c",
}

# Function to parse the JSON file
def parse_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to execute Proxmark3 command
def execute_command(command):
    try:
        subprocess.run(f'{CONFIG["command_prefix"]} "{command}"', shell=True, check=True)
    except subprocess.CalledProcessError as e:
        handle_error(f"Error executing command: {e}")

# Error handling function
def handle_error(error_message):
    # Display error message to the user (e.g., in a QMessageBox)
    pass

# Building the PyQt6 application
class Proxmark3App(QMainWindow):
    def __init__(self, menu_data):
        super().__init__()
        self.menu_data = menu_data
        self.layout_stack = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Proxmark3 Command Interface")
        self.showFullScreen()  # Full screen application

        # Create a central widget and a scroll area
        self.central_widget = QWidget(self)
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.central_widget)
        self.setCentralWidget(self.scroll_area)

        # Main layout
        self.main_layout = QVBoxLayout(self.central_widget)
        self.stacked_layout = QStackedLayout()
        self.main_layout.addLayout(self.stacked_layout)

        # Create the main menu
        self.create_menu(self.menu_data)

    def create_menu(self, menu_data, is_submenu=False):
        layout = QVBoxLayout()
        self.layout_stack.append({'name': 'Submenu', 'layout': layout} if is_submenu else {'name': 'Main Menu', 'layout': layout})

        # Add header showing current path
        path_label = QLabel("/".join(item['name'] for item in self.layout_stack), self)
        path_label.setFixedSize(QSize(280, 50))

        # Set the text color of path_label to a contrasting color (e.g., white)
        path_label.setStyleSheet("color: white;")

        layout.addWidget(path_label)

        if is_submenu:
            # Add a back button for submenus
            back_button = QPushButton("Back", self)
            back_button.clicked.connect(self.go_back)
            back_button.setFixedSize(QSize(280, 50))
            layout.addWidget(back_button)

        for name, command in menu_data.items():
            button = QPushButton(name, self)
            button.setFixedSize(QSize(280, 50))
            if isinstance(command, dict):
                # Submenu
                button.setText(">> " + name)  # Add ">>" indicator for submenus
                button.clicked.connect(lambda _, c=command, n=name: self.create_menu(c, True))
            else:
                # Command
                button.clicked.connect(lambda _, c=command: execute_command(c))
            layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        if is_submenu:
            self.stacked_layout.removeWidget(self.stacked_layout.currentWidget())
            self.stacked_layout.addWidget(widget)
            self.stacked_layout.setCurrentWidget(widget)
        else:
            self.stacked_layout.addWidget(widget)

    def go_back(self):
        if len(self.layout_stack) > 1:
            self.layout_stack.pop()  # Remove the current layout from the stack
            self.stacked_layout.removeWidget(self.stacked_layout.currentWidget())
            previous_layout = self.layout_stack[-1]['layout']
            for i in range(self.stacked_layout.count()):
                if self.stacked_layout.itemAt(i).layout() == previous_layout:
                    self.stacked_layout.setCurrentIndex(i)
                    break


# Main application loop
def main():
    app = QApplication([])
    menu_data = parse_json(CONFIG["json_file_path"])
    main_window = Proxmark3App(menu_data)
    main_window.show()
    app.exec()


if __name__ == '__main__':
    main()
