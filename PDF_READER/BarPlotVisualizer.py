import matplotlib.pyplot as plt
import numpy as np


class BarPlotVisualizer:
    def __init__(self, data_dict, x_label, y_label, title):
        self.data_dict = data_dict
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

    def plot(self):
        clients = list(self.data_dict.keys())
        keyword_counts = list(self.data_dict.values())
        positions = np.arange(len(clients))

        plt.figure(figsize=(10, 8))  # Adjusted for better layout

        bars = plt.barh(positions, keyword_counts, color='red', align='center')
        plt.yticks(positions, clients)  # No rotation needed now
        plt.xticks(np.arange(0, 11, 1))

        plt.ylabel(self.x_label, labelpad=10)  # Swapped x and y labels
        plt.xlabel(self.y_label)
        plt.title(self.title)
        plt.xlim(0, 10)  # Adjusted xlim instead of ylim for horizontal bars

        # Adjusted positioning of the text on the bars
        for pos, bar in zip(positions, bars):
            xval = bar.get_width()
            plt.text(xval + 0.2, pos, round(xval, 2), va='center', ha='left')

        plt.tight_layout()
        plt.show()
