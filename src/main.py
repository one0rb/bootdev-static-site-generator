from textnode import TextNode, TextType
from markdown import split_nodes_link, extract_markdown_links

print("hello world")

def main():
    dummy = TextNode("This is some text", TextType.BOLD, "https://boot.dev")
    print(dummy)
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.NORMAL,
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)
main()
