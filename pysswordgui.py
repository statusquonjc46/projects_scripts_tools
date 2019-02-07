#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# Simple password generator based on user input bit size, now in gui form.
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

import wx
import random
import string
import sys

char = string.ascii_letters + string.digits + '!@#$%^&*()_-+='


class centerWindow(wx.Frame):

    def __init__(self, parent, title):
        super(centerWindow, self).__init__(parent, title=title, size=(425, 250))

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)

        self.outP = wx.TextCtrl(pnl, wx.ID_ANY, pos=(10, 120), size=(400, 80),
                                style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        self.rb1 = wx.RadioButton(pnl, 11, label='8 Bit Password', pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(pnl, 22, label='16 Bit Password', pos=(10, 30))
        self.rb3 = wx.RadioButton(pnl, 33, label='32 Bit Password', pos=(10, 50))
        self.rb4 = wx.RadioButton(pnl, 44, label='64 Bit Password', pos=(10, 70))
        self.rb5 = wx.RadioButton(pnl, 55, label='128 Bit Password', pos=(10, 90))
        self.Bind(wx.EVT_RADIOBUTTON, self.onRadioGroup)

        sys.stdout = self.outP

        self.Centre()
        self.Show(True)

    def onRadioGroup(self, e):
        rb = e.GetEventObject()

        def rgen(num):
            return ''.join(random.SystemRandom().choice(char) for _ in range(int(num)))

        if '8' in rb.GetLabel():
            self.outP.Clear()
            print (rb.GetLabel(), 'Chosen:')
            print(rgen(8))
        if '16' in rb.GetLabel():
            self.outP.Clear()
            print (rb.GetLabel(), 'Chosen:')
            print(rgen(16))
        if '32' in rb.GetLabel():
            self.outP.Clear()
            print (rb.GetLabel(), 'Chosen:')
            print(rgen(32))
        if '64' in rb.GetLabel():
            self.outP.Clear()
            print (rb.GetLabel(), 'Chosen')
            print(rgen(64))
        if '12' in rb.GetLabel():
            self.outP.Clear()
            print (rb.GetLabel(), 'Chosen')
            print(rgen(128))


def main():

    pyGen = wx.App()

    frame = centerWindow(None, title='PysswordGUI.py')
    frame.Show()

    pyGen.MainLoop()


if __name__ == '__main__':
    main()
