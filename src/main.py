from textnode import TextNode, TextType
import re
from inline_markdown import text_to_text_node
from textnode import text_node_to_html_node
from htmlnode import ParentNode
from block_markdown import text_to_children

print("hello world")

def main():
    text = "This is *very* important text. **Please read this carefully!** Keep doing what you're doing."
    nodes = text_to_text_node(text)
    print("Text nodes:", [(node.text, node.text_type) for node in nodes])
    html_nodes = [text_node_to_html_node(node) for node in nodes]
    print("HTML nodes:", [(node.tag, node.value) for node in html_nodes])
main()
