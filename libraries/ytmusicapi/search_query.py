"""
Display a list of search results utilizing the ytmusicapi library.

Tyler
"""
search: str
search_results: str

# Import and initialize Youtube Music API 
from ytmusicapi import YTMusic
ytmusic = YTMusic("oauth.json")

# Obtain a search query from the user.
search = input("Please input a query to search for: ")

# Search for the query and display the results.
search_results = ytmusic.search(query=search, filter="songs", limit=1, ignore_spelling=True) # will search for 5 songs with the title "Oasis Wonderwall"
print("\n Category:", search_results[0]["category"], 
      "\n Title:", search_results[0]["title"], 
      "\n Album:", search_results[0]["album"]["name"],
      "\n Artist:", search_results[0]["artists"][0]["name"], 
      "\n Length:", search_results[0]["duration"])

