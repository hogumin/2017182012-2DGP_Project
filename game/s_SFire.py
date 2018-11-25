from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class SFire(Skill):
    def __init__(self):
        super(SFire, self).__init__('파이가', Skill_Data['SFire']['ID'], Skill_Data['SFire']['COST'], Skill_Data['SFire']['POWER'], Skill_Data['SFire']['UPGRADE'])

    def activate(self, my_index):
        if GPD.monsters[0].name is '케프카':
            GPD.monsters[0].HP -= int(self.POWER * (GPD.players[my_index].ATK / 10))
            GPD.monsters[0].hate[my_index] += self.POWER * 2
            print(GPD.monsters[0].name + '의 체력: ' + str(GPD.monsters[0].HP))
            GPD.monsters[0].FireorIce = GPD.monsters[0].FireorIce - 1
        else:
            for target_index in range(0,3):
                GPD.monsters[target_index].HP -= int(self.POWER * (GPD.players[my_index].ATK / 10))
                GPD.monsters[target_index].hate[my_index] += self.POWER * 2
                print(GPD.monsters[target_index].name + str(target_index) + '의 체력: ' + str(GPD.monsters[target_index].HP))