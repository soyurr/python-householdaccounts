# -*- coding: utf-8 -*- 
###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
import wx.dataview
###########################################################################
## Class MyFrame1
###########################################################################
from homebook import homebookSqliteCRUD
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"가계부", pos = wx.DefaultPosition, size = wx.Size( 1000,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"번호", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer8.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer8.Add( self.txtNo, 0, wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer8, 1, wx.EXPAND, 5 )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"날짜", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer9.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtDay = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.txtDay, 0, wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer9, 1, wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"구분", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer10.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.radioRe = wx.RadioButton( self, wx.ID_ANY, u"수입", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.radioRe, 0, wx.ALL, 5 )
        
        self.radioEx = wx.RadioButton( self, wx.ID_ANY, u"지출", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.radioEx, 0, wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"계정", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer11.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        comboAccountChoices =  ["월급","상여금","기타수입","식비","교통비","생필품","의류","의료비/건강비","통신비","공과금"]
        self.comboAccount = wx.ComboBox( self, wx.ID_ANY, u"선택하세요", wx.DefaultPosition, wx.DefaultSize, comboAccountChoices, 0 )
        bSizer11.Add( self.comboAccount, 0, wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer11, 1, wx.EXPAND, 5 )
        
        bSizer81 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"적요", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer81.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.txtRemark = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer81.Add( self.txtRemark, 0, wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer81, 1, wx.EXPAND, 5 )
        
        bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"수입", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer91.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.txtRevenue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer91.Add( self.txtRevenue, 0, wx.ALL, 5 )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"지출", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer91.Add( self.m_staticText8, 0, wx.ALL, 5 )
        
        self.txtExpense = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer91.Add( self.txtExpense, 0, wx.ALL, 5 )
        
        
        bSizer3.Add( bSizer91, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Insert", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        bSizer4.Add( self.m_button1, 1, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        bSizer4.Add( self.m_button2, 1, wx.ALL, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        bSizer4.Add( self.m_button3, 1, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Find", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        bSizer4.Add( self.m_button4, 1, wx.ALL, 5 )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"SelectAll", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        bSizer4.Add( self.m_button5, 1, wx.ALL, 5 )
        
        self.m_button9 = wx.Button( self, wx.ID_ANY, u"CLEAR", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        bSizer4.Add( self.m_button9, 1, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.tableView = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 550,500 ), 0 )
        self.m_dataViewColumn8 = self.tableView.AppendTextColumn( u"번호", 0 )
        self.m_dataViewColumn9 = self.tableView.AppendTextColumn( u"날짜", 0 )
        self.m_dataViewColumn10 = self.tableView.AppendTextColumn( u"수지구분", 0 )
        self.m_dataViewColumn11 = self.tableView.AppendTextColumn( u"계정과목", 0 )
        self.m_dataViewColumn12 = self.tableView.AppendTextColumn( u"적요", 0 )
        self.m_dataViewColumn13 = self.tableView.AppendTextColumn( u"수입", 0 )
        self.m_dataViewColumn14 = self.tableView.AppendTextColumn( u"지출", 0 )
        fgSizer1.Add( self.tableView, 0, wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 450,500 ), wx.TAB_TRAVERSAL )
        self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer13.SetMinSize( wx.Size( 500,-1 ) ) 
        self.m_button8 = wx.Button( self.m_panel3, wx.ID_ANY, u"그리기", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        
        bSizer13.Add( self.m_button8, 0, wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"날짜", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer13.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        self.txtStart = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.txtStart, 0, wx.ALL, 5 )
        
        self.m_staticText11 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer13.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        self.txtEnd = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.txtEnd, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer13 )
        self.m_panel3.Layout()
        fgSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.OnInsert )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnDelete )
        self.m_button3.Bind( wx.EVT_BUTTON, self.OnUpdate )
        self.m_button4.Bind( wx.EVT_BUTTON, self.OnFind )
        self.m_button5.Bind( wx.EVT_BUTTON, self.OnSelectAll )
        self.m_button9.Bind( wx.EVT_BUTTON, self.OnClear )
        self.m_button8.Bind( wx.EVT_BUTTON, self.OnDrawButton )
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def OnInsert( self, event ):
        day = self.txtDay.GetValue()
        if(self.radioRe.GetValue()):
            section = '수입'
            pass
        else:
            section = '지출'
            pass
        accounttitle = self.comboAccount.GetValue()
        remark = self.txtRemark.GetValue()
        revenue = self.txtRevenue.GetValue()
        expense = self.txtExpense.GetValue()
        try:
            homebookSqliteCRUD.insertData(day,section,accounttitle,remark,revenue,expense)
        except:
            print('예외발생!')
        finally:
            print("등록성공")
        event.Skip()
    
    def OnDelete( self, event ):
        event.Skip()
    
    def OnUpdate( self, event ):
        
        event.Skip()
    
    def OnFind( self, event ):
        event.Skip()
    
    def OnSelectAll( self, event ):
        rows = homebookSqliteCRUD.selectAll()
        x = 0 
        for row in rows:
            self.tableView.InsertItem(x, str(row[0]))
            self.tableView.SetItem(x, 1, row[1])
            self.tableView.SetItem(x, 2, row[2])
            self.tableView.SetItem(x, 3, row[3])
            self.tableView.SetItem(x, 4, row[4])
            self.tableView.SetItem(x, 5, row[5])
            x += 1
            # self.tableView.AppendColumn("{0},{1},{2},{3},{4},{5},{6}\n".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        event.Skip()
        
    def OnClear( self, event ):
        self.txtNo.Clear()
        self.txtDay.Clear()
        self.radioRe.SetValue(int(0))
        self.radioEx.SetValue(int(0))
        self.comboAccount.Clear()
        self.txtRemark.Clear()
        self.txtRevenue.Clear()
        self.txtExpense.Clear()
        self.txtStart.Clear()
        self.txtEnd.Clear()
        event.Skip()
    
    def OnDrawButton( self, event ):
        event.Skip()
    



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()


