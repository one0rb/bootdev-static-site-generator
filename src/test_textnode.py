import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_eq_false_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false_diff_texttype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_false_diff_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://one0rb.github.io")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, bold, https://boot.dev)",
            repr(node)
        )

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

if __name__ == "__main__":
    unittest.main()
