import re

def search_file(file, pattern):
    content = open(file).read()
    if re.search(pattern, content, re.MULTILINE | re.DOTALL):
        return True
    return False

### Part 1: Access the New York Times API (35 points)
def test_access_nyt():
    assert search_file("retrieve_movie_data.ipynb", rf"f\\\"\{{url\}}fq=\{{filter_query\}}&sort=\{{sort\}}&fl=\{{field_list\}}&begin_date=\{{begin_date\}}&end_date=\{{end_date\}}&api-key=\{{nyt_api_key\}}\\\"") == True, "query_url is correctly constructed (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"reviews_list = \[\]") == True, "An empty list reviews_list is created (1 point)."

    assert search_file("retrieve_movie_data.ipynb", rf"for p in range\(20\):") == True, "A for loop is created to loop through 20 times (3 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"curr_url = f\\\"\{{full_url\}}&page=\{{p\}}\\\"") == True, "The query_url is extended to include a page (1 point)."

    assert search_file("retrieve_movie_data.ipynb", rf"reviews = resp.json\(\)\[\\\"response\\\"\]\[\\\"docs\\\"\]") == True, "A GET request is made to retrieve results and the JSON data is stored in a variable called reviews (4 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"time.sleep\(12\)") == True, "A 12-second interval is used between queries (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"try.*?except") == True, "A try-except clause is used (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"try:.*?reviews = resp.json\(\)\[\\\"response\\\"\]\[\\\"docs\\\"\].*?for rev in reviews:") == True, "Inside the try clause, there is a loop to loop through the reviews['response']['docs'] list (3 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"reviews_list\.append\(rev\)") == True, "The reviews results are correctly appended to reviews_list (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"else:.*print\(p\)") == True, "The query page number is printed (1 point)."

    assert search_file("retrieve_movie_data.ipynb", rf"except KeyError:.*print\(p\).*break") == True, "The except clause prints out the page number that had no results, then breaks from the loop (2 points)."
    # Note: this is specified in the assignment, but actually, the except block in not entered for page numbers with no results. Instead the result looks like:
    # {'status': 'OK', 'copyright': 'Copyright (c) 2024 The New York Times Company. All Rights Reserved.', 'response': {'docs': [], 'meta': {'hits': 344, 'offset': 1000, 'time': 11}}}

    assert search_file("retrieve_movie_data.ipynb", rf"json.dumps\(reviews_list\[0:6\], indent=4\)") == True, "json.dumps with the argument indent=4 is used to preview the first five results (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"pd\.json_normalize\(reviews_list\)") == True, "reviews_list is converted to a Pandas DataFrame using json_normalize() (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"reviews_df\[\\\"title\\\"\] = reviews_df\[\\\"headline\.main\\\"\]\.apply\(lambda st: st\[st\.find\(\\\"\\\\u2018\\\"\)\+1:st\.find\(\\\"\\\\u2019 Review\\\"\)\]\)") == True, "The title is extracted from the 'headline.main' column and is saved in a new column 'title' (3 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"reviews_df\[\\\"keywords\\\"\] = reviews_df\[\\\"keywords\\\"\]\.apply\(extract_keywords\)") == True, "The 'keywords' column is correctly converted to string data using the supplied extract_keywords function (3 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"titles = reviews_df\[\\\"title\\\"\]\.to_list\(\)") == True, "A list called titles is created from the 'title' column using to_list() (2 points)."

### Part 2: Access The Movie Database API (40 points)
#### Preparation (4 points):
def test_access_mdb_prep():
    assert search_file("retrieve_movie_data.ipynb", rf"tmdb_movies_list = \[\]") == True, "An empty list called tmdb_movies_list is created (1 point)."

    assert search_file("retrieve_movie_data.ipynb", rf"request_counter = 1") == True, "A variable called request_counter is created and assigned the value of 1 (1 point)."

    assert search_file("retrieve_movie_data.ipynb", rf"for t in titles:") == True, "A for loop is created to loop through the titles list (2 points)."

#### Inside the titles for loop (12 points):
def test_access_mdb_loop():
    assert search_file("retrieve_movie_data.ipynb", rf"request_counter += 1") == True, "request_counter is incremented by 1 (1 point)."

    assert search_file("retrieve_movie_data.ipynb", rf"if request_counter % 50 == 0:.*time\.sleep\(1\)") == True, "time.sleep(1) when request_counter reaches a multiple of 50 (3 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"requests\.get\(f\\\"\{{url\}}\{{urllib.parse.quote_plus\(t\)\}}\{{tmdb_key_string\}}\\\", timeout=10\)") == True, "A GET request that sends the title to The Movie Database search is performed, and the JSON results are retrieved (4 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"try:.*except") == True, "A try-except clause is used (3 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"except:.*print\(f\\\"\{{t\}} not found\\\"\)") == True, "The except clause prints out a statement if a movie is not found (1 point)."
    # Note: If no movie is found, result looks like:
    # {'page': 1, 'results': [], 'total_pages': 1, 'total_results': 0}

#### Inside the try clause (20 points):
def test_access_mdb_try():
    assert search_file("retrieve_movie_data.ipynb", rf"movie_id = resp\[\\\"results\\\"\]\[0\]\[\\\"id\\\"\]") == True, "The movie ID is collected from the first result and saved as a variable (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"det_url = f\\\"https:\/\/api\.themoviedb\.org\/3\/movie\/\{{movie_id\}}\?api_key=\{{tmdb_api_key\}}\\\".*requests\.get\(det_url\)") == True, "A GET request is made using the movie query URL and movie ID to retrieve the full movie details in JSON format (4 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"genre = \[x\[\\\"name\\\"\] for x in det_resp\[\\\"genres\\\"\]\]") == True, "The genre names are extracted from the results into a list called genres (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"spoken_languages = \[x\[\\\"english_name\\\"\] for x in det_resp\[\\\"spoken_languages\\\"\]\]") == True, "The spoken_languages' English names are extracted from the results into a list called spoken_languages (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"production_countries = \[x\[\\\"name\\\"\] for x in det_resp\[\\\"production_countries\\\"\]\]") == True, "The production_countries' names are extracted from the results into a list called production_countries (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"\{{.*\\\"title\\\": det_resp.get\(\\\"title\\\", None\),.*\}}") == True, "A dictionary is created with the specified 15 fields (4 points)."

    # Note: This is the full regex, but makes the test slow
    # rf"\{{.*\\\"title\\\": det_resp.get\(\\\"title\\\", None\),.*\\\"original_title\\\": det_resp.get\(\\\"original_title\\\", None\),.*\\\"budget\\\": det_resp.get\(\\\"budget\\\", None\),.*\\\"genre\\\": genre,.*\\\"language\\\": det_resp.get\(\\\"language\\\", None\).*.*\\\"spoken_languages\\\": spoken_languages,.*\\\"homepage\\\": det_resp.get\(\\\"homepage\\\", None\),.*\\\"overview\\\": det_resp.get\(\\\"overview\\\", None\),.*\\\"popularity\\\": det_resp.get\(\\\"popularity\\\", None\),.*\\\"runtime\\\": det_resp.get\(\\\"runtime\\\", None\),.*\\\"revenue\\\": det_resp.get\(\\\"revenue\\\", None\),.*\\\"release_date\\\": det_resp.get\(\\\"release_date\\\", None\),.*\\\"vote_average\\\": det_resp.get\(\\\"vote_average\\\", None\),.*\\\"vote_count\\\": det_resp.get\(\\\"vote_count\\\", None\),.*\\\"production_countries\\\": production_countries,\}}"

    assert search_file("retrieve_movie_data.ipynb", rf"tmdb_movies_list\.append\(\{{") == True, "The results dictionary is appended to the tmdb_movies_list list (3 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"print\(t\)") == True, "A message is printed with the name of the movie to indicate that the title was found. (1 point)"

#### Actions after the results are collected (4 points):
def test_access_mdb_actions():
    assert search_file("retrieve_movie_data.ipynb", rf"json\.dumps\(tmdb_movies_list\[0:5\], indent=4\)") == True, "The first five results are previewed using json.dumps with the argument indent=4 (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"movies_df = pd\.read_json\(\\\"movies\.json\\\"\)") == True, "The results are converted to a DataFrame called tmdb_df with pd.DataFrame() (2 points)."

### Part 3: Merge and Clean the Data for Export (25 points)
def test_clean():
    assert search_file("retrieve_movie_data.ipynb", rf"merge_df = pd\.merge\(reviews_df, movies_df, on=\\\"title\\\"\)") == True, "The New York Times reviews and TMDB DataFrames are merged on the title column (4 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"columns_to_fix = merge_df\.loc\[:, merge_df\.apply\(lambda col: col\.astype\(str\)\.str\.contains\(\\\"\\\\\[\\\"\)\)\.any\(\)\]\.columns") == True, "A list called columns_to_fix is created to store the names of the genres, spoken_languages, and production_countries columns (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"characters_to_remove = \[.*r\\\"\\\\\[\\\", r\\\"\\\\\]\\\",.*r\\\"\\\\\'\\\"") == True, "A list is created called characters_to_remove containing [, ], and ' (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"for c in columns_to_fix:") == True, "A for loop is created to loop through columns_to_fix (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"merge_df\[c\] = merge_df\[c\]\.astype\(str\)") == True, "The columns to fix are converted to the string data type (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"merge_df\[c\] = merge_df\[c\]\.str\.replace\(char, \\\"\\\", regex=True\)") == True, "characters_to_remove is looped through to remove the characters from the string using the Pandas str.replace() method (4 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"merge_df\.head\(\)") == True, "The head of the updated DataFrame is displayed to confirm the list characters were removed (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"merge_df\.drop\(columns=\\\"byline\.person\\\", inplace=True\)") == True, "The byline.person column is dropped (2 points)."

    assert search_file("retrieve_movie_data.ipynb", rf"merge_df\.drop_duplicates\(\)") == True, "Duplicate rows are deleted (1 point)."

    assert search_file("retrieve_movie_data.ipynb", rf"merge_df.*\.reset_index\(drop=True\)") == True, "The DataFrame index is reset (1 point)."

    assert search_file("retrieve_movie_data.ipynb", rf"merge_df\.to_csv\(\\\"collected_data\.csv\\\", index=False\)") == True, "The DataFrame is exported to a CSV file without the index (3 points)."
