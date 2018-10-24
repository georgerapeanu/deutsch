import random
import tkinter
from functools import partial

Verben = [
("backen","backte","gebacken","haben","a coace"),
("beginnen","begann","begonnen","haben","a incepe"),
("beißen","biss","gebissen","haben","a musca"),
("betrügen","betrog","betrogen","haben","a insela"),
("bieten","bot","geboten","haben","a oferi"),
("bitten","bat","gebeten","haben","a ruga"),
("bleiben","blieb","geblieben","sein","a ramane"),
("braten","briet","gebraten","haben","a frige"),
("brechen","brach","gebrochen","haben","a rupe"),
("brennen","brannte","gebrannt","sein","a arde"),
("bringen","brachte","gebracht","haben","a aduce"),
("denken","dachte","gedacht","haben","a gandi"),
("erlöschen","erlosch","erloschen","sein","a se stinge"),
("erschrecken","erschrack","erschrocken","sein","a se speria"),
("essen","aß","gegessen","haben","a manca"),
("fahren","fuhr","gefahren","sein","a merge"),
("fallen","fiel","gefallen","sein","a cadea"),
("fangen","fing","gefangen","haben","a prinde"),
("finden","fand","gefunden","haben","a gasi"),
("fliegen","flog","geflogen","sein","a zbura"),
("fliehen","floh","geflohen","sein","a evada"),
("frieren","fror","gefroren","sein","a ingheta"),
("gebären","gebar","geboren","sein","a naste"),
("geben","gab","gegeben","haben","a da"),
("gehen","ging","gegangen","sein","a merge"),
("gelingen","gelang","gelungen","sein","a reusi"),
("gelten","galt","gegolten","haben","a valora"),
("genießen","genoss","genossen","haben","a savura"),
("geschehen","geschah","geschehen","sein","a se intampla"),
("gewinnen","gewann","gewonnen","haben","a castiga"),
("gießen","goss","gegossen","haben","a turna"),
("graben","grub","gegraben","haben","a sapa"),
("greifen","griff","gegriffen","haben","a apuca"),
("haben","hatte","gehabt","haben","a avea"),
("halten","hielt","gehalten","haben","a opri"),
("hängen","hing","gehangen","haben","a atarna"),
("heben","hob","gehoben","haben","a ridica"),
("heißen","hieß","geheißen","haben","a se numi"),
("helfen","half","geholfen","haben","a ajuta"),
("kennen","kannte","gekannt","haben","a cunoaste"),
("kommen","kam","gekommen","sein","a veni"),
("können","konnte","gekonnt","haben","a putea"),
("kriechen","kroch","gekrochen","sein","a se tara"),
("laden","lud","geladen","haben","a incarca"),
("lassen","ließ","gelassen","haben","a lasa"),
("laufen","lief","gelaufen","sein","a alerga"),
("leiden","litt","gelitten","haben","a suferi"),
("leihen","lieh","geliehen","haben","a imprumuta"),
("lesen","las","gelesen","haben","a citi"),
("liegen","lag","gelegen","haben","a sta culcat"),
("lügen","log","gelogen","haben","a minti"),
("meiden","mied","gemieden","haben","a evita"),
("messen","maß","gemessen","haben","a masura"),
("mögen","mochte","gemocht","haben","a dori"),
("müssen","musste","gemusst","haben","a trebui"),
("nehmen","nahm","genommen","haben","a lua"),
("raten","riet","geraten","haben","a sfatui"),
("reißen","riss","gerissen","sein","a rupe"),
("riechen","roch","gerochen","haben","a mirosi"),
("rufen","rief","gerufen","haben","a chema"),
("saufen","soff","gesoffen","haben","a bea mult"),
("schaffen","schuff","geschaffen","haben","a crea"),
("scheinen","schien","geschienen","haben","a parea"),
("schieben","schob","geschoben","haben","a impinge"),
("schlafen","schlief","geschlafen","haben","a dormi"),
("schlagen","schlug","geschlagen","haben","a bate"),
("schleichen","schlich","geschlichen","sein","a se furisa"),
("schließen","schloss","geschlossen","haben","a inchide"),
("schmeißen","schmiss","geschmissen","haben","a arunca"),
("schmelzen","schmolz","geschmolzen","sein","a se topi"),
("schreiben","schrieb","geschrieben","haben","a scrie"),
("schreien","schrie","geschrien","haben","a tipa"),
("schweigen","schwieg","geschwiegen","haben","a tacea"),
("schwimmen","schwamm","geschwommen","sein","a inota"),
("sehen","sah","gesehen","haben","a vedea"),
("sein","war","gewesen","sein","a fi"),
("singen","sang","gesungen","haben","a canta"),
("sitzen","saß","gesessen","haben","a sedea"),
("sollen","sollte","gesollt","haben","a trebui"),
("sprechen","sprach","gesprochen","haben","a vorbi"),
("stehen","stand","gestanden","sein","a sta in picioare"),
("steigen","stieg","gestiegen","sein","a urca"),
("stehlen","stahl","gestohlen","haben","a fura"),
("sterben","starb","gestorben","sein","a muri"),
("stinken","stank","gestunken","haben","a mirosi urat"),
("streiten","stritt","gestritten","haben","a se certa"),
("tragen","trug","getragen","haben","a purta"),
("treffen","traf","getroffen","haben","a intalni"),
("treten","trat","getreten","sein","a calca"),
("tun","tat","getan","haben","a face"),
("verderben","verdarb","verdorben","haben","a strica"),
("vergessen","vergaß","vergessen","haben","a uita"),
("verlieren","verlor","verloren","haben","a pierde"),
("wachsen","wuchs","gewachsen","sein","a creste"),
("werden","wurde","geworden","sein","a deveni"),
("werfen","warf","geworfen","haben","a arunca"),
("wissen","wusste","gewusst","haben","a sti"),
("wollen","wollte","gewollt","haben","a vrea"),
("ziehen","zog","gezogen","sein","a trage"),
]

buttons = ['ä','ö','ü','ß']

def pressButt(ide):
	if focused_entry is not None:
		focused_entry.insert("insert",buttons[ide])
def check(a,x2,no):
	if str(a.get()) == x2:
		global solved
		solved = solved + 1
		a.configure(bg = "green",state = 'disabled')
		if solved == 3:
			app(random.randrange(0,len(Verben),1))
	
	else:
		a.configure(bg = "red")

def remember_focus(event):
	global focused_entry
	focused_entry = event.widget
		
def app(ide):
	global solved
	solved = 0
	global top
	global tmp1
	global tmp2
	global tmp3
	global tmp4
	global tmp5
	global x1
	global y1
	global z1
	global u1
	global w1
	global x2
	global y2
	global z2
	global u2
	global w2
	global a
	global b
	global c
	global d
	if top is None:
		top = tkinter.Tk()
		tmp1 = tkinter.Canvas(top)
		tmp2 = tkinter.Canvas(top)
		tmp3 = tkinter.Canvas(top)
		tmp4 = tkinter.Canvas(top)
		tmp5 = tkinter.Canvas(top)
		x1 = tkinter.Label(tmp1,height = 1,width = 12,text = "infinitv:")
		y1 = tkinter.Label(tmp2,height = 1,width = 12,text = "präteritum:")
		z1 = tkinter.Label(tmp3,height = 1,width = 12,text = "partizip II:")
		w1 = tkinter.Label(tmp4,height = 1,width = 12,text = "hilfsverben:")
		u1 = tkinter.Label(tmp5,height = 1,width = 12,text = "übersetzung:")
		x1.pack(side = tkinter.LEFT)
		y1.pack(side = tkinter.LEFT)
		z1.pack(side = tkinter.LEFT)
		w1.pack(side = tkinter.LEFT)
		u1.pack(side = tkinter.LEFT)
		x2 = tkinter.Entry(tmp1,bg = 'white')
		x2.insert("0",Verben[ide][0])
		x2.configure(state = 'disabled')
		y2 = tkinter.Entry(tmp2,bg = 'white')
		y2.bind('<Return>',partial(check,y2,Verben[ide][1]))
		y2.bind('<FocusIn>',remember_focus)
		z2 = tkinter.Entry(tmp3,bg = 'white')
		z2.bind('<Return>',partial(check,z2,Verben[ide][2]))
		z2.bind('<FocusIn>',remember_focus)
		w2 = tkinter.Entry(tmp4,bg = 'white')
		w2.bind('<Return>',partial(check,w2,Verben[ide][3]))
		w2.bind('<FocusIn>',remember_focus)
		u2 = tkinter.Entry(tmp5,bg = 'white')
		u2.insert("0",Verben[ide][4])
		u2.configure(state = 'disabled')
		x2.pack(side = tkinter.LEFT)
		y2.pack(side = tkinter.LEFT)
		z2.pack(side = tkinter.LEFT)
		w2.pack(side = tkinter.LEFT)
		u2.pack(side = tkinter.LEFT)
		tmp1.pack()
		tmp2.pack()
		tmp3.pack()
		tmp4.pack()
		tmp5.pack()
		
		a = tkinter.Button(top,text = buttons[0],takefocus = False,command = partial(pressButt,0))
		b = tkinter.Button(top,text = buttons[1],takefocus = False,command = partial(pressButt,1))
		c = tkinter.Button(top,text = buttons[2],takefocus = False,command = partial(pressButt,2))
		d = tkinter.Button(top,text = buttons[3],takefocus = False,command = partial(pressButt,3))
		a.pack(side = tkinter.LEFT)
		b.pack(side = tkinter.LEFT)
		c.pack(side = tkinter.LEFT)
		d.pack(side = tkinter.LEFT)
	else:
		x1.configure(height = 1,width = 12,text = "infinitv:")
		y1.configure(height = 1,width = 12,text = "präteritum:")
		z1.configure(height = 1,width = 12,text = "partizip II:")
		w1.configure(height = 1,width = 12,text = "hilfsverben:")
		u1.configure(height = 1,width = 12,text = "übersetzung:")
		x1.pack(side = tkinter.LEFT)
		y1.pack(side = tkinter.LEFT)
		z1.pack(side = tkinter.LEFT)
		w1.pack(side = tkinter.LEFT)
		u1.pack(side = tkinter.LEFT)
		x2.configure(state = 'normal',bg = 'white')
		x2.delete(0, 'end')
		x2.insert("0",Verben[ide][0])
		x2.configure(state = 'disabled')
		y2.bind('<Return>',partial(check,y2,Verben[ide][1]))
		y2.configure(state = 'normal',bg = 'white')
		y2.delete(0, 'end')
		y2.bind('<FocusIn>',remember_focus)
		z2.bind('<Return>',partial(check,z2,Verben[ide][2]))
		z2.configure(state = 'normal',bg = 'white')
		z2.delete(0, 'end')
		z2.bind('<FocusIn>',remember_focus)
		w2.bind('<Return>',partial(check,w2,Verben[ide][3]))
		w2.configure(state = 'normal',bg = 'white')
		w2.delete(0, 'end')
		w2.bind('<FocusIn>',remember_focus)
		u2.configure(state = 'normal',bg = 'white')
		u2.delete(0, 'end')
		u2.insert("0",Verben[ide][4])
		u2.configure(state = 'disabled')
		x2.pack(side = tkinter.LEFT)
		y2.pack(side = tkinter.LEFT)
		z2.pack(side = tkinter.LEFT)
		w2.pack(side = tkinter.LEFT)
		u2.pack(side = tkinter.LEFT)
		tmp1.pack()
		tmp2.pack()
		tmp3.pack()
		tmp4.pack()
		tmp5.pack()
		
		a.configure(text = buttons[0],takefocus = False,command = partial(pressButt,0))
		b.configure(text = buttons[1],takefocus = False,command = partial(pressButt,1))
		c.configure(text = buttons[2],takefocus = False,command = partial(pressButt,2))
		d.configure(text = buttons[3],takefocus = False,command = partial(pressButt,3))
		a.pack(side = tkinter.LEFT)
		b.pack(side = tkinter.LEFT)
		c.pack(side = tkinter.LEFT)
		d.pack(side = tkinter.LEFT)
		
	tkinter.mainloop()
	
def __main__():
	global top
	top = None
	app(random.randrange(0,len(Verben),1))
__main__()
