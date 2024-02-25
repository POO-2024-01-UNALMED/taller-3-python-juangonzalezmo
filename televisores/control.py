class Control:
    def __init__(self):
        self.tv=None
    
    def enlazar(self,tv):
        self.tv=tv
        tv.control=self
    
    def turnOn(self):
        self.tv.estado=True
    def turnOff(self):
        self.tv.estado=False

    def canalUp(self):
        if self.tv.estado==True and self.canal>=1 and self.canal<120:
            self.tv.canal+=1
    def canalDown(self):
        if self.tv.estado==True and self.canal>1 and self.canal<=120:
            self.tv.canal-=1

    def volumenUp(self):
        if self.tv.estado==True and self.volumen>=0 and self.volumen<7:
            self.tv.volumen+=1
    def volumenDown(self):
        if self.tv.estado==True and self.volumen>0 and self.volumen<=7:
            self.tv.volumen-=1 

    def setCanal(self,canal):
        
        if self.tv.estado==True and canal>=1 and canal<=120:
            self.tv.canal=canal       
    def setVolumen(self,volumen):

        if self.tv.estado==True and volumen>=0 and volumen<=7:
            self.tv.volumen=volumen

    def getTv(self):
        return self.tv
    def setTv(self,tv):
        self.tv=tv