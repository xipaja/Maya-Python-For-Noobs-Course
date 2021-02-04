import maya.cmds as cmds
import maya.mel as mel
import sys

def ui():

    # UI Basics
    win = 'ConnectAttrsTestUI'
    if(cmds.window(win, exists = 1)):
        cmds.deleteUI(win)

    cmds.window(win, rtf = 1, w = 2, h = 2, t = 'Connect Attributes', s = 1)
    cmds.columnLayout(adj = 1)

    # Fill with stuff

    cmds.rowColumnLayout(nc = 2)
    # first parameter is the global name Maya will know it as - useful for querying; tx is text
    cmds.textField('cat_driver_tf', tx = 'Drivers', w = 250)
    cmds.button(l = 'Load', c = lambda x: loadDriver())

    cmds.textField('cat_driven_tf', tx = 'Driven', w = 250)
    cmds.button(l = 'Load', c = lambda x: loadDriven())

    # Reset layout so the next button will take up the normal full space of the UI
    cmds.setParent('..')

    # use the import format here so we don't have to reload every time we run/test
    cmds.button(l = 'Run', c = 'import connectAttrsTest as cat; reload(cat); cat.run()')

    # Launch UI
    cmds.showWindow(win)


def loadDriver():
    # Query what obj you have selected and what attr in the channel box you have selected
    # Then will fill in the text field with what you have selected

    # List selections
    selected = cmds.ls(sl = 1)
    # We're only supporting one selection in this tool, so make sure user has only selected one obj
    if len(selected) != 1:
        cmds.warning('Please select only 1 object!')
    else:
        # Fill text field with the info we have now
        obj = selected[0]
        # Query the attrs that are selected in the channel box
        # First param is what channel box it is, and it's always gonna be mainChannelBox
        # q is a query flag, and sma is selected main attributes
        attrs = cmds.channelBox('mainChannelBox', q = 1, sma = 1)
        
        if not attrs:
           cmds.warning('Please select 1 attribute!')
        else:
            if len(attrs) != 1:
                cmds.warning('Please select 1 attribute!')
            else:
                # If one obj is selected and one attr is selected, print which obj and which attr they are
                attr = attrs[0]
                print '{}.{}'.format(obj, attr)

                # first param is global name, e is edit mode, tx is text
                cmds.textField('cat_driver_tf', e = 1, tx = '{}.{}'.format(obj, attr))

def loadDriven():
    # Grab multple objs and one attr you have selected in the channel box, and add the attr to the end
    # of each one in that obj list

    selected = cmds.ls(sl = 1)
   
    attrs = cmds.channelBox('mainChannelBox', q = 1, sma = 1)
    if not attrs:
        cmds.warning('Please select 1 attribute')
    else:
        if len(attrs) != 1:
            cmds.warning('Please select 1 attribute')
        else:
            attr = attrs[0]
            outputs = []
            # Format selected names without the Maya "u"
            # Append the attr to the end of it before we make it part of the list
            for obj in selected:
                output = '{}.{}'.format(obj, attr)
                outputs.append(str(output))

            # Format string
            outputs = str(outputs).replace('[', '')
            outputs = str(outputs).replace(']', '')
            outputs = str(outputs).replace("'", '')

            cmds.textField('cat_driven_tf', e = 1, tx = outputs)
            print outputs


def run():
    # Query driver and driven text fields
    driver = cmds.textField('cat_driver_tf', q = 1, tx = 1)
    driven = cmds.textField('cat_driven_tf', q = 1, tx = 1)
    
    # We want the drivens as a string
    # exec means run whatever's in the parenthesis as one line of code
    toExec = "['{}']".format(driven)
    toExec = toExec.replace(",", "', '")

    print toExec

    exec('drivens = {}'.format(toExec))

    # Now they are connected, so say the driver is tx of one sphere and the driven are tx of the 
    # other spheres, moving tx on the one sphere would now move the other spheres on their tz axis
    for i in drivens:
        print i
        cmds.connectAttr(driver, i)