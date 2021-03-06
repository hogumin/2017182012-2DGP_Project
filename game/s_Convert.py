from BaseSkill import*
import json
import GamePlayingData as GPD

Skill_data_file = open('json\\Skill.json', 'r')
Skill_Data = json.load(Skill_data_file)
Skill_data_file.close()

class Convert(Skill):
    def __init__(self):
        super(Convert, self).__init__('생명력변환', Skill_Data['Convert']['ID'], Skill_Data['Convert']['COST'], Skill_Data['Convert']['POWER'], Skill_Data['Convert']['UPGRADE'])

    def activate(self, my_index):
        GPD.Battlelog.append(GPD.players[my_index].name + '의 생명력변환')
        GPD.Battlelog.append(GPD.players[my_index].name + '의 HP ' + str(int(GPD.players[my_index].HP * 0.2)) + '감소')
        GPD.Battlelog.append(GPD.players[my_index].name + '의 MP ' + str(int(GPD.players[my_index].HP * 0.2)) + '회복')

        GPD.players[my_index].MP += int(GPD.players[my_index].HP * 0.2)
        GPD.players[my_index].HP -= int(GPD.players[my_index].HP * 0.2)
        if GPD.players[my_index].HP <= 0:
            GPD.players[my_index].HP = 1
        if GPD.players[my_index].MP > GPD.players[my_index].MAX_MP:
            GPD.players[my_index].MP = GPD.players[my_index].MAX_MP
        GPD.CleanLog()
