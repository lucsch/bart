#!/usr/bin/env python3
import os
import wx
import sys
import wx.html


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
        self.SetStatusText("version: {}.{} ({})".format(VERSION_MAJOR_MINOR, COMMIT_NUMBER, COMMIT_ID), 1)

        # config file
        # self.m_config = wx.FileConfig(self.m_title)

        # add icon
        # icon = wx.Icon()
        # icon.CopyFromBitmap(siboulo_icon.GetBitmap())
        # self.SetIcon(icon)
        self.test_html()

    def test_html(self):
        # get the template directory (support bundle version)
        bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath((os.path.dirname(__file__))))
        html_path = os.path.join(bundle_dir, "html")
        template_header = os.path.join(html_path, "header.html")
        template_list = os.path.join(html_path, "list.html")

        self.m_header_ctrl.SetBorders(0)
        self.m_header_ctrl.LoadFile(template_header)

        self.m_result_ctrl.SetBorders(0)
        self.m_result_ctrl.LoadFile(template_list)

    def __del__(self):
        pass

    def _create_menu_bar(self):
        self.m_menu = wx.MenuBar(0)

        # GAME
        self.m_menu_game = wx.Menu()
        self.m_menui_game_new = self.m_menu_game.Append(wx.ID_ANY, "New game..." + "\t" + "Ctrl+N")
        self.m_menui_game_reset = self.m_menu_game.Append(wx.ID_ANY, "Reset")
        self.m_menu.Append(self.m_menu_game, "Game")

        # ROUND
        self.m_menu_round = wx.Menu()
        self.m_menui_round_set_score = self.m_menu_round.Append(wx.ID_ANY, "Set Score..." + "\t" + "Ctrl+S")
        self.m_menu.Append(self.m_menu_round, "Round")

        # PLAYER
        self.m_menu_player = wx.Menu()
        self.m_menui_player_add = self.m_menu_player.Append(wx.ID_ANY, "Add...")
        self.m_menui_player_del = self.m_menu_player.Append(wx.ID_ANY, "Remove...")
        self.m_menu.Append(self.m_menu_player, "Player")

        # STATISTICS
        self.m_menu_stat = wx.Menu()
        self.m_menui_stat_leaderboard = self.m_menu_stat.Append(wx.ID_ANY, "Leaderborad")
        self.m_menui_stat_by_player = self.m_menu_stat.Append(wx.ID_ANY, "By players")
        self.m_menu.Append(self.m_menu_stat, "Statistics")

        # HELP
        self.m_menu_help = wx.Menu()
        self.m_menu_help.Append(wx.ID_ABOUT, "About...")

        self.m_menu.Append(self.m_menu_help, "Help")
        self.SetMenuBar(self.m_menu)


    def _create_controls(self):
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        self.m_header_ctrl = wx.html.HtmlWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 80),
                                                wx.html.HW_NO_SELECTION | wx.html.HW_SCROLLBAR_NEVER)
        bSizer1.Add(self.m_header_ctrl, 0, wx.EXPAND, 5)
        self.m_result_ctrl = wx.html.HtmlWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                wx.html.HW_SCROLLBAR_AUTO)
        bSizer1.Add(self.m_result_ctrl, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        self.m_result_ctrl.SetBackgroundColour(wx.Colour(4,73,14))
        self.m_header_ctrl.SetBackgroundColour(wx.BLACK)
