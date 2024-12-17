init python:
    gallery = Gallery()

    gallery.button("elf")
    gallery.unlock_image("CG_elf")

    gallery.button("vam")
    gallery.unlock_image("CG_vam")

    gallery.button("and")
    gallery.unlock_image("CG_and")



screen gallery_nav:
    vbox:
        xalign 0.0

        spacing 10
        xoffset -100
        # textbutton "엘프와의 추억" action ShowMenu("elf_gallery")
        # textbutton "뱀파이어와의 추억" action ShowMenu("vam_gallery")
        # textbutton "안드로이드와의 추억" action ShowMenu("and_gallery")

        imagebutton idle "images/gui_image/Character_Solt_A.png" hover "images/gui_image/Character_Solt_B.png" action ShowMenu("elf_gallery")
        imagebutton idle "images/gui_image/Character_Solt_A.png" hover "images/gui_image/Character_Solt_B.png" action ShowMenu("vam_gallery")
        imagebutton idle "images/gui_image/Character_Solt_A.png" hover "images/gui_image/Character_Solt_B.png" action ShowMenu("and_gallery")
        #textbutton "하나와의 추억" action ShowMenu("fri_gallery") # 조건 충족시 나와야함
    
    # frame:
    #     background None
    #     xalign 0.01
    #     yalign 0.98
        textbutton "Return":
            action Return()
            yoffset 200

screen elf_gallery():
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        use gallery_nav
        grid 3 2:
            add gallery.make_button(name="elf",unlocked=im.Scale("images/background/elf_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="elf",unlocked=im.Scale("images/background/elf_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="elf",unlocked=im.Scale("images/background/elf_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="elf",unlocked=im.Scale("images/background/elf_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="elf",unlocked=im.Scale("images/background/elf_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="elf",unlocked=im.Scale("images/background/elf_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            spacing 20

    # frame:
    #     background None
    #     xalign 0.01
    #     yalign 0.98
    #     textbutton "Return" action Return()



screen vam_gallery():
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        use gallery_nav
        grid 3 2:
            add gallery.make_button(name="vam",unlocked=im.Scale("images/background/vam_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="vam",unlocked=im.Scale("images/background/vam_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="vam",unlocked=im.Scale("images/background/vam_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="vam",unlocked=im.Scale("images/background/vam_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="vam",unlocked=im.Scale("images/background/vam_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="vam",unlocked=im.Scale("images/background/vam_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            spacing 20

    # frame:
    #     background None
    #     xalign 0.01
    #     yalign 0.98
    #     textbutton "Return" action Return()



screen and_gallery():
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        use gallery_nav
        grid 3 2:
            add gallery.make_button(name="and",unlocked=im.Scale("images/background/and_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="and",unlocked=im.Scale("images/background/and_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="and",unlocked=im.Scale("images/background/and_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="and",unlocked=im.Scale("images/background/and_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="and",unlocked=im.Scale("images/background/and_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            add gallery.make_button(name="and",unlocked=im.Scale("images/background/and_screen.png",400, 225),locked=im.Scale("images/background/locked.png",400, 225))
            spacing 20

    # frame:
    #     background None
    #     xalign 0.01
    #     yalign 0.98
    #     textbutton "Return" action Return()