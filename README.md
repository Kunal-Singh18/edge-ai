# Motor Fault Detection using Edge AI

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/Kunal-Singh18/edge-ai)

## Overview  
This project leverages **Edge AI** for early detection of motor faults by analyzing **vibration signals** collected from an ADXL345 accelerometer sensor. A deep learning model is trained using Python and Keras, then optimized and deployed on an STM32F4 microcontroller for real-time inference at the edge, enabling efficient and low-latency fault detection without dependency on cloud services.

## Key Features  
- **Sensor Data Acquisition:** Real-time vibration data capture via I2C from the ADXL345 accelerometer sensor.  
- **Deep Learning Model Development:**  
  - Developed using Python and TensorFlow/Keras with the Sequential API.  
  - Model architecture designed for time-series vibration data classification.  
  - Trained on labeled datasets of normal and faulty motor states.  
- **Model Optimization:** Conversion of the Keras model to TensorFlow Lite or other embedded-friendly formats suitable for STM32 deployment.  
- **Edge Deployment:** Running optimized inference directly on STM32F4 microcontroller using embedded AI libraries.  
- **Signal Processing:** Filtering, normalization, and feature extraction implemented to improve model robustness.  
- **Real-Time Fault Detection:** Low-latency, on-device classification enabling immediate fault alerts.

## Tech Stack  
- Python, TensorFlow/Keras (Sequential API) for model training  
- STM32F4 microcontroller for embedded inference  
- ADXL345 accelerometer sensor for vibration data acquisition  
- Embedded C/C++ for microcontroller implementation