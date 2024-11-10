import pgzrun
WIDTH=800
HEIGHT=800
TITLE="game"
totall=0
all_questions=[]
question_num=-1
question=[]
timer=10
game_over=False

q1_box=Rect(50,350,240,150)
q2_box=Rect(320,350,240,150)
q3_box=Rect(50,550,240,150)
q4_box=Rect(320,550,240,150)
skip_box=Rect(600,350,150,400)
fancy_thing=Rect(0,0,800,80)
timer_box=Rect(600,150,150,150)
question_box=Rect(50,150,500,150)
questions_box=[q1_box,q2_box,q3_box,q4_box]
def draw():

    screen.draw.filled_rect(q1_box,"orange")
    screen.draw.filled_rect(q2_box,"orange")
    screen.draw.filled_rect(q3_box,"orange")
    screen.draw.filled_rect(q4_box,"orange")
    screen.draw.filled_rect(skip_box,"green")
    screen.draw.filled_rect(fancy_thing,"gray")
    screen.draw.filled_rect(timer_box,"gray")
    screen.draw.filled_rect(question_box,"orange")
    screen.draw.textbox(question[0],question_box,color="white")
    screen.draw.textbox(question[1],q1_box,color="white")
    screen.draw.textbox(question[2],q2_box,color="white")
    screen.draw.textbox(question[3],q3_box,color="white")
    screen.draw.textbox(question[4],q4_box,color="white")
    screen.draw.textbox(":)",fancy_thing,color="white")
    screen.draw.textbox(str(timer),timer_box,color="white")
    screen.draw.textbox("skip",skip_box,color="white")


def file_reading():
    global all_questions
    global totall
    q=open("questions.txt","r")
    all_questions=q.readlines()
    totall=len(all_questions)
file_reading()
def read_question():
    global game_over
    global question
    global question_num
    global timer
    timer=10
    question_num=question_num+1
    if question_num>=11:
        game_over1()
    else:
        question=all_questions[question_num].split(",")
        print (question)

read_question()

def update_time():
    global game_over
    global timer
    if timer <= 0:
        game_over1()
    else:
        timer=timer-1
clock.schedule_interval(update_time,1)
def on_mouse_down(pos):
    global game_over
    global totall
    global timer
    nummber=1
    for box in questions_box:
        if box.collidepoint(pos):
            if nummber==int(question[5]):
                totall=totall+1

                read_question()
            else:
                game_over1()
        nummber=nummber+1
        if skip_box.collidepoint(pos):
            read_question()
 
def game_over1():
    global game_over,question,timer
    game_over=True
    timer=0
    question=["game_over","-","-","-","-",5]


def update():
    pass
pgzrun.go()