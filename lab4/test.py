import unittest
import file


class TestFile(unittest.TestCase):
    """------------------OPEN-FILE------------------"""
    def test_open_file_not_found(self):
        incorrect_names_list = ['', 'AAAAA', 'name', 'nafile', 'name2000.html']
        for name in incorrect_names_list:
            self.assertRaises(FileNotFoundError, file.read_word_list_from_file, name)

    def test_open_file_incorrect_value(self):
        self.assertRaises(ValueError, file.read_word_list_from_file, 4)

    def test_open_file_no_rights(self):
        self.assertRaises(Exception, file.read_word_list_from_file, "test")

    """------------------MEM-DICT------------------"""
    def test_dictionary_return(self):
        self.assertIsInstance(file.mem_dict("text"), dict)

