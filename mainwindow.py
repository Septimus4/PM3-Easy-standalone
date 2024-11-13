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
    QTextEdit,
    QSizePolicy,
    QScroller,
)
from PyQt5.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PM3 Easy GUI")
        self.setFixedSize(240, 320)  # Set window size for vertical display

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main vertical layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # List widget to display Lua scripts
        self.script_list = QListWidget()
        self.script_list.setStyleSheet(
            "font-size: 14px; padding: 5px;"
        )
        self.script_list.setSpacing(5)
        self.script_list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.script_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.script_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        main_layout.addWidget(self.script_list)

        # Enable touch-based scrolling
        QScroller.grabGesture(self.script_list, QScroller.LeftMouseButtonGesture)

        # Execute button
        self.execute_button = QPushButton("Execute Script")
        self.execute_button.setStyleSheet(
            "font-size: 14px; padding: 8px; min-height: 40px;"
        )
        self.execute_button.clicked.connect(self.execute_script)
        main_layout.addWidget(self.execute_button)

        # Toggle output button
        self.toggle_output_button = QPushButton("Show Output")
        self.toggle_output_button.setStyleSheet(
            "font-size: 14px; padding: 8px; min-height: 40px;"
        )
        self.toggle_output_button.setCheckable(True)
        self.toggle_output_button.clicked.connect(self.toggle_output)
        main_layout.addWidget(self.toggle_output_button)

        # Text widget to display output (initially hidden)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.hide()  # Start hidden
        self.output_text.setStyleSheet("font-size: 12px;")
        self.output_text.setFixedHeight(100)  # Adjust as needed
        main_layout.addWidget(self.output_text)

        # Load scripts
        self.load_scripts()

    def load_scripts(self):
        # Updated script directory path
        script_dir = os.path.join(os.getcwd(), "proxmark3", "client", "luascripts")
        if not os.path.exists(script_dir):
            QMessageBox.critical(
                self, "Error", f"Script directory not found:\n{script_dir}"
            )
            return

        scripts = [
            f for f in os.listdir(script_dir)
            if os.path.isfile(os.path.join(script_dir, f)) and f.endswith(".lua")
        ]
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
        script_path = os.path.join(
            os.getcwd(), "proxmark3", "client", "luascripts", script_name
        )

        # Use 'proxmark3' command from the environment
        pm3_client = "proxmark3"

        # Let the Proxmark3 client auto-detect the device
        command = [pm3_client, "-s", script_path]

        try:
            # Disable the execute button to prevent multiple clicks
            self.execute_button.setEnabled(False)
            self.output_text.clear()

            # Show the output text widget if it's hidden
            if not self.output_text.isVisible():
                self.output_text.show()
                self.toggle_output_button.setChecked(True)
                self.toggle_output_button.setText("Hide Output")

            # Start the subprocess
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
            )

            # Read output line by line
            while True:
                line = process.stdout.readline()
                if not line:
                    break
                self.output_text.append(line.strip())
                QApplication.processEvents()  # Allow GUI to update

            process.wait()

            # Re-enable the execute button
            self.execute_button.setEnabled(True)

            if process.returncode == 0:
                QMessageBox.information(
                    self, "Success", "Script executed successfully."
                )
            else:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Script execution failed with return code {process.returncode}.\n"
                    f"Check the output for more details.",
                )

        except Exception as e:
            QMessageBox.critical(self, "Execution Error", str(e))
            self.execute_button.setEnabled(True)

    def toggle_output(self):
        if self.toggle_output_button.isChecked():
            self.output_text.show()
            self.toggle_output_button.setText("Hide Output")
        else:
            self.output_text.hide()
            self.toggle_output_button.setText("Show Output")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Set a larger default font for the entire application
    app.setStyleSheet("QWidget { font-size: 14px; }")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
