
import numpy as np
import pandas as pd


animals = ["Common Raccoon Dog", "Wild Boar", "Japanese Hare", "Japanese Badger", "Rodents"]

# 1 indicates predation
# Rows indicate predators, and columns indicate prey
# The order is: Common Raccoon Dog, Wild Boar, Japanese Hare, Japanese Badger, Rodents
adjacency_matrix = np.array([
    [0, 0, 1, 0, 1],  # Common Raccoon Dog preys on Japanese Hare and Rodents
    [0, 0, 1, 0, 1],  # Wild Boar preys on Japanese Hare and Rodents
    [0, 0, 0, 0, 0],  # Japanese Hare doesn't prey on any of the listed animals
    [0, 0, 0, 0, 1],  # Japanese Badger preys on Rodents
    [0, 0, 0, 0, 0]   # Rodents don't prey on any of the listed animals
])


adjacency_df = pd.DataFrame(adjacency_matrix, index=animals, columns=animals)

print(adjacency_df)
