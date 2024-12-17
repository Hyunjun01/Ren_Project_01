screen screen_text(txt, time, textspeed):
    frame:
        background None
        xalign 0.5
        yalign 0.5
        padding(0, 0)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            text txt slow_cps textspeed:
                size 70
                color "#fff"

        timer time action Return()


screen screen_Loading:
    frame:
        background None
        xalign 0.5
        yalign 0.5
        padding(0, 0)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            hbox:
                text "Loading" slow_cps 30:
                    size 70
                    color "#fff"
                text " . . . . . ." slow_cps 4:
                    size 70
                    color "#fff"

        timer 5 action Return()





