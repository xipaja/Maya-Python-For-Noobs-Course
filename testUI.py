import maya.cmds as cmds

def createUI():
    win = 'testUI'
    if (cmds.window(win, exists = 1)):
        cmds.deleteUI(win)
        
    cmds.window(win, rtf = 1, w = 280, h = 280, t = win, s = 1)
    cmds.columnLayout(adj = 1)
    
    cmds.button()
    cmds.button()
    cmds.textField()
    cmds.intSlider()
    cmds.floatSlider()
    cmds.text(l = 'l is label')
    cmds.textScrollList()
    
    # nc = num of columns, nr = num of rows
    cmds.rowColumnLayout(nc = 2)    
    cmds.button()
    cmds.button()
    cmds.button()
    cmds.button()
    
    # this goes back to the og layout
    cmds.setParent('..')
    # l is label and c is command - basically an onClick
    cmds.button(l = 'label', c = 'print "yes"')
    # the lambda here makes sure the func you define is available in 
    cmds.button(l = 'label2', c = lambda x: func1())
    # or you can do this but it's hacky too 
    cmds.button(l = 'test label', c = 'import testUI; reload(testUI); testUI.func1()')
    cmds.button()
    cmds.button()

    
    cmds.showWindow(win)
        
createUI()

def func1():
    print 'yes'