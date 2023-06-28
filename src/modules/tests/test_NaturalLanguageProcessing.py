import pytest
from unittest.mock import MagicMock
from src.modules.NaturalLanguageProcessing import NaturalLanguageProcessing

nl = NaturalLanguageProcessing()

def test_smoke():
    assert isinstance(nl, NaturalLanguageProcessing)

def test_word_tokenize():
    text = "Hello, my name is Kely"
    tokens = nl.word_tokenize(text)

    assert len(tokens) == 6
    assert tokens == ['hello', ',', 'my', 'name', 'is', 'kely']

def test_tag_words():
    tokens = ['hello', ',', 'my', 'name', 'is', 'kely']
    tag_words = nl.tag_words(tokens)

    assert len(tag_words) == 6
    assert tag_words == [('hello', 'NN'), (',', ','), ('my', 'PRP$'), \
                          ('name', 'NN'), ('is', 'VBZ'), ('kely', 'RB')]

def get_keywords():
    text = "Hello, my name is Kely"
    keywords = nl.get_keywords(text)
    
    assert len(keywords) == 6
    assert keywords == ['hello', ',', 'my', 'name', 'is', 'kely']

def test_stemmer_word_list():
    words = ['hello', ',', 'my', 'name', 'is', 'kely']
    stemmer_word_list = nl.stemmer_word_list(words)
    
    assert len(stemmer_word_list) == 6
    assert stemmer_word_list == ['hello', ',', 'my', 'name', 'is', 'keli']

def test_get_synonyms():
    word = 'fazer'
    get_synonyms = nl.get_synonyms(word)

    assert len(get_synonyms) > 1

def test_is_similar():
    word1 = 'batata'
    word2 = 'maquinas'

    is_similar = nl.is_similar(word1, word2)

    assert is_similar is False
