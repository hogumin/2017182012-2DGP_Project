from BasePlayer import*
from s_Blizzard import*
from s_SFire import*
from s_Convert import*
from s_ManaShift import*
import json
import GamePlayingData as GPD


BlackMage_data_file = open('json\\Player.json', 'r')
BlackMage_Data = json.load(BlackMage_data_file)
BlackMage_data_file.close()


class BlackMage(Player):
    def __init__(self,party_num):
        super(BlackMage, self).__init__('흑마도사', BlackMage_Data['BlackMage']['HP'], BlackMage_Data['BlackMage']['MAX_HP'],
                                        BlackMage_Data['BlackMage']['MP'], BlackMage_Data['BlackMage']['MAX_MP'],
                                        BlackMage_Data['BlackMage']['LEVEL'], BlackMage_Data['BlackMage']['EXP'],
                                        BlackMage_Data['BlackMage']['MAX_EXP'], BlackMage_Data['BlackMage']['ATK'],
                                        BlackMage_Data['BlackMage']['DEF'],0,0)
        self.party_num = party_num
        self.frame=0
        self.attack_animation = 0
        self.anistep = 0

        # 0 common  1 attack ready  2 attack  3 magic 4 victory 5 lesshp 6 damaged 7 die
        self.act_type = 0
        self.act_type_tmp = 0

        self.status_string = self.name + '  ' + 'HP: ' + str(self.HP) + '/' + str(self.MAX_HP) + ' ' + 'MP: ' + \
                             str(self.MP) + '/' + str(self.MAX_MP)
        self.skill = [Blizzard(),SFire(),Convert(),ManaShift()]

    def draw(self):
        if self.act_type == 0:
            GPD.BlackMage.image.clip_draw(0, 0, 72, 72, 600 + self.attack_animation, 420 - 75 * self.party_num)
        elif self.act_type == 1:
            GPD.BlackMage.image.clip_draw(72, 0, 72, 72, 600 + self.attack_animation, 420 - 75 * self.party_num)
        elif self.act_type == 2:
            GPD.BlackMage.image.clip_draw(144 + 72 * int(self.frame % 3), 0, 72, 72, 500, 420 - 75 * self.party_num)
        elif self.act_type == 3:
            GPD.BlackMage.image.clip_draw(360 + 72 * int(self.frame % 2), 0, 72, 72, 600, 410 - 75 * self.party_num)
        elif self.act_type == 4:
            if int(self.frame % 2):
                GPD.BlackMage.image.clip_draw(504, 0, 72, 72, 600, 420 - 75 * self.party_num)
            else:
                GPD.BlackMage.image.clip_draw(0, 0, 72, 72, 600 + self.attack_animation, 420 - 75 * self.party_num)
        elif self.act_type == 5:
            GPD.BlackMage.image.clip_draw(576, 0, 72, 72, 600, 420 - 75 * self.party_num)
        elif self.act_type == 6:
            GPD.BlackMage.image.clip_draw(648, 0, 72, 72, 600, 420 - 75 * self.party_num)
        elif self.act_type== 7:
            GPD.BlackMage.image.clip_draw(720, 0, 72, 72, 600, 420 - 75 * self.party_num)

    def renew_status(self):
        self.status_string = self.name + '  ' + 'HP: ' + str(int(self.HP)) + '/' + str(self.MAX_HP) + ' ' + 'MP: ' + \
                             str(self.MP) + '/' + str(self.MAX_MP)

    def attack(self,my_index,target_index):
        if self.ATK / 2 - GPD.monsters[target_index].DEF > 0:
            dmg = int(self.ATK / 2 - GPD.monsters[target_index].DEF)
            GPD.monsters[target_index].HP -= dmg
            GPD.Battlelog.append(self.name + '가 ' + GPD.monsters[target_index].name + '에게 ' + str(dmg) + '피해')
        else:
            GPD.Battlelog.append(self.name + '의 공격이 빗나감')

        GPD.CleanLog()
