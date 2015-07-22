# -*- coding: cp1252 -*-
from math import *
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import pygame



potentials = ['Pip', 'Magwitch', 'Estella', 'Miss Havisham', 'Jaggers', \
              'Joe', 'Biddy', 'Drummle', 'Orlick', 'Pumblechook', \
              'Herbert', 'Wemmick']

useranswers=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pipanswers = [0, 0.5, 1, 1, 0, 1, 0.5, 1, 1, 1, 0.5, 1, 0.5, 0.5, 1, 1]
magwitchanswers = [0, 1, 0, 0.5, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1]
estellaanswers = [0, 0, 0, 0.5, 0.5, 0, 0, 0, 1, 1, 0.5, 1, 0, 0, 0, 0]
havishamanswers = [0, 1, 0, 0.5, 0.5, 1, 0.5, 0, 1, 0, 0, 0, 0.5, 1, 1, 1]
jaggersanswers = [1, 0.5, 1, 1, 0, 0, 0.5, 0, 1, 1, 0.5, 1, 0.5, 0, 0, 0]
joeanswers = [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0.5, 1, 1]
biddyanswers = [0.5, 0, 0, 0.5, 0.5, 1, 1, 1, 0, 0, 0, 0, 0.5, 0, 1, 1]
drummleanswers = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0.5, 0, 0]
orlickanswers = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0.5, 0, 0.5, 1, 1, 1]
pumblechookanswers = [0.5, 0.5, 1, 1, 0.5, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
herbertanswers = [0.5, 0, 0, 0.5, 1, 1, 1, 1, 0, 0, 0.5, 0, 0.5, 0.5, 1, 1]
wemmickanswers = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 0.5, 0.5, 0, 0]






characteranswers = [pipanswers, magwitchanswers, estellaanswers, \
                    havishamanswers, jaggersanswers, joeanswers, \
                    biddyanswers, drummleanswers, orlickanswers, \
                    pumblechookanswers, herbertanswers, wemmickanswers]

n = 0
m = 0
v = 0
selected = False

scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

finalresults = []

def find_key(dic, val):
    return [k for k, v in dic.iteritems() if v == val][0]

def compare():
    thedictionary = {'Pip': 'You care about your friends, but you will not let that get in the way of your own social and financial ambitions.  You have a moral code, but you sometimes break it.', \
'Magwitch': 'At first glance, you seem completely selfless.  You always stick up for your friends, and you act based \
on what you think is right, not based on greed.  Still, behind all that selflessness is a slightly less wholesome motive: the desire to seem better than your peers', \
'Estella': 'You do not care that much about anything.  You are cold, but not because you are greedy or self-conscious.  In your eyes, the world is yours to toy with.', \
'Miss Havisham': 'You are not friendly and you do not care about what people think of you.  You are motivated by only one thing: the desire for justice.', \
'Jaggers': 'As people go, you are very materialistic.  You want money, but perhaps more importantly, you want people to think of you as high-class.', \
'Joe': 'You are a model human.  You stick up for your friends, you do what you think is fair, and you are not overly greedy or vain.  Good job!', \
'Biddy': 'You are a model human.  You stick up for your friends, you do what you think is fair, and you are not overly greedy or vain.  Good job!', \
'Drummle': 'As people go, you are very materialistic.  You want money, but perhaps more importantly, you want people to think of you as high-class.', \
'Orlick': 'You care about money, but greed is not your sole motivator.  You do not care what people think of you, or how popular you are, but you are driven by a desire for justice.', \
'Pumblechook': 'As people go, you are very materialistic.  You want money, but perhaps more importantly, you want people to think of you as high-class', \
'Herbert': 'You are a model human.  You stick up for your friends, you do what you think is fair, and you are not overly greedy or vain.  Good job!', \
'Wemmick': 'You care about money and appearances, and some might say you are greedy.  But you also greatly value your friends.   As for an internal moral code, well, it appears you lack one...'}
    

    percentages = {}
    names = {}
    for character in characteranswers:
        
        y = 0
        for (i, j) in zip(useranswers, character):
            x = 1 - (abs(i - j))
            y = y + x
            
        scores[characteranswers.index(character)] = y
    
    for lolz in range(len(scores)):
        percentage = 100*(scores[lolz]/16)
        answer = potentials[lolz]
        percentages[answer] = percentage
    final = sorted(percentages.values())
    
    final.reverse()
    question.destroy()
    answer1.destroy()
    answer2.destroy()
    answer3.destroy()
    Begin.destroy()
    last.destroy()

    x = Label(root, text = "Hello there, %s" % (find_key(percentages, final[0])))
    yourguy = find_key(percentages, final[0])
    lastthing = Message(root, text = thedictionary[yourguy], justify = CENTER, width = 200)
    x.config(font = ("times", 20, "bold"))
    x.pack()
    for f in final:
        names[f] = find_key(percentages, f)
        del percentages[find_key(percentages, f)]
        hooray = 'You are %s %% the same as %s' % (f, names[f])
        z = Label(root, text = hooray)
        z.pack()
    blank = Label(root, text = "")
    blank.pack()
    lastthing.pack()
    songdic = {'Miss Havisham': 'mrgrinchhi.ogg', \
               'Pip': 'dontstopbelievingpiphi.ogg', \
                'Biddy': 'dontstopbelievingbiddyhi.ogg', \
                'Orlick': 'psychokillerhi.ogg', \
                'Drummle': 'ihateeverythingaboutyouhi.ogg', \
                'Magwitch': 'breakingthelawhi.ogg', \
                'Jaggers': 'bettergetalawyerhi.ogg', \
                'Estella': 'breakyourhearthi.ogg', \
                'Joe': 'isingasonghi.ogg', \
                'Herbert': 'ohmygodhi.ogg', \
                'Pumblechook': 'youresovainhi.ogg', \
                'Wemmick': 'psychohi.ogg'}
    
    pygame.mixer.music.load(songdic[yourguy])
    pygame.mixer.music.play()
    
    
    
    
            


def valued():
    global n
    global selected
    global useranswers
    useranswers[n] = 1
    selected = True
    
def middle():
    global n
    global selected
    global useranswers
    useranswers[n] = 0.5
    selected = True
    
def unvalued():
    global n
    global selected
    global useranswers
    useranswers[n] = 0
    selected = True
    
def start():
    global please_select
    global n
    global m
    global x
    global answer1
    global answer2
    global answer3
    
    x = StringVar(root)
    question.config(text = questions[n])
    welcome.destroy()
    Begin.config(text = "Next question", command = next)
    Begin.pack_forget()
    answer1 = Radiobutton(root, text = answers[m], command = valued, value=2, variable = x)
    answer2 = Radiobutton(root, text = answers[m+1], command = middle, value=1, variable=x)
    answer3 = Radiobutton(root, text = answers[m+2], command = unvalued, value=0, variable=x)
    x.set(None)
    answer1.pack()
    answer2.pack()
    answer3.pack()
    Begin.pack()
    please_select = Label(root, text = "")
    please_select.pack()
    pygame.mixer.init()
    pygame.mixer.music.load('whooshhi10.ogg')
    pygame.mixer.music.play()

    

def next():
    global please_select
    global last
    global v
    global n
    global m
    global answer1
    global answer2
    global answer3
    global selected

    
    x.set(None)
    please_select.config(text = "")
    
    if selected == False:
        please_select.config(text = "Please select an answer.")
    elif selected == True:
        if n == 15:
            compare()
        elif n < 15:
            pygame.mixer.init()
            pygame.mixer.music.load('whooshhi10.ogg')
            pygame.mixer.music.play()
            n +=1
            m+=3
            question.config(text = questions[n])
            answer1.config(text = answers[m])
            answer2.config(text = answers[m+1])
            answer3.config(text = answers[m+2])
            selected = False
            if n == 1:
                pygame.mixer.init()
                pygame.mixer.music.load('whooshhi10.ogg')
                pygame.mixer.music.play()
                
                last = Button(root, text = "Go back", command = previous)
                last.pack()
            if answers[m+1] == "":
                answer2.pack_forget()
            else:
                welcome.destroy()
                question.pack_forget()
                Begin.pack_forget()
                answer1.pack_forget()
                answer2.pack_forget()
                answer3.pack_forget()
                last.pack_forget()
                please_select.pack_forget()
                question.pack()
                
                answer1.pack()
                answer2.pack()
                answer3.pack()
                Begin.pack()
                last.pack()
                please_select.pack()
            
            
            
    
    

def previous():
    global n
    global v
    global m
    global answer1
    global answer2
    global answer3

    n -=1
    m -= 3
    question.config(text = questions[n])
    answer1.config(text = answers[m])
    answer2.config(text = answers[m+1])
    answer3.config(text = answers[m+2])
    please_select.config(text = "")
    x.set(None)
    if answers[m+1] == "":
            answer2.pack_forget()
    else:
        question.pack_forget()
        Begin.pack_forget()
        answer1.pack_forget()
        answer2.pack_forget()
        answer3.pack_forget()
        last.pack_forget()
        please_select.pack_forget()
        question.pack()
        answer1.pack()
        answer2.pack()
        answer3.pack()
        Begin.pack()
        last.pack()
        please_select.pack()
    
    if n <1:
        last.destroy()
        
    
    
    
questions = ["You have just won the lottery.  You have \
friends who do not ask you for any money, but who you know could use it.", \
"You find a wallet on the ground with a substantial amount \
of money.  Beside the wallet on the ground, you see a hundred dollar bill.  \
There is a phone number inside the wallet at which you could reach the \
wallet's owner.", "Your neighbor is rich.  Are you jealous?", \
"An evil alien race brainwashed your friend, and now he is offering \
to give you ten thousand dollars, no strings attached.  Do you take it?", \
"Your friend in California is very ill.  You haven't talked to him in \
a while, and you know he doesn't expect you to visit him.", \
"You are teaching your friend how to play basketball.  \
He is terrible, and you are tempted to make fun of him.", \
"Your old high school buddy gets in an accident and \
becomes blind and mute.  It is becoming difficult to \
continue a normal relationship with him.", \
"Your classmate is involved in a gang, and you \
know he has gotten himself in a very dangerous situation.  \
Helping him would be dangerous, but could save his life.", \
"You've been friends with your neighbor since you were two years old, \
but now you are entering elementary school.  Your neighbor gets made \
fun of frequently, but you are considered cool.", \
"You are about to graduate college and are eager to start your \
life as an adult.  However, your parents tell you that anyone who \
doesn't go to graduate school is uneducated and uncivilized.", \
"You fall in love at first site.  Suddenly, you realize \
that your new sweetheart is significantly wealthier than you.  \
The conversation turns to your car, which is in \
reality a beat-up 1983 red sports car.", \
"At lunch, when the table question is asked, are you more \
afraid of waiting or of your answer appearing foolish?", \
"You hear about the government killing its own civilians in Syria on \
the radio.  How personally affected do you feel when you hear the news?", \
"You are an amazing chess player.  Somehow, your friend Bob managed to \
cheat in a game in chess that you should have won.  The game wasn't \
very important, but you still feel annoyed.  \
How do you treat Bob in the future?", \
" 'All is fair in love and war' - agree or disagree.", \
"A burglar robs a million dollars from person X.  There is no \
chance that the burglar will ever be caught or sent to jail.  \
However, it is in person X's power to rob the money back from the \
burglar.  Would that be justified?"]


answers = ["No way! It's my money!", "Well, maybe I'll take him out to a \
nice dinner or something.", "I don't need all this money! Why not give a \
lot of it to my friend?", "Keep the wallet and the $100", "Give the wallet to \
the owner, but keep the $100", "Give the wallet to the owner and ask him \
whether the money next to it was his.", "Yes", "", "No", "Of course I'll take \
it, and while I'm at it, I'll see if he'll offer more.", \
"I'll take it, I guess, but I want this whole ordeal to be over with soon...", \
"No, I won't take it!  It's dirty money!", "I'm going to buy a plane ticket right away", "I'll send him \
a postcard - I wish I could go but it would be too hard.", "We haven't talked \
for a long time.  I know he wouldn't mind if I didn't see him, \n so it's okay \
not to go", "Well, this is pretty tedious, but I'm determined to help him no matter what", \
           "", "Jeez this is frustrating!  I think we're going to have to stop, \
\n because this is getting embarassing.", "We're friends forever! I don't care if he's \
blind or mute or anything!", "I don't want to hurt his feelings, so I'm going \
to gradually reduce \n how much time I spend with him", "I'm not going to be able to stand \
being around him anymore.  \n It's nothing personal, but I'm going to have to \
stop hanging out with him", "Help him - He's my best \
friend; I'd do anything for him", "", "Don't help him - He got himself into \
this mess and I won't get myself killed over it.", \
           "I'm at a new school, so it's time to make new friends", \
           "I will join the other kids and lightly tease my neighbor, but \
privately remain friends with him", "Whenever my friend is made fun of, I \
will publically defend him", "Well, I definitely don't want my parents to think \
badly of me, so I'll go to grad school.", "", "I don't care what they \
think of me - I want to get on with my life", "Tell her you have a \
$200,000 lamborghini", "Tell her you have a sweet red sports car", "Tell \
her you have a beat up 1983 red sports car", "Appearing foolish", "", \
           "Waiting", "I can't believe this is happening.  I'm going to  \
find out how I can help", "That's really sad, but it's not as if I can really \
do anything about it", "It doesn't really affect me, so I don't care that much", "I will \
avoid talking to him again", "I'm angry, but I will continue to be friends \
with him", "Who cares?  It's a chess game!", "Disagree", "", "Agree", "Yes", \
           "", "No"]

           

    
root = Tk()

root.title("Which Great Expectations Character Are You?")
root.geometry("520x460")



welcome = Message(root, text = "Which Great Expectations character are you?  \
Start the quiz to find out.  Remember, choose the best available answer \
to each question, even if no answer perfectly matches your opinion.", width = 400,\
                  justify = CENTER)

welcome.pack()

question = Message(root, text = "", width = 400, justify = CENTER)
question.config(font = ("times", 12, "italic"))
question.pack()



Begin = Button(root, text="Start the quiz", command = start)
Begin.pack()






root.mainloop()
    




           

