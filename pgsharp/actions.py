from matplotlib import pyplot as plt

from android import controller
from android.controller import tap, play_record
from processing import filtering, clustering


def open_pokestop():
    image = controller.screenshot()
    pokestop_filtered = filtering.pokestops(image)
    means = clustering.kmeans(pokestop_filtered, 5)
    # find the bottom-most mean
    mean = max(means, key=lambda mean: mean[1])
    x, y = mean
    tap(x, y)
    plt.imshow(pokestop_filtered)
    for mean in means:
        plt.scatter(*mean, color='white')
    plt.scatter(x, y, color='red')
    plt.show()


def turn_pokestop():
    play_record('turn_pokestop')
