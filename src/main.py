from textnode import TextNode, TextType
from markdown import split_nodes_delimiter

print("hello world")

def main():
    dummy = TextNode("This is some text", TextType.BOLD, "https://boot.dev")
    print(dummy)
    node = [
        TextNode('Both **bold** and *italic*', TextType.NORMAL),
    ]
    print(f"Initial text:\n{node}")
    new_nodes = split_nodes_delimiter(node, '**', TextType.BOLD)
    print(f"Italic split result:\n{new_nodes}")
    new_nodes = split_nodes_delimiter(new_nodes, '*', TextType.ITALIC)
    print(f"Bold split result: \n{new_nodes}")

main()
