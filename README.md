This repository contains a Python package and a Jupyter notebook designed to work with 12-lead ECG data from https://physionet.org/content/ptb-xl/1.0.3/

The primary goal is to facilitate ECG data handling and classification of ECG signals. The ecg_data_handler.py module provides essential utilities for reading, plotting, and extracting features from ECG records,
while the 12LeadECGClassificationModel.ipynb notebook uses 4 fifferent classification model for ECG signals:

Temporal Convolutional Networks (TCN): Utilizes dilated convolutions for sequence processing, excellent for long-term dependencies in time series data.
Recurrent Neural Networks (RNN): Processes sequential data, maintaining a 'memory' of past inputs; ideal for context-sensitive tasks but struggles with long sequences.
Convolutional Neural Networks (CNN): Primarily for image processing, uses convolutional layers to automatically learn spatial hierarchies of features.
Inception Time (IT): Adapts the Inception architecture for time series, combining convolutional layers of varying sizes for multi-scale feature learning.

Contents
ecg_data_handler.py: A Python module that includes the ECGDataHandler class. This class provides methods for reading ECG records from a specified directory, plotting ECG leads, and extracting basic features such as average amplitudes for each lead.

12LeadECGClassificationModel.ipynb: A Jupyter notebook that demonstrates how to use the ECGDataHandler class for data preprocessing and feature extraction, followed by the training of a classification model on the processed ECG data.

Dependencies
Python 3.9: Ensure compatibility and leverage the latest features and improvements in Python's ecosystem.
WFDB: A library for reading and writing WFDB files, directly compatible with PhysioNet's ECG datasets.
Matplotlib: A comprehensive library for creating static, animated, and interactive visualizations in Python.
NumPy: A fundamental package for scientific computing with Python, used for efficient operations on multi-dimensional arrays and matrices.

