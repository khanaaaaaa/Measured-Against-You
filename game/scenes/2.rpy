label chapter1:
    scene crosswalk with fade

    thought "December."
    thought "Cold enough that my breath fogs the moment I step outside."
    thought "The academy district is all fluorescent light and hurrying people."
    thought "My shoelace comes undone at the crosswalk."
    thought "I crouch down to tie it."
    thought "Stand back up."
    thought "And—"
    thought "..."
    thought "There is a person standing on the other side of the road."
    thought "Tall. Black coat."
    thought "Snow just starting to fall around him."
    thought "He looks up from his phone."
    thought "Directly at me."
    thought "Noh Ye-Jun."
    thought "It's actually him."
    thought "The light is red."
    thought "Neither of us moves."

    show yejuntalk at center_char
    yejun "...You still look the same."
    hide yejuntalk

    menu:
        "\"But you don't.\"":
            show yejunquiet at center_char
            inha "You don't."
            yejun "..."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "No. I don't."
            hide yejuntalk

        "Say nothing.":
            show yejunquiet at center_char
            thought "I don't know what to say."
            thought "So I say nothing."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "It's been a while."
            hide yejuntalk

    thought "The light turns green."
    thought "We cross in opposite directions."
    thought "I don't look back."
    thought "..."
    thought "I looked back."
    thought "He was already gone."

    jump chapter2

label chapter2:
    scene classroom with fade

    thought "Three days later."
    thought "He transferred into my academy."
    thought "Of course he does."

    show minjismiletalk at center_char
    minji "Did you hear? The transfer student."
    minji "Canada, Ivy League prep... Perfect grades."
    minji "And In-Ha— he is so pretty."
    hide minjismiletalk
    show minjiquiet at center_char
    inha "I know who he is."
    hide minjiquiet
    show minjismiletalk at center_char
    minji "...You do?"
    hide minjismiletalk

    menu:
        "\"We grew up next door to each other.\"":
            show minjiquiet at center_char
            inha "We grew up next door to each other."
            hide minjiquiet
            show minjismiletalk at center_char
            minji "WHAT. And you never told me?!"
            hide minjismiletalk
            show minjiquiet at center_char
            inha "It didn't come up."
            hide minjiquiet

        "\"It doesn't matter.\"":
            show minjiquiet at center_char
            inha "It doesn't matter. I just know him."
            hide minjiquiet
            show minjismiletalk at center_char
            minji "That is so unsatisfying."
            hide minjismiletalk

    thought "He walks in."
    thought "The classroom shifts around him."
    thought "He doesn't perform. Doesn't look around."
    thought "Just sits down and opens his notebook."
    thought "He was always like that."
    thought "Effortless."
    thought "I used to find it annoying."
    thought "I still do."
    thought "I open my sketchbook."
    thought "Draw a line."
    thought "Cross it out."

    jump chapter3

label chapter3:
    scene academy_night with fade

    thought "Late."
    thought "Everyone has gone home."
    thought "I forgot my sketchbook in the studio."
    thought "I push open the door."
    thought "Lights still on."
    thought "Ye-Jun is sitting at the back table."
    thought "My sketchbook open in front of him."

    show yejunquiet at center_char
    inha "Hey—!"
    hide yejunquiet

    show yejuntalk at center_char
    yejun "Sorry."
    yejun "I found it by the door."
    yejun "I opened it to check for a name."
    hide yejuntalk
    show yejunquiet at center_char

    thought "He closes it carefully and slides it toward me."
    thought "His expression has changed."
    thought "Something quiet and heavy behind his eyes."
    thought "How much did he see."

    menu:
        "\"It's fine. They're just sketches.\"":
            inha "It's fine. They're just sketches."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "They were good."
            hide yejuntalk
            show yejunquiet at center_char
            inha "Don't."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I mean it."
            hide yejuntalk
            show yejunquiet at center_char
            inha "I said don't."
            hide yejunquiet

        "\"You shouldn't have opened it.\"":
            inha "You shouldn't have opened it."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "You're right. I'm sorry."
            yejun "They were good though."
            hide yejuntalk
            show yejunquiet at center_char
            inha "That's not the point."
            hide yejunquiet

    thought "I grab the sketchbook and leave."
    thought "I don't look back."
    thought "Pages titled 'Not Enough.'"
    thought "'Second Place.'"
    thought "'If I disappeared, would anyone notice?'"
    thought "He saw all of it."
    thought "And he said they were good."
    thought "I don't know what to do with that."

    jump chapter4

label chapter4:
    scene classroom with fade

    thought "A week passes. We don't speak."
    thought "But I notice things."
    thought "He never eats with anyone."
    thought "He stares at his phone but never types."
    thought "He answers teachers correctly and then goes quiet again immediately."
    thought "Tired."
    thought "Not exam-tired."
    thought "The kind of tired that comes from performing the same role for too long."

    show minjismiletalk at center_char
    minji "In-Ha. You've been staring at him."
    hide minjismiletalk
    show minjiquiet at center_char

    menu:
        "\"I'm thinking about the exam.\"":
            inha "I'm thinking about the exam."
            hide minjiquiet
            show minjismiletalk at center_char
            minji "He is not the exam."
            hide minjismiletalk

        "\"Does he always look that tired?\"":
            inha "Does he always look that tired?"
            hide minjiquiet
            show minjismiletalk at center_char
            minji "Most people just think he looks mysterious."
            hide minjismiletalk
            show minjiquiet at center_char
            inha "Most people aren't looking closely enough."
            hide minjiquiet
            show minjismiletalk at center_char
            minji "...I need you to think about what you just said."
            hide minjismiletalk

    show minjiquiet at center_char
    inha "Drop it."
    hide minjiquiet
    show minjismiletalk at center_char
    minji "Dropped. Gone. Never existed."
    hide minjismiletalk

    thought "She will bring it up again within the hour."

    jump chapter5

label chapter5:
    scene rooftop with fade

    thought "I find him on the rooftop."
    thought "By accident."
    thought "I came up here to be alone."
    thought "He's lying on the ground, jacket under his head, eyes closed."
    thought "Is he sleeping.. on concrete... in December."

    show yejunquiet at center_char
    inha "Hey."
    thought "Nothing."
    inha "Yah. Noh Ye-Jun."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I heard you the first time."
    hide yejuntalk
    show yejunquiet at center_char
    inha "Then why didn't you answer?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I was deciding if I wanted to."
    hide yejuntalk
    show yejunquiet at center_char
    thought "He opens one eye."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "You can sit down. I don't own the roof."
    hide yejuntalk
    show yejunquiet at center_char

    menu:
        "Sit down nearby.":
            thought "I sit down."
            thought "Closer than I planned."

        "Sit down far away.":
            thought "I sit on the opposite end."
            thought "He doesn't say anything."

    thought "We don't talk for a while."
    thought "The city hums below."
    thought "It's cold."
    thought "But somehow—"
    thought "—it's the most peaceful I've felt in weeks."

    hide yejunquiet
    show yejuntalk at center_char
    yejun "You come up here often?"
    hide yejuntalk
    show yejunquiet at center_char

    menu:
        "\"When it gets too loud downstairs.\"":
            inha "When it gets too loud downstairs."
            inha "My own head, mostly."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Yeah. I know that kind of loud."
            hide yejuntalk
            show yejunquiet at center_char

        "\"This is my first time.\"":
            inha "This is my first time actually."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Good instinct."
            hide yejuntalk
            show yejunquiet at center_char

    jump chapter6

label chapter6:
    scene rooftop with fade

    thought "It becomes a habit."
    thought "Neither of us planned it."
    thought "Every few days we end up on the roof."
    thought "Sometimes we talk. Sometimes we don't."
    thought "Both are fine."

    show yejuntalk at center_char
    yejun "You never told anyone about the sketchbook."
    hide yejuntalk
    show yejunquiet at center_char
    inha "There was nothing to tell."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "Most people would have been embarrassed."
    hide yejuntalk
    show yejunquiet at center_char

    menu:
        "\"I was. I just didn't show it.\"":
            inha "I was. I just didn't show it."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "That's what I mean."
            hide yejuntalk

        "\"I was angry. I got over it.\"":
            inha "I was angry. I got over it."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "How long did that take?"
            hide yejuntalk
            show yejunquiet at center_char
            inha "About a week."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Faster than I expected."
            hide yejuntalk

    show yejunquiet at center_char
    inha "Why did you come back?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "My visa expired."
    hide yejuntalk
    show yejunquiet at center_char
    inha "That's not what I mean."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I know."
    hide yejuntalk

    thought "He looks at the sky."

    show yejuntalk at center_char
    yejun "I don't have a better answer yet."
    hide yejuntalk
    show yejunquiet at center_char

    menu:
        "\"That's okay.\"":
            inha "That's okay."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "You're not going to push?"
            hide yejuntalk
            show yejunquiet at center_char
            inha "Would it help?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "No."
            hide yejuntalk
            show yejunquiet at center_char
            inha "Then no."
            hide yejunquiet

        "\"You'll tell me when you do.\"":
            inha "You'll tell me when you do."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Maybe."
            hide yejuntalk

    thought "Somehow that's the most honest thing anyone has said to me in months."

    jump chapter7
