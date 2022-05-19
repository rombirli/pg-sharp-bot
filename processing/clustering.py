from typing import List, Tuple

from sklearn.cluster import KMeans
import numpy as np


def kmeans(image: np.array, k: int) -> List[Tuple[int, int]]:
    X = np.array([[x, y]
                  for y, line in enumerate(image)
                  for x, px in enumerate(line)
                  if px])
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    return [tuple(center) for center in kmeans.cluster_centers_]
