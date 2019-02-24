from ..fLogger import logger
import math
import json

scoreArry = [0,1,10,100,1000,10000]

class Computerplayter():
    def __init__(self):
        '''
           init  computer player
        '''
        self.checkboard =  [[0 for i in range(15)] for i in range(15)]
        

    def computestep(self, steps, strcheckboard):
        logger.info("computestep is called")
        #logger.info(strcheckboard)
        tcheckboard = strcheckboard.split(',')

        for i in range(len(tcheckboard)):
            self.checkboard[math.floor(i/15)][i%15] = int(tcheckboard[i])
        
        color = 1 if int(steps)%2==0 else -1
        beststep = {'i':-1,'j':-1,'score':-1}
        enemybeststep = {'i':-1,'j':-1,'score':-1}

        for i in range(15):
            for j in range(15):
                if self.checkboard[i][j] == 0:
                    score = self.getscore(i,j,color)
                    enemyscore = self.getscore(i,j,-color)

                    if beststep['score'] < score:
                        beststep["i"] = i
                        beststep["j"] = j
                        beststep["score"] = score

                    if enemybeststep['score'] < enemyscore:
                        enemybeststep["i"] = i
                        enemybeststep["j"] = j
                        enemybeststep["score"] = enemyscore
        
        if beststep["score"] >= 10000:
            return beststep
        elif enemybeststep["score"] >= 10000:
            return enemybeststep
        elif beststep["score"] >= 1000:
            return beststep
        elif enemybeststep["score"] >= 1000:
            return enemybeststep

        logger.info("in computerplayer.py beststep:"+json.dumps(beststep))
        return beststep

    def getscore(self, i, j, color):
        return self.getRowScore(i,j,color)\
			  +self.getColScore(i,j,color)\
			  +self.getLeftSkewScore(i,j,color)\
			  +self.getRightSkewScore(i,j,color)
    
    def getRowScore(self, i, j, color):
        continuous = 1
        cj = j-1
        while cj>=0:
            if self.checkboard[i][cj] == color:
                continuous += 1
                cj -= 1
            else:
                break
        cj = j+1
        while cj<15:
            if self.checkboard[i][cj] == color:
                continuous += 1
                cj += 1
            else:
                break
        return scoreArry[continuous]

    def getColScore(self, i, j, color):
        continuous = 1
        for ci in range(i-1,-1,-1):
            if self.checkboard[ci][j] == color:
                continuous += 1
            else:
                break
        for ci in range(i+1,14):
            if self.checkboard[ci][j] == color:
                continuous += 1
            else:
                break      
        return scoreArry[continuous]
    
    def getLeftSkewScore(self, i, j, color):
        continuous = 1
        ci = i-1
        cj = j-1
        while ci>=0 and cj>=0:
            if self.checkboard[ci][cj] == color:
                continuous += 1
                ci -= 1
                cj -= 1
            else:
                break
        ci = i+1
        cj = j+1
        while ci<15 and cj<15:
            if self.checkboard[ci][cj] == color:
                continuous += 1
                ci += 1
                cj += 1
            else:
                break
        return scoreArry[continuous]
    
    def getRightSkewScore(self, i, j, color):
        continuous = 1
        ci = i-1
        cj = j+1
        while ci>=0 and cj<15:
            if self.checkboard[ci][cj] == color:
                continuous += 1
                ci -= 1
                cj += 1
            else:
                break
        ci = i+1
        cj = j-1
        while ci<15 and cj>=0:
            if self.checkboard[ci][cj] == color:
                continuous += 1
                ci += 1
                cj -= 1
            else:
                break
        return scoreArry[continuous]




computerplayter = Computerplayter()