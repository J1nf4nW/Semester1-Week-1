# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music_billboard = {"Taylor Swift": ["Patient Zero", "Cleveland!", "Babylon"], "Sienna Spiro": ["Great Expectation"], "Ella Langley": ["Choosin' Texas"], "Jamie Miller": ["Babydoll"], "Stella Lefty": ["Boston"], "Olivia Rodrigo": ["The Cure"], "Adela": ["Nicole Kidman"], "Ashe": ["Stop The Wedding"]}
# Pretty-print the data structure
pprint(music_billboard)
# Display details of one album recorded by a specific artist
artist = "Taylor Swift"
album = music_billboard[artist][1]
print("\nArtist:", artist)
print("Album:", album)