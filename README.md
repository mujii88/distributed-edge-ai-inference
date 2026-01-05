# distributed-edge-ai-inference


## Project Overview
This project implements a distributed Edge-AI inference system where lightweight edge devices stream data to a scalable backend that performs machine learning inference and synchronizes decisions in real time.


## Problem Statement
Edge devices such as IoT sensors or drones often lack the computational resources to run deep learning models locally. This project offloads inference to a backend service that processes streaming time-series data and detects anomalous behavior reliably and efficiently.

## Machine Learning Scope
- Data Type: Time-series sensor data
- Task: Anomaly detection
- Dataset: NASA CMAPSS (simulated streaming)
- Model: LSTM Autoencoder
- Inference Mode: Real-time

## High-Level Architecture
1. Edge Client simulates a lightweight device and streams sensor data.
2. Backend API receives data and performs ML inference.
3. Inference results are stored and synchronized.
4. Monitoring tracks latency, errors, and anomalies.
