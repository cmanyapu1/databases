"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

PlaylistSong = db.Table('PlaylistSong',
                        db.Column('playlist_id', db.Integer,
                                  db.ForeignKey("Playlist.id"),
                                  primary_key=True),
                        db.Column('song_id', db.Integer,
                                  db.ForeignKey("Song.id"),
                                  primary_key=True)

                        )


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "Playlist"

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.Text,
                     nullable=False)
    description = db.Column(db.Text,
                            nullable=False)

    songs = db.relationship(
        'Song',
        secondary=PlaylistSong,
        # cascade="all,delete",
        # back_populates='playlists',
    )


class Song(db.Model):
    """Song."""

    __tablename__ = "Song"

    # ADD THE NECESSARY CODE HERE
    id = db.Column(db.Integer,
                   primary_key=True)
    title = db.Column(db.Text,
                      nullable=False)
    artist = db.Column(db.Text,
                       nullable=False)

    playlists = db.relationship(
        'Playlist',
        secondary=PlaylistSong,
        # cascade="all,delete",
        # back_populates='songs',
    )


# class PlaylistSong(db.Model):
#     """Mapping of a playlist to a song."""
#
#     __tablename__ = "PlaylistSong"
#
#     # ADD THE NECESSARY CODE HERE
#     # id = db.Column(db.Integer,
#     #                primary_key=True)
#     playlist_id = db.Column(db.Integer,
#                        db.ForeignKey("Playlist.id"),
#                        primary_key=True)
#     song_id = db.Column(db.Integer,
#                           db.ForeignKey("Song.id"),
#                           primary_key=True)

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
