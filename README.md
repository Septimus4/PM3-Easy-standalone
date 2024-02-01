# PM3-Easy-Standalone

This project aims to enhance the Proxmark3 Easy by integrating it with a NanoPi NEO3 and a 3.2-inch SPI TFT LCD touch display. The goal is to create a standalone RFID tool with a graphical user interface (GUI) developed using Python and Qt.

## Project Overview

The Proxmark3 Easy is a versatile RFID tool used for reading, writing, and analyzing various RFID tags. By connecting it to a NanoPi NEO3—a compact single-board computer—and a 3.2-inch SPI TFT LCD touch display, this project transforms the Proxmark3 Easy into a portable, standalone device with an intuitive touch-based interface.

## Getting Started

1. **Hardware Requirements**:
   - Proxmark3 Easy
   - NanoPi NEO3
   - 3.2-inch SPI TFT LCD touch display
   - Necessary connectors and power supply

2. **Software Requirements**:
   - Python 3.x
   - PyQt5 or PySide2 for Qt bindings
   - Proxmark3 client software
   - SPI and GPIO libraries compatible with NanoPi NEO3

3. **Setup Instructions**:
   - **Hardware Setup**:
     - Connect the Proxmark3 Easy to the NanoPi NEO3 via USB.
     - Interface the SPI TFT LCD touch display with the NanoPi NEO3's SPI and GPIO pins. Refer to the [NanoPi NEO3 Wiki](https://wiki.friendlyelec.com/wiki/index.php/NanoPi_NEO3) for pin configurations.
   - **Software Setup**:
     - Install the required Python packages:
       ```bash
       pip install pyqt5
       ```
     - Clone this repository:
       ```bash
       git clone https://github.com/Septimus4/PM3-Easy-standalone.git
       ```
     - Navigate to the project directory and run the main application:
       ```bash
       python mainwindow.py
       ```

## Usage
Upon running the application, the GUI will display on the connected TFT LCD touch screen. The menu is dynamically generated based on the Lua scripts present in the client/luascripts directory. Users can navigate through the touch interface to select and execute these scripts directly, enabling various RFID operations facilitated by the Proxmark3 Easy.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FriendlyELEC](https://www.friendlyelec.com/) for the NanoPi NEO3 hardware and documentation.
- [Proxmark3 Community](https://github.com/RfidResearchGroup/proxmark3) for the Proxmark3 tools and resources.
- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) for the Python bindings for Qt.

For detailed information on connecting the Matrix - 2'8 SPI Key TFT to the NanoPi NEO, refer to the [FriendlyELEC Wiki](https://wiki.friendlyelec.com/wiki/index.php/Matrix_-_2%278_SPI_Key_TFT).

*Note: Ensure all hardware connections are secure and double-check pin configurations to prevent damage to components.* 
