import media
import fresh_tomatoes

cabin = media.Movie("Cabin in the Woods",
	"Its about a cabin in the woods.",
	"http://cdn.collider.com/wp-content/uploads/cabin-in-the-woods-poster-hi-res.jpg",
	"https://www.youtube.com/watch?v=u1Ea86glnRU",
	"2012")

space = media.Movie("2001: A Space Odyssey",
	"SPACE!!",
	"https://1.bp.blogspot.com/-RpZ1rglEeIk/T7TyEH0sEeI/AAAAAAAAEcA/O5XF3t56MY8/s1600/2001+A+Space+Odyssey+(1968)+Space+Station+One+by+Robert+McCall.jpg",
	"https://www.youtube.com/watch?v=lfF0vxKZRhc",
	"1968")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind", 
	"Jim Carey gives himself brain damage",
	"https://vinint.files.wordpress.com/2016/01/eternal-sunshine-of-the-spotless-mind-poster-artwork-kate-winslet-kirsten-dunst-tom-wilkinson.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc",
	"2004")

sunshine = media.Movie("Sunshine",
	"More space, more sun.",
	"http://83e2u32cf1b4dlzbl29etyxt.wpengine.netdna-cdn.com/wp-content/uploads/2013/05/Sunshine-Poster.jpg",
	"https://www.youtube.com/watch?v=YZ2-xR54UDU",
	"2007")

monty_python = media.Movie("Monty Python and the Holy Grail.",
	"King Arthurs quest for the holy grail.",
	"https://cdn.traileraddict.com/content/sony-pictures/montypythonholygrail.jpg",
	"https://www.youtube.com/watch?v=RDM75-oXGmQ",
	"1975")

airplane = media.Movie("Airplane!",
	"An airplane nearly crashes and a young boy is asked about Turkish Prison.",
	"https://www.movieposter.com/posters/archive/main/67/MPW-33875",
	"https://www.youtube.com/watch?v=qaXvFT_UyI8",
	"1980"
	)

movies = [cabin, space, eternal_sunshine, sunshine, monty_python, airplane]
fresh_tomatoes.open_movies_page(movies)
