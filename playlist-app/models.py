"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlist"


    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.Text,
                     nullable=False)
    description = db.Column(db.Text,
                     nullable=False)

    songs = db.relationship(
        'Song',
        secondary="PlaylistSong",
        # cascade="all,delete",
        backref="Playlist",
    )

class Song(db.Model):
    """Song."""

    __tablename__ = "song"

    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer,
                   primary_key=True)
    title = db.Column(db.Text,
                     nullable=False)
    artist = db.Column(db.Text,
                     nullable=False)

    playlists = db.relationship(
        'Playlist',
        secondary="PlaylistSong",
        # cascade="all,delete",
        backref="Song",
    )

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlist_song"

    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer,
                   primary_key=True)
    playlist_id = db.Column(db.Integer,
                       db.ForeignKey("playlist.id"),
                       primary_key=True)
    song_id = db.Column(db.Integer,
                          db.ForeignKey("song.id"),
                          primary_key=True)
                          
# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
