import unittest
from block_markdown import (
        markdown_to_blocks,
        block_to_block_type,
        text_to_children,
        paragraph_to_html_node,
        heading_to_html_node,
        code_to_html_node,
        quote_to_html_node,
        ulist_to_html_node,
        olist_to_html_node,
        block_to_html_node,
        markdown_to_html_node
)
from inline_markdown import text_to_text_node
from textnode import text_node_to_html_node
from htmlnode import ParentNode, LeafNode

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

class TestBlockToBlockType(unittest.TestCase):
    def test_values(self):
        heading = '## Heading 2'
        self.assertEqual(
                'heading',
                block_to_block_type(heading)
        )
        code = '```\nprint("Harrow world!")\n```'
        self.assertEqual(
                'code',
                block_to_block_type(code)
        )
        quote = '> To be or not to be,...\n> That is the question!'
        self.assertEqual(
                'quote',
                block_to_block_type(quote)
        )
        unordered_list = '* Bananas\n* Apples\n* Oranges'
        self.assertEqual(
                'unordered_list',
                block_to_block_type(unordered_list)
        )
        ordered_list = '1. Bananas\n2. Apples\n3. Oranges'
        self.assertEqual(
                'ordered_list',
                block_to_block_type(ordered_list)
        )
        paragraph = '1. Potato\n* Tomator'
        self.assertEqual(
                'paragraph',
                block_to_block_type(paragraph)
        )
    def test_errors(self):
        misordered_list = '1. Banana\n3. Apple\n4. Orange'
        self.assertEqual(
                'paragraph',
                block_to_block_type(misordered_list)
        )
        misquote = '> A quote...\nto be forgotten'
        self.assertEqual(
                'paragraph',
                block_to_block_type(misquote)
        )
        messy_list = '* mess\n* messier\n- messiest'
        self.assertEqual(
                'paragraph',
                block_to_block_type(messy_list)
        )

class TestTextToChildren(unittest.TestCase):
    def test_text_to_children(self):
        text = "This is *very* important text. **Please read this carefully!** Keep doing what you're doing."
        self.assertEqual(
            [
                LeafNode(None, 'This is ', None),
                LeafNode('i', 'very', None),
                LeafNode(None, ' important text. ', None),
                LeafNode('b', 'Please read this carefully!', None),
                LeafNode(None, " Keep doing what you're doing.", None)
            ],
            text_to_children(text)
        )

    def test_text_to_children(self):
        text = 'This is *improperly* formatted **markdown text.'
        with self.assertRaises(ValueError):
            text_to_children(text)

class ParagraphToHTMLNode(unittest.TestCase):
    def test_values(self):
        text = 'This is a random paragraph.\r\nWith random stuff.\nFingers crossed!'
        self.assertEqual(
            ParentNode(
                'p',
                [
                    LeafNode(
                        None,
                        'This is a random paragraph. With random stuff. Fingers crossed!',
                        None
                    )
                ],
                None
            ),
            paragraph_to_html_node(text)
        )

class HeadingToHTMLNode(unittest.TestCase):
    def test_values(self):
        block = '### What a heading!'
        self.assertEqual(
            ParentNode('h3', [LeafNode(None, 'What a heading!', None)], None),
            heading_to_html_node(block)
        )

class CodeToHTMLNode(unittest.TestCase):
    def test_values(self):
        block = "```\nprint('dummy code')\nprint('for dummies!')\n```"
        self.assertEqual(
            ParentNode(
                'pre',
                ParentNode(
                    'code',
                    [
                        LeafNode(
                            None,
                            "print('dummy code')\nprint('for dummies!')",
                            None
                        )
                    ],
                    None
                ),
                None
            ),
            code_to_html_node(block)
        )

class QuoteToHTMLNode(unittest.TestCase):
    def test_values(self):
        block = '> There was a young woman from Ealing\n> Who had a peculiar feeling\n> She lay on her back\n> Opened her crack\n> And pissed all over the ceiling'
        self.assertEqual(
            ParentNode(
                'blockquote',
                [
                    LeafNode(
                        None,
                        'There was a young woman from Ealing\nWho had a peculiar feeling\nShe lay on her back\nOpened her crack\nAnd pissed all over the ceiling',
                        None,
                    )
                ],
                None
            ),
            quote_to_html_node(block)
        )

class UlistToHTMLNode(unittest.TestCase):
    def test_values(self):
        block = '* First item\n* Last item'
        self.assertEqual(
            ParentNode(
                'ul',
                [
                    ParentNode(
                        'li',
                        [LeafNode(None, 'First item', None)],
                        None
                    ),
                    ParentNode(
                        'li',
                        [LeafNode(None, 'Last item', None)],
                        None
                    ),
                ],
                None
            ),
            ulist_to_html_node(block)
        )

class OlistToHTMLNode(unittest.TestCase):
    def test_values(self):
        block = '1. Numero Uno\n2. Numero Dos'
        self.assertEqual(
            ParentNode(
                'ol',
                [
                    ParentNode(
                        'li',
                        [LeafNode(None, 'Numero Uno', None)],
                        None
                    ),
                    ParentNode(
                        'li',
                        [LeafNode(None, 'Numero Dos', None)],
                        None
                    ),
                ],
                None
            ),
            olist_to_html_node(block)
        )

class BlockToHTMLNode(unittest.TestCase):
    def test_paragraph(self):
        block = '* A list with\n- WRONG\n* formatting!'
        self.assertEqual(
            ParentNode(
                'p',
                [
                    LeafNode( 'i', ' A list with - WRONG ', None),
                    LeafNode(None, ' formatting!', None)
                ],
                None
            ),
            block_to_html_node(block)
        )

class MarkdownToHTMLNode(unittest.TestCase):
    def test_function(self):
        markdown = """# Sample Static Site

## First Heading

This is an example website, let's see if it can manage to do everything that it needs to do.
Otherwise, this whole project would've been a bit silly...

## The worst code

Below has been the **most annoying** bit of code to deal with:

```
def __eq__(self, other):
    if not isinstance(other, HTMLNode):
        return False
    return (self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props)
```

It was:

1. Showing an `AssertionError` that looked correct!
2. Had me and Boots stumped for about an hour!
3. There was so much copying and pasting!
4. Then I mistyped the adjustments I made afterwards, to cause the error to come up again!

As a wise woman once told me:

> Things are easy, once you quit!

### Acknowlegments

Many thank to [Boots](https://boot.dev), I would never have survived without you!"""
        html_node = markdown_to_html_node(markdown)
        html_string = html_node.to_html()
        print(f'\n{html_node}')
