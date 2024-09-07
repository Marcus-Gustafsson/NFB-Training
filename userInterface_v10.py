import sys
import json
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Signal
from QtDesingerUI.MainWindowV7_ui import Ui_MainWindow
from QtDesingerUI.Undo_dialog_ui import Ui_undoConfirmationDialog
from QtDesingerUI.Lost_connection_dialog_ui import Ui_LostConnectionConfirmationDialog
import multiprocessing
import random
import pandas as pd
import datetime
from main import main_function, initialization

from QtDesingerUI.SplashScreen_ui import Ui_Dialog
from PySide6.QtWidgets import QDialog, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, Qt, QEasingCurve, QTimer


class Ui_MainWindow(QMainWindow, Ui_MainWindow):
    trainingCompleted = Signal()
    lostConnectionMuse2 = Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        # This line sets the default page of the stackedWidget to the first page.
        self.stackedWidget.setCurrentIndex(0)

        # Add this flag
        self.animation_shown = False
        # Assuming the QLabel you added to the stacked widget is named 'animatedLabel'
        self.opacity_effect = QGraphicsOpacityEffect(self.animatedLabel)
        self.animatedLabel.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0)
        self.animatedLabel.setStyleSheet("color: #FFFFFF;")
        
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(3000)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

        if not self.animation_shown:
            QTimer.singleShot(1000, self.start_fade_in)
            self.animation_shown = True




        self.current_day = None
        # Add an attribute to store the selected video path
        self.selected_training_path = None
        self.update_all_button_states()

        # Connect the custom signal to the slot
        self.trainingCompleted.connect(self.update_all_button_states)
        self.lostConnectionMuse2.connect(self.showLostConnectionDialog)

        ######Buttons######
        self.pb_startTraining.clicked.connect(self.start_training)

        self.pb_VideoTraining_1.clicked.connect(self.select_random_training_video)
        self.pb_VideoTraining_2.clicked.connect(self.select_random_training_video)
        self.pb_VideoTraining_3.clicked.connect(self.select_random_training_video)

        self.pb_ImageTraining_1.clicked.connect(self.select_training_image)
        self.pb_ImageTraining_2.clicked.connect(self.select_training_image)
        self.pb_ImageTraining_3.clicked.connect(self.select_training_image)
        self.pb_ecologicalVideo.clicked.connect(self.play_ecological_video)

        self.pb_Undo.clicked.connect(self.showUndoConfirmation)

        #Connect "Back" button to switch back to "Days" page
        self.pb_BackButton.clicked.connect(self.switch_to_days_page)

        # Connect the "Day X" button to switch to the second page.
        self.pb_Day1.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day1, "Day 1"))
        #self.pb_Day2.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day2, "Day 2"))
        self.pb_Day3.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day3, "Day 3"))
        #self.pb_Day4.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day4, "Day 4"))
        self.pb_Day5.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day5, "Day 5"))
        #self.pb_Day6.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day6, "Day 6"))
        self.pb_Day7.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day7, "Day 7"))
        #self.pb_Day8.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day8, "Day 8"))
        self.pb_Day9.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day9, "Day 9"))
        #self.pb_Day10.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day10, "Day 10"))
        self.pb_Day11.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day11, "Day 11"))
        #self.pb_Day12.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day12, "Day 12"))
        self.pb_Day13.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day13, "Day 13"))
        #self.pb_Day14.clicked.connect(lambda: self.set_current_day_button_and_switch(self.pb_Day14, "Day 14"))
    
    def showUndoConfirmation(self):
        self.dialog = QDialog()
        self.ui = Ui_undoConfirmationDialog()
        self.ui.setupUi(self.dialog)
        self.ui.pb_Undo_Yes.clicked.connect(self.performUndo)
        self.ui.pb_Undo_No.clicked.connect(self.dialog.reject)
        self.dialog.exec()
    
    def showLostConnectionDialog(self):
        self.dialog = QDialog()
        self.ui = Ui_LostConnectionConfirmationDialog()
        self.ui.setupUi(self.dialog)
        self.ui.pb_Understood.clicked.connect(self.dialog.reject)
        self.dialog.exec()
        
    def performUndo(self):
        # Determine the base path and CSV file path
        if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
            base_path = os.path.dirname(sys.executable)
            base_path = os.path.dirname(base_path)
            csv_path = os.path.join(base_path, "Training_log.csv")
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(base_path, "TrainingMedia", "Training_log.csv")

        # Check if the CSV file exists
        if not os.path.exists(csv_path):
            print("Training log file does not exist.")
            return

        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_path)

        # Get the current day label text (e.g., "Day 1")
        current_day = self.page2_dayLabel.text()

        # Filter the DataFrame for the selected training day
        df_current_day = df[df['Training Day'] == current_day]

        # Check if there are any entries for the selected training day
        if df_current_day.empty:
            print("No training media found for the selected training day.")
            return

        # Identify the last entry for the selected training day
        last_entry_index = df_current_day.index[-1]

        # Remove that entry from the main DataFrame
        df = df.drop(last_entry_index)

        # Save the DataFrame back to the CSV file
        df.to_csv(csv_path, index=False)
        print("Last training video for the selected training day has been undone.")
        self.update_all_button_states()
        self.dialog.accept()

    ####Functions and methods####
    @staticmethod
    def get_json_file_path():
    # Get the directory of the currently running script or executable
        exe_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the .json file in the same directory
        json_file_path = os.path.join(exe_dir, 'nfb_parameters.json')
        return json_file_path

    @staticmethod
    def get_training_path(video_name):
        if getattr(sys, '_MEIPASS', False):  # Running as a PyInstaller bundle
            base_path = os.path.dirname(sys.executable)  # Get the directory containing the .exe file
        else:  # Running in a normal Python environment
            base_path = os.path.dirname(os.path.abspath(__file__))  # Get the directory containing the Python script
        return os.path.join(base_path, 'TrainingMedia', video_name)


    def update_json_file(self, chosen_day , training_path, baseline_length):
        json_file_path = self.get_json_file_path()
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {
                "MUSE_SELECTED": True,
                "NEGATIVE_FEEDBACK": True,
                "FEEDBACK_ALG": True,
                "FREQUENCY_RANGE": [3.0, 7.0],
                "FEEDBACK_BUFFER_SIZE": 16,
                "NUMBER_OF_SAMPLES": 512,
                "SAMPLING_FREQUENCY": 256,
                "BASELINE_LENGTH": 45, 
                "TRAINING_INPUT": "TrainingMedia\Video Training\Training_video_1.mp4",
                "CHOSEN_DAY" : "Day 1"
                }
        data['TRAINING_INPUT'] = training_path
        data['CHOSEN_DAY'] = chosen_day
        data['BASELINE_LENGTH'] = baseline_length
        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=4)
    
    def update_info_text(self, day):
        # Define the instruction text for each scenario
        text_for_day_1 = (
    """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">"""
    """<html><head><meta name="qrichtext" content="1" /><style type="text/css"> """
    """p, li { white-space: pre-wrap; } """
    """hr { height: 1px; border-width: 0; } """
    """li.unchecked::marker { content: "\\2610"; } """
    """li.checked::marker { content: "\\2612"; } """
    """</style></head><body style="font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;">"""
    """<p style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">If You Need to Stop:</span></p> """
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">"""
    """<li style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Feel uncomfortable? Press “Q” on your keyboard to stop the video immediately.</li>"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">You can try again whenever you feel ready.</li></ul> """
    """<p style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Training Steps:</span></p> """
    """<ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Select Your Video:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">First day of training?</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Click "Ecological Video"</li>"""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">After "Ecological Video"</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Click "Image Training 1" or "Video Training 1"</li>"""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Begin Training:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Press "Start Training."</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Video Training: Focus your eyes on the red dot and try to slow down the video as much as possible.</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Image Training: Try keeping the image as clear as possible.</li>"""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Move to the Next Video:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Finished a video?</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Select another available training video.</li>"""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Complete Your Training:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Everything green, including “Ecological Video”? You’re done for today!</li>"""
    """</ul>"""

    """<p style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Help for Interrupted Videos:</span></p> """
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">"""
    """<li style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Interrupted during a video? Click “Undo” to make it available again if it's green.</li></ul> """
    """</body></html>"""
)



        text_for_day_13 = (
    """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">"""
    """<html><head><meta name="qrichtext" content="1" /><style type="text/css"> """
    """p, li { white-space: pre-wrap; } """
    """hr { height: 1px; border-width: 0; } """
    """li.unchecked::marker { content: "\\2610"; } """
    """li.checked::marker { content: "\\2612"; } """
    """</style></head><body style="font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;">"""
    """<p style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">If You Need to Stop:</span></p> """
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">"""
    """<li style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Feel uncomfortable? Press “Q” on your keyboard to stop the video immediately.</li>"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">You can try again whenever you feel ready.</li></ul> """
    """<p style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Training Steps:</span></p> """
    """<ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Select Your Video:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Starting today's training?</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Click "Image Training 1" or "Video Training 1"</li>"""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Begin Training:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Press "Start Training."</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Video Training: Focus your eyes on the red dot and try to slow down the video as much as possible.</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Image Training: Try keeping the image as clear as possible.</li>"""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Move to the Next Video:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Finished a video?</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Select another available training video.</li>"""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">End with an Ecological Video:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">All training videos green?</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Click “Ecological Video” and press “Start Training.”</li>"""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Complete Your Training:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Everything green, including “Ecological Video”? You’re done for today!</li>"""
    """</ul>"""

    """<p style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Help for Interrupted Videos:</span></p> """
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">"""
    """<li style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Interrupted during a video? Click “Undo” to make it available again if it's green.</li></ul> """
    """</body></html>"""
)



        text_for_other_days = (
    """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">"""
    """<html><head><meta name="qrichtext" content="1" /><style type="text/css"> """
    """p, li { white-space: pre-wrap; } """
    """hr { height: 1px; border-width: 0; } """
    """li.unchecked::marker { content: "\\2610"; } """
    """li.checked::marker { content: "\\2612"; } """
    """</style></head><body style="font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;">"""
    """<p style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">If You Need to Stop:</span></p> """
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">"""
    """<li style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Feel uncomfortable? Press “Q” on your keyboard to stop the video immediately.</li>"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">You can try again whenever you feel ready.</li></ul> """
    """<p style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Training Steps:</span></p> """
    """<ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Select Your Video:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Starting today's training?</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Click "Image Training 1" or "Video Training 1"</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Otherwise select any available training video."""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Begin Training:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Press "Start Training."</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Video Training: Focus your eyes on the red dot and try to slow down the video as much as possible.</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Image Training: Try keeping the image as clear as possible.</li>"""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Move to the Next Video:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Finished a video?</li>"""
    """</ul>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Select another available training video.</li>"""
    """</ul>"""

    """<li style="margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Complete Your Training:</span></li>"""
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 20px; margin-right: 0px;">"""
    """<li style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Everything green? You’re done for today!</li>"""
    """</ul>"""

    """<p style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style="font-weight:700;">Help for Interrupted Videos:</span></p> """
    """<ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">"""
    """<li style="margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Interrupted during a video? Click “Undo” to make it available again if it's green.</li></ul> """
    """</body></html>"""
)

        # Apply the text based on the current day
        if day == "Day 1":
            self.infoTextEdit.setHtml(text_for_day_1)
        elif day == "Day 13":
            self.infoTextEdit.setHtml(text_for_day_13)
        else:
            self.infoTextEdit.setHtml(text_for_other_days)
    
    def set_current_day_button_and_switch(self, button, day):
        self.current_day_button = button
        # Update the info text based on the selected day
        self.update_info_text(day)
        self.switch_to_training_page(day)


    def switch_to_training_page(self, day):
        # Set the label text to the respective day
        self.page2_dayLabel.setText(day)
        self.current_day = day
        self.update_button_state(self.current_day_button, day)
        self.pb_startTraining.setEnabled(False)
        # Switch to the training page
        self.stackedWidget.setCurrentIndex(2)


    def switch_to_days_page(self):
    # This line sets the active page of the stackedWidget to the days page.
        self.stackedWidget.setCurrentIndex(1)

    def update_button_state(self, button, day):

        video_count, image_count, eco_count = self.is_training_complete(day)
        total_count = video_count + image_count + eco_count

        def set_button_style(button, enabled, color=None):
            button.setEnabled(bool(enabled))
            if color == "green":
                # If the color is green, apply green background color
                button.setStyleSheet(f"background-color: {color};")
            elif color == "yellow" or color == "#CCAD00":  # Using a mellow yellow for the base color
                # Apply the mellow yellow background color and adjust hover/pressed styles
                button.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: #CCAD00;\n"  # Base color
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: #B8A000;\n"  # Darker yellow for hover
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: #A38F00;\n"  # Even darker yellow for pressed
                                    "}\n"
                                    "QPushButton:disabled {\n"
                                    "    background-color: #272727;\n"  # Disabled state remains the same
                                    "}\n")
            else:
                # Default style for buttons without specific color instructions
                button.setStyleSheet(u"QPushButton {\n"
                                    "    background-color: #555;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: #666;\n"
                                    "}\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: #444;\n"
                                    "}\n"
                                    "QPushButton:disabled {\n"
                                    "    background-color: #272727;\n"
                                    "}\n")


        # Enable or disable training buttons based on counts
        set_button_style(self.pb_VideoTraining_1, video_count < 1)
        set_button_style(self.pb_VideoTraining_2, video_count == 1)
        set_button_style(self.pb_VideoTraining_3, video_count == 2)
        set_button_style(self.pb_ImageTraining_1, image_count < 1)
        set_button_style(self.pb_ImageTraining_2, image_count == 1)
        set_button_style(self.pb_ImageTraining_3, image_count == 2)

        # Set colors for completed trainings
        if video_count > 0: set_button_style(self.pb_VideoTraining_1, False, "green")
        if video_count > 1: set_button_style(self.pb_VideoTraining_2, False, "green")
        if video_count > 2: set_button_style(self.pb_VideoTraining_3, False, "green")
        if image_count > 0: set_button_style(self.pb_ImageTraining_1, False, "green")
        if image_count > 1: set_button_style(self.pb_ImageTraining_2, False, "green")
        if image_count > 2: set_button_style(self.pb_ImageTraining_3, False, "green")

        # Use the same base path logic as in the select_random_training_video function
        if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
            base_path = os.path.dirname(sys.executable)
            base_path = os.path.dirname(base_path)
            csv_path = os.path.join(base_path,"Training_log.csv")
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(base_path, "TrainingMedia", "Training_log.csv")

        
        # Check if the file exists; if not, return False immediately
        if os.path.exists(csv_path):
        
            # Read the csv file
            df = pd.read_csv(csv_path)

            # Filter the DataFrame for the selected training day
            df_day = df[df['Training Day'] == day]

            # Check if the button is a day button
            if "Day" in button.objectName():
                # Define the threshold for when a day is considered completely done
                day_button_complete_threshold = 7 if day in ["Day 1", "Day 13"] else 6

                if total_count >= day_button_complete_threshold:

                    # Check if there are any entries for the selected training day
                    if not df_day.empty:
                        # Extract the date of the last entry for the day
                        last_entry_date = df_day.iloc[-1]['Date']

                        # Convert date to desired format (e.g., "DD/MM - YY")
                        completion_date = pd.to_datetime(str(last_entry_date), format='%Y%m%d').strftime('%d/%m - %y')

                        # Update the button's text to include the completion date
                        button.setText(f"{day} ({completion_date})")
                        set_button_style(button, False, "green")
                elif video_count > 2 or image_count > 2:
                    # Logic for midway progress (before the day is complete but after significant progress)
                    set_button_style(button, True, "#CCAD00")
                    # Update the button's text to include the completion date
                    button.setText(f"{day}")
                else:
                    # Default style for when the day is neither complete nor at midway progress
                    button.setText(day)  # Reset the text to original without date
                    set_button_style(button, True)

        
            # Logic to show/hide and enable/disable the ecological video button
        if day == "Day 1":
            self.pb_ecologicalVideo.setVisible(True)
            if eco_count == 0 or None:

                self.pb_ecologicalVideo.setEnabled(True)
                self.pb_ecologicalVideo.setStyleSheet(u"QPushButton {\n"
                                                "    background-color: #555;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: #666;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: #444;\n"
                                                "}\n"
                                                "QPushButton:disabled {\n"
                                                "    background-color: #272727;\n"
                                                "}\n"
                                                )
                self.pb_VideoTraining_1.setEnabled(False)
                self.pb_VideoTraining_2.setEnabled(False)
                self.pb_VideoTraining_3.setEnabled(False)
                self.pb_ImageTraining_1.setEnabled(False)
                self.pb_ImageTraining_2.setEnabled(False)
                self.pb_ImageTraining_3.setEnabled(False)

            elif day == "Day 1":
                self.pb_ecologicalVideo.setEnabled(False)
                self.pb_ecologicalVideo.setStyleSheet("background-color: green")
        
        elif day == "Day 13" and total_count >= 6:
            self.pb_ecologicalVideo.setVisible(True)
            self.pb_ecologicalVideo.setEnabled(True)
            self.pb_ecologicalVideo.setStyleSheet(u"QPushButton {\n"
                                                "    background-color: #555;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: #666;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: #444;\n"
                                                "}\n"
                                                "QPushButton:disabled {\n"
                                                "    background-color: #272727;\n"
                                                "}\n"
                                                )
            if eco_count == 1:
                self.pb_ecologicalVideo.setEnabled(False)
                self.pb_ecologicalVideo.setStyleSheet("background-color: green")

        elif day == "Day 13":
            self.pb_ecologicalVideo.setVisible(True)
            self.pb_ecologicalVideo.setStyleSheet(u"QPushButton {\n"
                                                "    background-color: #555;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: #666;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed {\n"
                                                "    background-color: #444;\n"
                                                "}\n"
                                                "QPushButton:disabled {\n"
                                                "    background-color: #272727;\n"
                                                "}\n"
                                                )
            self.pb_ecologicalVideo.setEnabled(False)
        else: self.pb_ecologicalVideo.setVisible(False)

        # Enable or disable the undo button based on completion status
        # Ensure comparisons return Python booleans
        self.pb_Undo.setEnabled(bool(total_count > 0))

        # Disable start training if all trainings are complete
        self.pb_startTraining.setEnabled(bool(total_count < 6))
    
    
    
    def update_all_button_states(self):
        # Update the state for each day's button
        self.update_button_state(self.pb_Day1, "Day 1")
        #self.update_button_state(self.pb_Day2, "Day 2")
        self.update_button_state(self.pb_Day3, "Day 3")
        #self.update_button_state(self.pb_Day4, "Day 4")
        self.update_button_state(self.pb_Day5, "Day 5")
        #self.update_button_state(self.pb_Day6, "Day 6")
        self.update_button_state(self.pb_Day7, "Day 7")
        #self.update_button_state(self.pb_Day8, "Day 8")
        self.update_button_state(self.pb_Day9, "Day 9")
        #self.update_button_state(self.pb_Day10, "Day 10")
        self.update_button_state(self.pb_Day11, "Day 11")
        #self.update_button_state(self.pb_Day12, "Day 12")
        self.update_button_state(self.pb_Day13, "Day 13")
        #self.update_button_state(self.pb_Day14, "Day 14")
        self.update_button_state(self.pb_VideoTraining_1, self.current_day)
        self.update_button_state(self.pb_VideoTraining_2, self.current_day)
        self.update_button_state(self.pb_VideoTraining_3, self.current_day)
        self.update_button_state(self.pb_ImageTraining_1, self.current_day)
        self.update_button_state(self.pb_ImageTraining_2, self.current_day)
        self.update_button_state(self.pb_ImageTraining_3, self.current_day)
        self.update_button_state(self.pb_ecologicalVideo, self.current_day)
        self.pb_startTraining.setEnabled(False)

    def select_random_training_video(self):

        # Determine the base path and video folder path
        level_mapping = {
            "Day 1": "Video Training",
            "Day 3": "Video Training",
            "Day 5": "Video Training",
            "Day 7": "Video Training",
            "Day 9": "Video Training",
            "Day 11": "Video Training",
            "Day 13": "Video Training"
        }
        # Get the current day label text (e.g., "Day 1")
        current_day = self.page2_dayLabel.text()

        training_baseline_length = 45 # In seconds (s)
        
        level_folder = level_mapping.get(current_day, current_day)
        
        if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
            base_path = os.path.dirname(sys.executable)
            base_path = os.path.dirname(base_path)
            video_folder_path = os.path.join(base_path, level_folder)
            csv_path = os.path.join(base_path, "Training_log.csv")
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
            video_folder_path = os.path.join(base_path, "TrainingMedia", level_folder)
            csv_path = os.path.join(base_path, "TrainingMedia", "Training_log.csv")

        # Check if the CSV file exists; if it does, read the played videos
        played_videos = []
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            played_videos = [os.path.basename(training_path) for training_path in df[df['Training Day'] == current_day]['Training Media'].tolist()]

        # Get a list of all video files in the current day's folder
        video_files = [f for f in os.listdir(video_folder_path) if f.endswith('.mp4')]

        # Remove already played videos from the list
        video_files = [video for video in video_files if video not in played_videos]

        # Randomly select a video file
        selected_video = random.choice(video_files)

        # Store the full path to the selected video
        self.selected_training_path = os.path.join(video_folder_path, selected_video)

        # Store the chosen day in the JSON file
        self.update_json_file(current_day, self.selected_training_path, training_baseline_length)

        # Activates start-button after video has been chosen
        self.pb_startTraining.setEnabled(True)


    def select_training_image(self):

        current_day = self.page2_dayLabel.text()
        training_baseline_length = 45 # In seconds (s)


        # Define the image folder
        image_folder_name = "Image Training"

        if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
            base_path = os.path.dirname(sys.executable)
            base_path = os.path.dirname(base_path)
            image_folder_path = os.path.join(base_path, image_folder_name)
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
            image_folder_path = os.path.join(base_path, "TrainingMedia", image_folder_name)

        # Get a list of all image files in the folder
        image_files = [f for f in os.listdir(image_folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]


        # In the future, if you want to select a random image or implement any selection logic, you can modify here.
        # For now, we are just selecting the first image (or a specific one if you prefer).
        selected_image = image_files[0] if image_files else None

        if selected_image:
            # Store the full path to the selected image
            self.selected_training_path = os.path.join(image_folder_path, selected_image)
        else:
            print("No image files found in the directory.")
            self.selected_training_path = None
        
        # Store the chosen day in the JSON file
        self.update_json_file(current_day, self.selected_training_path, training_baseline_length)

        # Activates start-button after video has been chosen
        self.pb_startTraining.setEnabled(True)



    def play_ecological_video(self):
        # Define the path to the ecological video in the TrainingMedia folder
        if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
            base_path = os.path.dirname(sys.executable)
            base_path = os.path.dirname(base_path)
            ecological_training_path = os.path.join(base_path, "ecological_video.mp4")
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
            ecological_training_path = os.path.join(base_path, "TrainingMedia", "ecological_video.mp4")
        
        # Update the JSON file with the ecological video details
        current_day = self.page2_dayLabel.text()

        ecological_baseline_length = 500 # In seconds (s), big enough number to maintain baseline during whole ecological video duration (no NFB during ecological video = evaluation video, only background info recording)
        
        self.update_json_file(current_day, ecological_training_path, ecological_baseline_length )

        # Activates start-button after video has been chosen
        self.pb_startTraining.setEnabled(True)



    def is_training_complete(self, day):
        # Use the same base path logic as in the select_random_training_video function
        if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
            base_path = os.path.dirname(sys.executable)
            base_path = os.path.dirname(base_path)
            csv_path = os.path.join(base_path,"Training_log.csv")
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(base_path, "TrainingMedia", "Training_log.csv")

        
        # Check if the file exists; if not, return False immediately
        if not os.path.exists(csv_path):
            return 0,0,0
        
        # Read the csv file
        df = pd.read_csv(csv_path)

        # Check if 'Training Video' column exists
        if 'Training Media' not in df.columns:
            return 0, 0, 0
            
        # Check for the presence of the day's training based on the "Training Day" column
        training_entries = df[df['Training Day'] == day]

        # Check if training entries for the given day are present
        if training_entries.empty:
            # No entries for the given day, return 0 counts
            return 0, 0, 0

        # If entries are present, calculate counts
        video_count = training_entries['Training Media'].str.contains("Video Training").sum()
        eco_count = training_entries['Training Media'].str.contains("ecological_video").sum()
        image_count = training_entries['Training Media'].str.contains("Image Training").sum()
        
        # This checks if both videos have been played/trained with for the specific day
        return video_count, image_count, eco_count
    
    def update_ui_after_training(self):
        self.trainingCompleted.emit()

    
    def lost_connection_Muse2(self):
        self.lostConnectionMuse2.emit()

    def start_training(self):

        try:
            initialization()
            main_function(connection_lost_callback=self.lost_connection_Muse2, training_completed_callback=self.update_ui_after_training)

        except Exception as e:
            print(f'Error occurred while starting main.py: {e}')

    def start_fade_in(self):
        self.animation.setDirection(QPropertyAnimation.Forward)
        self.animation.start()
        self.animation.finished.connect(self.start_fade_out)

    def start_fade_out(self):
        self.animation.finished.disconnect(self.start_fade_out)  # Disconnect previous signal
        self.animation.setDirection(QPropertyAnimation.Backward)
        self.animation.start()
        self.animation.finished.connect(self.close_page)

    def close_page(self):
        self.animation.finished.disconnect(self.close_page)  # Disconnect the signal
        # Switch to another page in the QStackedWidget when the animation completes
        self.stackedWidget.setCurrentIndex(1)

####Running main interface#####
def run_ui():
    app = QApplication(sys.argv)
    main_win = Ui_MainWindow()
    main_win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    multiprocessing.freeze_support()
    run_ui()