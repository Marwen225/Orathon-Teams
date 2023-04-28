class Objet:
    def __init__(self,id, Poid, Valeur):
        self.id = id    #le numero du l'objet
        self.Poid = Poid #le poid du l'objet
        self.Valeur = Valeur  #la valeur du l'objet
        self.Rapport = Valeur/Poid  #le rapport Valeur / Poid du l'objet

def Sort(objets): #fonction pour trier les objects par rapport Valeur/Poid
    for i in range(len(objets)):
        for j in range(n-i-1):
            if objets[j].Rapport < objets[j+1].Rapport:
                objets[j],objets[j+1]=objets[j+1],objets[j]
    return objets

n = int(input('Nombre des objets: ')) #lire le nombre des objets
P = int(input('Capacity du sac: ')) #lire la capacity du sac a dos

objets=[] #creer une liste vide des objets

for i in range(n):
    poid= float(input(f"Poid de l'objet {i+1}: ")) #lire le poid de chaque objet
    valeur= float(input(f"Valeur de l'objet {i+1}: ")) #lire la valeur de chaque objet
    objet = Objet(i+1,poid,valeur) #varible de type Objet(class)
    objets.append(objet) #Pour ajouter un objet dans la liste objets

objets = Sort(objets) #Pour trier les objets
Pcons = 0 
x = {} 

for i in range(n):
    x.update(
        {
            f'Objet {objets[i].id}':1 if objets[i].Poid + Pcons <= P else 0
        }   #Pour ajouter l'objet dans X
    )
    if objets[i].Poid + Pcons <= P:
        Pcons += objets[i].Poid

print(x)#Afficher la resultat
