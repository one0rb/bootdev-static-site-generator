from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_strings = []
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split_strings = old_node.text.split(delimiter)
        for i in range(len(split_strings)):
            if not split_strings[i]:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_strings[i], TextType.NORMAL))
            else:
                new_nodes.append(TextNode(split_strings[i], text_type))
    return new_nodes
