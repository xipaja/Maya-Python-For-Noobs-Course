import maya.cmds as cmds
import maya.mel as mel
import sys

# Create groups
cmds.group(n = 'joints_group', em = 1, w = 1)
cmds.group(n = 'control_group', em = 1, w = 1)

# Clear selection
cmds.select(cl = 1)

# Create joints
cmds.joint(n = 'shoulder_joint')
cmds.joint(n = 'elbow_joint', p = [6, 0, 0])
cmds.joint(n = 'wrist_joint', p = [12, 0, 0])
cmds.parent('shoulder_joint', 'joints_group')

# Create control hierarchy
cmds.circle(n = 'shoulder_control', ch = 0, r = 2)
cmds.setAttr('shoulder_control.ry', 90)

cmds.circle(n = 'elbow_control', ch = 0, r = 2)
cmds.setAttr('elbow_control.ry', 90)
cmds.setAttr('elbow_control.tx', 6)

cmds.circle(n = 'wrist_control', ch = 1, r = 2)
cmds.setAttr('wrist_control.ry', 90)
cmds.setAttr('wrist_control.tx', 12)

cmds.parent('wrist_control', 'elbow_control')
cmds.parent('elbow_control', 'shoulder_control')
cmds.parent('shoulder_control', 'control_group')

# Freeze tranforms
cmds.makeIdentity('control_group', a = 1, t = 1, r = 1, s = 1)

# Constraints
cmds.parentConstraint('shoulder_control', 'shoulder_joint')
cmds.parentConstraint('elbow_control', 'elbow_joint')
cmds.parentConstraint('wrist_control', 'wrist_joint')

# Cleaning up
sys.stdout.write('Created arm rig')