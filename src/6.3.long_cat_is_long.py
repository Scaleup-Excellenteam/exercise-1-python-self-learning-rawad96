# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 14:53:06 2025

@author: USER
"""

def long_cat_is_long(text):    
    cleanText = ''.join(c if c.isalpha() or c.isspace() else " " for c in text)
    
    wordsLen = {word: len(word) for word in set(cleanText.split())}
    
    return wordsLen
    
    
    
if __name__ == '__main__':
    print(long_cat_is_long("""You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat."""))
    
    