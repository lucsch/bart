#!/usr/bin/env python3
import argparse
import wx

from bart.framemain import FrameMain


class BartApp(wx.App):
    """
    Main application class
    init the 'framemain' and the main loop
    """

    def OnInit(self):
        # parsing the command line
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', nargs='?', default=wx.EmptyString)
        args = parser.parse_args()
        print(args.filename)

        dlg = FrameMain()
        dlg.Show(True)
        self.SetTopWindow(dlg)
        return True


if __name__ == '__main__':
    app = BartApp()
    app.MainLoop()
