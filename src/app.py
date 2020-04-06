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


    while True:
        string = str(input())
        if string == 'd':
            item = menu.navigate_next()
            if item:
                print("> " + item.title)
        if string == 'a':
            item = menu.navigate_previous()
            if item:
                print("> " + item.title)
        if string == 's':
            item = menu.navigate_down()
            if item:
                print("v " + item.title)
        if string == 'w':
            item = menu.navigate_up()
            if item:
                print("/\ " + item.title)

if __name__ == '__main__':
    main()
