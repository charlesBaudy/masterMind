import random

class Jeu:
    
    def compare(self, code, tentative):
        result = ["R","R","R","R"]
        for i in range(0,4):
            if code[i] == tentative[i]:
                result[i] = "Noir"
            elif tentative[i] in code:
                result[i] = "Blanche"
            else:
                result[i] = "Rien"
        return result

    def genereCode(self):
        possibleColors = ["R", "G", "B", "Y", "O", "P"]
        c1 = random.choice(possibleColors)
        c2 = random.choice(possibleColors)
        c3 = random.choice(possibleColors)
        c4 = random.choice(possibleColors)
        return [c1, c2, c3, c4]
    
    def tentative(self):
        c1 = customInput("couleur 1? ")
        c2 = customInput("couleur 2? ")
        c3 = customInput("couleur 3? ")
        c4 = customInput("couleur 4? ")
        return [c1, c2, c3, c4]



def customInput(text): 
    possibleColors = ["R", "G", "B", "Y", "O", "P"]
    while True:
        val = input(text)
        if val in possibleColors:
            return val
        else:
            print('value should be in ["R", "G", "B", "Y", "O", "P"]')
            continue