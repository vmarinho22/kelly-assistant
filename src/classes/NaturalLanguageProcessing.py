from typing import Any

from nltk.corpus import stopwords, wordnet
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


class NaturalLanguageProcessing:
    
    """
        Dedicated class to use natural language processing
    """
    
    def word_tokenize(self, text: str) -> list[str]:
        """
            Method to tokenize a string text
        """
        tokens: list[str] = word_tokenize(text.lower())
        return tokens
    
    def get_keywords(self, text: str) -> list[str]:
        """
            Method to filter and get keywords of a large text
        """
        # Remove stop words (common words that usually have no meaning by themselves)
        tokens: list[str] = self.word_tokenize(text)
        stop_words: set[str] = set(stopwords.words('portuguese'))
        filtered_tokens: list[str] = [word for word in tokens if not word.lower() in stop_words]

        # Calculate the frequency of words
        fdist: FreqDist = FreqDist(filtered_tokens)
        
        # Get the 8 most common words
        keywords: list[tuple[Any, int]] = fdist.most_common(8) # select the five words of the sentence
        formatted_keywords: list[str] = [word[0] for word in keywords] # Get just word in tuple. Exp.: ('text', 1)
        
        return formatted_keywords
    
    def stemmer_word_list(self, words: list[str]) -> list[str]:
        """
            Method to apply stemming syntax to word list
        """
        # Filter list by stemming context
        stemmer = PorterStemmer()
        
        stemmed_list = [stemmer.stem(word) for word in words]
        
        return stemmed_list 
    
    def get_synonyms(self, word: str) -> list[str]:
        """
            Method to get synonyms of a word
        """
        synonyms: list = []
        
        for synset in wordnet.synsets(word, lang='por'):
            for lemma in synset.lemmas(lang='por'):
                synonyms.append(lemma.name())
                
        synonyms: list = list(set(synonyms))
        
        return synonyms
    
    def is_similar(self, word_one: str, word_two: str) -> bool:
        """
            Method to verify similarity of two words
        """
        synsets_one = wordnet.synsets(word_one)
        synsets_two = wordnet.synsets(word_two)
        
        for synset1 in synsets_one:
            for synset2 in synsets_two:
                if synset1.wup_similarity(synset2) > 0.8:
                    return True
        
        return False