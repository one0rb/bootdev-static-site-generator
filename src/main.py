from textnode import TextNode, TextType

print("hello world")

def main():
    dummy = TextNode("This is some text", TextType.BOLD, "https://boot.dev")
    print(dummy)

main()
