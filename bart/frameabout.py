#!/usr/bin/env python3
import wx
from bart.bitmaps import bart_icon
from bart.version import COMMIT_ID
from bart.version import COMMIT_NUMBER
from bart.version import BRANCH_NAME
from bart.version import VERSION_MAJOR_MINOR


class FrameAbout(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"About", pos=wx.DefaultPosition, size=wx.DefaultSize,
                           style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self._create_controls()

        self.m_bmp_ctrl.SetBitmap(bart_icon.GetBitmap())
        my_txt = "Version {}.{}\n".format(VERSION_MAJOR_MINOR, COMMIT_NUMBER)
        my_txt = my_txt + "Revision: {}\n".format(COMMIT_ID)
        my_txt = my_txt + "Branch: {}\n".format(BRANCH_NAME)
        my_txt = my_txt + wx.GetLibraryVersionInfo().GetVersionString() + "\n"
        my_txt = my_txt + wx.GetOsDescription()
        self.m_txt_ctrl.SetValue(my_txt)

    def _create_controls(self):
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)
        self.m_bmp_ctrl = wx.StaticBitmap(self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize,
                                          0)
        bSizer3.Add(self.m_bmp_ctrl, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_name_ctrl = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Bart (BAR-darT)", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.m_name_ctrl.Wrap(-1)
        self.m_name_ctrl.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))
        bSizer3.Add(self.m_name_ctrl, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        self.m_txt_ctrl = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(350, 300),
                                      wx.TE_MULTILINE)
        bSizer3.Add(self.m_txt_ctrl, 1, wx.ALL | wx.EXPAND, 5)
        self.m_panel1.SetSizer(bSizer3)
        self.m_panel1.Layout()
        bSizer3.Fit(self.m_panel1)
        bSizer2.Add(self.m_panel1, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer2)
        self.Layout()
        bSizer2.Fit(self)
