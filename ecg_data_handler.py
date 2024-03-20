import wfdb
import os
import matplotlib.pyplot as plt
import numpy as np

class ECGDataHandler:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def read_ecg_record(self, record_name):
     
        record_path = os.path.join(self.data_dir, record_name)
        record = wfdb.rdrecord(record_path)
        return record

    def plot_ecg_lead(self, record, lead_name):
     
        if lead_name not in record.sig_name:
            raise ValueError(f"Lead {lead_name} not found in dataset.")

        lead_index = record.sig_name.index(lead_name)
        ecg_lead = record.p_signal[:, lead_index]

        plt.figure(figsize=(12, 4))
        plt.plot(ecg_lead)
        plt.title(f"ECG Lead {lead_name}")
        plt.xlabel("Time (Samples)")
        plt.ylabel("Amplitude")
        plt.show()

    @staticmethod
    def extract_features(record):
        
        average_amplitudes = {}
        for i, lead_name in enumerate(record.sig_name):
            # calculate avg ampl for single ecg
            average_amplitude = np.mean(record.p_signal[:, i])
            average_amplitudes[lead_name] = average_amplitude

        return average_amplitudes


