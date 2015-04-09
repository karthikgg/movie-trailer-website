__author__ = 'kgottiparthy'
import webbrowser


class Movies():
    """
    Movies class
    Args:
          title: Title of the movie.
          poster_image: url of the poster image.
          youtube_trailer: url of the youtube trailer.
          reviews: movie reviewed out of 10
    """
    def __init__(self, title, poster_image, youtube_trailer, reviews):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.reviews = reviews

    def show_trailer(self):
        webbrowser.open (self.youtube_trailer)