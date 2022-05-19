import matplotlib.pyplot as plt

from pgsharp.actions import open_pokestop
from processing.filtering import Filters
from android.controller import screenshot

image = screenshot()
plt.imshow(Filters.pgsharp(image)),
plt.title('pgsharp')
plt.show()
plt.imshow(Filters.pokestops(image))
plt.title('pokestops')
plt.show()
plt.imshow(Filters.sea(image))
plt.title('sea')
plt.show()
plt.imshow(Filters.road_grey(image))
plt.title('road grey')
plt.show()
plt.imshow(Filters.road_yellow(image))
plt.title('road yellow')
plt.show()
plt.imshow(Filters.land(image))
plt.title('land')
plt.show()

