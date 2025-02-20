from inline_markdown import text_to_text_node
from textnode import text_node_to_html_node
from htmlnode import ParentNode

bt_head = 'heading'
bt_code = 'code'
bt_quote = 'quote'
bt_ulist = 'unordered_list'
bt_olist = 'ordered_list'
bt_para = 'paragraph'

def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        if not block:
            continue
        filtered_blocks.append(block.strip())
    return filtered_blocks

def block_to_block_type(block):
    lines = block.splitlines()
    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return bt_head
    if len(lines) > 2 and lines[0] == "```" and lines[-1] == "```":
        return bt_code
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return bt_para
        return bt_quote
    if block.startswith('* '):
        for line in lines:
            if not line.startswith('* '):
                return bt_para
        return bt_ulist
    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return bt_para
        return bt_ulist
    if block.startswith('1. '):
        for i, line in enumerate(lines, start=1):
            if not line.startswith(f'{i}. '):
                return bt_para
        return bt_olist
    return bt_para

def text_to_children(text):
    children = []
    text_nodes = text_to_text_node(text)
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.splitlines()
    paragraph = ' '.join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p', children)

def heading_to_html_node(block):
    i = 0
    while block[i] == '#':
        i += 1
    if i + 1 > len(block):
        raise ValueError("Invalid heading!")
    text = block[i + 1:]
    children = text_to_children(text)
    return ParentNode(f'h{i}', children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError('Invalid code block!')
    text = block[4:-4]
    children = text_to_children(text)
    return ParentNode('pre', ParentNode('code', children))

def quote_to_html_node(block):
    lines = block.splitlines()
    stripped_lines = []
    for line in lines:
        if not line.startswith('>'):
            raise ValueError('Invalid blockquote!')
        stripped_lines.append(line.lstrip('> '))
    text = '\n'.join(stripped_lines)
    children = text_to_children(text)
    return ParentNode('blockquote', children)

def ulist_to_html_node(block):
    lines = block.splitlines()
    children = []
    for line in lines:
        if not line.startswith('* ') and not line.startswith('- '):
            raise ValueError('Invalid unordered list!')
        stripped_line = line[2:]
        child = text_to_children(stripped_line)
        children.append(ParentNode('li', child))
    return ParentNode('ul', children)

def olist_to_html_node(block):
    lines = block.splitlines()
    children = []
    for i, line in enumerate(lines, start=1):
        stripped_line = line.lstrip(f'{i}. ')
        child = text_to_children(stripped_line)
        children.append(ParentNode('li', child))
    return ParentNode('ol', children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == bt_para:
        return paragraph_to_html_node(block)
    if block_type == bt_head:
        return heading_to_html_node(block)
    if block_type == bt_code:
        return code_to_html_node(block)
    if block_type == bt_quote:
        return quote_to_html_node(block)
    if block_type == bt_ulist:
        return ulist_to_html_node(block)
    if block_type == bt_olist:
        return olist_to_html_node(block)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode('div', children)
