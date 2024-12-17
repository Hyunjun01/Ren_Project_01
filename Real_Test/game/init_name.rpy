


define me = Character("[persistent.player_name]")


label OP:

    scene green_screen with OPfade

    play sound "audio/sound/SE_Typing_05c.wav.mp3"
    call screen screen_text("환영합니다.", 3, 7)

    play sound "audio/sound/SE_Typing_05c.wav.mp3"
    call screen screen_text("당신의 이름을 입력해주세요.", 4, 15)

    # $ persisent.player_name = ""
    
    $ persistent.player_name = renpy.input("이름을 입력해주세요\n {size=-15}(기본 이름은 '인공'으로 설정됩니다)", length=10)

    if not persistent.player_name.strip():
        $ persistent.player_name = "인공"
    
    pause 0.2
    play sound "audio/sound/SE_Booting_02.wav.mp3"
    call screen screen_Loading
    play sound "audio/sound/SE_Confirm_02.wav.mp3"
    pause 0.5

    play sound "audio/sound/SE_Typing_05c.wav.mp3"
    call screen screen_text("환영합니다. [me] 플레이어님", 4, 20)


    me "흐음"





