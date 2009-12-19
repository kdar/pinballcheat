import wx
from wx import xrc

import ConfigParser
import string
import os

import CheatProxy as cp

#---------------------------------
class MainFrame (wx.Frame):
  #=================================
  def PreCreate (self, pre):
    """ This function is called during the class's initialization.
        
    Override it for custom setup before the window is created usually to
    set additional window styles using SetWindowStyle() and SetExtraStyle()."""
    pass

  #=================================
  def __init__ (self, parent, res):
    pre = wx.PreFrame ()
    self.PreCreate (pre)
    res.LoadOnFrame (pre, parent, "Id_Main_Frame")
    self.PostCreate (pre)

    self.cmdHighScoreMenu = xrc.XRCCTRL (self, "Id_HighScore_Menu_Cmd")
    self.cmdHighScoreShiftup = xrc.XRCCTRL (self, "Id_HighScore_Shiftup_Cmd")
    self.cmdHighScoreShiftdown = xrc.XRCCTRL (self, "Id_HighScore_Shiftdown_Cmd")
    self.cmdHighScoreReset = xrc.XRCCTRL (self, "Id_HighScore_Reset_Cmd")
    self.cmdHighScoreSaveToFile = xrc.XRCCTRL (self, "Id_HighScore_SaveToFile_Cmd")
    self.cmdHighScoreLoadFromFile = xrc.XRCCTRL (self, "Id_HighScore_LoadFromFile_Cmd")
    self.menuHighScore = res.LoadMenu ("Id_HighScore_Menu")
    self.cmdHighScoreSave = xrc.XRCCTRL (self, "Id_HighScore_Save_Cmd")
    self.cmdHighScoreUndo = xrc.XRCCTRL (self, "Id_HighScore_Undo_Cmd")
    self.cmdHighScoreRetrieve = xrc.XRCCTRL (self, "Id_HighScore_Retrieve_Cmd")
    self.rdoHighScoreRoot = xrc.XRCCTRL (self, "Id_HighScore_Root_Rdo")
    self.txtHighScorePath = xrc.XRCCTRL (self, "Id_HighScore_Path_Txt")
    self.txtHighScoreName1 = xrc.XRCCTRL (self, "Id_HighScore_Name1_Txt")
    self.txtHighScoreScore1 = xrc.XRCCTRL (self, "Id_HighScore_Score1_Txt")
    self.txtHighScoreName2 = xrc.XRCCTRL (self, "Id_HighScore_Name2_Txt")
    self.txtHighScoreScore2 = xrc.XRCCTRL (self, "Id_HighScore_Score2_Txt")
    self.txtHighScoreName3 = xrc.XRCCTRL (self, "Id_HighScore_Name3_Txt")
    self.txtHighScoreScore3 = xrc.XRCCTRL (self, "Id_HighScore_Score3_Txt")
    self.txtHighScoreName4 = xrc.XRCCTRL (self, "Id_HighScore_Name4_Txt")
    self.txtHighScoreScore4 = xrc.XRCCTRL (self, "Id_HighScore_Score4_Txt")
    self.txtHighScoreName5 = xrc.XRCCTRL (self, "Id_HighScore_Name5_Txt")
    self.txtHighScoreScore5 = xrc.XRCCTRL (self, "Id_HighScore_Score5_Txt")
    self.menuExit = xrc.XRCCTRL (self, "Id_Menu_Exit")
    self.mainStatus = xrc.XRCCTRL (self, "Id_Main_Status")

    self.Bind (wx.EVT_BUTTON, self.OnCmd_HighScore_Menu, id = xrc.XRCID ("Id_HighScore_Menu_Cmd"))
    self.Bind (wx.EVT_MENU, self.OnCmd_HighScore_Shiftup, id = xrc.XRCID ("Id_HighScore_Shiftup_Cmd"))
    self.Bind (wx.EVT_MENU, self.OnCmd_HighScore_Shiftdown, id = xrc.XRCID ("Id_HighScore_Shiftdown_Cmd"))
    self.Bind (wx.EVT_MENU, self.OnCmd_HighScore_Reset, id = xrc.XRCID ("Id_HighScore_Reset_Cmd"))
    self.Bind (wx.EVT_MENU, self.OnCmd_HighScore_SaveToFile, id = xrc.XRCID ("Id_HighScore_SaveToFile_Cmd"))
    self.Bind (wx.EVT_MENU, self.OnCmd_HighScore_LoadFromFile, id = xrc.XRCID ("Id_HighScore_LoadFromFile_Cmd"))    
    self.Bind (wx.EVT_BUTTON, self.OnCmd_HighScore_Save, id = xrc.XRCID ("Id_HighScore_Save_Cmd"))
    self.Bind (wx.EVT_BUTTON, self.OnCmd_HighScore_Undo, id = xrc.XRCID ("Id_HighScore_Undo_Cmd"))
    self.Bind (wx.EVT_BUTTON, self.OnCmd_HighScore_Retrieve, id = xrc.XRCID ("Id_HighScore_Retrieve_Cmd"))
    self.Bind (wx.EVT_MENU, self.OnCloseWindow, id = xrc.XRCID ("Id_Menu_Exit"))

    self.Bind (wx.EVT_CLOSE, self.OnCloseWindow)    

    self.cheat = cp.CheatProxy ()
    self.PopulateEntries ()

  #=================================
  def PopulateEntries (self):
    try:
      self.txtHighScoreName1.SetValue (self.cheat.GetName (1))
      self.txtHighScoreScore1.SetValue (self.cheat.GetScore (1))
      self.txtHighScoreName2.SetValue (self.cheat.GetName (2))
      self.txtHighScoreScore2.SetValue (self.cheat.GetScore (2))
      self.txtHighScoreName3.SetValue (self.cheat.GetName (3))
      self.txtHighScoreScore3.SetValue (self.cheat.GetScore (3))
      self.txtHighScoreName4.SetValue (self.cheat.GetName (4))
      self.txtHighScoreScore4.SetValue (self.cheat.GetScore (4))
      self.txtHighScoreName5.SetValue (self.cheat.GetName (5))
      self.txtHighScoreScore5.SetValue (self.cheat.GetScore (5))

      self.EnableControls (1)
      self.mainStatus.SetStatusText (" Retrieved data from registry successfully")
    except Exception:
      self.EnableControls (0)
      self.mainStatus.SetStatusText (" Error retrieving data from registry")

  #=================================
  def EnableControls (self, enable):
    self.txtHighScoreName1.Enable (enable)
    self.txtHighScoreScore1.Enable (enable)
    self.txtHighScoreName2.Enable (enable)
    self.txtHighScoreScore2.Enable (enable)
    self.txtHighScoreName3.Enable (enable)
    self.txtHighScoreScore3.Enable (enable)
    self.txtHighScoreName4.Enable (enable)
    self.txtHighScoreScore4.Enable (enable)
    self.txtHighScoreName5.Enable (enable)
    self.txtHighScoreScore5.Enable (enable)
    self.cmdHighScoreSave.Enable (enable)
    self.cmdHighScoreUndo.Enable (enable)
    self.cmdHighScoreMenu.Enable (enable)

  #=================================
  def OnCloseWindow (self, event):
    self.Destroy ()

  #=================================
  def OnCmd_HighScore_Menu (self, event):
    self.PopupMenu (self.menuHighScore)

  #=================================
  def OnCmd_HighScore_Shiftup (self, event):
    self.txtHighScoreName1.SetValue (self.txtHighScoreName2.GetValue ())
    self.txtHighScoreScore1.SetValue (self.txtHighScoreScore2.GetValue ())
    self.txtHighScoreName2.SetValue (self.txtHighScoreName3.GetValue ())
    self.txtHighScoreScore2.SetValue (self.txtHighScoreScore3.GetValue ())
    self.txtHighScoreName3.SetValue (self.txtHighScoreName4.GetValue ())
    self.txtHighScoreScore3.SetValue (self.txtHighScoreScore4.GetValue ())
    self.txtHighScoreName4.SetValue (self.txtHighScoreName5.GetValue ())
    self.txtHighScoreScore4.SetValue (self.txtHighScoreScore5.GetValue ())
    self.txtHighScoreName5.SetValue ("")
    self.txtHighScoreScore5.SetValue ("-999")

    self.mainStatus.SetStatusText (" Shifted entries up")

  #=================================
  def OnCmd_HighScore_Shiftdown (self, event):
    self.txtHighScoreName5.SetValue (self.txtHighScoreName4.GetValue ())
    self.txtHighScoreScore5.SetValue (self.txtHighScoreScore4.GetValue ())
    self.txtHighScoreName4.SetValue (self.txtHighScoreName3.GetValue ())
    self.txtHighScoreScore4.SetValue (self.txtHighScoreScore3.GetValue ())
    self.txtHighScoreName3.SetValue (self.txtHighScoreName2.GetValue ())
    self.txtHighScoreScore3.SetValue (self.txtHighScoreScore2.GetValue ())
    self.txtHighScoreName2.SetValue (self.txtHighScoreName1.GetValue ())
    self.txtHighScoreScore2.SetValue (self.txtHighScoreScore1.GetValue ())   
    self.txtHighScoreName1.SetValue ("")
    self.txtHighScoreScore1.SetValue ("-999")

    self.mainStatus.SetStatusText (" Shifted entries down")

  #=================================
  def OnCmd_HighScore_Reset (self, event):
    self.txtHighScoreName1.SetValue ("")
    self.txtHighScoreScore1.SetValue ("-999")
    self.txtHighScoreName2.SetValue ("")
    self.txtHighScoreScore2.SetValue ("-999")
    self.txtHighScoreName3.SetValue ("")
    self.txtHighScoreScore3.SetValue ("-999")
    self.txtHighScoreName4.SetValue ("")
    self.txtHighScoreScore4.SetValue ("-999")
    self.txtHighScoreName5.SetValue ("")
    self.txtHighScoreScore5.SetValue ("-999")

    self.mainStatus.SetStatusText (" All entries were reset. Click \"undo\" to undo these changes")

  #=================================
  def OnCmd_HighScore_SaveToFile (self, event):
    config = ConfigParser.ConfigParser ()
    config.add_section ("High scores")
    config.set ("High scores", "0.Name", self.txtHighScoreName1.GetValue ())
    config.set ("High scores", "0.Score", self.txtHighScoreScore1.GetValue ())
    config.set ("High scores", "1.Name", self.txtHighScoreName2.GetValue ())
    config.set ("High scores", "1.Score", self.txtHighScoreScore2.GetValue ())
    config.set ("High scores", "2.Name", self.txtHighScoreName3.GetValue ())
    config.set ("High scores", "2.Score", self.txtHighScoreScore3.GetValue ())
    config.set ("High scores", "3.Name", self.txtHighScoreName4.GetValue ())
    config.set ("High scores", "3.Score", self.txtHighScoreScore4.GetValue ())
    config.set ("High scores", "4.Name", self.txtHighScoreName5.GetValue ())
    config.set ("High scores", "4.Score", self.txtHighScoreScore5.GetValue ())

    dlg = wx.FileDialog (
      self, message = "Save file as ...", 
      defaultDir = os.getcwd (), 
      defaultFile = "", 
      wildcard = "INI (*.ini)|*.ini|All files (*.*)|*.*", 
      style = wx.SAVE
    )

    if (dlg.ShowModal () == wx.ID_OK):
      f = open (dlg.GetPath (), "w")
      config.write (f)
      f.close ()

    dlg.Destroy ()

  #=================================
  def OnCmd_HighScore_LoadFromFile (self, event):
    dlg = wx.FileDialog (
      self, message = "Choose a file",
      defaultDir = os.getcwd (), 
      defaultFile = "",
      wildcard = "INI (*.ini)|*.ini|All files (*.*)|*.*",
      style=wx.OPEN | wx.CHANGE_DIR
    )

    if (dlg.ShowModal() == wx.ID_OK):
      config = ConfigParser.ConfigParser ()
      list = config.read (dlg.GetPath ())

      if (list == None):
        self.mainStatus.SetStatusText (" Unable to read saved scores")
      else:
        self.txtHighScoreName1.SetValue (config.get ("High scores", "0.Name"))
        self.txtHighScoreScore1.SetValue (config.get ("High scores", "0.Score"))
        self.txtHighScoreName2.SetValue (config.get ("High scores", "1.Name"))
        self.txtHighScoreScore2.SetValue (config.get ("High scores", "1.Score"))
        self.txtHighScoreName3.SetValue (config.get ("High scores", "2.Name"))
        self.txtHighScoreScore3.SetValue (config.get ("High scores", "2.Score"))
        self.txtHighScoreName4.SetValue (config.get ("High scores", "3.Name"))
        self.txtHighScoreScore4.SetValue (config.get ("High scores", "3.Score"))
        self.txtHighScoreName5.SetValue (config.get ("High scores", "4.Name"))
        self.txtHighScoreScore5.SetValue (config.get ("High scores", "4.Score"))

    dlg.Destroy ()

  #=================================
  def OnCmd_HighScore_Save (self, event):
    namelist = []
    namelist.append (self.txtHighScoreName1.GetValue ())
    namelist.append (self.txtHighScoreName2.GetValue ())
    namelist.append (self.txtHighScoreName3.GetValue ())
    namelist.append (self.txtHighScoreName4.GetValue ())
    namelist.append (self.txtHighScoreName5.GetValue ())

    scorelist = []
    scorelist.append (self.txtHighScoreScore1.GetValue ())
    scorelist.append (self.txtHighScoreScore2.GetValue ())
    scorelist.append (self.txtHighScoreScore3.GetValue ())
    scorelist.append (self.txtHighScoreScore4.GetValue ())
    scorelist.append (self.txtHighScoreScore5.GetValue ())

    self.cheat.Save (namelist, scorelist)

    self.mainStatus.SetStatusText (" Saved data successfully")

  #=================================
  def OnCmd_HighScore_Undo (self, event):
    self.PopulateEntries ()

  #=================================
  def OnCmd_HighScore_Retrieve (self, event):
    self.cheat.Open (self.rdoHighScoreRoot.GetSelection (), self.txtHighScorePath.GetValue ())
    self.PopulateEntries ()