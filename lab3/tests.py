import unittest
import names


class TestNames(unittest.TestCase):

    def test_normal_work(self):
        self.assertEqual(2001, len(names.extr_name('name2006.html')))
        self.assertEqual(2001, len(names.extr_name('name2008.html')))

    def test_file_not_found(self):
        incorrect_names_list = ['', 'AAAAA', 'name', 'name2000', 'name2000.html']
        for name in incorrect_names_list:
            self.assertRaises(FileNotFoundError, names.extr_name, name)

    def test_no_right_to_resd(self):
        self.assertRaises(Exception, names.top_names, "test_file")
