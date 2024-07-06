# Media Information and Comparison Tool

This Python program allows users to interact with the OMDB public API to get information about movies and TV shows. 
It provides functionalities for retrieving media (movies/TV shows) details, searching media by keyword and genre, and comparing media based on IMDb ratings and runtime.

## Features

- **Get Movie/TV Show Information:** Retrieve detailed information about a specific movie or TV show by title (title, type, year, plot, director, actors, genre, IMDb rating and runtime).
- **Search Media with Genre Filter:** Search for movies or TV shows using a keyword and filter the results by genre.
- **Compare Media Ratings:** Compare the IMDb ratings of two movies or TV shows.
- **Compare Media Runtime:** Compare the runtime of two movies or TV shows.

## Example

### Get Movie/TV Show Information:

- Enter the title of the movie or TV show to retrieve detailed information (title, type, year, plot, director, actors, genre, IMDb rating and runtime).

### Search Media with Genre Filter:

- Enter a keyword to search for media and a genre to filter the results.

### Compare Media Ratings:

- Enter the titles of two movies or TV shows to compare their IMDb ratings.

### Compare Media Runtime:

- Enter the titles of two movies or TV shows to compare their runtimes.

## Classes and Functions

### Classes:

- **API:** Handles communication with the OMDB API.
- **Media:** Abstract base class for representing media information.
- **Movie:** Subclass of Media for movies.
- **TV_Show:** Subclass of Media for TV shows.
- **Media_Type:** Factory class for creating Media objects based on type.

### Functions:

- **get_media_info(api):** Retrieves and displays information for a specific movie or TV show.
- **genre_search(api):** Searches for media by keyword and filters by genre.
- **rating_comparison(api):** Compares IMDb ratings of two movies or TV shows.
- **runtime_comparison(api):** Compares the runtimes of two movies or TV shows.
- **Main():** Main function to run the application.