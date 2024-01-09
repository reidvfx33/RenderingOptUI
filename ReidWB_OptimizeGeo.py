import maya.cmds as cmds

global geoStats
geoStats = [1,1,0,1,1,1,1,1,1,0]
def createUI(windowTitle):

    windowID = 'myWindoWID'

    if cmds.window(windowID, exists = True):
        cmds.deleteUI(windowID)

    cmds.window( windowID, title = windowTitle, sizeable = True, resizeToFitChildren = True) 
    cmds.columnLayout( adjustableColumn=True )
    cmds.setParent( '..' )
    
    cmds.columnLayout()
    cmds.optionMenu(label='Effect', changeCommand= whatSel)
    cmds.menuItem( label='All Geometry')
    cmds.menuItem( label='Selected Objects' )
    
    cmds.columnLayout()
    cmds.optionMenu('cs', label = 'Cast Shadows', changeCommand = shadowValue)
    cmds.menuItem( label='On')
    cmds.menuItem( label='Off')
    
    cmds.columnLayout()
    cmds.optionMenu('rs', label = 'Recieve Shadows', changeCommand = receiveValue)
    cmds.menuItem( label='On')
    cmds.menuItem( label='Off' )
    
    cmds.columnLayout()
    cmds.optionMenu('ho', label = 'Hold out', changeCommand = holdValue)
    cmds.menuItem( label='Off')
    cmds.menuItem( label='On' )

    cmds.columnLayout()
    cmds.optionMenu('mb', label = 'Motion Blur', changeCommand = motionValue)
    cmds.menuItem( label='On')
    cmds.menuItem( label='Off' )
    cmds.showWindow() 
    
    cmds.columnLayout()
    cmds.optionMenu('pv', label = 'Primary Visibilty', changeCommand = visValue)
    cmds.menuItem( label='On')
    cmds.menuItem( label='Off' )
    
    cmds.columnLayout()
    cmds.optionMenu('ss', label = 'Smooth Shading', changeCommand = smoothValue)
    cmds.menuItem( label='On')
    cmds.menuItem( label='Off' )
    
    cmds.columnLayout()
    cmds.optionMenu('vir', label = 'Visible in Reflections', changeCommand = virValue)
    cmds.menuItem( label='On')
    cmds.menuItem( label='Off' )
    
    cmds.columnLayout()
    cmds.optionMenu('vir2', label = 'Visible in Refractions', changeCommand = viraValue)
    cmds.menuItem( label='On')
    cmds.menuItem( label='Off' )

    
    cmds.columnLayout()
    cmds.optionMenu('ds', label = 'Double Sided', changeCommand = doubleValue)
    cmds.menuItem( label='On')
    cmds.menuItem( label='Off' )

    
    cmds.columnLayout()
    cmds.optionMenu('op', label = 'Opposite', changeCommand = opValue)
    cmds.menuItem( label='Off')
    cmds.menuItem( label='On' )
    
    cmds.columnLayout( adjustableColumn=True )
    cmds.button( label='OK', command = fin)


   



def whatSel( item):        
    global n
    if item == "All Geometry":
        n = 0
    else:

        n = 1

def shadowValue( item ):
    if item == "Off":
        geoStats[0] = 0
    else:
        geoStats[0] = 1

def receiveValue( item ):
    if item == "Off":
        geoStats[1] = 0
    else:
        geoStats[1] = 1    
        
def holdValue( item ):
    if item == "Off":
        geoStats[2] = 0
    else:
        geoStats[2] = 1
def motionValue( item ):
    if item == "Off":
        geoStats[3] = 0
    else:
        geoStats[3] = 1
def visValue( item ):
    if item == "Off":
        geoStats[4] = 0
    else:
        geoStats[4] = 1       
        
def smoothValue( item ):
    if item == "Off":
        geoStats[5] = 0
    else:
        geoStats[5] = 1 
        
def virValue( item ):
    if item == "Off":
        geoStats[6] = 0
    else:
        geoStats[6] = 1 
                         
def viraValue( item ):
    if item == "Off":
        geoStats[7] = 0
    else:
        geoStats[7] = 1

def doubleValue( item ):
    if item == "Off":
        geoStats[8] = 0
    else:
        geoStats[8] = 1 
                         
def opValue( item ):
    if item == "Off":
        geoStats[9] = 0
    else:
        geoStats[9] = 1                                           


def fin(*args):
    if n == 0:
        cmds.SelectAllPolygonGeometry()
        selection = cmds.ls(sl=True)
        for each in selection:
            cmds.setAttr(each + ".castsShadows", geoStats[0])
            cmds.setAttr(each + ".receiveShadows", geoStats[1])
            cmds.setAttr(each + ".holdOut", geoStats[2])
            cmds.setAttr(each + ".motionBlur", geoStats[3])
            cmds.setAttr(each + ".primaryVisibility", geoStats[4])
            cmds.setAttr(each + ".smoothShading", geoStats[5])
            cmds.setAttr(each + ".visibleInReflections", geoStats[6])
            cmds.setAttr(each + ".visibleInRefractions", geoStats[7])
            cmds.setAttr(each + ".doubleSided", geoStats[8])
            cmds.setAttr(each + ".opposite", geoStats[9])    
    if n == 1:
        oneselection = cmds.ls( selection=True )     
        for each in oneselection:
            cmds.setAttr(each + ".castsShadows", geoStats[0])
            cmds.setAttr(each + ".receiveShadows", geoStats[1])
            cmds.setAttr(each + ".holdOut", geoStats[2])
            cmds.setAttr(each + ".motionBlur", geoStats[3])
            cmds.setAttr(each + ".primaryVisibility", geoStats[4])
            cmds.setAttr(each + ".smoothShading", geoStats[5])
            cmds.setAttr(each + ".visibleInReflections", geoStats[6])
            cmds.setAttr(each + ".visibleInRefractions", geoStats[7])
            cmds.setAttr(each + ".doubleSided", geoStats[8])
            cmds.setAttr(each + ".opposite", geoStats[9])            


  

    
   

createUI('Render Optimize')
