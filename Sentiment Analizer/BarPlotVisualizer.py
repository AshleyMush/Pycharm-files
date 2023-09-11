import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta


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

        plt.figure(figsize=(10, 8))

        colors = ['blue' if count == -1 else 'red' for count in keyword_counts]  # Change color to blue for empty notes
        bars = plt.barh(positions, keyword_counts, color=colors, align='center')
        plt.yticks(positions, clients)
        plt.xticks(np.arange(0, 11, 1))

        plt.ylabel(self.x_label, labelpad=10)
        plt.xlabel(self.y_label)
        plt.title(self.title)
        plt.xlim(0, 10)

        for pos, bar in zip(positions, bars):
            xval = bar.get_width()
            plt.text(xval + 0.2, pos, round(xval, 2), va='center', ha='left')

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)

        plt.show()

    def plot_sentiment(self, sentiment_scores):
        dates = [datetime.now() - timedelta(days=i) for i in range(len(sentiment_scores))]
        plt.plot(dates, sentiment_scores)
        plt.xlabel('Date')
        plt.ylabel('Sentiment Score')
        plt.title('Client Progress Over Time')
        plt.show()
