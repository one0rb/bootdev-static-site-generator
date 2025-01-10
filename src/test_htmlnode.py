import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("div","I wish I could read")
        self.assertEqual("div", node.tag)
        self.assertEqual("I wish I could read", node.value)
        self.assertEqual(None, node.children)
        self.assertEqual(None, node.props)

    def test_to_html(self):
        node =HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(
            ' href="https://boot.dev" target="_blank"', node.props_to_html()
        )

    def test_repr(self):
        node = HTMLNode("h3", "This is a header", None, {"color": "red"})
        self.assertEqual(
            "HTMLNode(h3, This is a header, children: None, {'color': 'red'})",
            repr(node)
        )

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "Hello world!", {"class": "greeting"})
        self.assertEqual(
            '<p class="greeting">Hello world!</p>', node.to_html()
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello world!")
        self.assertEqual(
            'Hello world!', node.to_html()
        )

    def test_to_html_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr(self):
        node = LeafNode("p", "Hello world!", {"class": "greeting"})
        self.assertEqual(
            "LeafNode(p, Hello world!, {'class': 'greeting'})", repr(node)
        )

if __name__ == "__main__":
    unittest.main()
