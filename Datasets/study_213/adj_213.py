"""
Adjacency Matrix for study 213

Note the following species ID -> species matchings:

7058 ['Merluccius bilinearis']      -> Silver hake
    Highly predatory and typically feeds on fish and crustaceans
    They are voracious predators and feed on fish, crustaceans, and squid.

8572 ['Squalus acanthias']          -> Spiny dogfish
    They are aggressive hunters and have a sizable diet that can range from squid, fish, crab, jellyfish, sea cucumber, shrimp and other invertebrates

39601 ['Doryteuthis pealeii']       -> Longfin inshore squid
    They are a key prey species for a variety of marine mammals, diving birds, and finfish species. 

8901 ['Urophycis chuss']            -> Red hake
    Primary predators of red hake include spiny dogfish, cod, goosefish, and silver hake

7730 ['Peprilus triacanthus']       -> American butterfish
    They are semi-pelagic, and form loose schools that feed upon small invertebrates.
    They have a high natural mortality rate and are preyed upon by many species of fish, marine mammals, and seabirds.
"""

import numpy as np

# Note that in this example, there are basically three "apex" predators, the two hake and the dogfish
# However, all silver hake and the spiny dogfish will eat each other and the red hake. 
# An undirected network will actually just be a complete graph since all the predators eat 
# both of the "prey" species and each other as well as themselves
adjacency_matrix = np.array([
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
])

# Here, we have a directed variant where predators have edges pointing to prey, but not the otherway around
# Now, the squid have no outgoing edges, and the butterfish only has one
adjacency_matrix_directed = np.array([
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
])