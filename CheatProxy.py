import wx
import _winreg as winreg

#---------------------------------
#A wrapper class to emulate static class methods
class Callable:
  def __init__(self, anycallable):
    self.__call__ = anycallable

#---------------------------------
class RootType:
  #An enumeration of values corresponding to the high score preferences
  #in the GUI.
  HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE = range (2)

  #=================================
  def GetKey (root):
    #Emulation of a switch statement
    value = {
      RootType.HKEY_CURRENT_USER: lambda: winreg.HKEY_CURRENT_USER,
      RootType.HKEY_LOCAL_MACHINE: lambda: winreg.HKEY_LOCAL_MACHINE
    }[root]()

    return value
  GetKey = Callable (GetKey)

#---------------------------------
class CheatProxy:
  #=================================
  def __init__ (self, root = RootType.HKEY_CURRENT_USER, path = "Software\\Microsoft\\Plus!\\Pinball\\SpaceCadet"):
    """ Path is the path where the keys are located for the Pinball game """
    
    self.root = root
    self.path = path
    self.Open ()

  #=================================
  def Open (self, root = None, path = None):
    """ Opens a given registry path for this object """

    if (root == None):
      root = self.root
    if (path == None):
      path = self.path
    
    try:
      self.key = winreg.OpenKey (RootType.GetKey (root), path, 0, winreg.KEY_ALL_ACCESS)
    except EnvironmentError:
      wx.MessageBox ("Error in opening registry key.", "Error", wx.ICON_ERROR)
      self.key = None

    self.root = root
    self.path = path

  #=================================
  def GetName (self, rank):
    """ Gets the name of a person of a particular rank """
    
    name = ""
    
    try:
      name = winreg.QueryValueEx (self.key, str (int (rank) - 1) + ".Name")[0]
    except EnvironmentError:
      raise Exception ("Could not query value")

    return name

  #=================================
  def GetScore (self, rank):
    """ Gets the score of a person of a particular rank """

    score = ""

    try:
     score = winreg.QueryValueEx (self.key, str (int (rank) - 1) + ".Score")[0]
    except EnvironmentError:
      raise Exception ("Could not query value.")

    return score

  #=================================
  def Save (self, namelist, scorelist):
    """ Saves the values to the registry. The name and score list
        must be in the correct order, and must be no more than 5 entries. """

    for x in xrange (len (namelist)):
      winreg.SetValueEx (self.key, str (x) + ".Name", 0, winreg.REG_SZ, namelist[x])

    for x in xrange (len (scorelist)):
      winreg.SetValueEx (self.key, str (x) + ".Score", 0, winreg.REG_SZ, scorelist[x])

    val = self.CalculateVerification (namelist, scorelist)
    winreg.SetValueEx (self.key, "Verification", 0, winreg.REG_SZ, str (val))

  #=================================
  def CalculateVerification (self, namelist, scorelist):
    """ The Pinball game doesn't want just everyone modifying its scores
        via the registry. So they add a verification to make sure that the
        scores in the registry are correct. This calculates that verification """

    val = 0
    for x in xrange (len (namelist)):
      for y in xrange (len (namelist[x])):
        val += ord (namelist[x][y])

    for x in xrange (len (scorelist)):
      val += int (scorelist[x])

    return val
