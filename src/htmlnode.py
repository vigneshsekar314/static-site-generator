class HTMLNode:

    def __init__(self, tag: str | None = None, value: str| None = None, children: list | None = None, props: dict| None = None) -> None:
        if value is None and children is None:
            raise ValueError("either \"value\" or \"children\" should hold a non-None type value.") 
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props = "" 
        if self.props is not None:
            for (key, value) in self.props.items(): 
                props += f" {key}=\"{value}\""
        return props

    def __repr__(self):
        return type(self).__name__ + "(" + self.__nonstr(self.tag) + ", " + self.__nonstr(self.value) + ", " + self.__nonstr(self.children) + ", " + self.__nonstr(self.props) + ")"

    def __nonstr(self, obj) -> str:
        if type(obj) == list:
            chlist = ""
            for i in obj:
                chlist += i.__repr__()
            return chlist
        if type(obj) == dict:
            chlist2 = ""
            for (k,v) in obj.items():
                chlist2 += f" {k}=\"{v}\""
            return chlist2
        return obj if obj is not None else "None"


def main():
    node = HTMLNode("p", "this is a para")
    print(node)

if __name__ == "__main__":
    main()
