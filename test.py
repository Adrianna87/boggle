from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    # def test_main(self):
    #     with app.test_client() as client:
    #         res = client.get("/")
    #         html= res.get_data(as_text=True)

    # Would have had trouble writing this up myself but definintely
    # knew this was something to test for
    def test_valid_word(self):
        """Test if word is valid by modifying the board in the session"""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"],
                                 ["C", "A", "T", "T", "T"]]
        response = self.client.get('/submit-word?word=cat')
        self.assertEqual(response.json['result'], 'ok')
    
    def test_word_on_board(self):
        """Test if word is on board"""
        self.client.get('/')
        response = self.client.get('/submit-word?word=dogs')
        self.assertEqual(response.json['result'], 'not-on-board')

    def test_not_blank(self):
        """Test if word was submitted"""
        self.client.get('/')
        response = self.client.get('/submit-word?word=')
        self.assertEqual(response.json['result'], 'not-word')

    def test_not_numeric(self):
        """Test if word does not contain numbers"""
        self.client.get('/')
        response = self.client.get('/submit-word?word=appl3')
        self.assertEqual(response.json['result'], 'not-word')

    def word_in_dict(self):
        """Test if word contained within dictionary"""

        self.client.get('/')
        response = self.client.get('/check-word?word=abcdefg')
        self.assertEqual(response.json['result'], 'not-word')


    # TODO -- write tests for every view function / feature!

