from LcdMenu import LcdMainMenu, MenuItem, LcdScene
from anytree import NodeMixin, RenderTree, Walker

menu = None

def main():
    menu = LcdMainMenu('MainMenu', children= [
        MenuItem('System', children=[
            MenuItem('Network', children=[
                MenuItem('IP-Stuff', children=[
                    LcdScene('TestScene')
                ])
            ]),
            MenuItem('CPU'),
            MenuItem('GPU')
        ]),
        MenuItem('Data')
    ])

    for pre, _, node in RenderTree(menu):
        treestr = u"%s%s" % (pre, node.title)
        print(treestr.ljust(8))

    item = menu.navigate_next()
    print("> " + item.title)
    item = menu.navigate_next()
    print("> " + item.title)
    item = menu.navigate_down()

    if item is not None:
        print("v " + item.title)

        item = menu.navigate_next()

        if item is not None:
            print("> " + item.title)

            item = menu.navigate_next()

            if item is not None:
                print("> " + item.title)

                item = menu.navigate_previous()

                if item is not None:
                    print("> " + item.title)
if __name__ == '__main__':
    main()
