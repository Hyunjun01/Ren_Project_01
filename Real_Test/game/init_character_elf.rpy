init:

    define e = Character("프레야")

    define elf_xcen = 860
    define elf_y = 820

    define elf_xleft = 350
    define elf_xright = 1450

    

    image elf:
        "images/elf/el.png"
        anchor(0.5, 0.5)
        zoom 1.2
        xpos 860
        ypos elf_y
        block:
            linear 0.75 ypos elf_y - 2
            linear 0.75 ypos elf_y + 2
            repeat

    image elf agr:
        "images/elf/el_agr.png"
        anchor(0.5, 0.5)
        zoom 1.2
        xpos 860
        ypos 820
    
    image elf dang:
        "images/elf/el_dang.png"
        anchor(0.5, 0.5)
        zoom 1.2
        xpos 860
        ypos 820

    image elf mung:
        "images/elf/el_mung.png"
        anchor(0.5, 0.5)
        zoom 1.2
        xpos 860
        ypos 820
    
    image elf hwang:
        "images/elf/el_hwang.png"
        anchor(0.5, 0.5)
        zoom 1.2
        xpos 860
        ypos 820
    
    image elf hwang2:
        "images/elf/el_hwang2.png"
        anchor(0.5, 0.5)
        zoom 1.2
        xpos 860
        ypos 820
    
    image elf hpy:
        "images/elf/el_hpy.png"
        anchor(0.5, 0.5)
        zoom 1.2
        xpos 860
        ypos 820

    image elf hum:
        "images/elf/el_hum.png"
        anchor(0.5, 0.5)
        zoom 1.2
        xpos 860
        ypos 820
    
    image elf hum2:
        "images/elf/el_hum2.png"
        anchor(0.5, 0.5)
        zoom 1.2
        xpos 860
        ypos 820
    



    image elf_big:
        "images/elf/el.png"
        anchor(0.5, 0.5)
        zoom 1.5
        xpos 840
        ypos 1000

    image elf_big agr:
        "images/elf/el_agr.png"
        anchor(0.5, 0.5)
        zoom 1.5
        xpos 840
        ypos 1000
    
    image elf_big dang:
        "images/elf/el_dang.png"
        anchor(0.5, 0.5)
        zoom 1.5
        xpos 840
        ypos 1000



    
