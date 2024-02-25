# Columbia AI Module 6 Challenge: Data Sourcing

## Requirements

### Part 1: Access the New York Times API (35 points)
- [X] query_url is correctly constructed (2 points).
- [X] An empty list reviews_list is created (1 point).
- [X] A for loop is created to loop through 20 times (3 points).
- [X] The query_url is extended to include a page (1 point).
- [X] A GET request is made to retrieve results and the JSON data is stored in a variable called reviews (4 points).
- [X] A 12-second interval is used between queries (2 points).
- [X] A try-except clause is used (2 points).
- [X] Inside the try clause, there is a loop to loop through the reviews["response"]["docs"] list (3 points).
- [X] The reviews results are correctly appended to reviews_list (2 points).
- [X] The query page number is printed (1 point).
- [X] The except clause prints out the page number that had no results, then breaks from the loop (2 points).
- [X] json.dumps with the argument indent=4 is used to preview the first five results (2 points).
- [X] reviews_list is converted to a Pandas DataFrame using json_normalize() (2 points).
- [X] The title is extracted from the "headline.main" column and is saved in a new column "title" (3 points).
- [X] The "keywords" column is correctly converted to string data using the supplied extract_keywords function (3 points).
- [X] A list called titles is created from the "title" column using to_list() (2 points).

### Part 2: Access The Movie Database API (40 points)
#### Preparation (4 points):
- [X] An empty list called tmdb_movies_list is created (1 point).
- [X] A variable called request_counter is created and assigned the value of 1 (1 point).
- [X] A for loop is created to loop through the titles list (2 points).
#### Inside the titles for loop (12 points):
- [X] request_counter is incremented by 1 (1 point).
- [X] time.sleep(1) when request_counter reaches a multiple of 50 (3 points).
- [X] A GET request that sends the title to The Movie Database search is performed, and the JSON results are retrieved (4 points).
- [X] A try-except clause is used (3 points).
- [X] The except clause prints out a statement if a movie is not found (1 point).
#### Inside the try clause (20 points):
- [X] The movie ID is collected from the first result and saved as a variable (2 points).
- [X] A GET request is made using the movie query URL and movie ID to retrieve the full movie details in JSON format (4 points).
- [X] The genre names are extracted from the results into a list called genres (2 points).
- [X] The spoken_languages' English names are extracted from the results into a list called spoken_languages (2 points).
- [X] The production_countries' names are extracted from the results into a list called production_countries (2 points).
- [X] A dictionary is created with the specified 15 fields (4 points).
- [X] The results dictionary is appended to the tmdb_movies_list list (3 points).
- [X] A message is printed with the name of the movie to indicate that the title was found. (1 point)
#### Actions after the results are collected (4 points):
- [X] The first five results are previewed using json.dumps with the argument indent=4 (2 points).
- [X] The results are converted to a DataFrame called tmdb_df with pd.DataFrame() (2 points).

### Part 3: Merge and Clean the Data for Export (25 points)
- [X] The New York Times reviews and TMDB DataFrames are merged on the title column (4 points).
- [X] A list called columns_to_fix is created to store the names of the genres, spoken_languages, and production_countries columns (2 points).
- [X] A list is created called characters_to_remove containing [, ], and ' (2 points).
- [X] A for loop is created to loop through columns_to_fix (2 points).
- [X] The columns to fix are converted to the string data type (2 points).
- [X] characters_to_remove is looped through to remove the characters from the string using the Pandas str.replace() method (4 points).
- [X] The head of the updated DataFrame is displayed to confirm the list characters were removed (2 points).
- [X] The byline.person column is dropped (2 points).
- [X] Duplicate rows are deleted (1 point).
- [X] The DataFrame index is reset (1 point).
- [X] The DataFrame is exported to a CSV file without the index (3 points).