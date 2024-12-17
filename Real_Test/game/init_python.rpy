init python:
    def play_clip_center():
        # 사운드 재생
        renpy.play("audio/sound/SFX_Emoticon_Motion_Dot.wav.mp3")

        # 이미지 순차적으로 표시
        renpy.show("clip", at_list=[char_pos(680, 200)])
        renpy.pause(0.21)

        renpy.show("clip2", at_list=[char_pos(653, 198)])
        renpy.pause(0.4)

        renpy.show("clip3", at_list=[char_pos(674, 198)])
        renpy.pause(0.4)

        renpy.show("clip4", at_list=[char_pos(695, 198)])
        renpy.pause(1)

        renpy.hide("clip")
        renpy.hide("clip2")
        renpy.hide("clip3")
        renpy.hide("clip4")
    
    




    def play_emoji(emoji, x_pos, y_pos):
        if emoji == "exc":
            # 0.4
            renpy.play("audio/sound/SFX_Emoticon_Motion_Heart.wav.mp3")
        elif emoji == "que":
            # 0.4
            renpy.play("audio/sound/SFX_Emoticon_Motion_Question.wav.mp3")
        elif emoji == "lg":
            # 0.4
            renpy.play("audio/sound/SFX_Emoticon_Motion_Surprise.wav.mp3")
        # elif emoji == "kira":
        #     # 1
        #     renpy.play("audio/sound/SFX_Emoticon_Motion_Twinkle.wav.mp3")
            
        
        renpy.show(emoji, at_list=[emo_sion(x_pos, y_pos)])
        renpy.pause(0.4)

        renpy.hide(emoji)
        renpy.with_statement(dissolve)



    def play_kira(x_pos, y_pos):
        renpy.play("audio/sound/SFX_Emoticon_Motion_Twinkle.wav.mp3")
        renpy.show("kira", at_list=[char_pos(x_pos, y_pos)])
        renpy.pause(1)
        renpy.hide("kira")
        renpy.with_statement(dissolve)

    
################################################################ 갤러리


    g = Gallery()

