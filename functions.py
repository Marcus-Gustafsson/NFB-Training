from pylsl import StreamInlet, resolve_stream
import time

# Information can be found at: https://mind-monitor.com/FAQ.php#oscspec
MUSE2_SENSOR_TP9 = 0
MUSE2_SENSOR_AF7 = 1
MUSE2_SENSOR_AF8 = 2
MUSE2_SENSOR_TP10 = 3

def storeMuse(queue, no_connection_or_artifacts_or_sample_rate_event, sample_rate=256, sensor_indices=[MUSE2_SENSOR_AF7, MUSE2_SENSOR_AF8], buffer_size=16, startup_delay = 1):
    
    """ 
    Store EEG data from Muse2 device in a queue.

    :param queue: Queue to store the EEG data.
    :param no_connection_or_artifacts_or_sample_rate_event: Event to signal that no connection has been made/connection to Muse2 has been lost.
    :param sample_rate: Sampling rate of the EEG device.
    :param sensor_indices: List of indices of the EEG sensors to store.
    :param buffer_size: Size of the buffer to store before putting in the queue.
    :param startup_delay: Time delay to let hardware to start streaming correctly 
    
    """
    
    no_connection_or_artifacts_or_sample_rate_event.set() # Assume no connection until a EEG stream has been resolved
    streams = resolve_stream('type', 'EEG')
    if(len(streams) != 0):
        no_connection_or_artifacts_or_sample_rate_event.clear() # Connection has been established
    inlet = StreamInlet(streams[0])
    tempBuffer = {sensor: [] for sensor in sensor_indices}
    sample_interval = 1 / sample_rate


    # Sampling rate check variables
    sample_count = 0
    start_time = None
    check_interval = 100  
    out_of_range_start_time = None  
    out_of_range_duration = 5.0  

    # Wait for a brief period to allow the stream to establish before starting to pull samples
    time.sleep(startup_delay)
    last_sample_time = time.time() 
    connection_timeout = 2.0  # Consider the connection lost after 2 second without data
    
    while True:
        try:
            sample, timestamp = inlet.pull_sample(timeout=sample_interval * 1.1)
            if sample is not None and timestamp is not None:
                if start_time is None:
                    start_time = timestamp  # Start time of the first sample
                
                last_sample_time = time.time()
                sample_count += 1

                for sensor in sensor_indices:
                    tempBuffer[sensor].append(sample[sensor])
                    
                if all(len(buffer) >= buffer_size for buffer in tempBuffer.values()):
                    sensor_data = {sensor: tempBuffer[sensor] for sensor in sensor_indices}
                    queue.put(sensor_data)
                    tempBuffer = {sensor: [] for sensor in sensor_indices}
                
                if sample_count >= check_interval:
                    elapsed_time = timestamp - start_time
                    actual_sample_rate = sample_count / elapsed_time

                    # Check if the actual sample rate is out of the acceptable range
                    if actual_sample_rate < 240 or actual_sample_rate > 270:
                        if out_of_range_start_time is None:
                            out_of_range_start_time = time.time()
                        elif time.time() - out_of_range_start_time > out_of_range_duration:
                            print(f"DBG: Sample rate out of acceptable range for longer than {out_of_range_duration}s, exiting...")
                            no_connection_or_artifacts_or_sample_rate_event.set()
                            break
                    else:
                        out_of_range_start_time = None

                    sample_count = 0
                    start_time = timestamp

            # If a significant time has passed since the last sample, consider the connection lost
            if (time.time() - last_sample_time) > connection_timeout:
                no_connection_or_artifacts_or_sample_rate_event.set()
                break  # Break out of the loop if the connection is lost
                    
        except IndexError:
            print("Received a sample with an unexpected format or insufficient channels.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")