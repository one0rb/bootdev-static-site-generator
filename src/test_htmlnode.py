import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
