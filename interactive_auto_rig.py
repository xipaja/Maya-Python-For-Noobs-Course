
import maya.cmds as cmds
import maya.mel as mel
import sys

def createProxies():
    # Create proxies for the rig to pull in later
    amount = 5
    
    for i in range(amount):
        count = i+1
        loc = cmds.spaceLocator(n = 'locator_{}_proxy'.format(count), p = [0, i*2.5, 0])
        cmds.makeIdentity(loc, a = 1, t = 1)
        mel.eval('CenterPivot;')
        
def createRig():
    # scale compensate - rigging thing
    sc = 0
    locs = cmds.ls('*_proxy')
    
    for loc in locs:
        
        # Check if it has parents
        parentLoc = cmds.listRelatives(loc, p = 1)
        
        # Create joints
        cmds.select(cl = 1)
        jnt = cmds.joint(n = loc.replace('_proxy', '_joint'), sc = sc)
        constraint = cmds.parentConstraint(loc, jnt)
        cmds.delete(constraint)
        cmds.makeIdentity(jnt, a = 1, t = 1, r = 1, s = 1)
        
        # Check if locators have any parents and parent the joint to that
        if(parentLoc):
            parentJoint = parentLoc[0].replace('_proxy', '_joint')
            cmds.parent(jnt, parentJoint)
            
        # Controls
        
        # Creating a control
        con = cmds.circle(n = loc.replace('_proxy', '_control'), ch = 0)
         # Creating a group at origin0
        grp = cmds.group(n = loc.replace('_proxy', '_group'), em = 1, w = 1)
         # parenting the control to that group
        cmds.parent(con, grp)
        cnst = cmds.parentConstraint(loc, grp)
        cmds.delete(cnst)
        cmds.parentConstraint(con, jnt)
        
        if(parentLoc):
             parentControl = parentLoc[0].replace('_proxy', '_control')
             cmds.parent(grp, parentControl)
             
    # delete locators because we don't need them anymore
    cmds.delete(locs)
    sys.stdout.write('Success!')    
             
    
