# The script of the game goes in this file.

# Initialize variables
init python:
    persistent.affection = 0
    cocaine = 0
    name = "barrow"

# Make timeline
default timeline1 = ["timeline1"]
default timeline2 = ["timeline1", "timeline2"]
default timeline3 = ["timeline1", "timeline2", "timeline3"]
default timeline4 = ["timeline1", "timeline2", "timeline3", "timeline4"]
default timeline5 = ["timeline1", "timeline2", "timeline3", "timeline4", "timeline5"]
default timeline6 = ["timeline1", "timeline2", "timeline3", "timeline4", "timeline5", "timeline6"]

default Lightbox_image = ""

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Doctor = Character("Dr.Darby", who_color="#71c3ff")
image Doctor 1 = "Doctor1.png"
image Doctor 2 = "Doctor2.png"
image Doctor 3 = "Doctor3.png"

define Barrow = Character("Isaac Barrow", who_color="#ff8c00")
image Barrow 1 = "Barrow1.png"
image Barrow 2 = "Barrow2.png"
image Barrow 3 = "Barrow3.png"
image Barrow 4 = "Barrow4.png"
image Barrow 6 = "Barrow6.png"

define Newton = Character("Isaac Newton", who_color="#6ccf60")
image Newton 1 = "Newton.png"

define Captain = Character("Captain Brockmann", who_color="#ad60cf")
image Captain 1 = "Captain1.png"
image Captain 2 = "Captain2.png"

define Sailor = Character("Sailor", who_color="#002bff")
image Sailor 1 = "Sailor.png"

define Pirate1 = Character("Pirate1", who_color="#519c51")
image Pirate1 1 = "Pirate1.png"
define Pirate2 = Character("Pirate2", who_color="#9c5151")
image Pirate1 2 = "Pirate2.png"
define Pirate3 = Character("Pirate3", who_color="#9a9c51")
image Pirate1 3 = "Pirate3.png"

define Narrator = Character(" ")
define Player = "[name]"
define Unknown = Character("???")

#backgrounds/images
image black = "#000"
image lab = "lab.png"
image controlPanel1 = "controlPanel1.png"
image controlPanel2 = "controlPanel2.png"
image energy = "energy.png"
image smoke = "smoke.png"
image button = "button.png"
image london = "london-street.jpg"
image house = "house.jfif"
image dock = "dock.jpeg"
image london2 = "london2.png"
image grass = "grass.png"
image deck = "deck.png"
image doorway = "doorway.png"
image jojo = "jojo.png"
image math = "math.png"
image cabin = "cabin.png"
image superior = "chadBarrow.png"

# The game starts here.

label start:

    $ cocaine = 0
    $ future = "false"

    # Show a background.
    scene lab 

    # This shows a character sprite.
    show Doctor 1

    # These display lines of dialogue.
    play sound "audio/Darby/0.mp3"
    Doctor "Ah welcome, you must be my new assistant."
    stop sound
    show Doctor 2

    play sound "audio/Darby/1.mp3"
    Doctor "hmmn, what was your name again?"
    stop sound

    $ name = renpy.input("Enter a name:")

    show Doctor 3
    play sound "audio/Darby/2.mp3"
    Doctor "Oh of course, [name], thank you for applying. After my former assistant had that time incident, I've been rather shorthanded."
    stop sound

    menu:

        "You're welcome, I'm ready to learn!":
            show Doctor 1
            play sound "audio/Darby/3.mp3"
            Doctor "The pleasure is all mine. It is an honor to have the prodigy of our time in my humble lab."
            stop sound

        "Time incident…?":
            show Doctor 1
            play sound "audio/Darby/4.mp3"
            Doctor "Fear not, I'm sure he felt nothing as his body was torn through time. The machine wasn't fully functional but he snuck a test run. Sigh, he was such a bright young man, innovation exuded from his every action."
            stop sound

    play sound "audio/Darby/5.mp3"        
    Doctor "Ah, as your first assignment, could you please enter the chamber and hit the button beside the energy gauge."
    stop sound
    hide Doctor 1 with dissolve

    scene button with dissolve

    play sound "audio/Adam/0.mp3"
    Narrator "You walk into the roomy chamber, admiring the sleek interior paneling."
    stop sound

    scene energy with dissolve

    play sound "audio/Adam/1.mp3"
    Narrator "Tapping the button, the infinity gauge begins to fill. You swivel to face the doctor."
    stop sound

    scene controlPanel1 with dissolve

    play sound "audio/Adam/2.mp3"
    Narrator "His back turned to you. He seems to be muttering something as he scans the control panel."
    stop sound

    play sound "audio/Darby/6.mp3"
    Doctor "They say you're a genius, that one day you'll become a mind that could rival even me…"
    stop sound

    scene smoke with dissolve

    play sound "audio/Adam/3.mp3"
    Narrator "The door zips shut, energy is half full, and smoke begins to fill your vision."
    stop sound

    scene black with dissolve

    play sound "audio/Adam/4.mp3"
    Narrator "Your eyes wane, and the words Circular Motion ring in your head."
    stop sound
    
    scene controlPanel2 with dissolve

    play sound "audio/Darby/7.mp3"
    Doctor "Alas, that day will never come."
    stop sound
    
    scene black with dissolve

    Player "Body's still slightly numb…Cold cobble…? Is this the afterlife…? What is that light?"

    scene london with dissolve

    play sound "audio/Dason/0.mp3"
    Unknown "Oh my, how the angel has fallen."
    stop sound

    menu:

        "Huh?":
            play sound "audio/Dason/1.mp3"
            Unknown "Gonna sleep there forever? Wouldn't want to catch a cold right? *extends hand out"
            stop sound

        "That voice…am I in heaven?":
            play sound "audio/Dason/1.mp3"
            Unknown "Gonna sleep there forever? Wouldn't want to catch a cold right? *extends hand out"
            stop sound

    play sound "audio/Adam/6.mp3"
    Narrator "You place your hand on his hardened palm. He gently lifts you to your feet, his smile melting away the pain."
    stop sound

    show Barrow 1

    Player "I must really be in heaven now… w-who are you?"

    play sound "audio/Dason/2.mp3"
    Barrow "Isaac Barrow at your service, and you are?"
    stop sound

    Player "[name]"

    play sound "audio/Dason/3.mp3"
    Barrow "What a fitting name, but it doesn't sound from here?"
    stop sound 
    
    menu:

        "Ah, that's because…"
        "I'm from out of town":
            play sound "audio/Dason/4.mp3"
            Barrow "Oh, how lovely, a fittingly cute name."
            stop sound

        "I'm from the future":
            $ future = "true"
            show Barrow 2
            play sound "audio/Dason/5.mp3"
            Barrow "ha ha what a funny fellow you are. You're clearly not from around here with how you're dressed."
            stop sound

    show Barrow 1

    play sound "audio/Dason/6.mp3"
    Barrow "Where were you going in such a rush to endup on the road?"
    stop sound
    
    menu:

        "I was going to umm…"
        "The Church":
            jump Church

        "The Library":
            jump Library
       
        "The Ocean":
            jump Ocean

        "I don't know":
            jump IDK

label Church:
    Narrator "Church path"
    return
label Library:
    Narrator "Library path"
    return
label IDK:
    Narrator "IDK path"
    return
label Ocean:
    play sound "audio/Dason/7.mp3"
    Barrow "The ocean, you say? Why, the ocean is quite a formidable place; trust me, without a solid plan, nothing good will come out of an adventure at the sea."
    stop sound

    play sound "audio/Adam/6.5.mp3"
    Narrator "Barrow looks you up and down before settling his gaze on yours with an amusing, challenging spark in his eyes."
    stop sound

    play sound "audio/Dason/8.mp3"
    Barrow "Well, young lass, do YOU have what it takes to challenge Mother Earth's greatest behemoth? Surely, with such fine, exotic silks containing the most vibrant of colours, you must have a retinue of sailors at your service, no?"
    stop sound

    menu:
        "I, err…"
        "just came from the future, so of course I don’t have anything planned!":
            show Barrow 4
            $ future = "true"
            play sound "audio/Dason/9.mp3"
            Barrow "Ha, Ha, Ha! Do not fret, m’lady, for I, the great, holy, professor Isaac Barrow shall personally arrange accommodations fit for the king Charles II himself, long live his name, for your majestic voyage. You do know, I have quite the experience when it comes to these things."
            stop sound

        "am not in need of such superfluous additions.":
            show Barrow 4
            play sound "audio/Dason/9.mp3"
            Barrow "Ha, Ha, Ha! Do not fret, m’lady, for I, the great, holy, professor Isaac Barrow shall personally arrange accommodations fit for the king Charles II himself, long live his name, for your majestic voyage. You do know, I have quite the experience when it comes to these things."
            stop sound

        "already have travel accommodations planned with a boat at the ready.":
            show Barrow 4
            play sound "audio/Dason/9.mp3"
            Barrow "Ha, Ha, Ha! Do not fret, m’lady, for I, the great, holy, professor Isaac Barrow shall personally arrange accommodations fit for the king Charles II himself, long live his name, for your majestic voyage. You do know, I have quite the experience when it comes to these things."
            stop sound

        "love you.":
            show Barrow 4
            $ persistent.affection += 2
            play sound "audio/Dason/9.mp3"
            Barrow "Ha, Ha, Ha! Do not fret, m’lady, for I, the great, holy, professor Isaac Barrow shall personally arrange accommodations fit for the king Charles II himself, long live his name, for your majestic voyage. You do know, I have quite the experience when it comes to these things."
            stop sound

        "hate you.":
            show Barrow 4
            $ persistent.affection -= 2
            play sound "audio/Dason/9.mp3"
            Barrow "Ha, Ha, Ha! Do not fret, m’lady, for I, the great, holy, professor Isaac Barrow shall personally arrange accommodations fit for the king Charles II himself, long live his name, for your majestic voyage. You do know, I have quite the experience when it comes to these things."
            stop sound

    hide Barrow 4 with dissolve
    scene london2 with dissolve

    play sound "audio/Adam/7.mp3"
    Narrator "Barrow firmly takes your hand in his muscular, manly grip, ignoring your murmurs of objection, and hurries you down the busy street. As you walk, taking in the fresh scent of manure, you notice the road widen and the buildings grow in grandeur and size."
    stop sound

    show Barrow 2

    play sound "audio/Dason/10.mp3"
    Barrow "Mmm, yes, I will have to take you to the smallest of my eight villas in central London, as it does happen to be the closest. Oh well, I suppose it shall suffice."
    stop sound

    menu:

        "That’s amazing":
            $ persistent.affection += 2
           
        "*Press X to doubt*":
            $ persistent.affection -= 2

    scene grass with dissolve

    play sound "audio/Adam/8.mp3"
    Narrator "Barrow continues, firm and steady. As the building fades into grassy green."
    stop sound

    show Barrow 2

    play sound "audio/Dason/11.mp3"
    Barrow "I’m sure you understand. My villa is far secluded, as to avoid the distractions that peasants often bring."
    stop sound

    menu:

        "Hey that is rude.":
            play sound "audio/Dason/624.mp3"
            Barrow "Rude? My dear, you must understand that people like us must separate ourselves from their like, for the good of both us and them. You know, separate but equal."
            stop sound
            $ persistent.affection -= 2

        "Haha of course the present":
            play sound "audio/Dason/12.mp3"
            Barrow "I knew you would understand."
            stop sound
            $ persistent.affection += 2

        "peasants…":
            play sound "audio/Dason/13.mp3"
            Barrow "Ya, like those poor people."
            stop sound

    play sound "audio/Dason/14.mp3"
    Barrow "Ah, we have arrived."
    stop sound

    scene house with dissolve

    play sound "audio/Adam/9.mp3"
    Narrator "Barrow gestures for his servant to get him a boat prepared for a voyage."
    stop sound

    show Barrow 1 at right with move
    show Sailor 1 at left with move

    play sound "audio/Sailor/0.mp3"
    Sailor "Yes sir. The boat will be ready right away sir."

    hide Sailor 1 with dissolve
    show Barrow 1 at center with move

    play sound "audio/Dason/15.mp3"
    Barrow "This should only take them a few minutes. Why don’t we go for a stroll and you can tell me more about where you’re from."
    stop sound

    if future == "true":
        menu:

            "I’m from the future.":
                play sound "audio/Dason/16.mp3"
                Barrow "Why are you being so evasive about your place of origin? You aren’t a savage, are you?"
                stop sound
                play sound "audio/Dason/17.mp3"
                Barrow "If you are, I am a man of god and I can help you in your pursuit of civility."
                stop sound
                
            "It is umm.. complicated.":
                play sound "audio/Dason/18.mp3"
                Barrow "If I recall correctly you came from the future."
                stop sound 
                play sound "audio/Dason/19.mp3"
                Barrow "I have my doubts but I will pry no further."
                stop sound
                $ persistent.affection += 2
    
    elif future == "false":
        menu:

            "I’m from the future.":
                play sound "audio/Dason/16.mp3"
                Barrow "Why are you being so evasive about your place of origin? You aren’t a savage, are you?"
                stop sound
                play sound "audio/Dason/17.mp3"
                Barrow "If you are, I am a man of god and I can help you in your pursuit of civility."
                stop sound

    play sound "audio/Dason/20.mp3"
    Barrow "If what you say is true then you can surely answer a few questions."
    stop sound

    play sound "audio/Dason/21.mp3"
    Barrow "In the future, it is certain that all will be taught of my heroic adventures and my intricate studies. How many languages can I speak fluently?"
    stop sound

    menu:

        "1":
            scene black with dissolve
            play sound "audio/Dason/22.mp3"
            Barrow "What do you take me for, common rabble!? Begone, wench!"
            stop sound
            jump death

        "5":
            show Barrow 4
            play sound "audio/Dason/23.mp3"
            Barrow "Aha, I can see why you might think that; however, your futuristic teachings have failed you. You better hope you can answer the following questions."
            stop sound

        "7":
            show Barrow 4
            play sound "audio/Dason/23.mp3"
            Barrow "Aha, I can see why you might think that; however, your futuristic teachings have failed you. You better hope you can answer the following questions."
            stop sound

        "8":
            play sound "audio/Dason/24.mp3"
            Barrow "Ah, very good, so you are from the future! Pray tell, how many hours a day do you dedicate to your studies about me, there?"
            stop sound
            
        "11":
            show Barrow 4
            play sound "audio/Dason/23.mp3"
            Barrow "Aha, I can see why you might think that; however, your futuristic teachings have failed you. You better hope you can answer the following questions."
            stop sound

    show Barrow 2
    play sound "audio/Dason/25.mp3"
    Barrow "Hmm, which of these languages do I not speak?"
    stop sound

    menu:

        "English":
            scene black with dissolve
            play sound "audio/Dason/22.mp3"
            Barrow "What do you take me for, common rabble!? Begone, wench!"
            stop sound
            jump death

        "Latin":
            scene black with dissolve
            play sound "audio/Dason/22.mp3"
            Barrow "What do you take me for, common rabble!? Begone, wench!"
            stop sound
            jump death

        "French":
            scene black with dissolve
            play sound "audio/Dason/22.mp3"
            Barrow "What do you take me for, common rabble!? Begone, wench!"
            stop sound
            jump death

        "Peasant":
            play sound "audio/Dason/214.mp3"
            Barrow "Excellent. The future has educated you well."
            stop sound

    play sound "audio/Adam/10.mp3"
    Narrator "A swift figure scurries by. Halting in front of Barrow. A book tightly clutched against his chest he mutters out a sentence."
    stop sound

    show Barrow 2 at right with move
    show Newton 1 at left with move
    
    play sound "audio/Newton/0.mp3"
    Unknown "h-have a safe trip professor."
    stop sound

    hide Newton 1 with move
    show Barrow 2 at center with move

    play sound "audio/Adam/11.mp3"
    Narrator "As fast as he arrived, he was gone. Running back towards the mansion"
    stop sound

    menu:

        "Who was that":
            play sound "audio/Dason/26.mp3"
            Barrow "Ah that was my student, Isaac Newton, he is a bright young lad who will surely grow up to do great things."
            stop sound
            play sound "audio/Dason/27.mp3"
            Barrow "Not as great as me of course."
            stop sound

        "Professor?":
            show Barrow 4
            play sound "audio/Dason/28.mp3"
            Barrow "Why does that come as a surprise."
            stop sound
            menu:

                "...":
                    play sound "audio/Dason/29.mp3"
                    Barrow "Did I not introduce myself earlier?"
                    stop sound
                    $ persistent.affection -= 2
                    menu:

                        "...":
                            play sound "audio/Dason/30.mp3"
                            Barrow "The audacity of this witch, to even question my profession."
                            stop sound
                            $ persistent.affection -= 2
                            menu:

                                "I’m sorry, I didn’t mean it that way":
                                    show Barrow 2
                                    play sound "audio/Dason/31.mp3"
                                    Barrow "You are forgiven for your ignorance. Do not cross me again."
                                    stop sound
                                    $ persistent.affection -= 2

                                "witch??":
                                    jump death

                                "Be careful, boy, or I will cast a spell on you.":
                                    jump death

    show Barrow 2 at right with move

    play sound "audio/Adam/12.mp3"
    Narrator "The sailor runs back and stands at attention"
    stop sound
    
    show Sailor 1 at left with move

    play sound "audio/Sailor/1.mp3"
    Sailor "The king sends his finest boat for you sir."
    stop sound

    play sound "audio/Sailor/2.mp3"
    Sailor "Please make your way to the dock sir."
    stop sound

    hide Sailor 1 with move
    hide Barrow 2 with move
    scene dock with dissolve
    play sound "audio/Adam/13.mp3"
    Narrator "The concentrated scent of shit sits heavy in the air as you approach the London dockyard. The smell of the green, murky, polluted water of the river Thames mingles with this scent, producing a unique sensory experience."
    stop sound

    play sound "audio/Adam/14.mp3"
    Narrator "Out before you, a large, well crafted wooden ship stands ready for departure."
    stop sound

    show Barrow 3

    play sound "audio/Adam/15.mp3"
    Narrator "The bright sun illuminates Barrow’s muscular figure as he stands triumphantly out towards the ship."
    stop sound

    play sound "audio/Dason/32.mp3"
    Barrow "Ah, what a wonderful aroma. Reminds me of my youth."
    stop sound

    play sound "audio/Dason/33.mp3"
    Barrow "Let's carry on."
    stop sound

    hide Barrow 3
    scene deck with dissolve

    play sound "audio/Adam/16.mp3"
    Narrator "The two of you board the massive ship. It pillars above the peasant realm. The weight of its magnificence shatters the waves that oppose it."
    stop sound

    Player "Ah how lovely, in the future this river got canceled on twitter."

    show Barrow 1

    Barrow "..."
    play sound "audio/Dason/35.mp3"
    Barrow "... Anyways. "
    stop sound

    play sound "audio/Dason/36.mp3"
    Barrow "Ah, it has been so long since I’ve been on a boat. I remember my studious trip to Paris, when I was just a young man. All my life, I had been told what a glorious, extravagant place Paris was. Oh, how I had been lied to. French people, let me tell you. The city smelled exclusively of baguettes!"
    stop sound

    play sound "audio/Dason/37.mp3"
    Barrow "Oh, ‘culture this,’ ‘architecture this’. It is all blasphemy! Paris is a sick place for sick people who are of inferior culture and lacking in intelligence. The 10 months I spent there are 10 months wasted that I will never get back."
    stop sound

    play sound "audio/Dason/38.mp3"
    Barrow "You know, under proper management, the French people could prosper. Under the rule of King Charles II, and if they quit speaking peasant and started speaking the King’s English, Paris could come to be a tolerable place. But, most of all, one overarching reason I hate Paris trumps them all."
    stop sound

    play sound "audio/Dason/39.mp3"
    Barrow "Oh, as you are from the future you should know the reason."
    stop sound

    play sound "audio/Dason/41.mp3"
    Barrow "Tell me. Why was I disappointed from my trip to Paris?"
    stop sound

    menu:

        "The universities were not to your standards":
            play sound "audio/Dason/42.mp3"
            Barrow "‘Not to my standards’ is a funny way to phrase it. My dear, the universities there were not to anybody’s standards! In Paris, buildings sagged, libraries collected dust, and ‘scholars’ drooled. I would hardly wish to subject London’s poorest beggars to such barbarousness."
            stop sound

        "There were too many peasants":
            show Barrow 4
            play sound "audio/Dason/43.mp3"
            Barrow "Sigh. Incorrect. The future is as disappointing as my trip to france. The universities there were not to anybody’s standards! In Paris, buildings sagged, libraries collected dust, and ‘scholars’ drooled. I would hardly wish to subject London’s poorest beggars to such barbarousness. My disappointment is immeasurable and my day is ruined."
            stop sound

        "The food was not to your taste":
            show Barrow 4
            play sound "audio/Dason/43.mp3"
            Barrow "Sigh. Incorrect. The future is as disappointing as my trip to france. The universities there were not to anybody’s standards! In Paris, buildings sagged, libraries collected dust, and ‘scholars’ drooled. I would hardly wish to subject London’s poorest beggars to such barbarousness. My disappointment is immeasurable and my day is ruined."
            stop sound

        "The air quality was too poor":
            show Barrow 4
            play sound "audio/Dason/43.mp3"
            Barrow "Sigh. Incorrect. The future is as disappointing as my trip to france. The universities there were not to anybody’s standards! In Paris, buildings sagged, libraries collected dust, and ‘scholars’ drooled. I would hardly wish to subject London’s poorest beggars to such barbarousness. My disappointment is immeasurable and my day is ruined."
            stop sound

    show Barrow 1
    play sound "audio/Dason/44.mp3"
    Barrow "You must know of my trip to Italy. It was the talk of the town. Now who was I there to meet?"
    stop sound

    menu:

        "Giorno Giovanna and Paolo Bucciarati":
            show Barrow 4
            play sound "audio/Dason/45.mp3"
            Barrow "I have never heard of those mathematicians, let alone spoken with them. They really teach you nothing in the future, don’t they?"
            stop sound

        "Adam Zheng and Noah Borek":
            show Barrow 4
            play sound "audio/Dason/45.mp3"
            Barrow "I have never heard of those mathematicians, let alone spoken with them. They really teach you nothing in the future, don’t they?"
            stop sound

        "Vincenzo Viviani and Carlo Renaldini":
            play sound "audio/Dason/46.mp3"
            Barrow "Yes, that is right. Renaldini was fabulous to collaborate with. In fact, his paper on algebra was fascinating.  Viviani was a most dedicated disciple and mathematician; Galileo taught him well."
            stop sound

        "Giovanni Cassini and Galileo Galilei":
            show Barrow 4
            play sound "audio/Dason/45.mp3"
            Barrow "I have never heard of those mathematicians, let alone spoken with them. They really teach you nothing in the future, don’t they?"
            stop sound

    show Barrow 2
    play sound "audio/Dason/47.mp3"
    Barrow "Ah, Florence was a most accommodating, lively place. You should have seen the great Medici Library. It’s grand architecture and vast collection of coinage are simply-"
    stop sound

    show Barrow 1 at right with move
    show Sailor 1 at left with move
    
    play sound "audio/Sailor/3.mp3"
    Sailor "Barrow, sir! There are pirates approaching from the East."
    stop sound

    play sound "audio/Adam/17.mp3"
    Narrator "Barrow’s face briefly flushed in annoyance at the sailor’s interruption, before he continued on."
    stop sound

    show Barrow 1 at center with move
    hide Sailor 1 with move

    play sound "audio/Dason/48.mp3"
    Barrow "-simply amazing! The knowledge I gained from that library helped me greatly in financing my trip. Moreover, All the Italian scholars I met there were very pleasant and could hold their own in any intellectual conversations, frequent as they we- "
    stop sound

    play sound "audio/Adam/18.mp3"
    Narrator "For some time, a large, looming pirate ship had been approaching your ship. Now, they were within shouting range."
    stop sound

    show Barrow 1 at left with move
    show Pirate1 1 at right with move

    play sound "audio/Pirates/0.mp3"
    Pirate1 "Where do you think you're going in this rickety old tree? Enter our waters you must pay a fee."
    stop sound

    play sound "audio/Adam/19.mp3"
    Narrator "Barrow, again, completely ignored this intrusion."
    stop sound

    play sound "audio/Dason/49.mp3"
    Barrow "-ere. I do believe I actually learned quite a bit from the mathematicians there. Not more than I taught them, though, of cou-"
    stop sound

    show Pirate1 2 at right with move

    play sound "audio/Pirates/1.mp3"
    Pirate2 "Pay the fee and leave with your head. Waste our time and you’ll end up dead."

    play sound "audio/Adam/20.mp3"
    Narrator "Amused, Barrow begins to converse with the pirates."
    stop sound

    play sound "audio/Dason/50.mp3"
    Barrow "You sure talk big, why don’t you come over here and try me."
    stop sound
    
    show Pirate1 3 at right with move

    play sound "audio/Pirates/2.mp3"
    Pirate2 "Bring it, little man."
    stop sound

    show Barrow 6 at left with dissolve

    play sound "audio/Dason/51.mp3"
    Barrow "If it’s a fight you want. Then it will be a fight you get!"
    stop sound

    play sound "audio/Elias/0.mp3"
    Unknown "Back off."
    stop sound

    play sound "audio/Adam/21.mp3"
    Narrator "A shadow emerges from behind the pirates. The sleek annular glasses shimmer in the light, his curled hair contrasting the pristine condition of his turtleneck. Jeans slightly faded with a ferret in place of a scarf."
    stop sound

    hide pirate 3 with dissolve 
    hide Barrow 6 with dissolve

    scene doorway with dissolve

    play sound "audio/Elias/1.mp3"
    Unknown "This man is not to be messed with"
    stop sound

    play sound "audio/Elias/2.mp3"
    Unknown "Let me handle him"
    stop sound

    scene deck with dissolve
    show Barrow 6 

    play sound "audio/Dason/53.mp3"
    Barrow "Ah, why if it isn’t the almighty, king of pirates, captain Brockmann."
    stop sound

    scene jojo with dissolve
    play sound "audio/Dason/54.mp3"
    Barrow "Oh? You're approaching me? Instead of running away, you're coming right to me?"
    stop sound

    play sound "audio/Elias/3.mp3"
    Captain "I can't beat the shit out of you without getting closer."
    stop sound

    play sound "audio/Dason/100.mp3"
    Barrow "Ho ho! Then come as close as you like!"
    stop sound

    play sound "audio/Adam/22.mp3"
    Narrator "As the distance between Captain Brockmann and Barrow closes, they each begin to outstretch their arms. Then, all of a sudden Barrow wraps Brockmann in his tight, muscular, loving embrace."
    stop sound

    scene deck with dissolve
    show Barrow 1 at left with dissolve
    show Captain 1 at right with dissolve

    play sound "audio/Elias/4.mp3"
    Captain "Sorry about my men, they always want to throw hands. It seems they still have much to learn."
    stop sound

    play sound "audio/Dason/55.mp3"
    Barrow "No worries, I didn’t want to kill them all anyways. It would have been too much work explaining it all to the king again."
    stop sound

    play sound "audio/Adam/23.mp3"
    Narrator "Captain Brockmann faces towards you"
    stop sound

    play sound "audio/Elias/5.mp3"
    Captain "If I may talk to you in private."
    stop sound

    scene cabin with dissolve
    hide Barrow 1 with dissolve
    hide Captain 1 with dissolve

    play sound "audio/Adam/24.mp3"
    Narrator "Captain Brockmann leads you into the ship's cabin. Grabbing a nearby stool he sits and faces towards you."
    stop sound

    show Captain 2 with dissolve

    play sound "audio/Elias/6.mp3"
    Captain "Dr. Darby’s new assistant I presume."
    stop sound

    menu:

        "Yes":
            play sound "audio/Elias/7.mp3"
            Captain "Thought so."
            stop sound

        "How did you know":
            play sound "audio/Elias/8.mp3"
            Captain "Why, isn't it obvious? Based on your massive brain bulging out of your forehead, and your intellectual gaze I could determine - just kidding, it was your modern clothing. Tell me, why haven't you changed yet? You stick out like a sore thumb."
            stop sound

    Player "You must be his former assistant that helped him build the machine."

    play sound "audio/Elias/9.mp3"
    Captain "Yes, that is me. I was less of an assistant and more of a partner."
    stop sound

    play sound "audio/Elias/10.mp3"
    Captain "But he feared me; he feared that I would take his fame."
    stop sound

    Player "This is perfect, you can help me get back. The two of us should be able to build a similar time machine."

    play sound "audio/Elias/11.mp3"
    Captain "It’s impossible!"
    stop sound

    play sound "audio/Elias/12.mp3"
    Captain "I’ve tried… there is just one part that he kept secret from me."
    stop sound

    play sound "audio/Elias/13.mp3"
    Captain "The power source of this law defying contraption was a perpetual motion machine. It was the crowing invention that brought him fame."
    stop sound

    play sound "audio/Elias/14.mp3"
    Captain "However even the doctor didn’t seem to know how it worked. Almost as if he stole it from somebody else."
    stop sound

    play sound "audio/Elias/15.mp3"
    Captain "Anyways I see you are trying to gain Barrow’s favor. No one can stand being around that man for long, so I'd assume there is something in it for you."
    stop sound

    play sound "audio/Elias/16.mp3"
    Captain "Let me tell you the secret to his heart, and to his brilliant mind."
    stop sound

    hide Captain 2 with dissolve
    play sound "audio/Adam/25.mp3"
    Narrator "The captain pries open a box, taking out a few bags and handing it to you."
    stop sound
    show Captain 2 with dissolve

    play sound "audio/Elias/17.mp3"
    Captain "Opium, fresh from Turkey."
    stop sound

    menu:

        "Thanks":
            play sound "audio/Elias/18.mp3"
            Captain "That man is absolutely addicted to this stuff. Just a few puffs and he will tell you anything."
            stop sound

        "Am I supposed to smoke this?":
            play sound "audio/Elias/18.mp3"
            Captain "That man is absolutely addicted to this stuff. Just a few puffs and he will tell you anything."
            stop sound

    scene black with dissolve

    play sound "audio/Adam/26.mp3"
    Narrator "The adventurous mood was broken and after a brief chat the ships parted ways."
    stop sound

    play sound "audio/Adam/27.mp3"
    Narrator "Heading back to the dock, the return was filled with Barrow's rambling."
    stop sound

    scene dock with dissolve
    show Barrow 3 with dissolve

    play sound "audio/Dason/56.mp3"
    Barrow "Wasn’t that a grand time."
    stop sound

    menu:

        "Sure was":
            play sound "audio/Dason/57.mp3"
            Barrow "Well i’ll be off now, you know where to find me if  you want a good time."
            stop sound

            play sound "audio/Adam/28.mp3"
            Narrator "With a final wink he bids you farewell."
            stop sound
            return

        "You know what would be a grander time?(opium)":
            play sound "audio/Dason/58.mp3"
            Barrow "A grander time than spending time with me?? Impossible."
            stop sound

            play sound "audio/Adam/29.mp3"
            Narrator "Before he can throw you into the river. You pull out a bag of opium."
            stop sound

            play sound "audio/Adam/30.mp3"
            Narrator "Barrow’s eyes light up with pure joy as he whips a long pipe out of his pocket."
            stop sound

            play sound "audio/Dason/59.mp3"
            Barrow "This sure hits the spot. Here I have this."
            stop sound

            play sound "audio/Adam/31.mp3"
            Narrator "He hands you a piece of paper."
            stop sound

            scene math with dissolve
            Player "Wtf is this??"

            $ persistent.affection += 60

            return

label death:
    scene black with dissolve
    play sound "audio/Adam/32.mp3"
    Narrator "Barrow in a fit of rage picks you up and throws you in the River Thames."
    stop sound
    play sound "audio/Water.mp3"
    play sound "audio/Adam/33.mp3"
    Narrator "You drowned, get good."
    stop sound
    return
