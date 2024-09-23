# Neurofeedback (NFB) Training

This project is part of a degree project with a focus on neurofeedback training (NFB) using the Muse 2 portable EEG headband. 

Currently only for windows 10+ due to the third-party software "BlueMuse" compatibility.

## Showcase
![ApplicationFrameHost_iaU3YK0udd](https://github.com/user-attachments/assets/acdf2f5e-30bd-40fd-82d2-0bb6bdf45954)

  
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

3. **Muse 2 Integration**:
   Ensure that your Muse 2 device is connected and streaming data. The application will automatically detect and process the EEG data in real time.

    The [BlueMuse](https://github.com/kowalej/BlueMuse) app to enable a stream between the Muse 2 EEG headband and the computer.

## Usage

1. **Importing Training Media**

   Training media is not included on github due to size of files, reach out to me to get training media files.

2. **Run the Application**:
   Once installed, run the main interface:
   ```bash
   python userInterface_v10.py
   ```


Make sure all required libraries are installed by referring to the `requirements.txt` file.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Original code by [Máté Károly Tóth](https://kth.diva-portal.org/smash/get/diva2:1773405/FULLTEXT01.pdf).
- Latest modifications and improvements by Marcus Gustafsson.
