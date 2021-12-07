#!/usr/bin/env python3
import os
import wx

# from siboulo.bitmaps import siboulo_icon
from bart.version import COMMIT_ID
from bart.version import COMMIT_NUMBER
from bart.version import VERSION_MAJOR_MINOR


###########################################################################
#  Class FrameMain
###########################################################################

class FrameMain(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1000, 600),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # init controller
        self.m_title = u"BART"
        self.SetTitle(self.m_title)

        # create controls and menus
        self._create_controls()
        self._create_menu_bar()

        self.CreateStatusBar(2)
        self.SetStatusBarPane(-1)  # don't display menu hints
        self.SetStatusText("version: {}.{} ({})".format(VERSION_MAJOR_MINOR, COMMIT_NUMBER, COMMIT_ID),1)

        # config file
        # self.m_config = wx.FileConfig(self.m_title)

        # add icon
        # icon = wx.Icon()
        # icon.CopyFromBitmap(siboulo_icon.GetBitmap())
        # self.SetIcon(icon)

    def __del__(self):
        pass

    def _create_menu_bar(self):
        pass

    def _create_controls(self):
        pass
