# Constructing-a-Water-Quality-Index
This repository contains the project Construction of a Water Quality Index, developed as part of an undergraduate course project at the Indian Institute of Technology Kanpur. The project introduces a comprehensive Water Quality Index (WQI) tailored for India, combining machine learning and environmental science to assess and visualize water quality across various regions.

# Overview
This project aims to:

1. Develop a Water Quality Index (WQI) based on Indian standards.
2. Utilize machine learning to determine parameter significance.
3. Visualize water quality trends across districts and states using heatmaps.

# Steps to develop a WQI 

# 1. Data Preparation -
Utilized groundwater quality data from 2010 to 2018, covering multiple districts and states. The key step is creation of a labelled dataset denoting healthy/unhealthy              groundwater based on the BIS limits.
Code is available in data_prep.py

# 2. Training a neural network -
A DNN was trained to learn to classify a water instance as healthy/unhealthy. We used the network to get significances for the water parameters.
Code is available in training.py

# 3. Estimating Weights - 
Model weights were interpreted in order to have feature importances using Shapley values. Code is available in weights.py

# 4. Sub-Indices - 
Model parameters need to be brought to a uniform scale in order for the index to make sense. We used a piecewise linear function based on BIS limits for the same. Details can be seen in the report. (report.pdf) Code can be seen in sub-indices.py. Rating plots for several parameters are also uploaded.

# 5. Plotting - 
Finally the index was plotted on a map of India using matplotlib. We used the districts latitude and longitude to determine its location on the map. Code can be seen in plot.py as well as the plots are also uploaded.


