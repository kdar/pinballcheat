import sys
import wx
from wx import xrc

import MainFrame as mf

#---------------------------------
class MainApp (wx.App):
  #=================================
  def __init__ (self):
    wx.App.__init__ (self, redirect = False)

  #=================================
  def OnInit (self):
    self.res = xrc.XmlResource ("resource.xml")
    self.frame = mf.MainFrame (None, self.res)

    self.SetTopWindow (self.frame)
    self.frame.Show (True)    
    
    return True

#=================================
def main (argv):
  app = MainApp ()
  app.MainLoop ()

#=================================
if (__name__ == "__main__"):
  main (sys.argv)
