from pico2d import*
from SAVEManager import*
import game_framework
import GamePlayingData as GPD
import battle, battle_boss, title


def enter():
    global background, menu, font
    global current_time, Prevtime
    global message_index
    global total_money, total_exp
    #open_canvas()
    if GPD.monsters[0].name != '케프카':
        background = battle.background
    else:
        background = battle_boss.background_final
    current_time = 0
    Prevtime = 0
    message_index = 0
    GPD.bgm.battlewin.repeat_play()

    for i in range(0, 4):
        if GPD.players[i].act_type != 7:
            GPD.players[i].act_type = 4

    total_money = 0
    total_exp = 0
    if GPD.monsters[0].name != '케프카':
        for i in range(0, 3):
            total_money += GPD.monsters[i].MONEY
            total_exp += GPD.monsters[i].EXP
    else:
        total_money += GPD.monsters[0].MONEY
        total_exp += GPD.monsters[0].EXP

    GPD.money += total_money
    for i in range(0,4):
        GPD.players[i].EXP += total_exp



def exit():
    for i in range(0, 4):
        GPD.players[i].act_type = 0

    if GPD.monsters[0].name == '케프카':
        GPD.now_map = 0
        GPD.Player.x = 461
        GPD.Player.y = 353
        Save_game()


def update():
    global message_index

    for i in range (0,4):
        GPD.players[i].frame += game_framework.frame_time * 4

    if message_index >= 7:
        if GPD.monsters[0].name == '케프카':
            game_framework.change_state(title)
        else:
            game_framework.pop_state()


def draw():
    global backgound
    global message_index
    clear_canvas()

    # 배경 출력
    background.clip_draw(0, 0, 1000, 740, 400, 400, 800, 500)

    # 플레이어 출력
    for i in range(0, 4):
        GPD.players[i].draw()

    # 하단 메뉴 출력
        GPD.Menu.image.clip_draw(0, 0, 240, 160, 400, 75, 800, 150)
    if GPD.monsters[0].name == '케프카':
        if message_index == 0:
            GPD.Ingame_font.font.draw(360, 75, '전투 승리', [255, 255, 255])
        elif message_index == 1:
            GPD.Ingame_font.font.draw(300, 75, '마지막 보스를 물리치셨습니다..', [255, 255, 255])
        elif message_index == 2:
            GPD.Ingame_font.font.draw(300, 75, '데이터를 저장하고 타이틀로 이동합니다.', [255, 255, 255])
    else:
        if message_index == 0:
            GPD.Ingame_font.font.draw(360, 75, '전투 승리', [255, 255, 255])
        elif message_index == 1:
            GPD.Ingame_font.font.draw(300, 75, '골드 ' + str(total_money) + '를 획득하였습니다.', [255, 255, 255])
        elif message_index == 2:
            GPD.Ingame_font.font.draw(300, 75, '경험치 ' + str(total_exp) + '를 획득하였습니다.', [255, 255, 255])
        elif message_index == 3:
            GPD.Ingame_font.font.draw(300, 75, GPD.players[0].name + '가 레벨업 하였습니다.', [255, 255, 255])
        elif message_index == 4:
            GPD.Ingame_font.font.draw(300, 75, GPD.players[1].name + '가 레벨업 하였습니다.', [255, 255, 255])
        elif message_index == 5:
            GPD.Ingame_font.font.draw(300, 75, GPD.players[2].name + '가 레벨업 하였습니다.', [255, 255, 255])
        elif message_index == 6:
            GPD.Ingame_font.font.draw(300, 75, GPD.players[3].name + '가 레벨업 하였습니다.', [255, 255, 255])

    update_canvas()


def pause(): pass


def resume(): pass


def handle_events():
    global message_index

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            pass
        # a 선택 s 뒤로가기
        elif event.type == SDL_KEYDOWN:
            GPD.Menu.sound.play()
            if event.key == SDLK_ESCAPE:
                # game_framework.change_state(map)
                game_framework.pop_state()
            elif event.key == SDLK_a:
                message_index += 1

                if message_index is 3:
                    if GPD.players[0].EXP >= GPD.players[0].MAX_EXP and GPD.players[0].act_type != 7:
                        GPD.players[0].EXP -= GPD.players[0].MAX_EXP
                        GPD.players[0].MAX_EXP += GPD.players[0].MAX_EXP * 2
                        GPD.players[0].LEVEL += 1
                        GPD.players[0].AP += 10
                    else:
                        message_index += 1

                if message_index is 4:
                    if GPD.players[1].EXP >= GPD.players[1].MAX_EXP and GPD.players[1].act_type != 7:
                        GPD.players[1].EXP -= GPD.players[1].MAX_EXP
                        GPD.players[1].MAX_EXP += GPD.players[1].MAX_EXP * 2
                        GPD.players[1].LEVEL += 1
                        GPD.players[1].AP += 10
                    else:
                        message_index += 1

                if message_index is 5:
                    if GPD.players[2].EXP >= GPD.players[2].MAX_EXP and GPD.players[2].act_type != 7:
                        GPD.players[2].EXP -= GPD.players[2].MAX_EXP
                        GPD.players[2].MAX_EXP += GPD.players[2].MAX_EXP * 2
                        GPD.players[2].LEVEL += 1
                        GPD.players[2].AP += 10
                    else:
                        message_index += 1

                if message_index is 6:
                    if GPD.players[3].EXP >= GPD.players[3].MAX_EXP and GPD.players[3].act_type != 7:
                        GPD.players[3].EXP -= GPD.players[3].MAX_EXP
                        GPD.players[3].MAX_EXP += GPD.players[3].MAX_EXP * 2
                        GPD.players[3].LEVEL += 1
                        GPD.players[3].AP += 10
                    else:
                        message_index += 1