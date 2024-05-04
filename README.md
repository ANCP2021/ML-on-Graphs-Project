# Time-Series Species Population Prediction: Food Networks and Graph Neural Networks
This repository contains a survey and exploration of machine learning (ML) methods, such as neural networks (NNs), regression models (RMs), and graph neural networks (GNNs), tailored to ecological modeling. Specifically, we evaluate the ensemble of models and predict species populations via time-series data and their respective predation dynamics.

## Folder Hierarchy
- Datasets: Houses the datasets utilized by the ML methods.
    - Lynx_Hare: Contains the popular lynx and hare dataset providing the population cycles between lynx and hare.
    - study_373 (Village survey Medium and large mammal survey data): Contains the top 5 species population for Study 373 of the BioTIME dataset.
    - study_213 ((Northeast Fisheries Science Center Bottom Trawl Survey Data (OBIS-USA))): Contains the top 5 species populations for Study 213 of the BioTIME dataset
- Models: Houses evaluated ML models.
    - GNNs: Contains GNN models used to compare against non-graphical ML models. Specific GNN models are Graph Convolutional Network and Graph Attention Network.
    - Neural_Networks: Contains NNs, specifically Feedforward Neural Networks (FNNs) and Long Short-Term Memory Networks (LSTM). There are two different FNN and LSTM models where one considers predation dynamics via a predation strength attribute and the other does not and serves as a baseline.
    - regression: Contains regression model ensemble including, linear regression, autoregressive models, and network autoregressive models.
        - notebooks_with_results: Folder used for the results of each model relative to the dataset (Lynx-Hare, Study 373, Study 213) used.
- notebooks: Miscellaneous notebooks used for data imputation, data preprocessing, food network visualizations, and preliminary results during the halfway point of our study.

## BioTIME Dataset Source

https://www.kaggle.com/datasets/thedevastator/global-species-abundance-and-diversity?resource=download