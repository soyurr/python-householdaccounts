import wx
import random
from homebook import homebookSqliteCRUD

class pieChartPanel(wx.Panel): 
    # data ={}      
    def __init__( self, parent): 
        wx.Panel.__init__(self,parent)
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        
    def SetData(self,data):
        self.data = data 
        rows = homebookSqliteCRUD.selectAll()
        totalRe = 0
        totalEx = 0
    
        for row in rows:
            if row[2] == '수입':
                totalRe += int(row[5])
            elif row[2] == '지출':
                totalEx += int(row[6])
        data = [totalRe,totalEx]
        
        self.Bind(wx.EVT_PAINT,self.OnPaint) 
        # 중요 - 새로이 그린 내용으로 갱신  
        self.Refresh() #중요 

    def SetData2(self,data):
        self.data = data 
        rows = homebookSqliteCRUD.selectAll()
        월급 = 0 
        상여금 = 0 
        기타수입 = 0 
        식비 = 0 
        교통비 = 0 
        생필품 = 0 
        의류 = 0 
        의료비 = 0 
        통신비 = 0 
        공과금 = 0
        for row in rows:

            # if row[3] == '월급' and row[5] != 0:
            #     월급 += int(row[5])
            # elif row[3] == '상여금' and row[5] != 0:
            #     상여금 += int(row[5])
            # elif (row[3] == '기타수입') and row[5] != 0:
            #     기타수입 += int(row[5])
            # elif row[3] == '식비' and row[6] != 0:
            #     식비 += int(row[6])
            # elif  row[3] == '교통비' and row[6] != 0:
            #     교통비 += int(row[6])
            # elif row[3] == '생필품' and row[6] != 0:
            #     생필품 += int(row[6])
            # elif row[3] == '의류' and row[6] != 0:
            #     의류 += int(row[6])
            # elif row[3] == '의료비' and row[6] != 0:
            #     의료비 += int(row[6])
            # elif row[3] == '통신비' and row[6] != 0:
            #     통신비 += int(row[6])
            # elif row[3] == '공과금' and row[6] != 0:
            #     공과금 += int(row[6])

            if row[3] == '월급' :
                월급 += int(row[5])
            elif row[3] == '상여금' :
                상여금 += int(row[5])
            elif (row[3] == '기타수입') :
                기타수입 += int(row[5])
            elif row[3] == '식비' :
                식비 += int(row[6])
            elif  row[3] == '교통비':
                교통비 += int(row[6])
            elif row[3] == '생필품':
                생필품 += int(row[6])
            elif row[3] == '의류':
                의류 += int(row[6])
            elif row[3] == '의료비':
                의료비 += int(row[6])
            elif row[3] == '통신비' :
                통신비 += int(row[6])
            elif row[3] == '공과금' :
                공과금 += int(row[6])
            
    
        data = [월급,상여금,기타수입,식비,교통비,생필품,의류,의료비,통신비,공과금]
        # self.data = ["월급":월급,"상여금":상여금,"기타수입":기타수입,"식비":식비,"교통비":교통비,"생필품":생필품,"의류":의류,"의료비":의료비,"통신비":통신비,"공과금":공과금]
        print(self.data)
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
        color = {}
        # 데이타 총량 산정
        for key in self.data:
            total += self.data[key]
        # print(total)
        print(self.data)
        
        # 전체총량에 차지하는 각 데이타를 360도  각도로 환산하고, 파이챠트에 구분표시할 색상을 임의로 생성 
        for key in self.data: #{'월급': 0, '상여금': 0, '기타수입': 20000, '식비': 17300, '교통비': 0, '생필품': 0, '의류': 0, '의료비': 0, '통신비': 0, '공과금': 0}
            #print(key)
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color[key] = (r,g,b) 
            self.data[key] = int(self.data[key]/total*360)
        print(color)
         
        # 아래 글씨를 쓰기 위한 색상 지정   
        self.brush.SetColour(wx.Colour(0,0,0,1)) 
        # 브러쉬 지정  
        self.dc.SetBrush(self.brush) 
        self.dc.DrawText("",350,40) 
         
        #DrawEllipticArc(X, Y, WX, WY, ST, LT) 
        # 원의 기준은 좌측 상단점(X,Y) 
        # 가로폭, 세로폭(WX,WY) 
        # 호의 시작 각도,끝나는 각도 (ST,LT) 
        sum = 0
        step = 70
        for key in self.data:
            if self.data[key] != 0:
                rgb = color[key] # (ss,ff,gg)
                r = rgb[0]
                g = rgb[1] 
                b = rgb[2] 
                self.brush.SetColour(wx.Colour(r,g,b,1)) 
                self.dc.SetBrush(self.brush) 
                self.dc.DrawRectangle(340, step, 30, 30) 
                self.dc.DrawEllipticArc(60, 60, 200, 200, sum,sum+self.data[key]) 
                self.dc.DrawText(key,400,step) 
                sum +=  self.data[key] 
                step += 30
            else:
                pass