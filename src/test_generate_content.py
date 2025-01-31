import unittest
from generate_content import extract_title, generate_page

class TestExtractTitle(unittest.TestCase):
    def test_title(self):
        md = 'THis is some Rubbish PREAMPLE\n# What a title\nAnd more junk text.'
        self.assertEqual(
            'What a title',
            extract_title(md)
        )

    def test_error(self):
        md = '## Not a title\nThis is some unformatted markdown.'
        with self.assertRaises(ValueError):
            extract_title(md)

#class TestGenerateContent(unittest.TestCase):
#    def test_values(self):
#        generate_page('content/index.md','template.html','public/index.html')

