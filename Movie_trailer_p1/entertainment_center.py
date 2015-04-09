__author__ = 'kgottiparthy'
import movie_trailer
import fresh_tomatoes


"""
Input the various movies that you want to list on the website using Movies class
"""

toy_story = movie_trailer.Movies("Toy story", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                 "https://www.youtube.com/watch?v=azyK_k52R1w", "8/10")
school_rock = movie_trailer.Movies("school of rock",
                                   "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                                   "www.youtube.com/watch?v=XCwy6lW5Ixc", "6/10")
avatar = movie_trailer.Movies("Avatar", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                              "https://www.youtube.com/watch?v=cRdxXPV9GNQ", "10/10")

movies = [toy_story, school_rock, avatar]
fresh_tomatoes.open_movies_page (movies)
