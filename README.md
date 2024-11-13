# PM3-Easy-Standalone

This project enhances the **Proxmark3 Easy** by integrating it with a **NanoPi NEO3** and a **3.2-inch SPI TFT LCD touch display**, creating a portable, standalone RFID tool with an intuitive touch-based interface developed using Python and Qt.

## Project Overview

The **Proxmark3 Easy** is a versatile RFID tool for reading, writing, and analyzing various RFID tags. By connecting it to a **NanoPi NEO3**—a compact single-board computer—and a **3.2-inch SPI TFT LCD touch display**, this project transforms the Proxmark3 Easy into a portable device with a touch-friendly graphical user interface (GUI).

## Getting Started

### Hardware Requirements

- **Proxmark3 Easy**
- **NanoPi NEO3**
- **3.2-inch SPI TFT LCD touch display**
- Necessary connectors and power supply

### Software Requirements

- **Python 3.x**
- **Poetry** (for Python dependency management)
- **PyQt5** (Qt bindings for Python)
- **Proxmark3 client software**
- **SPI and GPIO libraries** compatible with NanoPi NEO3

### Setup Instructions

#### Hardware Setup

- **Connect the Proxmark3 Easy** to the NanoPi NEO3 via USB.
- **Interface the SPI TFT LCD touch display** with the NanoPi NEO3's SPI and GPIO pins.
    - Refer to the [NanoPi NEO3 Wiki](https://wiki.friendlyelec.com/wiki/index.php/NanoPi_NEO3) for pin configurations.
    - For detailed information on connecting the Matrix - 2'8 SPI Key TFT to the NanoPi NEO, refer to the [FriendlyELEC Wiki](https://wiki.friendlyelec.com/wiki/index.php/Matrix_-_2%278_SPI_Key_TFT).

#### Software Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Septimus4/PM3-Easy-standalone.git
   cd PM3-Easy-standalone
   ```

2. **Install Poetry**

   If you haven't installed Poetry yet, follow the instructions on the [Poetry official website](https://python-poetry.org/docs/#installation).

   ```bash
   # Install Poetry (if not already installed)
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   Make sure to add Poetry to your PATH as instructed during installation.

3. **Install Dependencies Using Poetry**

   ```bash
   poetry install
   ```

   This command creates a virtual environment and installs all required dependencies specified in `pyproject.toml`.

4. **Activate the Virtual Environment**

   ```bash
   poetry shell
   ```

5. **Install the Proxmark3 Client**

   Ensure that the Proxmark3 client software is installed and accessible in your system PATH.

6. **Run the Application**

   ```bash
   python mainwindow.py
   ```

    - Alternatively, if using Poetry:

      ```bash
      poetry run python mainwindow.py
      ```

## Usage

Upon running the application, the GUI will display on the connected **3.2-inch TFT LCD touch screen**. The interface is optimized for touch input, with larger buttons and touch-friendly list items. Users can:

- **Navigate through the touch interface** to select and execute Lua scripts.
- **Scroll through the list of scripts** by pressing and dragging up or down.
- **Execute scripts directly**, enabling various RFID operations facilitated by the Proxmark3 Easy.
- **View or hide execution output** using the "Show Output"/"Hide Output" toggle button.

### Features

- **Dynamic Script Loading**: The menu is dynamically generated based on the Lua scripts present in the `proxmark3/client/luascripts` directory.
- **Touch-Friendly Interface**: Designed for a 240x320 vertical display, the GUI elements are sized for comfortable touch interaction.
- **Real-Time Output Display**: Users can view real-time output from the Proxmark3 client during script execution.

## Project Structure

```bash
PM3-Easy-standalone/
├── LICENSE.md
├── mainwindow.py
├── pyproject.toml
├── README.md
├── proxmark3/               # Proxmark3 client and scripts (submodule or subtree)
│   └── client/
│       └── luascripts/
│           ├── ...          # Lua scripts
```

- **`mainwindow.py`**: The main Python application file containing the GUI code.
- **`pyproject.toml`**: Configuration file for Poetry, specifying dependencies.
- **`proxmark3/client/luascripts`**: Directory containing Lua scripts sourced from the Proxmark3 repository.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

### Updating Lua Scripts

The Lua scripts in `proxmark3/client/luascripts` are included as a subtree from the [RfidResearchGroup/proxmark3](https://github.com/RfidResearchGroup/proxmark3) repository. To update the scripts:

1. **Fetch the Latest Changes**

   ```bash
   git remote add proxmark3-upstream https://github.com/RfidResearchGroup/proxmark3.git
   git fetch proxmark3-upstream
   ```

2. **Update the Subtree**

   ```bash
   git subtree pull --prefix=proxmark3 proxmark3-upstream master --squash
   ```

- **Display Issues**

  If the GUI does not display correctly on the TFT LCD touch screen:

    - Verify that the display is properly connected and configured.
    - Check the display drivers and ensure they are compatible with your hardware.

### Customizing the GUI

- **Adjusting for Different Screen Sizes**

  If you're using a different screen size, you may need to adjust the window dimensions in `mainwindow.py`:

  ```python
  self.setFixedSize(width, height)
  ```
  
## Acknowledgments

- **[FriendlyELEC](https://www.friendlyelec.com/)** for the NanoPi NEO3 hardware and documentation.
- **[Proxmark3 Community](https://github.com/RfidResearchGroup/proxmark3)** for the Proxmark3 tools and resources.
- **[PyQt5](https://riverbankcomputing.com/software/pyqt/intro)** for the Python bindings for Qt.

*Note: Ensure all hardware connections are secure and double-check pin configurations to prevent damage to components.*
