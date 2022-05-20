import matplotlib.pyplot as plt
from processing.clustering import kmeans
from processing.filtering import Filters
from processing.helpers import load_picture

image = load_picture('screen.png')
# show original
plt.imshow(image),
plt.title('original')
plt.savefig('figures/original.png')
# show pgsharp filter
plt.show()
plt.imshow(Filters.pgsharp(image)),
plt.title('pgsharp filter')
plt.savefig('figures/pgsharp.png')
plt.show()
# show pgsharp detected center on original picture
plt.imshow(image)
plt.scatter(*kmeans(Filters.pgsharp(image), 1)[0], color='red')
plt.title('pgsharp detected position')
plt.savefig('figures/pgsharp_pos.png')
plt.show()
# show pokestops filter
plt.imshow(Filters.pokestops(image))
plt.title('pokestops filter')
plt.savefig('figures/pokestops.png')
plt.show()
# show pgsharp detected center on original picture
plt.imshow(image)
for x, y in kmeans(Filters.pokestops(image), 20) :
    plt.scatter(x, y, color='red')
plt.title('pokestops detected position (top 20)')
plt.savefig('figures/pokestops_pos.png')
plt.show()
# show sea filter
plt.imshow(Filters.sea(image))
plt.title('sea filter')
plt.savefig('figures/sea.png')
plt.show()
# show road filters
plt.imshow(Filters.road_grey(image))
plt.title('road grey filter')
plt.savefig('figures/road_grey.png')
plt.show()
plt.imshow(Filters.road_yellow(image))
plt.title('road yellow filter')
plt.savefig('figures/road_yellow.png')
plt.show()
# show land filter
plt.imshow(Filters.land(image))
plt.title('land filter')
plt.savefig('figures/land.png')
plt.show()
