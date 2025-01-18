import unittest
from markdown import split_nodes_delimiter
from textnode import TextType, TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = [
                TextNode('This is text with a `code block` word', TextType.NORMAL)
        ]
        new_nodes = split_nodes_delimiter(node, '`', TextType.CODE)
        self.assertEqual(
                [
                    TextNode('This is text with a ', TextType.NORMAL),
                    TextNode('code block', TextType.CODE),
                    TextNode(' word', TextType.NORMAL)
                ],
                new_nodes
        )

    def test_split_nodes_delimiter_multiple_selections(self):
        node = [
                TextNode('Text with **bold**, **bolder** and **boldest** styles', TextType.NORMAL),
        ]
        new_nodes = split_nodes_delimiter(node, '**', TextType.BOLD)
        self.assertEqual(
                [
                    TextNode('Text with ', TextType.NORMAL),
                    TextNode('bold', TextType.BOLD),
                    TextNode(', ', TextType.NORMAL),
                    TextNode('bolder', TextType.BOLD),
                    TextNode(' and ', TextType.NORMAL),
                    TextNode('boldest', TextType.BOLD),
                    TextNode(' styles', TextType.NORMAL)
                ],
                new_nodes
        )

    def test_split_node_delimiter_multiple_styles(self):
        node = [
            TextNode('Both **bold** and *italic*', TextType.NORMAL),
        ]
        new_nodes = split_nodes_delimiter(node, '**', TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, '*', TextType.ITALIC)
        self.assertEqual(
                [
                    TextNode('Both ', TextType.NORMAL),
                    TextNode('bold', TextType.BOLD),
                    TextNode(' and ', TextType.NORMAL),
                    TextNode('italic', TextType.ITALIC)
                ],
                new_nodes
        )

