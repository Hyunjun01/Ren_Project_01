

label start:

    #show elf agr at snake_transform(elf_xcen, elf_y, 30, 0.05)
    #show elf
    
    call OP
    
    
    #scene CG_elf
    me "text"
    show elf
    #$ play_clip_center()
    me "text2"
    # $ play_emoji("exc",750, 200)
    # pause 0.5
    # $ play_emoji("que",550, 200)
    # pause 0.5
    # $ play_emoji("lg", 850, 200)
    # pause 0.5

    #$ play_kira(650, 320)
    
    menu:
        "History에 표시 1번":
            #"History에 표시 1번"
            # $ renpy.log("History에 표시 1번")
            # $ renpy.add_history("Player", "History에 표시 1번")
            pass
        "History에 표시 2번":
            # "History에 표시 2번"
            "ㄴㅇㅁㄴㅇ"
            pass
    
    "History"
        
    
    me "text3"
    
    me "text4" 
    me "text5"




    label testChoice:
        "1번을 선택했음"