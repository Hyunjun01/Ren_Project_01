init:
    
    # 캐릭터 포지션 지정
    transform char_pos(xposv, yposv):
        pos(xposv, yposv)
    # 비율 포지션 지정
    transform char_align(x_align, y_align):
        align(x_align, y_align)
    
    # show elf at snake_trnasform(elfCenter_xpos, elf_ypos, 30, 0.05, 6)
    # 떨림 함수 x좌표, y좌표, 떨림 강도, 한번 씩 움직이는 시간
    # 떨림 설명                   30                0.05
    transform snake_transform(char_xpos, char_ypos, amp, duration):
        ypos char_ypos
        xpos char_xpos
        block:
            linear duration xpos char_xpos + amp
            linear duration xpos char_xpos - amp
            linear duration xpos char_xpos + amp
            linear duration xpos char_xpos - amp
        linear duration xpos char_xpos    
    
    # 점프                                        100~150   0.1
    transform jump_transform(char_xpos, char_ypos, amp, duration):
        ypos char_ypos
        xpos char_xpos
        linear duration ypos char_ypos - amp 
        linear duration ypos char_ypos
    
    # 이동                    원래 좌표    이동 좌표   캐릭터 높이    가는 곳까지 걸리는 시간
    transform move_transform(char_expos, char_xpos, char_ypos, duration):
        xpos char_expos
        ease duration xpos char_xpos
    
    # 
    transform move_transform2(char_expos, char_eypos, char_ypos, duration):
        xpos char_expos
        ypos char_eypos
        ease duration ypos char_ypos

    # 인사할 때 쓰는 코드
    transform moveY_transform(char_expos, char_eypos, amp, duration, wait):
        xpos char_expos
        ypos char_eypos
        ease duration ypos char_eypos + amp
        pause wait
        ease duration ypos char_eypos




    # 이모지 점프
    transform emo_sion(x_pos, y_pos):
        xpos x_pos
        ypos y_pos
        linear 0.1 ypos y_pos - 30
        linear 0.1 ypos y_pos





# 실험 중인거 
    transform char_rotate(char_expos, char_eypos, char_ypos, amp, duration):
        xpos char_expos
        ypos char_eypos
        rotate 0
        ease duration rotate + amp
        ease duration rotate 0
        ease duration rotate - amp
        ease duration rotate 0
        ease duration rotate + amp
        ease duration ypos char_ypos
    
    transform bounce:
        pause .15
        yoffset 0
        easein .175 yoffset -10
        easeout .175 yoffset 0
        easein .175 yoffset -4
        easeout .175 yoffset 0
        yoffset 0