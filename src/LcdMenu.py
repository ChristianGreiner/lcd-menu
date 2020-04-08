from anytree import NodeMixin


class MenuItem(NodeMixin):
    scene = None
    isRoot = False

    def __init__(self, title, parent=None, children=None):
        super(MenuItem, self).__init__()
        self.title = title
        self.parent = parent
        if children:
            self.children = children

    def set_scene(self, scene):
        self.scene = scene


class LcdScene(MenuItem):
    content = None

    def __init__(self, title):
        self.title = title

    def activated(self):
        pass

    def update(self):
        pass


class LcdHomeScene(LcdScene):

    def __init__(self, title):
        self.title = title


class LcdMainMenu(MenuItem):
    currentNode = None
    depthCounter = 0
    horizontalCounter = 0

    def __init__(self, title, children=None):
        super(LcdMainMenu, self).__init__(title)
        self.isRoot = True
        if title:
            self.title = title
        if children:
            self.children = children
            self.currentNode = children[0]
        pass

    def update(self):
        pass

    def navigate_up(self):
        self.horizontalCounter = 0
        if self.currentNode.parent:
            if not self.currentNode.parent.isRoot:
                self.currentNode = self.currentNode.parent

            return self.currentNode

    def navigate_down(self):
        self.horizontalCounter = 0
        if self.currentNode.children:
            if len(self.currentNode.children) > 0:
                self.currentNode = self.currentNode.children[0]

        return self.currentNode

    def navigate_next(self):
        return self.__get_next_item(1)

    def navigate_previous(self):
        return self.__get_next_item(-1)

    def __get_next_item(self, direction):
        children = self.currentNode.parent.children

        if len(children) > 0:

            self.horizontalCounter += direction

            if self.horizontalCounter > len(children) - 1:
                self.horizontalCounter = 0
            elif self.horizontalCounter < 0:
                self.horizontalCounter = len(children) - 1

            self.currentNode = children[self.horizontalCounter]

            return self.currentNode

    def render(self):
        pass
