#Python Ajedrez

class Pieza:
    def __init__(self,_idd="X",_slot=[0,0],_isFree=0):
        self.IsPosFree=_isFree
        self.PiezaID=_idd
        self.slot=[_slot[0],_slot[1]]
    
    def Get_Slot(self):
        return(self.slot)
    
    def Show_Info(self):
        a_ = "placeable slot" if self.IsPosFree==0 else "not placeable slot"
        return(self.PiezaID,f"is in the slot {self.slot} and its a ",a_)
        
    def Move_Slot(self,_Pieza):
        _PiezaSlot=_Pieza.Get_Slot()
        if _Pieza!=self:
            if self.slot!=_PiezaSlot:
                tex=f"Moved to slot {_PiezaSlot}"
                self.slot=_PiezaSlot
                return(tex+f"  {self.Get_Slot()}")
            else:
                return("Cant Move")
        else:
            return("Soy yo!!!!")

class Tablero:
    def __init__(self,_w,_h):
        self.Width=_w
        self.Height=_h
        self.Tablero=[]
        self.TableroP=[]
        self.Crear_Tablero_Base()
        self.Crear_Tablero_Piezas()
    
    def Crear_Tablero_Base(self):
        for i in range(self.Height):
            for j in range(self.Width):
                if i%2==0:
                    if j%2!=0:
                        _id="⬛"
                    else:
                        _id="⬜"
                else:
                    if j%2==0:
                        _id="⬛"
                    else:
                        _id="⬜"
                try:
                    self.Tablero.append(Pieza(_id,[i,j]))
                except:
                    print("error")
    
    def Crear_Tablero_Piezas(self):
        for i in range(self.Height):
            for j in range(self.Width):
                if i==1:
                    _id="♙"
                elif i==6:
                    _id="♟"
                elif (i==0 or i==7)and(j==0 or j==7):
                    _id="♜"
                else:
                    _id=". "
                try:
                    self.TableroP.append(Pieza(_id,[i,j]))
                except:
                    print("error2")
                
    def Imprimir_Tablero_Base(self,_resalt=None):
        brekMax=self.Width-1
        brek=0
        fil=0
        for i in range(len(self.Tablero)):
            #print(self.Tablero[i][0]+self.Tablero[i][1],end=" ")
            try:
                print(self.Tablero[i].PiezaID,end=" ")
            except:
                print("error")
            if brek==brekMax:
                fil+=1
                brek=0
                print()
            else:
                brek+=1
        print()
        
    def Imprimir_Tablero_Piezas(self,_resalt=None):
        brekMax=self.Width-1
        brek=0
        fil=0
        for i in range(len(self.TableroP)):
            #print(self.Tablero[i][0]+self.Tablero[i][1],end=" ")
            try:
                print(self.TableroP[i].PiezaID,end=" ")
            except:
                print("error")
            if brek==brekMax:
                fil+=1
                brek=0
                print()
            else:
                brek+=1
        print()

a=Pieza()
b=Pieza("Y",[1,1])
print(a.Get_Slot())
print(b.Get_Slot())
print(a.Move_Slot(a))
print(a.Move_Slot(b))
print(a.Move_Slot(b))

try:
    tabl=Tablero(8,8)
    tabl.Imprimir_Tablero_Base()
    tabl.Imprimir_Tablero_Piezas()
except:
    print("error ext")