#!/usr/bin/env python3

import re

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance (value, str):
      self._value = value
    else:
      print("The value must be a string.")
      self._value = None
      return 0

  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
    
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
  
  def count_sentences(self):
    if not self.value:
      return 0

    if isinstance(self.value, str):
      regex = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"
      m = re.split(regex, self.value)
      return len(m)
    else:
      print("The value must be a string.")
      self._value = None
      return 0


string = MyString()
string.value = 1
string.count_sentences()