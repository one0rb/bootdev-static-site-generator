from copy_tree import copy_tree
from generate_content import generate_pages_recursive


def main():
    copy_tree('static', 'public')
    generate_pages_recursive('content', 'template.html', 'public')
main()
