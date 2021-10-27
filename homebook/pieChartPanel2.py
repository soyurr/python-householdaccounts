import wx
import random
from homebook import homebookSqliteCRUD

class pieChartPanel2(wx.Panel): 
         
    def __init__( self, parent): 
        wx.Panel.__init__(self,parent)
        self.Bind(wx.EVT_PAINT,self.OnPaint)
    
    def SetData(self,data): 
        self.data1 = data
        rows = homebookSqliteCRUD.selectAll()
        월급 = 0 
        상여금 = 0 
        기타수입 = 0 
        for row in rows:
            if row[2] == '수입' and row[3] == '월급':
                월급 += int(row[5])
            elif  row[2] == '수입' and row[3] == '상여금':
                상여금 += int(row[5])
            elif row[2] == '수입' and row[3] == '기타수입' :
                기타수입 += int(row[5])
    
        self.data1 = {"월급":월급,"상여금":상여금,"기타수입":기타수입}
        self.Bind(wx.EVT_PAINT,self.OnPaint) 
        # 중요 - 새로이 그린 내용으로 갱신  
        self.Refresh() #중요 

    def SetData2(self,data): 
        self.data2 = data
        rows = homebookSqliteCRUD.selectAll()
        식비 = 0 
        교통비 = 0 
        생필품 = 0 
        의류 = 0 
        의료비 = 0 
        통신비 = 0 
        공과금 = 0
        for row in rows:
            if row[3] == '식비':
                식비 += int(row[6])
            elif  row[3] == '교통비':
                교통비 += int(row[6])
            elif row[3] == '생필품':
                생필품 += int(row[6])
            elif row[3] == '의류':
                의류 += int(row[6])
            elif row[3] == '의료비':
                의료비 += int(row[6])
            elif row[3] == '통신비':
                통신비 += int(row[6])
            elif row[3] == '공과금':
                공과금 += int(row[6])
    
        self.data2 = {"식비":식비,"교통비":교통비,"생필품":생필품,"의류":의류,"의료비":의료비,"통신비":통신비,"공과금":공과금}
        self.Bind(wx.EVT_PAINT,self.OnPaint) 
        # 중요 - 새로이 그린 내용으로 갱신  
        self.Refresh() #중요 


    def OnPaint(self,event):
        self.dc = wx.PaintDC(self)
        self.brush = wx.Brush("#ffffff") #칠하는 용도 
        self.dc.SetBackground(self.brush)
        self.dc.Clear()
        font = wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.dc.SetFont(font)
        total =0
        total2 = 0
        color = {}
        # 데이타 총량 산정
        for key in self.data1:
            total += self.data1[key]
        for key in self.data2:
            total2 += self.data2[key]           
        
        # 전체총량에 차지하는 각 데이타를 360도  각도로 환산하고, 파이챠트에 구분표시할 색상을 임의로 생성 
        for key in self.data1:
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color[key] = (r,g,b)
            self.data1[key] = int(self.data1[key]/total*360)
            
        for key in self.data2:
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color[key] = (r,g,b)
            self.data2[key] = int(self.data2[key]/total2*360)
         
        # 아래 글씨를 쓰기 위한 색상 지정   
        self.brush.SetColour(wx.Colour(0,0,0,1)) 
        # 브러쉬 지정  
        self.dc.SetBrush(self.brush) 
        self.dc.DrawText("파이차트",400,10) 
         
        #DrawEllipticArc(X, Y, WX, WY, ST, LT) 
        # 원의 기준은 좌측 상단점(X,Y) 
        # 가로폭, 세로폭(WX,WY) 
        # 호의 시작 각도,끝나는 각도 (ST,LT) 
        # sum = 0
        # step = 40
        # for key in self.data: 
        #     r = color.get(key)[0] 
        #     g = color.get(key)[1] 
        #     b = color.get(key)[2] 
        #     self.brush.SetColour(wx.Colour(r,g,b,1)) 
        #     self.dc.SetBrush(self.brush) 
        #     self.dc.DrawEllipticArc(60, 60, 200, 200, sum,sum+self.data[key]) 
        #     self.dc.DrawRectangle(340, step, 30, 30) 
        #     self.dc.DrawText(key,400,step) 
        #     sum +=  self.data[key] 
        #     step += 30
        sum = 0
        step = 40
        for key in self.data1: 
            if self.data1[key] != 0:
                r = color.get(key)[0] 
                g = color.get(key)[1] 
                b = color.get(key)[2] 
                self.brush.SetColour(wx.Colour(r,g,b,1)) 
                self.dc.SetBrush(self.brush) 
                self.dc.DrawEllipticArc(60, 60, 200, 200, sum,sum+self.data1[key]) 
                self.dc.DrawRectangle(340, step, 30, 30) 
                self.dc.DrawText(key,400,step) 
                sum +=  self.data1[key] 
                step += 30
            else:
                pass
            
        sum = 0
        step = 40
        for key in self.data2: 
            if self.data2[key] != 0:
                r = color.get(key)[0] 
                g = color.get(key)[1] 
                b = color.get(key)[2] 
                self.brush.SetColour(wx.Colour(r,g,b,1)) 
                self.dc.SetBrush(self.brush) 
                self.dc.DrawEllipticArc(60, 60, 200, 200, sum,sum+self.data2[key]) 
                self.dc.DrawRectangle(340, step, 30, 30) 
                self.dc.DrawText(key,400,step) 
                sum +=  self.data2[key] 
                step += 30
            else:
                pass