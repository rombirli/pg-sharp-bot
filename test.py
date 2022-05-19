import matplotlib.pyplot as plt

from pgsharp.actions import open_pokestop
from processing.filtering import Filters
from android.controller import screenshot

image = screenshot()
plt.imshow(image),
plt.title('original')
plt.savefig('figures/original.png')
plt.show()
plt.imshow(Filters.pgsharp(image)),
plt.title('pgsharp')
plt.savefig('figures/pgsharp.png')
plt.show()
plt.imshow(Filters.pokestops(image))
plt.title('pokestops')
plt.savefig('figures/pokestops.png')
plt.show()
plt.imshow(Filters.sea(image))
plt.title('sea')
plt.savefig('figures/sea.png')
plt.show()
plt.imshow(Filters.road_grey(image))
plt.title('road grey')
plt.savefig('figures/road_grey.png')
plt.show()
plt.imshow(Filters.road_yellow(image))
plt.title('road yellow')
plt.savefig('figures/road_yellow.png')
plt.show()
plt.imshow(Filters.land(image))
plt.title('land')
plt.savefig('figures/land.png')
plt.show()
