from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Protect(Skill):
    def __init__(self):
        super(Protect, self).__init__('프로테스', Skill_Data['Protect']['ID'], Skill_Data['Protect']['COST'], Skill_Data['Protect']['POWER'], Skill_Data['Protect']['UPGRADE'])

    def activate(self, my_index):
        GPD.Battlelog.append(GPD.players[my_index].name + '의 프로테스')
        GPD.players[my_index].MP -= self.COST
        for i in range(0, 4):
            GPD.players[i].SHIELD += (self.POWER+GPD.players[my_index].DEF)
            GPD.Battlelog.append(GPD.players[i].name + '의 실드' + str(int((self.POWER + GPD.players[my_index].DEF))) + '증가')
        if GPD.monsters[0].name == '케프카':
            GPD.monsters[0].hate[my_index] += int(self.POWER / 3)
        else:
            for i in range(0, 3):
                GPD.monsters[i].hate[my_index] += int(self.POWER/3)
        GPD.CleanLog()
