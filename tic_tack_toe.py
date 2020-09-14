class GameData():

	def __init__(self,pl1,pl2):
		self.tack_list=['*','*','*','*','*','*','*','*','*']

		self.pl1=pl1
		self.pl2=pl2
		
		self.count=0
		self.entry=True
		
	def update(self,user,pos):
		if user=="player1":
			if self.tack_list[pos]!="0" and self.tack_list[pos]!="x":
				self.tack_list[pos]="0"
				return True
			else:
				return False
		elif user=="player2":
			if self.tack_list[pos]!="0" and self.tack_list[pos]!="x":
				self.tack_list[pos]="x"
				return True
			else:
				return False
	
	def check_tack(self):
		lst=self.tack_list

		if (lst[0]==lst[1] and lst[0]==lst[2] and lst[0]!='*')or(lst[3]==lst[4] and lst[3]==lst[5] and lst[3]!='*')or(lst[6]==lst[7] and lst[6]==lst[8] and lst[6]!='*'):
			return True
		elif (lst[0]==lst[3]and lst[0]==lst[6] and lst[0]!='*')or(lst[1]==lst[4] and lst[1]==lst[7] and lst[1]!='*')or(lst[2]==lst[5] and lst[2]==lst[8] and lst[2]!='*'):
			return True
		elif (lst[0]==lst[4] and lst[0]==lst[8] and lst[0]!='*') or (lst[2]==lst[4] and lst[2]==lst[6] and lst[2]!='*'):
			return True
		else:
			return False 
		
	def robo_choice(self):
		possible=[]
		for i in range(0,9):
			if self.tack_list[i]=='*':
				possible.append(i)

	
	def print_tack(self):
		lst=self.tack_list
		print('''
    |    |	
  {} |  {} |  {}
    |    |
--------------
    |    |	
  {} |  {} |  {}
    |    |
--------------
    |    |	
  {} |  {} |  {} 
    |    |     '''.format(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8]))


	def multi_play(self):
		if self.entry:
			print("Simble for {} is - 0\nSimble for {} is - x".format(self.pl1,self.pl2))
			self.entry=False 
		self.print_tack()
		while self.count<9:
			if self.count%2==0:
				pos=int(input("Player {}'s turn..Enter a number: ".format(self.pl1)))
				if 0<=pos<=9:
					updated=self.update("player1",pos)
					if updated:
						self.count+=1
						self.print_tack()
						if self.check_tack():
							print("player {} has won..congrajulations!!!!".format(self.pl1))
							exit()
					else:
						print("You have entered a number that is already tacked...going back..")
						self.multi_play()
						break
				else:
					print("You have entered an out of range number...going back..")
					self.multi_play()
					break
			else:
				pos=int(input("Player {}'s turn..Enter a number: ".format(self.pl2)))
				if 0<=pos<=9:
					updated=self.update("player2",pos)
					if updated:
						self.count+=1
						self.print_tack()
						if self.check_tack():
							print("player {} has won..congrajulations!!!!".format(self.pl2))
							exit()
					else:
						print("You have entered a number that is already tacked...going back..")
						self.multi_play()
						break
				else:
					print("You have entered an out of range number...going back..")
					self.multi_play()
					break
		print("The Game has ended....")

	def robo_play(self):
		if self.entry:
			print("Simble for {} is - 0\nSimble for {} is - x".format(self.pl1,self.pl2))
			self.entry=False 
		self.print_tack()
		while self.count<9:
			if self.count%2==0:
				pos=int(input("Player {}'s turn..Enter a number: ".format(self.pl1)))
				if 0<=pos<=9:
					updated=self.update("player1",pos)
					if updated:
						self.count+=1
						self.print_tack()
						if self.check_tack():
							print("player {} has won..congrajulations!!!!".format(self.pl1))
							exit()
					else:
						print("You have entered a number that is already tacked...going back..")
						self.robo_play()
						break
				else:
					print("You have entered an out of range number...going back..")
					self.robo_play()
					break
			else:
				print("The _-SaffronShot-_ making choice: ")
				pos=self.robo_choice()
				updated=self.update("player2",pos)
				if updated:
					self.count+=1
					self.print_tack()
					if self.check_tack():
						print("player {} has won..congrajulations!!!!".format(self.pl2))
						exit()
		print("The Game has ended....")
				

#----------------------------------------------------------------------------------------------------------------------------

print('''
-----------------------------------------------------------------------
=======================================================================
Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe
Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe
Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe
Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe
Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe Tic-Tac-Toe
=======================================================================
-----------------------------------------------------------------------
''')

print("\n")

#----------------------------------------------------------------------------------------------------------------------------

if __name__=="__main__":
	while True:
		print("1)Multi-Player\n2)Play against computer")
		try:
			choice=int(input("Enter your choice: "))
			if choice==1 or choice==2:
				break
			else:
				print("Please enter a valid choice: ")
		except:
			print("Please enter a valid choice\n")
	
	if choice==1:
		pl1=input("Enter player1 name: ")
		pl2=input("Enter player2 name: ")
		print("")	
		game=GameData(pl1,pl2)
		game.multi_play()
	else:
		print("This path is under devolopement.")
		exit()
		pl1=input("Enter players name: ")
		pl2="_-SaffronShot-_"
		print(f"Hi {pl1}...{pl2} will destroy you...\n")
		game=GameData(pl1,pl2)
		game.robo_play()
