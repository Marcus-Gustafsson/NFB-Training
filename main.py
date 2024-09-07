"""

Original Author: MÁTÉ KÁROLY TÓTH
Created within degree project: https://kth.diva-portal.org/smash/get/diva2:1773405/FULLTEXT01.pdf

Latest verison by: Marcus Gustafsson
Modified within degree project: TBA

"""


# cv2: A library for computer vision tasks, here it's mainly used for handling video frames.
import cv2

# numpy as np: A library for numerical operations, used for handling and manipulating arrays and mathematical operations.
import numpy as np

# time: A standard Python library for time-related tasks, it's used here to control the timing of various tasks like delays.
import time

# deque from collections: A deque (double-ended queue) is a data structure that allows you to add or remove elements from both ends efficiently. 
# Here it’s used to store and manipulate data efficiently.
from collections import deque

# multiprocessing as multiprocessing: This library is used for creating multiple processes allowing concurrent execution of tasks, 
# here it’s used to run data acquisition, processing, and visualization in parallel.
import multiprocessing

# Empty from queue: This is used to catch the exception when trying to read from an empty queue in multiprocessing.
from queue import Empty

# fft, fftfreq, ifft from scipy.fft: These functions are used for Fast Fourier Transform operations to analyze the frequency components of the EEG signal.
from scipy.fft import fft, fftfreq, ifft

# functions: This seems to be a custom module, possibly containing user-defined functions or other functionalities needed for the project.
from functions import storeMuse

# json: This library is used for handling JSON data. Here, it’s used to load configurations from a JSON file.
import json
import os
import sys
import datetime
import csv
import pyminizip

MUSE_SELECTED           = None
NEGATIVE_FEEDBACK       = None
FEEDBACK_ALG            = None
FREQUENCY_RANGE         = None
FEEDBACK_BUFFER_SIZE    = None
NUMBER_OF_SAMPLES       = None
SAMPLING_FREQUENCY      = None
BASELINE_LENGTH         = None
TRAINING_INPUT          = None
CHOSEN_DAY              = None



def log_training_video_to_csv(duration, training_psd_values, baseline_psd_values, shared_DN_values, datapoints_count, artifact_count, training_feedback_values):

    # Get the current date in YYYYMMDD format and time in HH:MM format
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    time_value = datetime.datetime.now().strftime("%H:%M")

    # Define the log filename
    if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
        base_path = os.path.dirname(sys.executable)  # Get the directory containing the .exe file
        base_path = os.path.dirname(base_path)  # Navigate one directory up to the TrainingMedia directory
        log_filename = os.path.join(base_path, "Training_log.csv")
    else:  # Running in a normal Python environment
        base_path = os.path.dirname(os.path.abspath(__file__))  # Get the directory containing the Python script
        log_filename = os.path.join("TrainingMedia", "Training_log.csv")

    # Compute statistics from training_psd_values
    if (datapoints_count != 0):
        non_artifact_data_percentage = round(1 - (artifact_count/datapoints_count),4)

    mean_psd_baseline = round(sum(baseline_psd_values) / len(baseline_psd_values), 3) if baseline_psd_values else 0
    # Convert the mean PSD from dB to uV^2/Hz

    mean_psd_Baseline_uV2_per_Hz = 10 ** (mean_psd_baseline / 10) if baseline_psd_values else 0
    # Round to two decimals
    mean_psd_Baseline_uV2_per_Hz = round(mean_psd_Baseline_uV2_per_Hz, 3) if mean_psd_Baseline_uV2_per_Hz else 0

    psd_STD_baseline = round(np.std(baseline_psd_values),3) if baseline_psd_values else 0
    # Convert the mean PSD from dB to uV^2/Hz
    psd_STD_baseline_uV2_per_Hz = 10 ** (psd_STD_baseline / 10) if psd_STD_baseline else 0
    # Round to two decimals
    psd_STD_baseline_uV2_per_Hz = round(psd_STD_baseline_uV2_per_Hz, 3) if psd_STD_baseline_uV2_per_Hz else 0

    mean_psd_training = round(sum(training_psd_values) / len(training_psd_values), 2) if training_psd_values else 0
    # Convert the mean PSD from dB to uV^2/Hz
    mean_psd_training_uV2_per_Hz = 10 ** (mean_psd_training / 10) if mean_psd_training else 0
    # Round to two decimals
    mean_psd_training_uV2_per_Hz = round(mean_psd_training_uV2_per_Hz, 3) if mean_psd_training_uV2_per_Hz else 0

    mean_psd_STD_training = round(np.std(training_psd_values),3) if training_psd_values else 0
    # Convert the mean PSD from dB to uV^2/Hz
    mean_psd_STD_training_uV2_per_Hz = 10 ** (mean_psd_STD_training / 10) if mean_psd_STD_training else 0
    # Round to two decimals
    mean_psd_STD_training_uV2_per_Hz = round(mean_psd_STD_training_uV2_per_Hz, 3) if mean_psd_STD_training_uV2_per_Hz else 0


    max_psd_training = round(max(training_psd_values), 3) if training_psd_values else 0
    # Convert the mean PSD from dB to uV^2/Hz
    max_psd_training_uV2_per_Hz = 10 ** (max_psd_training / 10) if max_psd_training else 0
    # Round to two decimals
    max_psd_training_uV2_per_Hz = round(max_psd_training_uV2_per_Hz, 3) if max_psd_training_uV2_per_Hz else 0

    min_psd_training = round(min(training_psd_values), 3) if training_psd_values else 0
    # Convert the mean PSD from dB to uV^2/Hz
    min_psd_training_uV2_per_Hz = 10 ** (min_psd_training / 10) if min_psd_training else 0
    # Round to two decimals
    min_psd_training_uV2_per_Hz = round(min_psd_training_uV2_per_Hz, 3) if min_psd_training_uV2_per_Hz else 0

    mean_feedback_value_training = round(sum(training_feedback_values) / len(training_feedback_values), 3) if training_feedback_values else 0

    # Loop through each index and value in the shared_DN_values list
    for index, dB_value in enumerate(shared_DN_values):
        # Check if the dB value is 0, directly set non_dB_value to 0
        if dB_value == 0:
            non_dB_value_rounded = 0
        else:
            # Convert the dB value to uV^2/Hz using the formula: 10^(dB_value/10)
            non_dB_value = 10 ** (dB_value / 10)
            # Round the converted value to two decimal places
            non_dB_value_rounded = round(non_dB_value, 3)
        
        # Update the list with the converted, rounded value
        shared_DN_values[index] = non_dB_value_rounded


    lower_bound_DN1 = round(shared_DN_values[0], 2)
    upper_bound_DN1 = round(shared_DN_values[1], 2)
    lower_bound_DN2 = round(shared_DN_values[2], 2)
    upper_bound_DN2 = round(shared_DN_values[3], 2)

    # Prepare the new data as a list
    new_row = [current_date, time_value, CHOSEN_DAY , TRAINING_INPUT, duration, mean_psd_Baseline_uV2_per_Hz, psd_STD_baseline_uV2_per_Hz, mean_feedback_value_training, mean_psd_training_uV2_per_Hz, mean_psd_STD_training_uV2_per_Hz, min_psd_training_uV2_per_Hz, max_psd_training_uV2_per_Hz, lower_bound_DN1, upper_bound_DN1, lower_bound_DN2, upper_bound_DN2, datapoints_count, artifact_count, non_artifact_data_percentage]

    # Check if the CSV file exists
    file_exists = os.path.exists(log_filename)

    with open(log_filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # If the file didn't exist, write the header first
        if not file_exists:
            writer.writerow(["Date", "Time", "Training Day", "Training Media", "Duration (seconds)", "Mean PSD from start to end of Baseline (uV^2/Hz)", "STD PSD from start to end of Baseline (uV^2/Hz)","Mean Feedback Value after baseline to end of training (1 <--> 0)"," Mean PSD after baseline to end of training (uV^2/Hz)", "STD PSD after baseline to end of training (uV^2/Hz)", "Min PSD (uV^2/Hz)", "Max PSD (uV^2/Hz)", "DR Lower Bound (after Baseline)", "DR Upper Bound (after Baseline)", "DR Lower Bound (At end of training)", "DR Upper Bound (At end of training)","Total amount datapoints (1 datapoint = One sample size of readings from one of the four sensor)", "Total amount artifacts detected (Atleast one artifact reading found in sample size of proccesed datapoint)", "Percentage artifact free datapoints"])

        # Write the new data
        writer.writerow(new_row)

def get_json_file_path():
    # Get the directory of the currently running script or executable
    exe_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(exe_dir, 'nfb_parameters.json')
    return json_file_path



def load_JSON():
    try:
        with open(json_file_path, 'r') as read_file:
            dct = json.load(read_file)
    
    # If the file 'nfb_parameters.json' is not found, execute the following block of code.
    except FileNotFoundError:

        dct= {
                "MUSE_SELECTED": True,
                "NEGATIVE_FEEDBACK": True,
                "FEEDBACK_ALG": True,
                "FREQUENCY_RANGE": [3.0 , 7.0],
                "FEEDBACK_BUFFER_SIZE": 16,
                "NUMBER_OF_SAMPLES": 512,
                "SAMPLING_FREQUENCY": 256,
                "BASELINE_LENGTH": 45, 
                "TRAINING_INPUT": "TrainingMedia\Video Training\Training_video_1.mp4",
                "CHOSEN_DAY" : "Day 1"
        }
    
    return dct


def get_JSON(dct):
        global MUSE_SELECTED, NEGATIVE_FEEDBACK, FEEDBACK_ALG, FREQUENCY_RANGE, FEEDBACK_BUFFER_SIZE, NUMBER_OF_SAMPLES, SAMPLING_FREQUENCY, BASELINE_LENGTH, TRAINING_INPUT, CHOSEN_DAY

        MUSE_SELECTED           = dct["MUSE_SELECTED"]
        NEGATIVE_FEEDBACK       = dct["NEGATIVE_FEEDBACK"]
        FEEDBACK_ALG            = dct["FEEDBACK_ALG"]
        FREQUENCY_RANGE         = dct["FREQUENCY_RANGE"]
        FEEDBACK_BUFFER_SIZE    = dct["FEEDBACK_BUFFER_SIZE"]
        NUMBER_OF_SAMPLES       = dct["NUMBER_OF_SAMPLES"]
        SAMPLING_FREQUENCY      = dct["SAMPLING_FREQUENCY"]
        BASELINE_LENGTH         = dct["BASELINE_LENGTH"]
        TRAINING_INPUT          = dct["TRAINING_INPUT"]
        CHOSEN_DAY              = dct["CHOSEN_DAY"]


def initialization():
    global json_file_path,muse_queue,nfb_queue,feedback_buffer,min1,max1,maxChange,dynRangeInc,dynRangeDec,mean_psd_db, MUSE2_SENSOR_TP9, MUSE2_SENSOR_AF7, MUSE2_SENSOR_AF8, MUSE2_SENSOR_TP10, DISPLAY_REFRESH_RATE,SAMPLING_INTERVAL, DN_CHANGE_ENABLE
    json_file_path = get_json_file_path()
    NFB_PARAMETERS = load_JSON()
    get_JSON(NFB_PARAMETERS)

    #---VARIABLES---
    SAMPLING_INTERVAL = 1.0 / SAMPLING_FREQUENCY
    DISPLAY_REFRESH_RATE = 16 #in Hz
    MUSE2_SENSOR_TP9 = 0
    MUSE2_SENSOR_AF7 = 1
    MUSE2_SENSOR_AF8 = 2
    MUSE2_SENSOR_TP10 = 3
    muse_queue = multiprocessing.Queue(5120)
    nfb_queue = multiprocessing.Queue(5120)
    feedback_buffer = deque(16*[0], 16)
    min1 = NUMBER_OF_SAMPLES
    max1 = 0.0
    DN_CHANGE_ENABLE = True #enable / disable dynamic range change during feedback phase

    maxChange= 0.05
    dynRangeInc = 0.0333
    dynRangeDec= 0.01

    mean_psd_db = 0.0

initialization()

def calcFeedBack(mean_psd_dB, dynRange, feedbackVal):
    """
    Calculate the feedback value based on the input mean PSD in dB, dynamic range, and previous feedback value.
    
    Parameters:
    mean_psd_dB (float): The mean power spectral density value in dB for the current time window.
    dynRange (list): A list containing two float values representing the current dynamic range [lower bound, upper bound].
    feedbackVal (float): The previous feedback value, used to smooth the transition between feedback values.

    Returns:
    newDynRange (list): Updated dynamic range [lower bound, upper bound].
    feedbackVal (float): Updated feedback value, calculated based on the current mean PSD and dynamic range.

    The function works as follows:
    1. Calculate the total range of the dynamic range.
    2. Normalize the mean PSD value to be within the range of 0 to 1.
    3. Adjust the dynamic range and feedback value based on the normalized mean PSD.
    4. Ensure that the feedback value changes smoothly, avoiding large jumps.
    5. Return the updated dynamic range and feedback value.
    """
    totalRange = dynRange[1]-dynRange[0]
    feedbackValTmp = (mean_psd_dB - dynRange[0]) / totalRange

    # Adjust upper bound of dynamic range
    if feedbackValTmp > 1:
        drU = dynRange[1] + dynRangeInc * totalRange
        feedbackValTmp = 1
    else:
        drU = dynRange[1] - dynRangeDec * totalRange
        
    # Adjust lower bound of dynamic range
    if feedbackValTmp < 0:
        drL = dynRange[0] - dynRangeInc * totalRange
        feedbackValTmp = 0
    else:
        drL = dynRange[0] + dynRangeDec * totalRange

    # Smooth transition of feedback value
    if feedbackValTmp < feedbackVal:
        if abs(feedbackValTmp - feedbackVal) > maxChange:
            feedbackVal -= maxChange
        else:
            feedbackVal = feedbackValTmp
    else:
        if abs(feedbackValTmp - feedbackVal) > maxChange:
            feedbackVal += maxChange
        else:
            feedbackVal = feedbackValTmp

    newDynRange = [drL, drU]
    return newDynRange, feedbackVal



def determineFreq(specFreq, brainwave_freq_band, round_down=True):
    """
    Determine the frequency indices corresponding to a specified brainwave frequency band.
    
    Parameters:
    specFreq (numpy array): Array of frequency values.
    brainwave_freq_band (list or tuple): A pair of values specifying the lower and upper bounds of the brainwave frequency band.
    round_down (bool, optional): If True, round the frequency bounds down to ensure the specified band is fully included. Default is True.
    
    Returns:
    lower_idx (int): Index of the lower bound of the frequency band in 'specFreq'.
    upper_idx (int): Index of the upper bound of the frequency band in 'specFreq'.
    """
    # Find the index in 'specFreq' closest to the lower bound of the brainwave frequency band
    lower_idx = np.argmin(np.abs(specFreq - brainwave_freq_band[0]))
    # Find the index in 'specFreq' closest to the upper bound of the brainwave frequency band
    upper_idx = np.argmin(np.abs(specFreq - brainwave_freq_band[1]))
    
    # Adjust the indices based on the 'round_down' parameter
    if round_down:
        # If rounding down, adjust indices to ensure the specified frequency band is fully included
        if specFreq[lower_idx] > brainwave_freq_band[0] and lower_idx > 0:
            lower_idx -= 1
        if specFreq[upper_idx] < brainwave_freq_band[1] and upper_idx < len(specFreq) - 1:
            upper_idx += 1
    else:
        # If not rounding down, adjust indices to exclude frequencies outside the specified band
        if specFreq[lower_idx] < brainwave_freq_band[0] and lower_idx < len(specFreq) - 1:
            lower_idx += 1
        if specFreq[upper_idx] > brainwave_freq_band[1] and upper_idx > 0:
            upper_idx -= 1
    
    # Return the adjusted indices
    return lower_idx, upper_idx


def meanPowerSpectralDensity(lowerBound, upperBound, w_amp, w_freq):
    """
    Calculate the mean Power Spectral Density (PSD) in decibels (dB) within a specified frequency range.
    
    Parameters:
    lowerBound (float): The lower bound of the frequency range (in Hz).
    upperBound (float): The upper bound of the frequency range (in Hz).
    w_amp (numpy array): The amplitude spectrum of the signal.
    w_freq (numpy array): The frequency values corresponding to the amplitude spectrum.
    
    Returns:
    mean_psd_db (float): The mean Power Spectral Density (in dB) within the specified frequency range.
    
    Raises:
    ValueError: If the lower or upper bound values are invalid, or if the amplitude and frequency arrays are not of the same length.
    ValueError: If any frequency value within the specified range is less than or equal to zero.
    """
    # Check if the lower and upper bounds are valid
    if lowerBound < 0 or upperBound >= len(w_freq) or lowerBound > upperBound:
        raise ValueError("Invalid lower or upper bound values.")
    
    # Check if the amplitude and frequency arrays are of the same length
    if len(w_amp) != len(w_freq):
        raise ValueError("Amplitude and frequency arrays must be of the same length.")

    # Find the indices corresponding to the lower and upper frequency bounds
    lower_idx = np.argmin(np.abs(w_freq - lowerBound))
    upper_idx = np.argmin(np.abs(w_freq - upperBound))
    
    # Extract the amplitude and frequency values within the specified range
    amp = w_amp[lower_idx:upper_idx+1]
    freq = w_freq[lower_idx:upper_idx+1]

    # Calculate the Power Spectrum (uV^2)
    ps = amp * amp

    # Ensure that all frequency values are strictly positive to avoid division by zero
    if any(freq <= 0):
        raise ValueError("Frequency values must be strictly positive for PSD calculation.")
    
    # Calculate the Power Spectral Density (PSD) in uV^2/Hz
    psd = ps / freq
    
    # Add a small constant to PSD values to avoid log(0)
    psd += 1e-10
    
    # Convert the PSD values to decibels (dB)
    psd_db = 10 * np.log10(psd)
    
    # Calculate the mean PSD value in dB
    mean_psd_db = np.mean(psd_db)
    
    return mean_psd_db


def calcSpectrum(fft_data_result, phaseBool=True, oneSidedBool=True):
    """
    Calculate the amplitude spectrum of a signal, and optionally its phase spectrum.
    
    Parameters:
    fft_data_result (numpy array): Complex values representing the Fourier Transform of a signal.
    phaseBool (bool, optional): If True, calculate and return the phase spectrum. Default is True.
    oneSidedBool (bool, optional): If True, return a one-sided spectrum for real input signals. Default is True.
    
    Returns:
    amp (numpy array): The amplitude spectrum of the input data.
    phase (numpy array, optional): The phase spectrum of the input data, returned if phaseBool is True.
    """
    # Calculate the amplitude spectrum and normalize it by the number of samples
    amp = np.abs(fft_data_result) / len(fft_data_result)
    
    # If one-sided spectrum is requested and the input is real, return only the positive frequency part
    if oneSidedBool:
        # Double the amplitude values (except for the DC component) to conserve energy
        amp = amp[:len(amp)//2] * 2
        amp[0] /= 2  # The DC component should not be doubled
        
    # If phase information is requested, calculate the phase spectrum
    if phaseBool:
        phase = np.angle(fft_data_result)
        # If one-sided spectrum is requested, return only the positive frequency part of the phase spectrum
        if oneSidedBool:
            phase = phase[:len(phase)//2]
        # Return both amplitude and phase spectra
        return amp, phase
    else:
        # If phase information is not requested, return only the amplitude spectrum
        return amp


def backup_training_log():
    # Determine the base path based on the execution context
    if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
        base_path = os.path.dirname(sys.executable)
        base_path = os.path.dirname(base_path)
        # Define the paths for the original log and the backup directory within "TrainingMedia"
        training_log_path = os.path.join(base_path, "Training_log.csv")
        backup_folder_path = os.path.join(base_path, "Backups")
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        training_log_path = os.path.join(base_path, "TrainingMedia", "Training_log.csv")
        backup_folder_path = os.path.join(base_path, "TrainingMedia", "Backups")

    # Ensure the backup folder exists, create if it doesn't
    if not os.path.exists(backup_folder_path):
        os.makedirs(backup_folder_path)

    # Define the path for the password-protected ZIP file
    zip_file_name = "Training_log_backup.zip"
    zip_file_path = os.path.join(backup_folder_path, zip_file_name)

    # Password for the ZIP file
    password = 'no_secrets_here'

    # Compress and password-protect the original log file directly into a ZIP archive
    pyminizip.compress(training_log_path, None, zip_file_path, password, 0)

    print(f"Password-protected backup created at: {zip_file_path} with password: {password}")

# Function to process the EEG data, calculate the power spectral density (PSD), and determine the feedback value.
def dataProcessing(muse_queue, nfb_queue, training_psd_values, baseline_psd_values, shared_DN_values, selected_sensors, artifact_count, datapoints_count, training_feedback_values):

    # Sensor index to name mapping
    if(len(selected_sensors) == 4):
        sensor_names = {
            0: "TP9",
            1: "AF7",
            2: "AF8",
            3: "TP10"
        }
    else:
        sensor_names = {
            0: "AF7",
            1: "AF8"
        }

    

    def artifacts_checking(signal, positive_threshold=250, negative_threshold=-250):
        """
        Check for artifacts in the signal.

        Parameters:
        signal (numpy array): The EEG signal from a single sensor.
        positive_threshold (float): The positive amplitude threshold to identify artifacts.
        negative_threshold (float): The negative amplitude threshold to identify artifacts.

        Returns:
        numpy array: The EEG signal, filtered if artifacts are detected.
        """

        # Create a copy of the signal array
        signal_copy = np.copy(signal)

        # Check for any artifacts in the signal
        if np.any(signal > positive_threshold) or np.any(signal < negative_threshold):
            artifact_count.value += 1
            signal_copy = filter_artifacts(signal_copy, positive_threshold, negative_threshold)
        
        return signal_copy

    def filter_artifacts(signal_copy, positive_threshold, negative_threshold):
        """
        Filter out artifacts from the signal by replacing them with the nearest valid value.

        Parameters:
        signal (numpy array): The EEG signal from a single sensor.
        positive_threshold (float): The positive amplitude threshold to identify artifacts.
        negative_threshold (float): The negative amplitude threshold to identify artifacts.

        Returns:
        numpy array: The filtered EEG signal.
        """
        for i, value in enumerate(signal_copy):
            if value > positive_threshold or value < negative_threshold:
                nearest_valid_index = find_nearest_valid_index(signal_copy, i, positive_threshold, negative_threshold)
                if nearest_valid_index != -1:
                    signal_copy[i] = signal_copy[nearest_valid_index]
                else:
                    replacement_value = -100 if value < negative_threshold else 25
                    signal_copy[i] = replacement_value
            
        return signal_copy

    def find_nearest_valid_index(signal_copy, artifact_index, positive_threshold, negative_threshold):
        """
        Find the index of the nearest valid value in the signal that does not exceed thresholds.

        Parameters:
        signal (numpy array): The EEG signal.
        artifact_index (int): Index of the artifact in the signal.
        positive_threshold (float): The positive amplitude threshold.
        negative_threshold (float): The negative amplitude threshold.

        Returns:
        int: The index of the nearest valid value.
        """
        left = right = artifact_index

        while left >= 0 or right < len(signal_copy):
            if left >= 0 and not (signal_copy[left] > positive_threshold or signal_copy[left] < negative_threshold):
                return left
            if right < len(signal_copy) and not (signal_copy[right] > positive_threshold or signal_copy[right] < negative_threshold):
                return right
            left -= 1
            right += 1

        return -1  # Indicating no valid index found


    BaselineBool = True  # Boolean variable to determine whether the baseline period is active or not¨
    t_end = time.time() + BASELINE_LENGTH  # Calculate the end time of the baseline period


    FB1 = 0.5  # Initial feedback value
    DN1 = [-5, 5]  # Initial dynamic range
    DN2 = [0 , 0]
    feedbackValue = 0  # Initial feedback value
     
    sensor_buffers = {sensor: deque(NUMBER_OF_SAMPLES*[0], NUMBER_OF_SAMPLES) for sensor in selected_sensors}

    if TRAINING_INPUT.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):  # Add all video formats you want to support
        is_video = True
    elif TRAINING_INPUT.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):  # Add all image formats you want to support
        is_video = False
    else:
        return

    while True:  # Infinite loop to continuously process incoming EEG data
        new_data_available = False  # Initialize a flag to check whether there is new data to process or not
        try:
            result = muse_queue.get_nowait()  # Try to get new EEG data from the queue 'muse_queue' without waiting
            new_data_available = True
        except Empty:  # If the queue is empty, pass
            pass
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
        
        if new_data_available:
            #print(f"Datapoints count = {datapoints_count}")
            all_sensor_data = [np.array(result[sensors]) for sensors in selected_sensors]

            meanPSDs = []
            for sensor_index, sensor_data in enumerate(all_sensor_data):
                # Increment datapoints_count for each new data point
                datapoints_count.value += 1
                # Apply artifact filtering to the sensor data
                artifacted_checked_data = artifacts_checking(sensor_data)
                sensor = selected_sensors[sensor_index]
                sensor_buffers[sensor].extendleft(artifacted_checked_data)
                output = np.array(sensor_buffers[sensor])
                output = np.reshape(output, (NUMBER_OF_SAMPLES,), 'C')
                preprocessedData = output.astype(float)
                # Frequency spectrum calculation
                specFreq = np.fft.fftfreq(NUMBER_OF_SAMPLES, SAMPLING_INTERVAL)[:NUMBER_OF_SAMPLES//2]
                fft_result = fft(preprocessedData)
                ampSpectrum = calcSpectrum(fft_result, False, True)
                ampSpectrum = ampSpectrum[:len(specFreq)]
                lb, ub = determineFreq(specFreq, FREQUENCY_RANGE)
                meanPSD = meanPowerSpectralDensity(lb, ub, ampSpectrum, specFreq)

                if not np.isnan(meanPSD):
                    meanPSDs.append(meanPSD)
                    
            average_PSD = np.mean(meanPSDs) if meanPSDs else np.nan
   
            if BaselineBool:  # If the baseline period is active
                if FEEDBACK_ALG:  # If feedback algorithm is selected
                    if not np.isnan(average_PSD): 
                        baseline_psd_values.append(average_PSD)
                        DN1, FB1 = calcFeedBack(average_PSD, DN1, FB1)
                    
                    if is_video == False:
                        feedbackValue = 0.0  # Assign a constant feedback value during the baseline period
                    else: feedbackValue = 0.5
                    
                    if time.time() >= t_end:  # If the current time has reached the end of the baseline period
                        BaselineBool = False  # Set the baseline period to inactive
                        print("DBG: BaseLine done...")
                        shared_DN_values[0] = DN1[0]
                        shared_DN_values[1] = DN1[1]

            else:  # If the baseline period is not active
                if FEEDBACK_ALG:  # If feedback algorithm is selected
                    if not np.isnan(average_PSD):
                        training_psd_values.append(average_PSD)
                        DN2, FB1 = calcFeedBack(average_PSD, DN1, FB1)

                    if DN_CHANGE_ENABLE and BaselineBool:
                        DN1 = DN2

                    feedbackValue = FB1
                    training_feedback_values.append(feedbackValue)

                    shared_DN_values[2] = DN2[0]
                    shared_DN_values[3] = DN2[1]
                
            if (BASELINE_LENGTH > 30):
                shared_DN_values[0] = DN1[0]
                shared_DN_values[1] = DN1[1]
            nfb_queue.put(feedbackValue)  # Put the determined feedback value into the 'nfb_queue' queue
            new_data_available = False  # Reset the flag to check whether there is new data to process or not


def visual(nfb_queue, training_psd_values, baseline_psd_values, shared_DN_values, visual_queue, no_connection_or_artifacts_or_sample_rate_event, artifact_count, datapoints_count, training_feedback_values):

    def handle_training_completion(start_time, training_psd_values, baseline_psd_values, shared_DN_values, datapoints_count, artifact_count, visual_queue, training_feedback_values):
        print("DBG: Training completed....")
        end_time = time.time()  # Capture the end time
        duration = int(end_time - start_time)  # Compute the duration in seconds
        log_training_video_to_csv(duration, training_psd_values, baseline_psd_values, shared_DN_values, datapoints_count, artifact_count, training_feedback_values)  # Call the logging function
        visual_queue.put("completed")

    
    def pixelate_image(image, feedback_val, min_pixelation=50, max_pixelation=750):
        """
        Pixelates the image based on the feedback value.
        :param image: Input image to be pixelated
        :param feedback_val: EEG feedback value (0 to 1), where 0 is highly pixelated and 1 is clear
        :param min_pixelation: Maximum pixelation (blurred) for feedback_val = 0
        :param max_pixelation: Minimum pixelation (clear) for feedback_val = 1
        :return: Tuple containing the pixelated image and the pixelation level
        """


        """
        Imagine you have an image that's 1000 pixels wide. If you set min_pixelation to 10, it means that when feedback_val is 0, the image will be resized down to 10 pixels wide and then blown back up to its original size, making it very blocky. 
        If max_pixelation is set to 500, it means that when feedback_val is 1, the image will be resized down to 500 pixels wide and then blown back up, which should still look relatively clear.

        Here's a step-by-step example of how the pixelation changes with feedback_val:

        When feedback_val = 1 (no pixelation wanted), pixelation_level will be set to 500 (your max_pixelation value). 
        Your image will be resized down to 500 pixels wide and then back up, looking fairly clear.

        When feedback_val = 0.5 (medium pixelation), the pixelation_level will be calculated to be halfway between 500 and 10, which is 255. 
        Your image will be resized down to 255 pixels wide and then back up, looking somewhat pixelated.

        When feedback_val = 0 (full pixelation), pixelation_level will be set to 10 (your min_pixelation value). 
        Your image will be resized down to 10 pixels wide and then back up, looking very blocky and pixelated.
                
        
        """

        pixelation_level = int((1 - feedback_val) * (max_pixelation - min_pixelation) + min_pixelation)
        pixelation_level = max(min_pixelation, min(pixelation_level, max_pixelation))  # Add constraints

        # Calculate the percentage
        pixelation_percentage = ((pixelation_level - min_pixelation) / (max_pixelation - min_pixelation)) * 100

        # Prevent division by zero or too small pixelation level
        pixelation_level = max(pixelation_level, 1)

        # Pixelate the image
        height, width = image.shape[:2]
        # Ensure the pixelation level does not exceed image dimensions
        pixelation_level = min(pixelation_level, height, width)
        small = cv2.resize(image, (pixelation_level, pixelation_level), interpolation=cv2.INTER_LINEAR)
        pixelated_image = cv2.resize(small, (width, height), interpolation=cv2.INTER_NEAREST)
        
        return pixelated_image, pixelation_percentage
    

    if TRAINING_INPUT.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):  # Add all video formats that should be supported
        is_video = True
        cap = cv2.VideoCapture(TRAINING_INPUT)
        # Optional: Choose a start frame, or set to 0 to start from the beginning
        START_FRAME = 0

        cap.set(cv2.CAP_PROP_POS_FRAMES, START_FRAME)

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        END_FRAME = total_frames - 1
        # Define desired buffer size (e.g., 200 frames)
        BUFFER_SIZE = 200
        cap.set(cv2.CAP_PROP_BUFFERSIZE, BUFFER_SIZE)

        if (cap.isOpened()== False):
            print("Video could not be opened.")
    elif TRAINING_INPUT.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):  # Add all image formats that should be supported
        is_video = False
        # Load the image to be pixelated
        Training_image = cv2.imread(TRAINING_INPUT)
        if Training_image is None and is_video == False:
            print("Error: Image not found.")
            exit()
    else:
        print("DBG: Unsupported training input format.")
        return

    start_time = time.time()  # Capture the start time

    
    """ LUT =  { #66ms for 12fps, 14ms for 32 fps, 4ms for 64 fps
        1: 4, # 63 fps
        2: 4, # 63 fps
        3: 4, # 63 fps
        4: 14, # 32 fps
        5: 14, # 32 fps
        6: 14,  # 32 fps
        7: 14,  # 32 fps
        8: 14,  # 32 fps
        9: 14,  # 32 fps
        10: 14, # 32 fps
        11: 14,  # 32 fps
        12: 14,  # 32 fps
        13: 66,  # 12 fps
        14: 66,  # 12 fps
        15: 66   # 12 fps
        ,} """
    
    LUT =  { #66ms for 12fps, 14ms for 32 fps, 4ms for 64 fps
        1: 66, # 12 fps
        2: 66, # 12 fps
        3: 66, # 12 fps
        4: 66, # 12 fps
        5: 14, # 32 fps
        6: 14,  # 32 fps
        7: 14,  # 32 fps
        8: 14,  # 32 fps
        9: 14,  # 32 fps
        10: 14, # 32 fps
        11: 14,  # 32 fps
        12: 4,  # 63 fps
        13: 4,  # 63 fps
        14: 4,  # 63 fps
        15: 4   # 63 fps
        ,}

    prev_frame_time = 0
    new_frame_time = 0


    if is_video:
        FBVal = 0.5
        frameTime = 14
    else: FBVal = 0

    N_FRAMES = 10  # average over N frames
    fps_values = [0] * N_FRAMES  # initialize a list with N zeros
    fps_index = 0

    ema_FB = None
    # Slow EMA
    alpha = 0.085

    # Smoothing factor; values closer to 1 make the transition smoother
    SMOOTHING_FACTOR = 0.95

    # Initialize a variable to track when the percentage first drops below 70%
    threshold_drop_time = None

    # Create a full-screen window
    cv2.namedWindow('NFB Training', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('NFB Training', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    loop_start_time = time.time()  # Start the timer
    while True:

        # Calculate elapsed time
        loop_elapsed_time = time.time() - loop_start_time

        try:
            result=nfb_queue.get_nowait()
        except Empty:
            pass
        else:
            FBVal = result

        if ema_FB is None:
            ema_FB = FBVal
        else:
            ema_FB = (FBVal * alpha) + (ema_FB * (1 - alpha))

        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        if is_video == True:

            if cap.isOpened:

                ret, frame = cap.read()
                currentFrame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                LV = round((ema_FB * 93.33 + 6.67) / 6.67)
                frameTime = SMOOTHING_FACTOR * frameTime + (1 - SMOOTHING_FACTOR) * LUT[LV]
                if ret == True:

                    font = cv2.FONT_HERSHEY_SIMPLEX
                    new_frame_time = time.perf_counter()  # Changed from time.time()
                    current_fps = 1 / (new_frame_time - prev_frame_time)
                    prev_frame_time = new_frame_time
                    fps_values[fps_index] = current_fps
                    fps_index = (fps_index + 1) % N_FRAMES
                    avg_fps = sum(fps_values) / N_FRAMES
                    int_fps = int(avg_fps)
                    str_fps = str(int_fps)
                    cv2.putText(frame, "Press 'Q' to exit", (7, 30), font, 1, (0, 215, 255), 2, cv2.LINE_AA)
                    cv2.putText(frame, f"Feedback value = {round(ema_FB,2)}", (7, 65), font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
                    cv2.putText(frame, f"Elapsed time = {round(loop_elapsed_time,2)}", (7, 95), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.imshow('NFB Training', frame) #fullscreen w/o resizing

                    key_pressed = cv2.waitKey(round(frameTime)) & 0xFF
                    if chr(key_pressed).lower() == 'q':
                        break
                    if loop_elapsed_time > 105 or currentFrame == END_FRAME or ret == False:
                        handle_training_completion(start_time, training_psd_values, baseline_psd_values, shared_DN_values,datapoints_count.value,artifact_count.value, visual_queue, training_feedback_values)
                        backup_training_log()
                        cap.release()
                        cv2.destroyAllWindows()
                        break

        else:
            # Apply pixelation based on the feedback value
            pixelated_image, pixelation_percentage = pixelate_image(Training_image, ema_FB)
            cv2.putText(pixelated_image, "Press 'Q' to exit", (7, 35), font, 1.5, (0, 215, 255), 2, cv2.LINE_AA)
            cv2.putText(pixelated_image, f"Feedback value = {round(ema_FB,2)}", (7, 70), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(pixelated_image, f"Elapsed time = {round(loop_elapsed_time,2)}", (7, 100), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.imshow('NFB Training', pixelated_image)

            # Check if the set duration has passed
            key_pressed = cv2.waitKey(14) & 0xFF
            if chr(key_pressed).lower() == 'q': 
                cv2.destroyAllWindows()
                break

            if loop_elapsed_time > 105: # Set duration in seconds
                handle_training_completion(start_time, training_psd_values, baseline_psd_values, shared_DN_values,datapoints_count.value,artifact_count.value, visual_queue, training_feedback_values)
                backup_training_log()
                cv2.destroyAllWindows()
                break

        if datapoints_count.value != 0:
            non_artifact_data_percentage = round(1 - (artifact_count.value / datapoints_count.value), 4)

            if non_artifact_data_percentage < 0.70 and time.time() - start_time > 10:
                # Record the time when percentage first drops below 70%
                if threshold_drop_time is None:
                    threshold_drop_time = time.time()
                print(f"Seconds below 70% = {time.time() - threshold_drop_time}")
                # Check if it's been below 70% for more than 5 seconds
                if time.time() - threshold_drop_time >= 5:
                    no_connection_or_artifacts_or_sample_rate_event.set()
            
        if no_connection_or_artifacts_or_sample_rate_event.is_set():
            print("DBG: Exiting due to lost connection/artifact setpoint/sample rate issues.")
            if is_video:
                cap.release()
            cv2.destroyAllWindows()
            return  # Exit the function



def main_function(connection_lost_callback=None, training_completed_callback=None):
    try:
        # Create the event for connection loss detection
        no_connection_or_artifacts_or_sample_rate_event = multiprocessing.Event()

        if MUSE_SELECTED:
            selected_sensors = [MUSE2_SENSOR_AF7, MUSE2_SENSOR_AF8]  # using AF7 and AF8
            #selected_sensors = [MUSE2_SENSOR_TP9, MUSE2_SENSOR_AF7, MUSE2_SENSOR_AF8, MUSE2_SENSOR_TP10]  # All sensors
            sample_rate = 256 # in Hz

            # Pass the list of selected sensors to the storeMuse function
            dataAcqP = multiprocessing.Process(target=storeMuse, args=(muse_queue,no_connection_or_artifacts_or_sample_rate_event, sample_rate, selected_sensors))
        

        # Create a Manager object to manage shared variables
        manager = multiprocessing.Manager()

        # Shared list to store psd values
        training_psd_values = manager.list()
        # Shared list to store psd values
        training_feedback_values = manager.list()
        # Shared list to store psd values
        baseline_psd_values = manager.list()

        artifact_count = manager.Value('i', 0)  # Shared integer, initialized to 0
        datapoints_count = manager.Value('i', 0)  # Shared integer, initialized to 0


        # Shared value to store DN1 when BaselineBool is set to False. 
        shared_DN_values = manager.list([0.0, 0.0, 0.0, 0.0])  # Initialize with [lowerBound, upperBound] for both baseLine and after training results

        dataAcqP.start()

        calcP = multiprocessing.Process(target=dataProcessing, args=(muse_queue, nfb_queue, training_psd_values, baseline_psd_values, shared_DN_values, selected_sensors, artifact_count, datapoints_count, training_feedback_values))
        calcP.start()

        """ calcP = multiprocessing.Process(target=dataProcessing, args=(muse_queue, nfb_queue, training_psd_values, baseline_psd_values, shared_DN_values, selected_sensors))
        calcP.start() """

        # Create a new queue for communication
        visual_queue = multiprocessing.Queue()

        visualP = multiprocessing.Process(target=visual, args=(nfb_queue, training_psd_values, baseline_psd_values, shared_DN_values, visual_queue, no_connection_or_artifacts_or_sample_rate_event,artifact_count, datapoints_count, training_feedback_values))
        visualP.start()

        # Wait for the visualP process to finish
        visualP.join()

        if no_connection_or_artifacts_or_sample_rate_event.is_set():
            print("DBG: Connection to the Muse2 headband was lost.")
            if connection_lost_callback:
                connection_lost_callback()  # Call the connection lost callback

        # Once visualP is done, check for the completed message
        while not visual_queue.empty():
            message = visual_queue.get()
            if message == "completed" and training_completed_callback:
                training_completed_callback()  # Call the training completed callback

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Properly terminate and join all processes
        dataAcqP.terminate()
        dataAcqP.join()

        calcP.terminate()
        calcP.join()

        visualP.terminate()
        visualP.join()



if __name__ == '__main__':
    multiprocessing.freeze_support()
    main_function()
