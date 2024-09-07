# NFB Device v10

This project is part of a degree project focusing on neurofeedback applications using the Muse 2 device. It integrates EEG data acquisition with a graphical user interface for real-time data visualization and analysis.

## Features
- **EEG Data Collection**: Captures and stores EEG signals from Muse 2 device sensors.
- **Real-time Video Processing**: Utilizes OpenCV for handling video frames and overlays data.
- **Interactive UI**: Built using PySide6, providing an easy-to-use interface for managing the device, data streams, and feedback.

## Showcase


  
## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/NFB-device_v10.git
   cd NFB-device_v10
   ```

2. **Install the required Python packages**:
   Make sure you have Python 3.x installed. Then, install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Application**:
   Once installed, run the main interface:
   ```bash
   python userInterface_v10.py
   ```

2. **Muse 2 Integration**:
   Ensure that your Muse 2 device is connected and streaming data. The application will automatically detect and process the EEG data in real time.


Make sure all required libraries are installed by referring to the `requirements.txt` file.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Original code by [Máté Károly Tóth](https://kth.diva-portal.org/smash/get/diva2:1773405/FULLTEXT01.pdf).
- Latest modifications and improvements by Marcus Gustafsson.
