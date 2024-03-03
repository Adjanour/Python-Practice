"""
Classes implementing the Ceasar Cipher
"""
# 22-02-2005

import string

class Message:
    self.valid_words = load_words(WORDLIST_FILENAME)
    def __init__(self,text):
        self.text = text
    
    def get_message_text(self,text):
        return self.text
    
    def get_valid_words(self):
        return self.valid_words
        
    def __str__(self):
        return self.text