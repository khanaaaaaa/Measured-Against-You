label chapter7:
    scene rooftop with fade

    thought "The sky is gray."
    thought "The kind that sits low and stays."
    thought "We've been up here for a while without talking."
    thought "It's become normal, that."
    thought "The silence between us."

    show yejuntalk at center_char
    yejun "You know what's funny?"
    hide yejuntalk
    show yejunquiet at center_char
    inha "What?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I spent years trying to become someone impressive."
    yejun "Every grade... every award."
    yejun "I kept thinking— one more thing."
    yejun "One more achievement and it'll finally feel like enough."
    hide yejuntalk

    menu:
        "\"Did it ever?\"":
            show yejunquiet at center_char
            inha "Did it ever?"
            hide yejunquiet
            show yejuntalk at center_char
            yejun "No."
            yejun "Not once."
            hide yejuntalk

        "\"That sounds exhausting.\"":
            show yejunquiet at center_char
            inha "That sounds exhausting."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "It was."
            yejun "It is."
            hide yejuntalk

    show yejuntalk at center_char
    yejun "But every time I thought about home..."
    yejun "I only remembered drawing beside you."
    yejun "You drawing people. Me drawing robots."
    yejun "You always said yours were better."
    hide yejuntalk
    show yejunquiet at center_char

    thought "He remembered that."
    thought "The exact same thing I remember."
    thought "All this time."

    menu:
        "\"Your robots were terrible.\"":
            inha "Your robots were genuinely terrible."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "They were structurally sound."
            hide yejuntalk
            show yejunquiet at center_char
            inha "They had three legs."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "For stability."
            hide yejuntalk
            show yejunquiet at center_char
            thought "He almost smiles."
            thought "Almost."

        "\"I never believed you when you said mine were better.\"":
            inha "I never believed you."
            inha "I thought you were just being nice."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I know."
            yejun "That's why I kept saying it."
            hide yejuntalk

    show yejuntalk at center_char
    yejun "I was eight and I was right about your drawings."
    hide yejuntalk
    show yejunquiet at center_char

    thought "I look at the city below."
    thought "I don't say anything."
    thought "Because I don't know what to do with someone who remembers the same things I do."

    jump chapter8

label chapter8:
    scene classroom with fade

    show minjiquiet at center_char

    thought "Mock exam results."
    thought "Posted on the board outside the main hall."
    thought "I wait until the crowd clears before I look."
    thought "I find my name."
    thought "Rank 4."
    thought "I find his name."
    thought "Rank 1."
    thought "Of course."

    hide minjiquiet
    show minjismiletalk at center_char
    minji "Rank 4 is incredible, In-Ha."
    hide minjismiletalk

    menu:
        "\"It's not first.\"":
            show minjiquiet at center_char
            inha "It's not first."
            hide minjiquiet
            show minjismiletalk at center_char
            minji "In-Ha—"
            hide minjismiletalk
            show minjiquiet at center_char
            inha "I'm fine."
            hide minjiquiet

        "Walk away without responding.":
            thought "I walk away."
            show minjismiletalk at center_char
            minji "In-Ha. Hey—"
            hide minjismiletalk
            thought "I keep walking."

    thought "I'm not fine."
    thought "I go to the bathroom."
    thought "Sit on the floor."
    thought "Breathe."
    thought "Count to ten."
    thought "Go back out."
    thought "Smile."
    thought "This is fine."
    thought "I just have to work harder."
    thought "That's all."

    jump chapter9

label chapter9:
    scene rooftop_rain with fade

    show yejunquiet at center_char

    thought "It's raining."
    thought "Properly raining."
    thought "We're both getting wet."
    thought "Neither of us suggests going inside."

    inha "I heard your parents want you to do medicine."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "Where did you hear that?"
    hide yejuntalk
    show yejunquiet at center_char
    inha "People talk."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "Yeah..."
    yejun "Medicine."
    yejun "Stable, respectable, and impressive."
    yejun "The full set."
    hide yejuntalk
    show yejunquiet at center_char
    inha "But you compose music."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I used to."
    hide yejuntalk
    show yejunquiet at center_char
    inha "You have everything."
    inha "Grades, talent, options."
    inha "And you're just going to give it up?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "Then why do I feel empty?"
    hide yejuntalk

    thought "Silence."
    thought "Rain."

    show yejuntalk at center_char
    yejun "You think I was looking down on you all these years?"
    hide yejuntalk

    menu:
        "\"Weren't you?\"":
            show yejunquiet at center_char
            inha "Weren't you?"
            hide yejunquiet

        "\"I don't know what I think.\"":
            show yejunquiet at center_char
            inha "I don't know what I think."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "That's honest."
            hide yejuntalk

    show yejuntalk at center_char
    yejun "I was jealous of you."
    hide yejuntalk
    show yejunquiet at center_char
    inha "That's not funny."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I'm not joking."
    yejun "You drew because you loved it."
    yejun "Not because someone graded it."
    yejun "Not because it looked good on paper."
    yejun "You just— loved it."
    yejun "I never had that."
    yejun "I only ever had expectations."
    hide yejuntalk

    menu:
        "\"That's not something to be jealous of.\"":
            show yejunquiet at center_char
            inha "That's not something to be jealous of."
            inha "Loving something doesn't mean you're good enough at it."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "You are good enough."
            hide yejuntalk
            show yejunquiet at center_char
            inha "You don't know that."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I've seen your sketchbook."
            hide yejuntalk
            show yejunquiet at center_char
            inha "..."
            hide yejunquiet

        "Say nothing.":
            thought "I don't say anything."
            thought "Because I don't know if he's right."
            thought "About me."
            thought "About himself."
            thought "About any of it."

    thought "The rain gets heavier."
    thought "I don't know who I feel more sorry for."
    thought "Him."
    thought "Or me."
    thought "Or both of us."
    thought "Two people who spent years measuring themselves against each other—"
    thought "—and neither of us ever felt like we were winning."

    jump chapter10

label chapter10:
    scene academy_night with fade

    thought "He starts coming to the art studio after hours."
    thought "Just to sit."
    thought "Sometimes headphones. Sometimes he hums."
    thought "I pretend not to notice."
    thought "For about three days."

    show yejunquiet at center_char
    inha "You're humming again."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "Sorry."
    hide yejuntalk

    menu:
        "\"Don't be. What is it?\"":
            show yejunquiet at center_char
            inha "Don't be. What is it?"
            hide yejunquiet

        "\"It's a little distracting.\"":
            show yejunquiet at center_char
            inha "It's a little distracting."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "I'll stop."
            hide yejuntalk
            show yejunquiet at center_char
            inha "..."
            inha "What is it though?"
            hide yejunquiet

    show yejuntalk at center_char
    yejun "Something I've been working on."
    yejun "It doesn't have a name yet."
    hide yejuntalk
    show yejunquiet at center_char
    inha "What does it sound like?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "Like winter."
    yejun "But the part of winter that's almost spring."
    yejun "When you can't tell yet which way it's going."
    hide yejuntalk
    show yejunquiet at center_char

    thought "I want to hear the whole thing."
    thought "I don't say that."
    thought "He goes back to his notebook."
    thought "I go back to my canvas."
    thought "The studio is quiet except for the scratch of pencil and brush."
    thought "It's the most comfortable I've felt around another person in a long time."
    thought "I don't examine that."

    jump chapter11

label chapter11:
    scene classroom with fade

    thought "Minji corners me after class."
    thought "She has been waiting."
    thought "I can tell by the look on her face."

    show minjismiletalk at center_char
    minji "I need you to be honest with me."
    hide minjismiletalk
    show minjiquiet at center_char
    inha "About what?"
    hide minjiquiet
    show minjismiletalk at center_char
    minji "Ye-Jun."
    hide minjismiletalk

    menu:
        "\"What about him?\"":
            show minjiquiet at center_char
            inha "What about him?"
            hide minjiquiet

        "\"I knew this was coming.\"":
            show minjiquiet at center_char
            inha "I knew this was coming."
            hide minjiquiet
            show minjismiletalk at center_char
            minji "Then you're prepared."
            hide minjismiletalk

    show minjismiletalk at center_char
    minji "You like him."
    hide minjismiletalk
    show minjiquiet at center_char
    inha "I don't."
    hide minjiquiet
    show minjismiletalk at center_char
    minji "You brought him coffee this morning."
    hide minjismiletalk
    show minjiquiet at center_char
    inha "I brought two coffees and he was there."
    hide minjiquiet
    show minjismiletalk at center_char
    minji "You remembered he takes it without sugar."
    hide minjismiletalk
    show minjiquiet at center_char
    inha "..."
    hide minjiquiet
    show minjismiletalk at center_char
    minji "You told me you don't even remember how I take mine."
    hide minjismiletalk
    show minjiquiet at center_char
    inha "You change it every week."
    hide minjiquiet
    show minjismiletalk at center_char
    minji "In-Ha."
    hide minjismiletalk

    menu:
        "\"I don't want to talk about this.\"":
            show minjiquiet at center_char
            inha "I don't want to talk about this."
            hide minjiquiet
            show minjismiletalk at center_char
            minji "That is basically a confession."
            hide minjismiletalk
            show minjiquiet at center_char
            inha "It is not a confession."
            hide minjiquiet
            show minjismiletalk at center_char
            minji "Confession-adjacent."
            hide minjismiletalk

        "\"Even if I did— it doesn't matter right now.\"":
            show minjiquiet at center_char
            inha "Even if I did— it doesn't matter."
            inha "We have exams. I don't have time for this."
            hide minjiquiet
            show minjismiletalk at center_char
            minji "You're going to be so lonely when you're successful."
            hide minjismiletalk
            show minjiquiet at center_char
            inha "I'll be fine."
            hide minjiquiet
            show minjismiletalk at center_char
            minji "That's what lonely people say."
            hide minjismiletalk

    jump chapter12

label chapter12:
    scene rooftop with fade

    thought "I ask him something I've been carrying for weeks."
    thought "I wait until we've been sitting long enough that it doesn't feel like an ambush."

    show yejunquiet at center_char
    inha "When we were kids—"
    inha "Did you actually think I was good at drawing?"
    inha "Or were you just being nice?"
    hide yejunquiet
    show yejuntalk at center_char
    yejun "Why does it matter now?"
    hide yejuntalk

    menu:
        "\"It's always mattered.\"":
            show yejunquiet at center_char
            inha "It's always mattered."
            hide yejunquiet

        "\"I just want to know. Honestly.\"":
            show yejunquiet at center_char
            inha "I just want to know."
            inha "Honestly."
            hide yejunquiet
            show yejuntalk at center_char
            yejun "Honestly?"
            hide yejuntalk
            show yejunquiet at center_char
            inha "Honestly."
            hide yejunquiet

    show yejuntalk at center_char
    yejun "I thought you were the best artist I'd ever seen."
    yejun "I still do."
    hide yejuntalk
    show yejunquiet at center_char
    inha "You've seen real artists since then."
    hide yejunquiet
    show yejuntalk at center_char
    yejun "I know what I think."
    hide yejuntalk
    show yejunquiet at center_char

    thought "I look at him."
    thought "He looks back."
    thought "Neither of us looks away."
    thought "This is dangerous."
    thought "I know exactly what this is."
    thought "And I don't move."

    hide yejunquiet

    menu:
        "Look away first.":
            show yejunquiet at center_char
            inha "..."
            hide yejunquiet
            thought "I look back at the city."
            thought "My heart is doing something I don't have words for."

        "Don't look away.":
            "I don't look away."
            show yejunquiet at center_char
            yejun "..."
            thought "He looks away first."
            thought "Down at his hands."
            thought "I don't know what that means."
            thought "I think about it for the rest of the day."
            hide yejunquiet

    jump chapter13

label chapter13:
    scene academy_night with fade

    thought "He brings his composition notebook one evening."
    thought "Sets it on the table between us without saying anything."
    thought "Just opens it."
    thought "Pages of musical notation."
    thought "Margins full of notes to himself."
    thought "Arrows. Question marks."
    thought "One section circled three times."

    show yejunsmile at center_char
    inha "This part—"
    inha "What does this feel like when you play it?"
    hide yejunsmile
    show yejuntalkhappy at center_char
    yejun "That part is you, actually."
    hide yejuntalkhappy
    show yejunsmile at center_char
    inha "Me?"
    hide yejunsmile
    show yejuntalkhappy at center_char
    yejun "The part that almost resolves and then doesn't."
    yejun "It keeps getting close and then pulling back."
    yejun "Like it's not ready yet."
    hide yejuntalkhappy

    menu:
        "\"That's not flattering.\"":
            show yejunsmile at center_char
            inha "That's not exactly flattering."
            hide yejunsmile
            show yejuntalkhappy at center_char
            yejun "It's my favorite part of the piece."
            hide yejuntalkhappy
            show yejunsmile at center_char
            inha "..."
            hide yejunsmile
            thought "I don't know what to do with that."

        "\"Does it ever resolve?\"":
            show yejunsmile at center_char
            inha "Does it ever resolve?"
            hide yejunsmile
            show yejuntalkhappy at center_char
            yejun "Eventually."
            yejun "I haven't written that part yet."
            hide yejuntalkhappy
            thought "Eventually."
            thought "I sit with that word for a moment."

    show yejunsmile at center_char
    inha "Can I hear it?"
    hide yejunsmile
    show yejuntalkhappy at center_char
    yejun "It's not finished."
    hide yejuntalkhappy

    menu:
        "\"I don't mind.\"":
            show yejunsmile at center_char
            inha "I don't mind."
            hide yejunsmile
            show yejuntalkhappy at center_char
            yejun "..."
            yejun "Okay."
            hide yejuntalkhappy

        "\"Unfinished things are more honest anyway.\"":
            show yejunsmile at center_char
            inha "Unfinished things are more honest anyway."
            hide yejunsmile
            show yejuntalkhappy at center_char
            yejun "..."
            yejun "Yeah."
            yejun "They are."
            hide yejuntalkhappy

    thought "He hums it quietly."
    thought "Just the melody."
    thought "Just his voice in the empty studio."
    thought "..."
    thought "I hate him."
    thought "I don't hate him at all."
    thought "I haven't hated him in a very long time."
    thought "I'm not sure I ever did."

    jump chapter14
