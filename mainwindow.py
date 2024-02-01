import sys
import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QMessageBox,
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PM3 Easy Standalone GUI")
        self.setGeometry(100, 100, 480, 320)  # Adjust the window size as needed

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # List widget to display Lua scripts
        self.script_list = QListWidget()
        layout.addWidget(self.script_list)

        # Execute button
        self.execute_button = QPushButton("Execute Selected Script")
        layout.addWidget(self.execute_button)
        self.execute_button.clicked.connect(self.execute_script)

        # Load scripts
        self.load_scripts()

    def load_scripts(self):
        # Assume the Lua scripts are in 'client/luascripts' directory
        script_dir = os.path.join(os.getcwd(), "client", "luascripts")
        if not os.path.exists(script_dir):
            QMessageBox.critical(
                self, "Error", f"Script directory not found:\n{script_dir}"
            )
            return

        scripts = [f for f in os.listdir(script_dir) if f.endswith(".lua")]
        if scripts:
            self.script_list.addItems(scripts)
        else:
            QMessageBox.information(
                self, "No Scripts Found", "No Lua scripts were found in the directory."
            )

    def execute_script(self):
        selected_items = self.script_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(
                self, "No Selection", "Please select a script to execute."
            )
            return

        script_name = selected_items[0].text()
        script_path = os.path.join(os.getcwd(), "client", "luascripts", script_name)

        # Command to execute the Lua script with Proxmark3 client
        # Adjust the device path as necessary
        device_path = "/dev/ttyACM0"  # or '/dev/ttyUSB0', adjust as necessary
        command = ["proxmark3", device_path, "-s", script_path]

        try:
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                QMessageBox.information(
                    self, "Success", f"Script executed successfully:\n{stdout.decode()}"
                )
            else:
                QMessageBox.critical(
                    self, "Error", f"Error executing script:\n{stderr.decode()}"
                )

        except Exception as e:
            QMessageBox.critical(self, "Execution Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
