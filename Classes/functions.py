import string

def load_words(text : str):
    """
    text: string, text  containing words
    returns: list of valid words. Words are strings of lowercase letters.
    """
    if text == None:
       return []
    else:
        for i in text:
            if i is not string.ascii_lowercase:
                text = text.replace(i,' ')