import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode

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
            "HTMLNode(tag:h3, value:This is a header, children:None, props:{'color': 'red'})",
            repr(node)
        )

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html()
        )

    def test_to_html_no_tag(self):
        node = ParentNode(None, LeafNode("b", "Bold text"))
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_recursive(self):
        node = ParentNode(
            "table",
            [
                ParentNode(
                    "tr",
                    [
                        LeafNode("td", "Cell one"),
                        LeafNode("td", "Cell two")
                    ]
                )
            ]
        )
        self.assertEqual(
            '<table><tr><td>Cell one</td><td>Cell two</td></tr></table>',
            node.to_html()
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
            "LeafNode(tag:p, value:Hello world!, props:{'class': 'greeting'})",
            repr(node)
        )

if __name__ == "__main__":
    unittest.main()
