define n = Character("Topsy the Triceratops")

define j = Character("Jeff Goldblum")


define circleirisin = ImageDissolve("imagedissolve circleiris.png", 2.0, 8 , reverse=True)
define circleirisout = ImageDissolve("imagedissolve circleiris.png", 2.0, 8)

define circleirisinslow = ImageDissolve("imagedissolve circleiris.png", 3.0, 8 , reverse=True)
define circleirisoutslow = ImageDissolve("imagedissolve circleiris.png", 3.0, 8)

define gui.choice_button_text_idle_color = '#888888'
define gui.choice_text_hover_color = '#0066cc'
define gui.textbox_height = 130

image vraptor = "vraptor.png"


    


#init python:
  #  def pickAConvo():
   #     conversationList=[1,2,3,4,5,6,7,8,9,10,11,12]
    #    conversation=renpy.random.choice(conversationList)
     #   if conversation==1:
      #    return(j "Ooh, look at that dog."
       #   n "…")
        #  conversationList.remove(1)
       # if conversation==2:
       #     j "Oh no! I left my environmentally-friendly reusable coffee cup at home!"
       #     n "I am not going back"
      #      conversationList.remove(2)
      #  if conversation==3:
      #      j "Have you ever considered the subjective nature of the human condition and its impact on the perception of sensory information?"
      #      j "If you consider that everyone perceives details differently, you could say that no-one has an objective idea of what the world is like."
      #      n "We had no conception of a world without dinosaurs. Then the sky fell down."
      #      conversationList.remove(3)
      #  if conversation==4:
      #      j "Do you remember that day we went to the fair?"
       #     n "You were on the dodgems for 45 minutes."
       #     conversationList.remove(4)
      #  if conversation==5:
       #     j "I’ve been thinking about getting a roomba."
       #     n "You won’t. You like vacuuming too much."
       #     conversationList.remove(5)
      #  if conversation==6:
      #      j "Have you heard this song? I love this song."
       #     n "I am 65 million years old and even I know this song."
        #    n "..."
         #   n "Turn it up."
         #   conversationList.remove(6)
    #    if conversation==7:
     #       j "Look at this guy’s license plate."
      #      n "GR888T. Oh, ho ho ho, I get it. Very good."
      #      conversationList.remove(7)
      #  if conversation==8:
      #      j "♫ Fly me to the moon, let me play among the stars… ♫"
      #      n "Please stop singing."
      #      n "..."
      #      n "Now it’s stuck in my head."
      #      conversationList.remove(8)
      #  if conversation==9:
      #      j "Look at that person running for the bus."
      #      n "They’re not going to make it."
      #      j "I think they might."
      #      n "Not going to happen."
      #      j "… oh, there goes the bus. They do not look happy."
      #      conversationList.remove(9)
      #  if conversation==10:
      #      j "^yaaawn^"
      #      n "I told you you shouldn’t have tried to binge watch the entire season."
      #      j "It’s not my fault she couldn’t decide between Mark and Sarah. I had to find out how it ended."
      #      conversationList.remove(10)
      #  if conversation==11:
      #      n "Is Chris Hemsworth really as muscly as he looks?"
      #      j "Even musclier."
      #      conversationList.remove(11)
      #  if conversation==12:
      #      j "“This is a really good book, no wonder everyone’s talking about it. I wonder what’s going to happen to Ned…"
      #      n "Please concentrate on the road."
      #      conversationList.remove(12)

image alpha_control:
    "spotlight.png"

    anchor (.5, .5)

    parallel:
        zoom 0
        linear .5 zoom .75
        pause 2
        linear 1.0 zoom 4.0

    parallel:
        xpos 0.0 ypos .6
        linear 1.5 xpos 1.0
        linear 1.0 xpos .5 ypos .2

    pause .5
    repeat

define spotlight = AlphaDissolve("alpha_control", delay=3.5)

init:
    image vraptor livecomposite = LiveComposite((200, 300),
                                             (0, 0), anim.Blink(Image("vraptor.png")),
                                             (0, 50), "vraptor.png",
                                             (0, 100), "vraptor.png")

 
 

label start:



    scene bg background0
    play music "Project Jeff main theme ver1.mp3" fadein 1.0

    "{i}It is an overcast Wednesday morning. Help esteemed actor Jeff Goldblum get to work on time!"
    
    j "I'm going to work, I'd better hurry or I'll be late."

    j "Oh look! There is my trusty triceratops, Topsy!"
    

    scene black
    with circleirisin
 
    scene bg background1
    with circleirisout
    show ft onejeff at Move((-0.5, 0.5), (0.0, 0.0), 4.0)
    # play sound "Test sound.mp3"
    

    "{i}It is peak hour. Traffic is crawling along, and Jeff has to be at work in 27 minutes."
    "{i}He has already been late twice this month, and cannot risk angering his boss."
    j "Oh no! I left my environmentally-friendly reusable coffee cup at home!"
    n "I am not going back"
    
    scene black
    with circleirisin
    show ft jeffhead

    j "Goodness Topsy, this traffic looks awful.  How should we go to work?"
  
    show ft trihead
    menu:

        "Stick with the normal route to work":
            play music "Project Jeff main theme stay in traffic ver1.mp3" fadeout 2.0 fadein 2.0
            jump screen2
        "Take a short cut down an unknown route":
            #stop music fadeout 1.0
            play music "Project Jeff main theme B ver 1.mp3" fadeout 4.0 #fadein 2.0
            jump screen3
    
label screen2:
    scene bg background2
    with circleirisoutslow
    show ft onejeff at Move((-0.5, 0.5), (0.0, 0.0), 4.0)
    "{i}Traffic has come to a complete standstill." 
    j "Ooh, look at that dog."
    n "…"
    "{i}Reports come over the radio of an overturned stegosaurus up ahead. It was carrying 15 tonnes of caramel fudge."
    "{i}Clean up is slow and delicious." 
    scene black
    with circleirisin
    show ft jeffhead
    j "What should we do Topsy? Wait it out, or turn off onto the side street?"
    show ft trihead
    menu:
        "Wait patiently":
            
            stop music fadeout 1.0
            play sound "Project Jeff ending A.mp3" 
            jump screen4
            
        "Turn off onto the side street":
            scene bg background2
            with circleirisoutslow
            scene bg backgroundb2
            with Dissolve(3.0)
            stop music fadeout 3.5
            pause 2.0
            jump screen5
label screen4:
    scene bg background4
    with circleirisoutslow
    "{i}Jeff obeyed all the road rules, and has arrived safely at work."
    "{i}Unfortunately, it is now 5:48pm, and work has closed for the day."
    "{i}Jeff must turn around and go home, where he will dream of living a different life."
    scene black
    with circleirisin
    show ft jeffhead
    j "I hate my life"
    hide ft jeffhead
    with Dissolve(0.5)
    #"The End"
    scene bg credits
    with circleirisoutslow
    menu:
        "Start again":
            jump start
        "Leave Jeff to his own devices":
            return
        
    
    
    return
label screen5:
    scene bg background5
    with vpunch
    
    "{i}Jeff pulled out into oncoming traffic without a clear line of sight."
    "{i}This was a reckless mistake- "
    with vpunch
    play sound "Project Jeff ending B.mp3" 
    "{i}Jeff has been squashed flat by a passing 30-tonne brontosaurus."
    with vpunch
    "{i}Road safety is everyone’s responsibility."
    #j "..."
    scene bg credits
    with circleirisoutslow
    menu:
        "Start again":
            jump start
        "Leave Jeff to his own devices":
            return
label screen3:
    scene bg background3
    with circleirisoutslow
    
    
    show img bush behind ft at right
    

    
    show vraptor behind ft, img
    
        #xalign 0.9
    "{i}Jeff has turned down a dark and scary path."
    show ft onejeff at Move((-0.5, 0.5), (0.0, 0.0), 4.0):
        # xalign 0.25
    with dissolve
    "{i}The road is unpaved and lacks speed limit signs."
    #play sound "Test sound.mp3"
    show img bush:
        xalign 0.9
        
    with hpunch
    #play sound "Test sound.mp3"
    #pause 1.0
    j "What was that?"
    show img bush:
        xalign 0.9
    with hpunch
    n "It's coming from that bush..."
    show img bush at Move((0.0, 0.0), (1.0, 1.0), 7.0)
    show ft onejeff at Move((0.0, 0.0), (-0.2, 0.2), 4.0)
    pause 1.0
    show vraptor at Move((0.0, 0.0), (-0.02, 0.02), 2.0)
    n "It's a velociraptor!!!!!"

    show vraptor
    with hpunch

    scene black
    with circleirisin
    show ft jeffhead
    j "ARRRRGGGGGHHHHHHHHH!!!!"
    show ft trihead
    n "What should we do? Run away, or stand and fight?"
    menu:
        "RUN AWAY!!!!!!!!!":
            jump screen6
        "Stand and fight":
            stop music fadeout 3.0
            play sound "Project Jeff ending D1.mp3" 
            jump screen7
label screen6:
    scene bg background6
    with circleirisoutslow
    stop music fadeout 10.0
    "{i}Jeff’s hardy triceratops boldly swipes at the velociraptor as they charge past, scaring it off."
    "{i}Jeff’s shirt is sacrificed in the process."
    scene black
    with circleirisin
    show ft jeffhead
    j "My shirt!"
    play sound "Project Jeff ending C.mp3" 
    
    scene bg background8
    with circleirisoutslow
    
    
    "{i}He arrives at work on time, shirtless and triumphant."
    "{i}His coworkers didn't seem to mind the lack of clothing" 
    "{i}Well done!"
    scene bg credits
    with circleirisoutslow
    menu:
        "Start again":
            jump start
        "Leave Jeff to his own devices":
            return
label screen7:
    scene bg background7
    with circleirisoutslow
    "{i}Against all medical advice, Jeff dismounts his faithful triceratops and engages the velociraptor in hand-to-hand combat."
    #play sound "Project Jeff ending D1.mp3" 
    j "@#@^#!#"
    #j "&^#!^@#!@^#^"
    n "This was not your best idea Jeff"
    #j "@!#&($#$$"
    j "..."
    #play sound "Project Jeff ending D1.mp3" 
     
    scene bg background9
    with circleirisout
    "{i}The velociraptor counters Jeff’s wild haymaker with its set of sharp, serrated teeth."
    with vpunch
    "{i}The velociraptor escapes back into the trees with a full belly."
    with vpunch
    j "My arm!"
    play sound "Project Jeff ending D2.mp3"
    "{i}Jeff arrives at work on time, but his boss reprimands him for the sharp decrease in his productivity."
    scene bg credits
    with circleirisoutslow
    menu:
        "Start again":
            jump start
        "Leave Jeff to his own devices":
            return