from TRADUCTOR import COORD_TRADUCTOR
from ICONS import Icon

class Piece:
	def __init__(self,_id="X",_slot=[0,0],_isFree=False,_team="test"):
		self.Team=_team
		self.IsPosFree=_isFree
		self.PiezaID=_id
		self.Slot=[_slot[0],_slot[1]]
		self.FirstMove=True
		self.PlaceSlots=[]
	
	def Update_Place_Slots(self,_tablero):
		def Search_Loop(_width,_height,_range=None):
			if _range==None:
				_range=_tablero.Width
			else:
				if _range==0:
					_range=2
				else:
					_range+=1
			#searchSlot=[]
			for x in range(_range):
				CoordExists=_tablero.Coord_In_Tablero([self.Slot[0]+(x*_width),self.Slot[1]+(x*_height)])
				NotMe=[self.Slot[0]+(x*_width),self.Slot[1]+(x*_height)]!=self.Slot
				if(NotMe and CoordExists):
					if _tablero.Tablero_Get_Slot([ self.Slot[0]+(x*_width),self.Slot[1]+(x*_height) ])[0].Show_Free()==True:
						#searchSlot.append([self.Slot[0]+(x*_width),self.Slot[1]+(x*_height)])
						self.PlaceSlots.append([self.Slot[0]+(x*_width),self.Slot[1]+(x*_height)])
						#print(COORD_TRADUCTOR([self.Slot[0]+(x*_width),self.Slot[1]+(x*_height)]).Return_Traduced())
					else:
						if self.PiezaID not in Icon().Peon:
							if _tablero.Tablero_Get_Slot([ self.Slot[0]+(x*_width),self.Slot[1]+(x*_height) ])[0].Show_Team()!=self.Team:
								#searchSlot.append([self.Slot[0]+(x*_width),self.Slot[1]+(x*_height)])
								self.PlaceSlots.append([self.Slot[0]+(x*_width),self.Slot[1]+(x*_height)])
							break
			#return(searchSlot)
		if self.Team=="Black":
			_dir=1
		elif self.Team=="White":
			_dir=-1
		
		#  P E O N
		if self.PiezaID in Icon().Peon:
			self.PlaceSlots=[]
			if self.FirstMove==True:
				Search_Loop(0,1*_dir,2)
			else:
				Search_Loop(0,1*_dir,1)
		
		#  T O W E R
		if self.PiezaID in Icon().Tower:
			self.PlaceSlots=[]

			Search_Loop(-1,0)
			Search_Loop(1,0)
			Search_Loop(0,-1)
			Search_Loop(0,1)
		
		#  H O R S E
		if self.PiezaID in Icon().Horse:
			self.PlaceSlots=[]
			Search_Loop(-1,-2,1)
			Search_Loop(+1,-2,1)
			Search_Loop(-1,+2,1)
			Search_Loop(+1,+2,1)
			Search_Loop(-2,-1,1)
			Search_Loop(-2,+1,1)
			Search_Loop(+2,-1,1)
			Search_Loop(+2,+1,1)
		
		#  A L F I L
		if self.PiezaID in Icon().Alfil:
			self.PlaceSlots=[]
			Search_Loop(-1,-1)
			Search_Loop(1,-1)
			Search_Loop(-1,1)
			Search_Loop(1,1)
		
		#  Q U E E N
		if self.PiezaID in Icon().Queen:
			self.PlaceSlots=[]
			Search_Loop(-1,0)
			Search_Loop(1,0)
			Search_Loop(0,-1)
			Search_Loop(0,1)

			Search_Loop(-1,-1)
			Search_Loop(1,-1)
			Search_Loop(-1,1)
			Search_Loop(1,1)
		
		#  Q U E E N
		if self.PiezaID in Icon().King:
			self.PlaceSlots=[]
			Search_Loop(-1,0,1)
			Search_Loop(1,0,1)
			Search_Loop(0,-1,1)
			Search_Loop(0,1,1)

			Search_Loop(-1,-1,1)
			Search_Loop(1,-1,1)
			Search_Loop(-1,1,1)
			Search_Loop(1,1,1)


	
	def Show_Piece(self):
		return(self.PiezaID)
	
	def Show_Slot(self):
		return(self.Slot)
	
	def Show_Place_Slots(self,_print=False):
		if _print==True:
			if len(self.PlaceSlots)>0:
				print(f"The Piece {self.Show_Piece()} in the slot: '{COORD_TRADUCTOR(self.Slot).Return_Traduced()}' can move to the following slots:")
				for i in (self.PlaceSlots):
					if i==self.PlaceSlots[-1]:
						end=""
					else:
						end=", "
					print(COORD_TRADUCTOR(i).Return_Traduced(),end=end)
				print()
			else:
				print(f"The Piece {self.Show_Piece()} in the slot: '{COORD_TRADUCTOR(self.Slot).Return_Traduced()}' can't move")
		else:
			return(self.PlaceSlots)
	
	def Show_Free(self):
		return(self.IsPosFree)
	
	def Show_Team(self):
		return(self.Team)
	
	def Show_Info(self):
		return(f"{self.Show_Piece()}\nTeam: {self.Team}\nSlot: xy{self.Show_Slot()}")

	def Set_Slot(self,slot):
		if self.Show_Free()==False:
			self.FirstMove=False
		self.Slot=slot
