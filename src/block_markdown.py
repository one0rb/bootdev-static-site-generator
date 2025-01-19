def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        if not block:
            continue
        filtered_blocks.append(block.strip())
    return filtered_blocks
