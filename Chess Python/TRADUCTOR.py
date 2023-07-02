class COORD_TRADUCTOR:
	def __init__(self,_coord):
		self.Coord=_coord
	
	def Return_Traduced(self):
		return self.Array_Coord() if isinstance(self.Coord,list) else self.Coord_Array()

	def Array_Coord(self):
		T1=""
		T2=str(self.Coord[1])
		if self.Coord[0]==0:
			T1="A"
		elif self.Coord[0]==1:
			T1="B"
		elif self.Coord[0]==2:
			T1="C"
		elif self.Coord[0]==3:
			T1="D"
		elif self.Coord[0]==4:
			T1="E"
		elif self.Coord[0]==5:
			T1="F"
		elif self.Coord[0]==6:
			T1="G"
		elif self.Coord[0]==7:
			T1="H"
		return(T1+T2)
	
	def Coord_Array(self):
		T1=-1
		T2=int(self.Coord[1])
		if self.Coord[0]=="A":
			T1=0
		elif self.Coord[0]=="B":
			T1=1
		elif self.Coord[0]=="C":
			T1=2
		elif self.Coord[0]=="D":
			T1=3
		elif self.Coord[0]=="E":
			T1=4
		elif self.Coord[0]=="F":
			T1=5
		elif self.Coord[0]=="G":
			T1=6
		elif self.Coord[0]=="H":
			T1=7
		return([T1,T2])
