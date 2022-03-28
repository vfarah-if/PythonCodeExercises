from game_of_life.string_builder import StringBuilder
from os import linesep as eol

class TestStringBuilderShould:

    
    def test_append_two_strings(self):
        string_builder = StringBuilder()
        
        string_builder.add('expect').add('ed')
        
        assert string_builder.to_string() == 'expected'
        
    def test_new_line_two_strings(self):
        string_builder = StringBuilder()
        
        string_builder.add('line 1').newline().add('line 2')
        
        assert string_builder.to_string() == (
            f"line 1{eol}"
            "line 2"
        )