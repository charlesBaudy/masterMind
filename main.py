from Jeu import Jeu

def main():
    jeu = Jeu()
    essai = 0
    maxEssais = 10

    code = jeu.genereCode()

    while(essai<maxEssais):
        print("essai n",essai+1)
        tentative = jeu.tentative()
        result = jeu.compare(code, tentative)
        print(result)
        if code == tentative:
            print("c'est gagné")
            return True
        else: 
            essai=essai+1
    
    print("c'est perdu")
    return False

main()        


