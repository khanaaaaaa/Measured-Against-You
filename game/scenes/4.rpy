label chapter14:
    scene exam_hall with fade

    thought "The exam hall smells like pencil shavings and cold air."
    thought "Every seat is filled."
    thought "The kind of silence that isn't really silence—"
    thought "—just everyone holding their breath at the same time."
    thought "I've sat in this room a hundred times."
    thought "I know this room."
    thought "It's fine. I studied for this."

    thought "The papers come down."
    thought "I flip mine over."
    thought "First question. I know it."
    thought "Second question. I know it."
    thought "Third question."
    thought "I—"

    scene black with fade

    thought "What was the formula."
    thought "I studied this. I studied this a hundred times."
    thought "It starts with— it starts with—"
    thought "My hand is shaking."
    thought "I press it flat against the desk."
    thought "It keeps shaking."
    thought "The room tilts."
    thought "The fluorescent lights buzz too loud."
    thought "Everything is too much."
    thought "Stop it."
    thought "Stop it. You know this."
    thought "I don't know this."
    thought "It's gone."
    thought "Everything I studied— just gone."
    thought "Like someone reached in and cleared the shelf."
    thought "Someone says my name."
    thought "Then louder."
    thought "Then I'm in the corridor."
    thought "Sitting on the floor with my back against the wall."
    thought "A teacher crouching beside me."
    thought "I don't remember walking out."

    show inha talk at center_char
    inha "I'm fine."
    inha "I just need a minute."
    hide inha

    thought "The teacher says something about water."
    thought "I nod."
    thought "I don't hear it."
    thought "I left in the middle of the exam."
    thought "I have never left in the middle of anything."

    jump chapter15

label chapter15:
    scene room with fade

    thought "Three days."
    thought "I don't go to the academy."
    thought "I tell my mom I have a cold."
    thought "My sketchbook sits on the desk."
    thought "I don't open it."
    thought "On the second day I pick up a pencil."
    thought "My hand shakes."
    thought "I put it down."
    thought "I've been drawing since I was five years old."
    thought "It has never not come."
    thought "Not when I was sick."
    thought "Not on the worst days."
    thought "It always came."
    thought "And now—"
    thought "Nothing."

    show minjiquiet at center_char
    minji "In-Ha."
    minji "Please just tell me you're alive."
    minji "I will come to your house."
    minji "I will stand outside and yell."
    minji "I have done it before."
    hide minjiquiet

    thought "I type: I'm alive."
    thought "I don't send it."
    thought "On the fourth day someone knocks."
    thought "Not Minji's knock."
    thought "Minji knocks like she's trying to break the door."

    show inha talk at center_char
    inha "Who is it?"
    hide inha

    yejun "It's me."

    show inha talk at center_char
    inha "How do you know where I live."
    hide inha

    yejun "Minji."
    yejun "She was worried."

    show inha talk at center_char
    inha "I'm fine."
    hide inha

    yejun "I know."
    yejun "I brought food."
    yejun "You don't have to open the door."
    yejun "I'll leave it here."

    "Footsteps."
    "Then silence."

    menu:
        "Open the door.":
            show inha talk at center_char
            inha "..."
            hide inha
            thought "I open the door."
            thought "He's at the end of the hallway."
            thought "He turns around."
            show yejuntalk at center_char
            yejun "Oh."
            hide yejuntalk
            show yejunquiet at center_char
            inha "You can come in."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "You don't have to—"
            hide yejuntalk
            show yejunquiet at center_char
            inha "I know."
            hide yejunquiet
            thought "He comes in."
            thought "He doesn't say anything about the room."
            thought "The sketchbook on the desk."
            thought "The pencil lying beside it untouched."
            thought "He just sits down on the floor and opens the bag."
            show yejuntalk at center_char
            yejun "Ramyeon. Banana milk."
            yejun "And a tangerine, you mentioned you liked them."
            hide yejuntalk
            show yejunquiet at center_char
            thought "I mentioned that once."
            thought "Months ago on the rooftop."
            thought "He remembered."
            inha "..."
            inha "Sit down properly. Not on the floor."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "The floor is fine."
            hide yejuntalk
            show yejunquiet at center_char
            inha "It's cold."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I've slept on a rooftop in December."
            yejun "I'll survive."
            hide yejuntalk
            thought "We eat ramyeon on the floor."
            thought "He doesn't ask what happened."
            thought "He doesn't ask if I'm okay."
            thought "He just— stays."
            thought "And somehow that's the only thing I needed."
            jump chapter15b

        "Don't open the door.":
            thought "I don't open the door."
            thought "I sit on the floor with my back against it."
            thought "I hear him set something down outside."
            thought "Footsteps leaving."
            thought "Silence."
            thought "I open the door."
            thought "Convenience store bag."
            thought "Ramyeon. Banana milk. A tangerine."
            thought "I mentioned once that I liked tangerines."
            thought "Months ago on the rooftop."
            thought "He remembered."
            thought "I sit back down on the floor."
            thought "I eat the tangerine."
            thought "It's the first thing I've eaten properly in two days."
            show minjiquiet at center_char
            minji "In-Ha I swear to god."
            hide minjiquiet
            thought "I pick up my phone."
            thought "I text Minji back."
            show inha talk at center_char
            inha "I'm alive. I'm okay. I'll come back tomorrow."
            hide inha
            show minjiquiet at center_char
            minji "You better."
            minji "Also Ye-Jun was worried too."
            minji "Just so you know."
            hide minjiquiet
            thought "I put my phone face down."
            thought "I look at the sketchbook on the desk."
            thought "I don't open it."
            thought "But I move it closer."
            thought "Just a little."
            jump chapter16

label chapter15b:
    scene room with fade

    show yejuntalk at center_char
    yejun "I couldn't play piano for two months once."
    hide yejuntalk
    show yejunquiet at center_char
    inha "What happened?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I just couldn't."
    yejun "I'd sit down and my hands wouldn't move."
    yejun "Or they'd move and everything came out wrong."
    yejun "Like I'd forgotten what music was supposed to feel like."
    hide yejuntalk
    show yejunquiet at center_char
    inha "Did it come back?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "Eventually."
    hide yejuntalk
    show yejunquiet at center_char
    inha "How?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I stopped trying to force it."
    yejun "I just sat at the piano every day."
    yejun "Didn't play."
    yejun "Just sat there."
    yejun "Until one day my hands moved on their own."
    hide yejuntalk

    menu:
        "\"That sounds impossible.\"":
            show yejunquiet at center_char
            inha "That sounds impossible."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "It felt impossible."
            yejun "And then it wasn't."
            hide yejuntalk

        "\"I don't know if I can just wait.\"":
            show yejunquiet at center_char
            inha "I don't know if I can just sit and wait."
            inha "That's not how I work."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I know."
            yejun "You're the kind of person who pushes through everything."
            hide yejuntalk
            show yejunquiet at center_char
            inha "Is that a bad thing?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Not bad."
            yejun "Just— sometimes the thing you're pushing against is yourself."
            hide yejuntalk
            show yejunquiet at center_char
            inha "..."
            hide yejunquiet

    show yejuntalk at center_char
    yejun "You don't have to wait alone either."
    hide yejuntalk
    show yejunquiet at center_char
    inha "..."
    inha "You're going to make that weird."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I'm not making it weird."
    hide yejuntalk
    show yejunquiet at center_char
    inha "You said it like a drama line."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I said it like a normal sentence."
    hide yejuntalk
    show yejunquiet at center_char
    inha "It was very soft."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "In-Ha."
    hide yejuntalk
    show yejunquiet at center_char
    inha "What."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "Just eat your ramyeon."
    hide yejuntalk

    thought "I eat my ramyeon."
    thought "The room is quiet."
    thought "Outside the window the city hums."
    thought "Snow starting again."
    thought "He stays until it gets late."
    thought "Just stands up, says goodnight, and goes."
    thought "Like it was nothing."
    thought "Maybe it is."
    thought "With him."

    jump chapter16

label chapter16:
    scene rooftop with fade

    thought "I go back to the academy the following week."
    thought "Everyone pretends not to notice I was gone."
    thought "Minji hugs me for thirty seconds without saying a word."
    thought "That's how I know she was really scared."

    show minjismiletalk at center_char
    minji "Don't do that again."
    hide minjismiletalk
    show minjismile at center_char
    inha "I won't."
    hide minjismile
    show minjismiletalk at center_char
    minji "I mean it, In-Ha."
    hide minjismiletalk
    show minjismile at center_char
    inha "I know."
    inha "I'm sorry."
    hide minjismile
    show minjismiletalk at center_char
    minji "Don't apologize to me."
    minji "Just don't disappear."
    hide minjismiletalk

    thought "He's on the roof when I get there after class."
    thought "He looks up."
    thought "Doesn't say anything."
    thought "I sit down."
    thought "We stay like that for a while."

    show yejuntalk at center_char
    yejun "I had a panic attack last year."
    yejun "In the middle of a presentation."
    yejun "Forty people in the room."
    yejun "I just stopped talking."
    yejun "Stood there for two minutes."
    yejun "Then walked out."
    hide yejuntalk

    menu:
        "\"What did you do after?\"":
            show yejunquiet at center_char
            inha "What did you do after?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Sat in a bathroom stall for an hour."
            yejun "Then went back and finished the presentation."
            hide yejuntalk
            show yejunquiet at center_char
            inha "You went back?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I didn't know what else to do."
            hide yejuntalk
            show yejunquiet at center_char
            inha "Nobody noticed?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Nobody asked."
            yejun "That was the worst part."
            hide yejuntalk

        "\"Why are you telling me this?\"":
            show yejunquiet at center_char
            inha "Why are you telling me this?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Because you looked like you needed to hear it."
            yejun "That it happens."
            yejun "That it doesn't mean you're broken."
            hide yejuntalk
            show yejunquiet at center_char
            inha "..."
            inha "Does it feel like that? When it happens."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Yeah. It does."
            yejun "But you're not."
            hide yejuntalk

    show yejuntalk at center_char
    yejun "It happens when I feel like I'm performing."
    yejun "Like I'm playing a version of myself that doesn't exist."
    yejun "And eventually the gap gets too wide."
    yejun "And I fall through it."
    hide yejuntalk
    show yejunquiet at center_char

    thought "The gap gets too wide and I fall through it."
    thought "I know that feeling."
    thought "I've known it my whole life."
    thought "I just never had words for it."

    inha "Does it get better?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I think you just get better at catching yourself before you fall."
    hide yejuntalk

    menu:
        "\"That's not very reassuring.\"":
            show yejunquiet at center_char
            inha "That's not very reassuring."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "No. But it's true."
            hide yejuntalk
            show yejunquiet at center_char
            inha "..."
            inha "Okay. I'll take true over reassuring."
            hide yejunquiet

        "\"Is that what you do? Catch yourself?\"":
            show yejunquiet at center_char
            inha "Is that what you do? Catch yourself?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I try."
            yejun "I don't always manage it."
            hide yejuntalk
            show yejunquiet at center_char
            inha "What helps when you don't?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Coming up here."
            yejun "Sitting somewhere quiet."
            yejun "Sometimes talking to someone."
            hide yejuntalk
            show yejunquiet at center_char
            inha "Someone."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Don't make it weird."
            hide yejuntalk
            show yejunquiet at center_char
            inha "..."
            inha "Maybe."
            hide yejunquiet

    jump chapter17

label chapter17:
    scene academy_night with fade

    thought "He plays me his composition."
    thought "On the small keyboard in the corner of the studio."
    thought "Just sits down and starts playing."
    thought "It starts quietly."
    thought "Then it opens."
    thought "Something warm underneath all the cold."
    thought "The part he said was me—"
    thought "I hear it."
    thought "Almost resolves."
    thought "Pulls back."
    thought "Almost."
    thought "Pulls back."
    thought "And then—"
    thought "It lands."
    thought "Softly."
    thought "He stops."
    thought "Looks at me."

    menu:
        "\"It's beautiful.\"":
            show yejunquiet at center_char
            inha "It's beautiful."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "It's not finished."
            hide yejuntalk
            show yejunquiet at center_char
            inha "I know. It's still beautiful."
            yejun "..."
            hide yejunquiet
            thought "He looks back at the keys."
            thought "Like he doesn't know what to do with that."

        "\"The part that was me— it resolved.\"":
            show yejunquiet at center_char
            inha "The part that was me."
            inha "It resolved this time."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Yeah."
            hide yejuntalk
            show yejunquiet at center_char
            inha "What changed?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I figured out where it wanted to go."
            hide yejuntalk
            thought "I don't ask what that means."
            thought "I think I already know."

        "Say nothing.":
            thought "I don't say anything."
            thought "I just sit with it."
            thought "He doesn't push for a response."
            thought "We just sit in the silence the music left behind."

    show yejuntalk at center_char
    yejun "I submitted it."
    yejun "To a composition program in Seoul."
    yejun "Last week."
    yejun "Without telling my parents."
    hide yejuntalk
    show yejunquiet at center_char
    inha "Are you serious."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "Yeah."
    hide yejuntalk
    show yejunquiet at center_char
    inha "What are you going to do if you get in?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I don't know yet."
    yejun "I just needed to know if I could do something for myself."
    yejun "Just once. Without asking permission first."
    hide yejuntalk

    menu:
        "\"Your parents are going to find out.\"":
            show yejunquiet at center_char
            inha "Your parents are going to find out."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I know."
            yejun "But at least I'll have done it."
            yejun "At least there'll be one thing that was just mine."
            hide yejuntalk

        "\"I think that's brave.\"":
            show yejunquiet at center_char
            inha "I think that's brave."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Or stupid."
            hide yejuntalk
            show yejunquiet at center_char
            inha "Sometimes those are the same thing."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Yeah. Sometimes they are."
            hide yejuntalk

    thought "We walk out of the building together."
    thought "At the corner where we split off he stops."

    show yejuntalk at center_char
    yejun "In-Ha."
    hide yejuntalk
    show yejunquiet at center_char
    inha "Mm?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "You'll draw again."
    yejun "When you're ready it'll come back."
    hide yejuntalk

    menu:
        "\"How do you know?\"":
            show yejunquiet at center_char
            inha "How do you know?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Because it's part of you."
            yejun "You can't lose something that's part of you."
            yejun "You can only misplace it for a while."
            hide yejuntalk
            show yejunquiet at center_char
            inha "..."
            hide yejunquiet
            thought "I nod."
            thought "I walk home."
            thought "Somewhere between the corner and my front door I start crying."
            thought "Not the bad kind."
            thought "Just the kind that comes when something tight finally loosens."
            jump ending_choice

        "\"I hope you're right.\"":
            show yejunquiet at center_char
            inha "I hope you're right."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I usually am."
            hide yejuntalk
            show yejunquiet at center_char
            inha "That is such an arrogant thing to say."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Goodnight, In-Ha."
            hide yejuntalk
            thought "I watch him walk away."
            thought "I am in so much trouble."
            jump ending_choice

label ending_choice:
    scene room with fade

    "That night."
    "I sit at my desk."
    "Sketchbook in front of me."
    "Pencil in my hand."
    "I don't force it."
    "I just sit."
    "Like he said."

    "Ten minutes."
    "Twenty."
    "My hand moves."
    "Just a line."
    "Then another."
    "Then—"

    "Oh."
    "There it is."

    "I draw until two in the morning."
    "His hands on the keyboard."
    "The rooftop."
    "The crosswalk in the snow."
    "Everything I've been holding."

    "I open to a fresh page."
    "I write a title."
    "Then I cross it out."
    "Then I write it again."

    "Things I Could Never Say."

    menu:
        "Keep the title. This is what the exhibition will be.":
            jump ending_a

        "Cross it out. Some things don't need names.":
            jump ending_b

        "Close the sketchbook. Not yet.":
            jump ending_c

label ending_a:
    scene room with fade

    show inha talk at center_char
    inha "..."
    inha "Okay."
    inha "Okay. I can do this."
    hide inha

    "I pick up the pencil."
    "I keep going."
    "I draw until the pencil goes dull."
    "Then I sharpen it."
    "Then I keep going."

    thought "I'm going to show them."
    thought "All of it."
    thought "Every ugly honest thing."
    thought "For the first time in a long time—"
    thought "I'm not measuring it against anything."
    thought "It's just mine."
    thought "And that's enough."

    scene black with fade
    "— Route A unlocked —"
    jump ending_a_final

label ending_b:
    scene room with fade

    "I cross it out."
    "The page stays blank except for the scratch of graphite."
    "Some things don't need titles."
    "Some things just need to exist."

    "I start drawing."
    "No plan. No title. No goal."
    "Just the pencil moving."

    show inha talk at center_char
    inha "..."
    hide inha

    "I draw his face."
    "I leave the eyes for last."
    "When I get there I stop."

    thought "I don't know his eyes well enough yet."
    thought "I'll finish it when I do."

    scene black with fade
    "— Route B unlocked —"
    jump ending_b_final

label ending_c:
    scene room with fade

    "I close the sketchbook."
    "Not yet."
    "That's okay."
    "Not yet is not never."

    show inha talk at center_char
    inha "..."
    inha "Tomorrow."
    hide inha

    "I put the pencil on the desk."
    "I turn off the light."
    "In the morning—"
    "I open the sketchbook."
    "I draw one line."
    "Just one."
    "That's enough for today."

    show minjismiletalk at center_char
    minji "You're back."
    hide minjismiletalk
    show inha talk at center_char
    inha "I'm back."
    hide inha
    show minjismiletalk at center_char
    minji "How are you actually."
    hide minjismiletalk
    show inha talk at center_char
    inha "Getting there."
    hide inha
    show minjismiletalk at center_char
    minji "That's the most honest you've been in months."
    hide minjismiletalk
    show inha talk at center_char
    inha "Don't push it."
    hide inha
    show minjismiletalk at center_char
    minji "Pushed. Absolutely pushed."
    hide minjismiletalk

    scene black with fade
    "— Route C unlocked —"
    jump ending_c_final
