import maya.cmds as cmds
import maya.mel as mm


# Scripts
def rotateMath(axis):
	degrees = [0, 90, 180, 270]
	currentRotVal = 0
	newRotValue = 0
	#look at the nearest degree the current rotation is in
	sel = cmds.ls(sl=True)
	for s in sel:
		currentRotVal = cmds.getAttr( s + axis)

		#rotate to the next available rotation value
		#look at the first value in the array
		for a in degrees:
			#if the currentRot is greater than, look at the next one
			if currentRotVal >= a: pass

			#if its greater than 270, then current is 0
			elif currentRotVal > max(degrees): newRotValue=0
			#else currentVal is current # in array
			else:
				newRotValue = a
				break

	return newRotValue

def r90x(*args):
	sel=cmds.ls(sl=True)
	for s in sel:
		cmds.setAttr(s+'.rotateX', rotateMath('.rotateX'))
   	 	cmds.setAttr(s+'.rotateY', 0)
		cmds.setAttr(s+'.rotateZ', 0)

def zn(*args):
	sel=cmds.ls(sl=True)
	for s in sel:
		cmds.setAttr(s+'.rotateX', 0)
		cmds.setAttr(s+'.rotateY', 0)
		cmds.setAttr(s+'.rotateZ', rotateMath('.rotateZ'))

def r90y(*args):
	sel=cmds.ls(sl=True)
	for s in sel:
		cmds.setAttr(s+'.rotateX', 0)
		cmds.setAttr(s+'.rotateY', rotateMath('.rotateY'))
		cmds.setAttr(s+'.rotateZ', 0)

def rotateZero(*args):
	sel=cmds.ls(sl=True)
	for s in sel:
   	 	cmds.setAttr(s+'.rotateX', 0)
		cmds.setAttr(s+'.rotateY', 0)
		cmds.setAttr(s+'.rotateZ', 0)

def loadWin(*args):
	# Make a new window
	#
	if cmds.window( 'toolwin', exists=True): cmds.deleteUI('toolwin', window=True)
	else: pass

	if cmds.dockControl('tooldock', exists=True): cmds.deleteUI('tooldock',control=True)
	else: pass

	globalWidth=160
	window = cmds.window( 'toolwin', title="Gabes QModeling Tool", iconName='Short Name', widthHeight=(200, globalWidth) )
	cmds.columnLayout( adjustableColumn=True )
	cmds.text( label='GENERAL' )
	cmds.button( label='Center Pivot', command=('import maya.mel as mm; mm.eval("CenterPivot")'))
	cmds.button( label='Delete All History', command=('mm.eval("DeleteHistory;delete -ch;")'))
	cmds.separator(height=10, style='none')

	cmds.text( label='ROTATE' )
	cmds.button( label='Rotate 90 X', command=r90x)
	cmds.button( label='Rotate 90 Y', command=r90y)
	cmds.button( label='Rotate 90 Z', command=zn)
	cmds.button( label='Rotate 0', command=rotateZero)
	cmds.separator(height=10, style='none')

	cmds.text( label='SELECT' )
	cmds.button( label='Duplicate Special', command=('mm.eval("instance; scale -r -1 1 1;")'))
	cmds.button( label='Select Edge Loop', command=('mm.eval("SelectEdgeLoopTool")'))
	cmds.button( label='Select Edge Ring', command=('mm.eval("SelectEdgeRingTool;")'))
	cmds.button( label='Edge to Face', command=('mm.eval("ConvertSelectionToFaces; PolySelectConvert 1;")'))
	cmds.button( label='Deselect All', command=('mm.eval("select -cl; autoUpdateAttrEd; statusLineUpdateInputField;")'))
	cmds.separator(height=10, style='none')

	cmds.text( label='CREATE' )
	cmds.button( label='Create Poly Tool', command=('mm.eval("setToolTo polyCreateFacetContext ; polyCreateFacetCtx -e -pc `optionVar -q polyKeepFacetsPlanar` polyCreateFacetContext")'))
	cmds.separator(height=10, style='none')

	cmds.text( label='MESH EDIT' )
	cmds.button( label='Combine', command=('mm.eval("polyUnite -ch 1 -mergeUVSets 1;")'))
	cmds.button( label='Seperate', command=('mm.eval(" polySeparate -ch 1;")'))
	cmds.separator(height=1)
	cmds.button( label='Extrude', command=('mm.eval("PolyExtrude")'))
	cmds.button( label='Insert Edge Loop', command=('mm.eval("SplitEdgeRingTool")'))
	cmds.button( label='iSplit Tool', command=('mm.eval("InteractiveSplitTool")'))
	cmds.separator(height=20, style='none')
	cmds.button( label='Save', command=('cmds.file(save=True); print "save"') )
	cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )

	allowedAreas = ['right', 'left']
	cmds.dockControl( 'tooldock', width=globalWidth, area='left', content='toolwin', allowedArea=allowedAreas, label='Gabes QModeling Tool' )

	cmds.setParent( '..' )
	cmds.showWindow( window )
