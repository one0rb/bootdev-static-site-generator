import unittest
from block_markdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = '''
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
'''
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            [
                '# This is a heading',
                'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ],
            blocks
        )

    def test_markdown_to_blocks_lines_whitespace(self):
        markdown = '''


## Heading 2


I have no idea what I should be putting here aside from:       

1. Lots of empty lines
2. Some trailing whitespace
'''
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            [
                '## Heading 2',
                'I have no idea what I should be putting here aside from:',
                '1. Lots of empty lines\n2. Some trailing whitespace'
            ],
            blocks
        )
