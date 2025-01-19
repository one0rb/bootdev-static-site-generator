import unittest
from inline_markdown import (
        split_nodes_delimiter,
        extract_markdown_images,
        extract_markdown_links,
        split_nodes_image,
        split_nodes_link
)
from textnode import TextType, TextNode
from htmlnode import LeafNode
from nodeconversion import (
        text_to_text_node,
        text_node_to_html_node
)

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_node(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_nodes = text_to_text_node(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_nodes
        )

    def test_error_raising(self):
        text = "This is some **failed**, not wait, *failed markdown"
        with self.assertRaises(ValueError):
            text_to_text_node(text)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_to_html_normal(self):
        text_node = TextNode("This is nothing special", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(None, html_node.tag)
        self.assertEqual("This is nothing special", html_node.value)

    def test_text_to_html_italic(self):
        text_node = TextNode("This is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual("i", html_node.tag)
        self.assertEqual("This is italic", html_node.value)

    def test_text_to_html_link(self):
        text_node = TextNode("This is an anchor?", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual("a", html_node.tag)
        self.assertEqual("This is an anchor?", html_node.value)
        self.assertEqual({"href": "https://boot.dev"}, html_node.props)

    def test_text_to_html_image(self):
        text_node = TextNode("This should be photo", TextType.IMAGE, "https://boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual("img", html_node.tag)
        self.assertEqual("", html_node.value)
        self.assertEqual({"src": "https://boot.dev", "alt": "This should be photo"}, html_node.props)

    def test_text_to_html_error(self):
        text_node = TextNode("ERROR! ERROR!", "fake_type")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

