import dynMenu
import dbInterface

myDB = dbInterface.createDB('test.db')
glob = "Test"

def test():
    print(glob)
    input()

def test2():
    det = myDB.getTableRows('CPU')
    line = ''
    for c in det:
        line += str(c[0]) + ' '
    b = dynMenu.Menu(line, True, a)
    det = myDB.getAllDetails('CPU')
    for c in det:
        line = ''
        for l in c:
            line += str(l) + '; '
        b.register_action(None, line)
    b.start()
    print(det[b.selected-2])
    input()


a = dynMenu.Menu("Test!!")
a.register_action(test, "Test!")
a.register_action(test2, "Another test!!!")
a.start()