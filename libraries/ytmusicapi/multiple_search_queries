"""
  Ask the user for the number of results, and display a list of 
  search results utilizing the ytmusicapi library.

  Tyler
"""


# Define the variables.
search_query: str
search_results: str
search_limit: str
next_result: int = 0
i: int


# Import and initialize Youtube Music API 
from ytmusicapi import YTMusic
ytmusic = YTMusic("oauth.json")

# Obtain a search query and search limit from the user.
search_query = input("Please input a query to search for: ")
search_limit = int(input("Please input the number of results to display: "))

# Search for the query.
search_results = ytmusic.search(query=search_query, filter="songs", limit=search_limit, ignore_spelling=True)

# Display the result to the user depending on the limit of results.
for i in range(search_limit):
      print("\n",
            "\n Title:", search_results[next_result]["title"], 
            "\n Album:", search_results[next_result]["album"]["name"],
            "\n Artist:", search_results[next_result]["artists"][0]["name"], 
            "\n Length:", search_results[next_result]["duration"])
      next_result += 1

