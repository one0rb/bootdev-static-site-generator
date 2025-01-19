import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_strings = []
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split_strings = old_node.text.split(delimiter)
        if len(split_strings) % 2 == 0:
            raise ValueError("Invalid markdown: inline styling not formatted correctly!")
        for i in range(len(split_strings)):
            if not split_strings[i]:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_strings[i], TextType.NORMAL))
            else:
                new_nodes.append(TextNode(split_strings[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        md_images = extract_markdown_images(old_node.text)
        if not md_images:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for md_image in md_images:
            sections = remaining_text.split(f"![{md_image[0]}]({md_image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown: image section not closed!")
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(md_image[0], TextType.IMAGE, md_image[1]))
            remaining_text = sections[1]
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        md_links = extract_markdown_links(old_node.text)
        if not md_links:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for md_link in md_links:
            sections = remaining_text.split(f"[{md_link[0]}]({md_link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown: link section not closed!")
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(md_link[0], TextType.LINK, md_link[1]))
            remaining_text = sections[1]
        if sections[1]:
            new_nodes.append(TextNode(sections[1], TextType.NORMAL))
    return new_nodes
