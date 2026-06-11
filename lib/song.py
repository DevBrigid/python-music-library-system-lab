class Song:
    # Step 1 & 2: Define Class Attributes
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artists_count = {}  
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Step 3: Trigger class methods upon new song creation
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    # --- Step 3: Class Methods Implementation ---

    @classmethod
    def add_song_to_count(cls):
        """Increments the value of count by one"""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds any new genres to class attribute genres (Unique values only)"""
        cls.genres.add(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds any new artists to class attribute artists (Unique values only)"""
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates class attribute genre_count"""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Updates class attribute artists_count and artist_count"""
        # Update prompt-required attribute
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1
            
        # Update test-required attribute to prevent failure
        cls.artist_count = cls.artists_count