'''
Created on 2021. 8. 2.

@author: pc368
'''

import wx
import math
class homebookPanel(wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(450,430 ), style = wx.TAB_TRAVERSAL )
    
    def SetData(self,data):
        self.data = data 
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        # 중요 - 새로이 그린 내용으로 갱신 
        self.Refresh() #중요 
                
    def OnPaint(self,e):
        dc = wx.PaintDC(self)
        brush = wx.Brush("white")
        dc.SetBackground(brush)
        dc.Clear()
        pen = wx.Pen(wx.Colour(0,0,255))
        dc.SetPen(pen)
        #############################
        dc.SetBrush(wx.Brush(wx.Colour(0,0,255)))
        size = len(self.data) 
        for x in range(0,size):
            # (좌측상단x,좌측상단y,사각형의가로,사각형의세로)
            dc.DrawRectangle((10+(x*40)),200-self.data[x], 30, self.data[x])
            # 데이터의 값을 글씨로 나타 냄 - (글씨, 좌측상단x, 좌측상단y)
            dc.DrawText(str(self.data[x]), (10+(x*40)), 210)
        #############################
     
        pass
    
    def __del__( self ):
        pass  
        
