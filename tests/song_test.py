import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("One Vision")

    def test_song_has_name(self):
        self.assertEqual("One Vision", self.song.name)