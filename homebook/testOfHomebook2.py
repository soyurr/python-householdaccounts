# -*- coding: utf-8 -*- 
###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import wx
import wx.xrc
###########################################################################
## Class MyFrame1
###########################################################################
from homebook import homebookSqliteCRUD
import sqlite3
from spyder.utils.qthelpers import QInputDialogMultiline
import matplotlib.pyplot as plt
from homebook.homebookPanel import homebookPanel
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"가계부", pos = wx.DefaultPosition, size = wx.Size( 1082,736 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
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
        
        comboAccountChoices = [ u"월급", u"상여금", u"기타수입", u"식비", u"교통비", u"생필품", u"의류", u"의료비/건강비", u"통신비", u"공과금" ]
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
        self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
        
        bSizer4.Add( self.m_button1, 1, wx.ALL, 5 )
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
        
        bSizer4.Add( self.m_button2, 1, wx.ALL, 5 )
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
        
        bSizer4.Add( self.m_button3, 1, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self, wx.ID_ANY, u"Find", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
        
        bSizer4.Add( self.m_button4, 1, wx.ALL, 5 )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"SelectAll", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
        
        bSizer4.Add( self.m_button5, 1, wx.ALL, 5 )
        
        self.m_button9 = wx.Button( self, wx.ID_ANY, u"CLEAR", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
        
        bSizer4.Add( self.m_button9, 1, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        #
        # self.list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size(  ), wx.LC_ICON|wx.BORDER_SUNKEN )
        # self.list.InsertColumn(0, '번호')
        # self.list.InsertColumn(1, '날짜', wx.Layout_RightToLeft)
        # self.list.InsertColumn(2, '수입/지출', wx.Layout_RightToLeft)
        # self.list.InsertColumn(3, '계정과목', wx.Layout_RightToLeft)
        # self.list.InsertColumn(4, '적요', wx.Layout_LeftToRight)
        # self.list.InsertColumn(5, '수입', wx.Layout_LeftToRight)
        # self.list.InsertColumn(6, '지출', width=250)
        #
        self.list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 550,430 ), wx.LC_REPORT|wx.BORDER_SUNKEN )
        
        self.list.InsertColumn(0, '번호')
        self.list.InsertColumn(1, '날짜', wx.Layout_RightToLeft)
        self.list.InsertColumn(2, '수입/지출', wx.Layout_RightToLeft)
        self.list.InsertColumn(3, '계정과목', wx.Layout_RightToLeft)
        self.list.InsertColumn(4, '적요', wx.Layout_RightToLeft)
        self.list.InsertColumn(5, '수입', wx.Layout_RightToLeft)
        self.list.InsertColumn(6, '지출', width=250)
        fgSizer1.Add( self.list, 0, wx.ALL, 5 )
        


        self.panel = homebookPanel(self)
        # self.panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 450,430 ), wx.TAB_TRAVERSAL )
        self.panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer13.SetMinSize( wx.Size( 500,-1 ) ) 
        self.m_button8 = wx.Button( self.panel, wx.ID_ANY, u"그리기", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
        self.m_button8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
        
        bSizer13.Add( self.m_button8, 0, wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self.panel, wx.ID_ANY, u"날짜", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer13.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        self.txtStart = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.txtStart, 0, wx.ALL, 5 )
        
        self.m_staticText11 = wx.StaticText( self.panel, wx.ID_ANY, u"~", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer13.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        self.txtEnd = wx.TextCtrl( self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.txtEnd, 0, wx.ALL, 5 )
        
        
        self.panel.SetSizer( bSizer13 )
        self.panel.Layout()
        fgSizer1.Add( self.panel, 1, wx.EXPAND |wx.ALL, 5 )
        
        
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
        self.list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.handle )
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
        
#삭제되는데 예외발생    
    def OnDelete( self, event ):
        no = self.txtNo.GetValue()
        try:
            homebookSqliteCRUD.delete(no)
        except:
            print('')
        finally:
            print('삭제완료')
        event.Skip()   
     
    def OnUpdate( self, event ):
        day = self.txtDay.GetValue()
        if(self.radioRe.GetValue()):
            section = '수입'
        elif(self.radioEx.GetValue()):
            section = '지출'
        accounttitle = self.comboAccount.GetValue()
        remark = self.txtRemark.GetValue()
        revenue = self.txtRevenue.GetValue()
        expense = self.txtExpense.GetValue()       
        no = self.txtNo.GetValue()
        try:
            homebookSqliteCRUD.update((day,section,accounttitle,remark,revenue, expense,no))
        except:
            print("예외발생!")
        finally:
            print("수정성공!")
        event.Skip()

#라디오 버튼 오류
    # def OnFind( self, event ):    
        # key = self.txtDay.GetValue()
        # row = homebookSqliteCRUD.select(key)
        #
        # self.txtNo.SetValue(str(row[0]))
        #
        # if self.radioRe.GetValue()  == 1:
        #     self.radioRe.SetValue(1)
        # else:
        #     self.radioEx.SetValue(1)
        #
        # self.comboAccount.SetValue(row[3])
        # self.txtRemark.SetValue(row[4])
        # self.txtRevenue.SetValue(str(row[5]))
        # self.txtExpense.SetValue(str(row[6]))
        #
        # event.Skip()

    def OnFind( self, event ):
        conn = sqlite3.connect("homebook.db")
        cur = conn.cursor()
        sql = 'SELECT * FROM HOMEBOOK WHERE DAY = ?'
        try:
            day = str(self.txtDay.GetValue())
            cur.execute(sql,(day,))
            rows = cur.fetchall()
            x = 0
            수입=0
            지출=0
            self.list.DeleteAllItems()
            for row in rows:
                self.list.InsertItem(x, str(row[0]))
                self.list.SetItem(x, 1, row[1])
                self.list.SetItem(x, 2, row[2])
                self.list.SetItem(x, 3, row[3])
                self.list.SetItem(x, 4, row[4])
                self.list.SetItem(x, 5, str(row[5]))
                self.list.SetItem(x, 6, str(row[6]))
                수입 += row[5]
                지출 += row[6]
                x += 1
        except Exception as e:           
            wx.MessageBox("찾는 자료가 없습니다.", "Message" ,wx.OK | wx.ICON_INFORMATION)  
        finally:
            cur.close()
            conn.close()
        event.Skip()
        

       
    def OnSelectAll( self, event ):
        self.list.DeleteAllItems()
        rows = homebookSqliteCRUD.selectAll()
        x=0
        수입=0
        지출=0
        for row in rows:
            self.list.InsertItem(x, str(row[0]))
            self.list.SetItem(x, 1, row[1])
            self.list.SetItem(x, 2, row[2])
            self.list.SetItem(x, 3, row[3])
            self.list.SetItem(x, 4, row[4])
            self.list.SetItem(x, 5, str(row[5]))
            self.list.SetItem(x, 6, str(row[6]))
            x += 1
            수입 += row[5]
            지출 += row[6]
        event.Skip()

    def OnClear( self, event ):
        self.txtNo.Clear()
        self.txtDay.Clear()
        self.radioRe.SetValue(int(0))
        self.radioEx.SetValue(int(0))
        self.comboAccount.SetValue("선택하세요")
        self.txtRemark.Clear()
        self.txtRevenue.Clear()
        self.txtExpense.Clear()
        self.txtStart.Clear()
        self.txtEnd.Clear()
        # self.list.ClearAll()  #이거 하면 셀렉트올 할 때 오류 남
        self.list.DeleteAllItems()
        event.Skip()
    
    def OnDrawButton( self, event ):
        rows = homebookSqliteCRUD.selectAll()
        수입 = 0
        지출 = 0
        for row in rows:
            if row[2] == '수입':
                수입 += int(row[5])
            elif row[2] == '지출':
                지출 += int(row[6])
        data = [수입, 지출]
        labels = 'Revenue','Expense'
        colors = ['yellow','green']
        explode = (0, 0.1)
        plt.pie(data, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90)
        plt.title('Pie chart of Revenue&Expense')
        plt.show()
        event.Skip()        

        # self.panel.SetData([56,78,90,55,78,99,45,34,89,87,65,33,76])
        self.panel.SetData([수입, 지출])
        self.panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        self.guiending()
        
        event.Skip()

  
    def handle( self, event ):
        num = event.GetIndex()
        no =self.list.GetItem(num, col=0).GetText()
        day =self.list.GetItem(num, col=1).GetText()
        section =self.list.GetItem(num, col=2).GetText()
        accounttitle =self.list.GetItem(num, col=3).GetText()
        remark =self.list.GetItem(num, col=4).GetText()
        revenue =self.list.GetItem(num, col=5).GetText()
        expense =self.list.GetItem(num, col=6).GetText()
      
        self.txtNo.SetValue(no)
        self.txtDay.SetValue(day)
        if section == '수입':
            self.radioRe.SetValue(1)
        else:
            section == '지출'
            self.radioEx.SetValue(1)
            
        self.comboAccount.SetValue(accounttitle)
        self.txtRemark.SetValue(remark)
        self.txtRevenue.SetValue(revenue)
        self.txtExpense.SetValue(expense)
        event.Skip()
   

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()


