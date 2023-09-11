import matplotlib.pyplot as plt
import numpy as np


class BarPlotVisualizer:
    def __init__(self, data_dict, x_label, y_label, title):
        self.data_dict = data_dict
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

    def plot(self, save_path=None):
        clients = list(self.data_dict.keys())
        keyword_counts = list(self.data_dict.values())
        positions = np.arange(len(clients))

        # Adjust the figure height and fontsize based on the number of clients
        height_factor = 0.5
        fig_height = len(clients) * height_factor
        if len(clients) < 20:
            fontsize = 10
        elif len(clients) < 50:
            fontsize = 8
        else:
            fontsize = 6

        plt.figure(figsize=(10, fig_height))

        colors = ['blue' if count == -1 else 'red' for count in keyword_counts]
        bars = plt.barh(positions, keyword_counts, color=colors, align='center')
        plt.yticks(positions, clients, fontsize=fontsize)
        plt.xticks(np.arange(0, 11, 1))

        plt.ylabel(self.x_label, labelpad=10)
        plt.xlabel(self.y_label)
        plt.title(self.title)
        plt.xlim(0, 10)

        for pos, bar in zip(positions, bars):
            xval = bar.get_width()
            plt.text(xval + 0.2, pos, round(xval, 2), va='center', ha='left', fontsize=fontsize)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)

        plt.show()
