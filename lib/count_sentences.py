
import re


class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):

            raise ValueError('''prints "The value must be a string." if not string.''')
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
   
        sentences = re.split(r'[.!?]', self.value)
        
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        print("The value must be a string.")
      
        return len(sentences)
