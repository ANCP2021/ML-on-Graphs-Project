from torch_geometric_temporal.signal import StaticGraphTemporalSignal
import numpy as np
import csv

class temporalGNNLoader(object):
    """Class to load csv data into StaticGraphTemporalSignal"""

    def __init__(self, filename) -> None:
        self.filename = filename

    def _get_edges(self, edges):
        self._edges = np.array(edges).T

    def _get_edge_weights(self):
        self._edge_weights = np.ones(self._edges.shape[1])
    
    def _get_targets_and_features(self):
        data_array = []
        with open(self.filename, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                data_row = [float(value) for value in row[1:]]
                data_array.append(data_row)
            data_2d_array = np.array(data_array)
            self.features = [
                data_2d_array[i : i + self.lags, :].T
                for i in range(data_2d_array.shape[0] - self.lags)
            ]
            self.targets = [
                data_2d_array[i + self.lags, :].T
                for i in range(data_2d_array.shape[0] - self.lags)
            ]
    
    def get_dataset(self, edges, lags: int = 4) -> StaticGraphTemporalSignal:
        self.lags = lags
        self._get_edges(edges=edges)
        self._get_edge_weights()
        self._get_targets_and_features()
        dataset = StaticGraphTemporalSignal(self._edges, self._edge_weights, self.features, self.targets)
        return dataset