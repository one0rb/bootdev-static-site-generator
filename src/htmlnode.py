# look through boot.dev and add in the __eq__ method to all these classes
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if not self.props:
            return ""
        props_html = ""
        for key,value in self.props.items():
            props_html += f" {key}=\"{value}\""
        return props_html

    def __repr__(self):
        return f"HTMLNode(tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: no tag")
        if not self.children:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        if isinstance(self.children, list):
            for child in self.children:
                children_html += child.to_html()
        else:
            children_html += self.children.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode(tag:{self.tag}, children:{self.children}, props:{self.props})"

    def __eq__(self, other):
        if not isinstance(other, ParentNode):
            return False
        return (self.tag == other.tag and
                self.children == other.children and
                self.props == other.props)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
 
    def __repr__(self):
        return f"LeafNode(tag:{self.tag}, value:{self.value}, props:{self.props})"

    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return (self.tag == other.tag and 
                self.value == other.value and 
                self.props == other.props)
