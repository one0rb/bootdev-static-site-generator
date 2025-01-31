import os
from block_markdown import markdown_to_html_node

def extract_title(md):
    lines = md.split('\n')

    for line in lines:
        if line.startswith('# '):
            return line[2:]
    raise ValueError('No title found')

def generate_page(frm_path, tpl_path, dst_path):
    print(f'Generating page from {frm_path} to {dst_path} using {tpl_path}')

    with open(frm_path, encoding="utf-8") as f:
        md = f.read()

    with open(tpl_path, encoding="utf-8") as f:
        tpl = f.read()

    html_node = markdown_to_html_node(md)
    content = html_node.to_html()
    title = extract_title(md)
    page = tpl.replace('{{ Title }}', title)
    page = page.replace('{{ Content }}', content)
    
    dst_dir = os.path.dirname(dst_path)
    os.makedirs(dst_dir, exist_ok=True)
    with open(dst_path, mode='w', encoding="utf-8") as f:
        f.write(page)

def generate_pages_recursive(src_dir_path, tpl_path, dst_dir_path):
    for file in os.listdir(src_dir_path):
        src_path = os.path.join(src_dir_path, file)
        dst_path = os.path.join(dst_dir_path, file)
        if os.path.isfile(src_path) and file[-3:] == '.md':
            generate_page(src_path, tpl_path, dst_path[:-3] + '.html')
        elif os.path.isdir(src_path):
            generate_pages_recursive(src_path, tpl_path, dst_path)
