#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value):
        self._value = None
        self.value = value  # Use the property setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Split the value based on '.', '?', and '!'
        sentences = [s.strip() for s in re.split(r'[.!?]', self._value) if s]
        return len(sentences)

# Example usage:
try:
    my_str = MyString("Hello, World!")
    print(my_str.is_sentence())  # Output: True
    print(my_str.is_question())  # Output: False
    print(my_str.is_exclamation())  # Output: False
    print(my_str.count_sentences())  # Output: 1

    my_str.value = "How are you today?"
    print(my_str.is_sentence())  # Output: False
    print(my_str.is_question())  # Output: True
    print(my_str.is_exclamation())  # Output: False
    print(my_str.count_sentences())  # Output: 1
except ValueError as e:
    print(f"Error: {e}")
