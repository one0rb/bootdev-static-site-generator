from textnode import TextNode, TextType
from inline_markdown import split_nodes_link, extract_markdown_links
from nodeconversion import text_to_text_node

print("hello world")

def main():
    dummy = TextNode("This is some text", TextType.BOLD, "https://boot.dev")
    print(dummy)
    text = "This is some **failed**, not wait, *failed markdown*"
    tester = text_to_text_node(text)
    print(tester)
main()
