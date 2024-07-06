import requests
from dotenv import load_dotenv, dotenv_values 
from abc import ABC, abstractmethod

load_dotenv()


# API class 
class API:
    def __init__(self):
        self.base_url = "http://www.omdbapi.com/"   
        self.config = dotenv_values(".env")
        self.api_key = self.config["OMDB_API_KEY"]

    def get_media_info(self, title):
        url = f"{self.base_url}?apikey={self.api_key}&t={title}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting data for movie/TV show {title}")
            return None
        
    def search_media_by_keyword(self, keyword):
            url = f"{self.base_url}?apikey={self.api_key}&s={keyword}"
            response = requests.get(url)
            if response.status_code == 200:
                return response.json().get("Search", [])
            else:
                print(f"Error searching movies/TV shows by keyword {keyword}")
                return None

    def filter_media_by_genre(self, medias, genre):
            filtered_medias = []
            for media in medias:
                media_details = self.get_media_info(media["Title"])
                if media_details and genre.lower() in media_details.get("Genre", "").lower():
                    filtered_medias.append(media_details)
            return filtered_medias


# Media class
class Media:
    def __init__(self, data):
        self.title = data.get("Title")
        self.type = data.get("Type")
        self.year = data.get("Year")
        self.plot = data.get("Plot")
        self.director = data.get("Director")
        self.actors = data.get("Actors")
        self.genre = data.get("Genre")
        self.imdb_rating = data.get("imdbRating", 0)
        self.runtime = data.get("Runtime")
        
    def compare_media_ratings(media1, media2):
        if media1.imdb_rating < media2.imdb_rating:
            return -1
        elif media1.imdb_rating > media2.imdb_rating:
            return 1
        else:
            return 0
        
    def compare_media_runtime(media1, media2):
        if media1.runtime < media2.runtime:
            return -1
        elif media1.runtime > media2.runtime:
            return 1
        else:
            return 0

    @abstractmethod
    def display_info(self):
        raise NotImplementedError("Subclasses should implement this method.")

    
# Movie class
class Movie(Media):
    def __init__(self, data):
        super().__init__(data)

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Type: {self.type}")        
        print(f"Year: {self.year}")
        print(f"Director: {self.director}")
        print(f"Actors: {self.actors}")
        print(f"Genre: {self.genre}")
        print(f"Plot: {self.plot}")
        print(f"IMDb Rating: {self.imdb_rating}")
        print("_______________________________________________________")
    

# TV shows class
class TV_Show(Media):
    def __init__(self, data):
        super().__init__(data)
        self.seasons = data.get("Seasons")
        self.episodes = data.get("Episodes", [])

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Type: {self.type}")        
        print(f"Year: {self.year}")
        print(f"Director: {self.director}")
        print(f"Actors: {self.actors}")
        print(f"Genre: {self.genre}")
        print(f"IMDb Rating: {self.imdb_rating}")
        print(f"Seasons: {self.seasons}")
        print(f"Episodes: {self.episodes}")
        print(f"Plot: {self.plot}")
        print("_______________________________________________________")


# Media_Type class
class Media_Type:

# creats the object (movie/TV show) based on the media type
    @staticmethod
    def create_media(data):
        if "movie" in data.get("Type", "").lower():
            return Movie(data)
        elif "series" in data.get("Type", "").lower():
            return TV_Show(data)
        else:
            print("Unsupported media type")
            return None


# get movie info function
def get_media_info(api):
    title = input("Enter the movie/TV show title: ")
    media_data = api.get_media_info(title)
    if media_data:
        media = Media_Type.create_media(media_data)
        if media:
            media.display_info()
    else:
        print("!! Failed to get movie/TV show data !!")

# search media with genre filter function
def genre_search(api):
    keyword = input("Enter a keyword to search for movies/TV shows: ")
    genre = input("Enter the genre to filter by: ")
    medias = api.search_media_by_keyword(keyword)
    filtered_medias = api.filter_media_by_genre(medias, genre)
    if filtered_medias:
        for media_data in filtered_medias:
            media = Media_Type.create_media(media_data)
            if media:
                media.display_info()
    else:
        print("!! Couldn't find any movies/TV shows with the entered genre !!")

# media ratings comparison function
def rating_comparison(api):
    title1 = input("Enter the first movie/TV show title: ")
    title2 = input("Enter the second movie/TV show title: ")

    media1_data = api.get_media_info(title1)
    media2_data = api.get_media_info(title2)

    if not media1_data or not media2_data:
        print("!! Failed to get movies/TV shows data. Please check the titles and try again !!")

    media1 = Media_Type.create_media(media1_data)
    media2 = Media_Type.create_media(media2_data)

    print(f"\n{media1.type} 1:")
    media1.display_info()

    print(f"\n{media2.type} 2:")
    media2.display_info()

    result = media1.compare_media_ratings(media2)

    if result == -1:
        print(f"\n'{media2.title}' is rated higher than '{media1.title}'.")
    elif result == 1:
        print(f"\n'{media1.title}' is rated higher than '{media2.title}'.")
    else:
        print(f"\n'{media1.title}' and '{media2.title}' have the same rating.")
     
# runtime comparision
def runtime_comparison(api):
    title1 = input("Enter the first movie/TV show title: ")
    title2 = input("Enter the second movie/TV show title: ")

    media1_data = api.get_media_info(title1)
    media2_data = api.get_media_info(title2)

    if not media1_data or not media2_data:
        print("!! Failed to get movies/TV shows data. Please check the titles and try again !!")

    media1 = Media_Type.create_media(media1_data)
    media2 = Media_Type.create_media(media2_data)

    print(f"\n{media1.title} runtime: {media1.runtime}")

    print(f"\n{media2.title} runtime: {media2.runtime}")

    result = media1.compare_media_runtime(media2)

    if result == -1:
        print(f"\n'{media2.title}' runtime is longer than '{media1.title}' runtime.\n")
    elif result == 1:
        print(f"\n'{media1.title}' runtime is longer than '{media2.title}' runtime.\n")
    else:
        print(f"\n'{media1.title}' and '{media2.title}' have the same runtime.\n")
     

# Main function
def Main():
    
    api = API()

    while True:
        choice = input("What would you like to do? (enter the option number)\n"
                       "1- Get movie/TV show information.\n"
                       "2- Search movies/TV shows with genre filter.\n"
                       "3- Movies/TV shows ratings comparison.\n"
                       "4- Movies/TV shows runtime comparison.\n"
                       "5- Exit.\n")
        
        if choice == "1":
            get_media_info(api)

        elif choice == "2":
            genre_search(api)
        
        elif choice == "3":
            rating_comparison(api)

        elif choice == "4":
            runtime_comparison(api)

        elif choice == "5":
            print("Exiting the program...")
            break
        
        else:
            print("Invalid option. Please try again.")

Main()