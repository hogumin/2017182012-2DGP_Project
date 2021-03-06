import GamePlayingData as GPD

class Effect():
    def __init__(self):
        self.frame = 0
        self.id = -1
        # 0 공격 1 힐 2 부활
        # over 10 is 플레이어 스킬
        # 1XX is 몬스터 스킬
        # 2XX is 보스 스킬

    def draw(self, my_num, party_num):
        if self.id == 0:
            if GPD.monsters[0].name != '케프카':
                GPD.Attack.image.clip_draw(0+int(self.frame % 3)*192, 0, 192, 192, 200, 410 - 100 * party_num)
            else:
                GPD.Attack.image.clip_draw(0 + int(self.frame % 3) * 192, 0, 192, 192, 200, 320,256,256)
        elif self.id == 1 or self.id == 16:
            GPD.Heal.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 4) * 192, 192,
                                     192, 600, 420 - 75 * party_num, 72, 72)
        elif self.id == 2:
            GPD.Raise.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 6) * 192, 192,
                                     192, 600, 420 - 75 * party_num, 72, 72)

        elif self.id == 11:
            if GPD.monsters[0].name != '케프카':
                GPD.Provoke.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                     192, 200, 410 - 100 * party_num,128,128)
            else:
                GPD.Provoke.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192,
                                            192, 192, 200, 320, 256, 256)

        elif self.id == 12:
            GPD.OverPower.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                        192, 120, 300, 400, 300)

        elif self.id == 13:
            GPD.Defiance.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 5) * 192, 192,
                                     192, 500, 420 - 75 * my_num, 100, 100)

        elif self.id == 14:
            if GPD.monsters[0].name != '케프카':
                GPD.Fell_Cleave.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 5) * 192, 192,
                                        192, 200, 410 - 100 * party_num)
            else:
                GPD.Fell_Cleave.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 5) * 192,
                                                192, 192, 200, 320, 256, 256)

        elif self.id == 15:
            if GPD.monsters[0].name != '케프카':
                GPD.Stone.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                        192, 200, 410 - 100 * party_num, 128, 128)
            else:
                GPD.Stone.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                          192, 200, 320, 256, 256)
        elif self.id == 17:
            GPD.Heal.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 4) * 192, 192,
                                        192, 600, 420 - 75 * 0, 72, 72)
            GPD.Heal.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 4) * 192, 192,
                                        192, 500, 420 - 75 * 1, 72, 72)
            GPD.Heal.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 4) * 192, 192,
                                        192, 600, 420 - 75 * 2, 72, 72)
            GPD.Heal.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 4) * 192, 192,
                                        192, 600, 420 - 75 * 3, 72, 72)

        elif self.id == 18:
            GPD.Protect.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                      192, 600, 420 - 75 * 0, 72, 72)
            GPD.Protect.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                        192, 500, 420 - 75 * 1, 72, 72)
            GPD.Protect.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                        192, 600, 420 - 75 * 2, 72, 72)
            GPD.Protect.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                        192, 600, 420 - 75 * 3, 72, 72)

        elif self.id == 19:
            if GPD.monsters[0].name != '케프카':
                GPD.Blizzard.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                      192, 200, 410 - 100 * party_num, 128, 128)
            else:
                GPD.Blizzard.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192,
                                             192, 192, 200, 320, 256, 256)
        elif self.id == 20:
            GPD.SFire.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                      192, 200, 300, 400, 300)
        elif self.id == 21:
            GPD.Convert.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                        192, 500, 420 - 75 * 3, 72, 72)
        elif self.id == 22:
            if self.frame < 19:
                GPD.Heal.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 3) - int(self.frame / 4) * 192, 192,
                                         192, 600, 420 - 75 * party_num, 72, 72)
            GPD.Convert.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                        192, 500, 420 - 75 * 3, 72, 72)
        elif self.id == 23:
            if GPD.monsters[0].name != '케프카':
                GPD.GustSlash.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 2) - int(self.frame / 5) * 192, 192,
                                         192, 200, 410 - 100 * party_num, 128, 128)
            else:
                GPD.GustSlash.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 2) - int(self.frame / 5) * 192,
                                              192, 192, 200, 320, 256, 256)
        elif self.id == 24:
            GPD.DeathBlossom.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 5) * 192, 192,
                                      192, 200, 300, 400, 400)

        elif self.id == 25:
            if GPD.monsters[0].name != '케프카':
                GPD.Assassinate.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 2) - int(self.frame / 5) * 192, 192,
                                          192, 200, 410 - 100 * party_num, 128, 128)
            else:
                GPD.Assassinate.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 2) - int(self.frame / 5) * 192,
                                                192, 192, 200, 320, 256, 256)

        elif self.id == 26:
            GPD.Diversion.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 5) * 192,
                                             192, 192, 200, 300, 400, 400)

        elif self.id == 100:
            GPD.Attack.image.clip_draw(0 + int(self.frame % 3) * 192, 0, 192, 192, 600, 420 - 75 * party_num)

        elif self.id == 200:
            GPD.HyperDrive.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 5) * 192,
                                          192, 192, 600, 420 - 75 * 0, 72, 72)
            GPD.HyperDrive.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 5) * 192,
                                           192, 192, 600, 420 - 75 * 1, 72, 72)
            GPD.HyperDrive.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 5) * 192,
                                           192, 192, 600, 420 - 75 * 2, 72, 72)
            GPD.HyperDrive.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 5) * 192,
                                           192, 192, 600, 420 - 75 * 3, 72, 72)
        elif self.id == 201:
            GPD.SFire.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                      192, 600, 300, 400, 300)
        elif self.id == 202:
            GPD.Blizzard.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                         192, 600, 300, 400, 300)
        elif self.id == 203:
            GPD.R_FIRE.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 1) - int(self.frame / 5) * 192, 192,
                                       192, 600, 300, 400, 300)
        elif self.id == 204:
            GPD.R_ICE.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 4) - int(self.frame / 5) * 192, 192,
                                      192, 600, 300, 400, 300)
        elif self.id == 205 or self.id == 206:
            GPD.Diversion.image.clip_draw(0 + int(self.frame % 5) * 192, int(192 * 5) - int(self.frame / 5) * 192,
                                          192, 192, 600, 300, 400, 400)

    def playFX(self):
        if self.id == 0:
            GPD.Attack.sound.play()
        elif self.id == 1 or self.id == 16:
            GPD.Heal.sound.play()
        elif self.id == 2:
            GPD.Raise.sound.play()

        elif self.id == 11:
            GPD.Provoke.sound.play()
        elif self.id == 12:
            GPD.OverPower.sound.play()
        elif self.id == 13:
            GPD.Defiance.sound.play()
        elif self.id == 14:
            GPD.Fell_Cleave.sound.play(3)
        elif self.id == 15:
            GPD.Stone.sound.play()
        elif self.id == 17:
            GPD.Heal.sound.play()
        elif self.id == 18:
            GPD.Protect.sound.play()
        elif self.id == 19:
            GPD.Blizzard.sound.play()
        elif self.id == 20:
            GPD.SFire.sound.play()
        elif self.id == 21:
            GPD.Convert.sound.play()
        elif self.id == 22:
            GPD.Heal.sound.play()
            GPD.Convert.sound.play()
        elif self.id == 23:
            GPD.GustSlash.sound.play()
        elif self.id == 24:
            GPD.DeathBlossom.sound.play(2)
        elif self.id == 25:
            GPD.Assassinate.sound.play()
        elif self.id == 26:
            GPD.Diversion.sound.play()

        elif self.id == 100:
            GPD.Attack.sound.play()

        elif self.id == 200:
            GPD.Attack.sound.play()
        elif self.id == 201:
            GPD.SFire.sound.play()
        elif self.id == 202:
            GPD.Blizzard.sound.play()
        elif self.id == 203:
            GPD.SFire.sound.play()
        elif self.id == 204:
            GPD.Blizzard.sound.play()
        elif self.id == 205:
            GPD.Diversion.sound.play()
        elif self.id == 206:
            GPD.Diversion.sound.play()