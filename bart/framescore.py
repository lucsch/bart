#!/usr/bin/env python3
import wx


###########################################################################
## Class FrameScore
###########################################################################


class FrameScore(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Score", pos=wx.DefaultPosition, size=wx.DefaultSize,
                           style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)

        self._create_controls()
        self.Bind(wx.EVT_SPINCTRL, self.on_spinctrl_change, id=self.m_shoot1_ctrl.GetId())
        self.Bind(wx.EVT_SPINCTRL, self.on_spinctrl_change, id=self.m_shoot2_ctrl.GetId())
        self.Bind(wx.EVT_SPINCTRL, self.on_spinctrl_change, id=self.m_shoot3_ctrl.GetId())

    def on_spinctrl_change(self, event):
        my_total = self.m_shoot1_ctrl.GetValue() + self.m_shoot2_ctrl.GetValue() + self.m_shoot3_ctrl.GetValue()
        self.m_result_ctrl.SetLabel(str(my_total))

    def _create_controls(self):
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Shoot"), wx.VERTICAL)
        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.AddGrowableCol(1)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        self.m_staticText2 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText2.Wrap(-1)
        fgSizer1.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.m_shoot1_ctrl = wx.SpinCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(250, -1), wx.SP_ARROW_KEYS, 0, 100, 0)
        fgSizer1.Add(self.m_shoot1_ctrl, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)
        self.m_staticText3 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText3.Wrap(-1)
        fgSizer1.Add(self.m_staticText3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.m_shoot2_ctrl = wx.SpinCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0)
        fgSizer1.Add(self.m_shoot2_ctrl, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)
        self.m_staticText4 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText4.Wrap(-1)
        fgSizer1.Add(self.m_staticText4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.m_shoot3_ctrl = wx.SpinCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0)
        fgSizer1.Add(self.m_shoot3_ctrl, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)
        sbSizer1.Add(fgSizer1, 1, wx.EXPAND, 5)
        bSizer4.Add(sbSizer1, 0, wx.EXPAND | wx.ALL, 5)
        bSizer4.Add((0, 0), 1, wx.EXPAND, 5)
        sbSizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Results"), wx.VERTICAL)
        self.m_result_ctrl = wx.StaticText(sbSizer2.GetStaticBox(), wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTER | wx.ST_NO_AUTORESIZE)
        self.m_result_ctrl.SetLabelMarkup(u"0")
        self.m_result_ctrl.Wrap(-1)
        self.m_result_ctrl.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))
        sbSizer2.Add(self.m_result_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        bSizer4.Add(sbSizer2, 0, wx.ALL | wx.EXPAND, 5)
        bSizer4.Add((0, 0), 1, wx.EXPAND, 5)
        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button(self, wx.ID_OK)
        m_sdbSizer1.AddButton(self.m_sdbSizer1OK)
        self.m_sdbSizer1Cancel = wx.Button(self, wx.ID_CANCEL)
        m_sdbSizer1.AddButton(self.m_sdbSizer1Cancel)
        m_sdbSizer1.Realize()
        bSizer4.Add(m_sdbSizer1, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(bSizer4)
        self.Layout()
        bSizer4.Fit(self)
        self.Centre(wx.BOTH)

