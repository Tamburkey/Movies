import webbrowser

class Movie():
	"""class with instance variables describing the movie"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date):  
		""" Constructor for class Movie w Instance Variables """
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.release_date = release_date
	def show_trailer(self):  
		""" Instance Method of class Movie which opens youtube """
		webbrowser.open(self.trailer_youtube_url)