
from curses import initscr,noecho,A_REVERSE,A_BLINK,A_STANDOUT,A_BOLD,COLOR_BLACK,COLOR_YELLOW,color_pair,pair_content,init_pair,curs_set,newwin,endwin,KEY_RIGHT,KEY_LEFT,KEY_DOWN,KEY_UP,beep,noecho,start_color,COLOR_RED,COLOR_GREEN,init_color
from random import randrange,sample
initscr()
level=0
curs_set(0)
start_color()
init_pair(1,COLOR_GREEN,COLOR_BLACK)
init_pair(2,COLOR_RED,COLOR_BLACK)
init_pair(3,COLOR_GREEN,COLOR_BLACK)
ct=1
noecho()
win = newwin(30,80,0,0)
win.keypad(1)
win.nodelay(1)
win.addstr(3,7,'IIIT GAMES PRESENT: BOMB DIFFUSER',color_pair(1))
win.addstr(5,11,'>>>InStRuCtIoNs<<<')
win.addstr(6,11,'LEFT  : To move left')
win.addstr(7,11,'RIGHT : To move right')
win.addstr(8,11,'UP    : To move up')
win.addstr(9,11,'DOWN  : To move down')
win.addstr(10,11,'  *   : ~BOMB~')
win.addstr(11,11,'  M   : ~MINE~')
win.addstr(12,9,'::::Press Esc to Start::::')
while(win.getch()!=27):
		if ct>60:
			while ct>0:
				win.addstr(3,7,'IIIT GAMES PRESENT: BOMB DIFFUSER',A_BOLD)
				ct-=1
		else: 
			
		
			win.addstr(3,7,'IIIT GAMES PRESENT: BOMB DIFFUSER')
		ct+=1
endwin()

while level < 3:
	win = newwin(30,80,0,0)
	win.keypad(1)
	win.nodelay(1)
	#win.border('~','~','-','-','B','O','M','B')
	robot_width=2
	robot_height=2
	bomb=[20,5+level*5]
	win.addch(bomb[1],bomb[0],'*',color_pair(2))
	class box:
		pass
	def robot():
		b=box()
		b.life=100
		
		b.myrobot=[[4,5],[5,5],[4,6],[5,6]]
		b.points=0
		b.decodes=0
		b.bombhit_flag=0
		b.bordercross_flag=0
		def myrobot(n):
			if n==0:
				return b.myrobot
			if n==3:
				return b.points
			if n==4:
				return b.life
			else :
				return b.decodes
		def move_robot(x):
			if x == KEY_RIGHT:
				for i in range(len(b.myrobot)):
					b.myrobot[i][0]+=1
			if x == KEY_LEFT:
				for i in range(len(b.myrobot)):
					b.myrobot[i][0]-=1
			if x == KEY_UP:
				for i in range(len(b.myrobot)):
					b.myrobot[i][1]-=1
			if x == KEY_DOWN:
				for i in range(len(b.myrobot)):
					b.myrobot[i][1]+=1
		def print_erase(x):
			if x == KEY_RIGHT:
				for i in range(len(b.myrobot)):
					win.addch(b.myrobot[i][1],b.myrobot[i][0]-1,' ')
			if x == KEY_LEFT:
				for i in range(len(b.myrobot)):
					win.addch(b.myrobot[i][1],b.myrobot[i][0]+1,' ')
			if x == KEY_UP:
				for i in range(len(b.myrobot)):
					win.addch(b.myrobot[i][1]+1,b.myrobot[i][0],' ')
			if x == KEY_DOWN:
				for i in range(len(b.myrobot)):
					win.addch(b.myrobot[i][1]-1,b.myrobot[i][0],' ')
		def create_robot(n):
			win.addstr(b.myrobot[0][1],b.myrobot[0][0],'{'+'}',color_pair(1))
			if(n==1):
				win.addstr(b.myrobot[2][1],b.myrobot[2][0],'\/')
			else: win.addstr(b.myrobot[2][1],b.myrobot[2][0],'/\\')
		def getbo():
			return b.bombhit_flag
		def getbr():
			return b.bordercross_flag
	
		def check():
			for i in range(len(b.myrobot)):
				if b.myrobot[i]==bomb:
					b.bombhit_flag=1
					if b.decodes==5:
						b.bombhit_flag=100
					return
			for i in range(len(b.myrobot)):
				for j in range(len(m)):
					if m[j]==b.myrobot[i]:
						m[j]=[]
						b.life-=20
				if b.life<=0:
				 	b.life_flag=0
				 	return

				for j in range(len(d)):
					if d[j]==b.myrobot[i]:
						d[j]=[]
						b.points+=10
						b.decodes+=1
				if b.myrobot[2][0] > 78 or  b.myrobot[0][0] < 1 or  b.myrobot[0][1] < 1 or b.myrobot[2][1] > 28:
					b.bordercross_flag=1
		a=box()
		a.check=check
		a.create_robot=create_robot
		a.print_erase=print_erase
		a.move_robot=move_robot
		a.create_robot=create_robot
		a.getbr=getbr
		a.getbo=getbo
		a.myrobot=myrobot
		return a
		

	myrobot=robot()
	key=KEY_RIGHT
	d=[]	
	m=[]
	p=[[12,35],[12,37],[12,36],[12,38],[12,39],[12,40]]
	d = [n for n in [[randrange(1,79,1),randrange(1,29,1)] for x in range(5)] if n not in myrobot.myrobot(0) or bomb or p]
	m = [n for n in [[randrange(1,79,1),randrange(1,29,1)] for x in range((level*10)+5)] if n not in myrobot.myrobot(0) or bomb or d or p]
	for i in range(len(d)):
			win.addch(d[i][1],d[i][0],'D',color_pair(1))
	for i in range(len(m)):
			win.addch(m[i][1],m[i][0],'M',color_pair(2))
	esc_flag=0
	t=0
	k=0
	pause=['PAUSED','pAUSED','paUSED','pauSED','pausED','pauseD','paused']
	
	while key!=27:
		if t%2==0:
			t+=1
			win.border('~','~','-','-','B','O','M','B')
			win.addstr(0,5,'#DIFFUSE CODES: '+str(myrobot.myrobot(2))+str('/5'))
			win.addstr(29,20,'#LIFE: '+str(myrobot.myrobot(4)))
			win.addstr(29,50,'#LEVEL: '+str(level))
		else:
			t-=1
			win.border('.','.','-','-','B','O','M','B')
			win.addstr(0,5,'#DIFFUSE CODES: '+str(myrobot.myrobot(2))+str('/5'),A_BOLD)
			win.addstr(29,20,'#LIFE: '+str(myrobot.myrobot(4)),A_BOLD)
			win.addstr(29,50,'#LEVEL: '+str(level))
		win.timeout(150-level*26)
		win.addstr(0,60,'#Score: '+str(myrobot.myrobot(3)),A_BOLD)
		lastkey=key
		keystroke=win.getch()
		noecho()
		if keystroke!=-1:
			key=keystroke
		if key==ord('p') or key==ord('P'):
			while(1):
				if k>99999999:k=0
				k+=1
				win.addstr(12,35,pause[k%7])
				key=win.getch()
				noecho()
				if key==ord('p') or key==ord('P'):
					win.addstr(12,35,'       ')
					break
				if key==27:
				 	esc_flag=1
				 	break
			key=lastkey
		if esc_flag==1:
		   	break
		myrobot.move_robot(key)
		myrobot.check()	
		if myrobot.getbo()>0: break
		if myrobot.getbr()==1 or myrobot.getbo()>0 or myrobot.myrobot(4)<=0: break
		myrobot.print_erase(key)

		myrobot.create_robot(t)
	endwin()
	if myrobot.myrobot(4)<=0:
		level=4		
		win=newwin(30,80,0,0)
		win.border('~','~','-','-','B','O','M','B')
		win.addstr(12,25,'OOophs!!!!!!! YOU LOST ALL UR LIFE!!!!')
		win.addstr(13,31,'You scored '+str(myrobot.myrobot(3))+' points')
		win.addstr(14,19,':(:(:(:((PRESS Esc TO LEAVE THE GAME):(:(:(:(')
		while(win.getch()!=27):
			continue
		endwin()
	
	elif myrobot.getbo()==100:
		win=newwin(30,80,0,0)
		win.border('~','~','-','-','B','O','M','B')
		if level!=2: win.addstr(12,22,'CONGRTULATIONS!! YOU HAV WON THE LEVEL!!!!',A_BLINK)
		else : win.addstr(12,19,'CONGRTULATIONS!! %%%YOU HAV WON THE GAME!!!!%%%',A_BLINK)
		win.addstr(13,29,'You scored '+str(myrobot.myrobot(3))+' points')
		if(level!=2): win.addstr(15,17,'<><><>Press any other key to go to higher level<><><>')
		win.addstr(14,19,':):):):)(PRESS Esc TO LEAVE THE GAME):):):):)')
		k=-1
		
		while(k==-1): 
			k=win.getch()
		if k==27:
			level=4
		endwin()

	else:
		level=4 
		win=newwin(30,80,0,0)
		win.border('~','~','-','-','B','O','M','B')
		win.addstr(12,25,'OOophs!!!!!!! YOU LOST THE GAME!!!!')
		win.addstr(13,31,'You scored '+str(myrobot.myrobot(3))+' points')
		win.addstr(14,19,':(:(:(:((PRESS Esc TO LEAVE THE GAME):(:(:(:(')
		while(win.getch()!=27):	
			continue
		endwin()
	level+=1
	
	
	
						




