import random
from PIL import Image
import numpy as np
from math import *
from matplotlib import pyplot as plt



def construction(nbr):
    Monde = [[0 for i in range (20)] for j in range (20)]
    Obstacle = [[random.randint(0,19) for j in range (2)] for i in range (nbr)]
    Random = 1
    for elts in Obstacle:
        Monde[elts[0]][elts[1]]=20
    for k in range (nbr):
        Random = random.randint(0,1)
        Autour = [[0,1],[-1,0],[0,-1],[1,0]]
        for elt in Autour:
            Random = random.randint(-2,2)
            while Random>=1:
                Random = random.randint(-2,2)
                try:
                    Monde[Obstacle[k][0]+elt[0]][Obstacle[k][1]+elt[1]]=20
                    if elt[0]==1:
                        elt[0]+=1
                    else:
                        elt[1]+=1
                except IndexError:
                    pass
    Visuel([Monde,0,Monde],0)

def InitialisationAleatoire(n,m):      #n = taille monde §§ m = nombre robot // nbr = nombre d'obstacle
    M = [[0 for i in range (n)] for j in range (n)]
    Mbis = [[0 for i in range (n)] for j in range (n)]
    Position = [[random.randint(0,n-1),random.randint(0,n-1)] for i in range (m)]
    for i in range (m):
        M[Position[i][0]][Position[i][1]] = 1
        Mbis[Position[i][0]][Position[i][1]] = -4
    i,j = random.randint(0,n-1), random.randint(0,n-1)
    Mbis[i][j] = 30
    return M,Position,Mbis

def InitialisationTest(n,z,nbr):
    M = [[0 for i in range (n)] for j in range (n)]
    Mbis = [[0 for i in range (n)] for j in range (n)]
    i,j =  int(n/2), n-1
    k,l =  int(n/2), 1
    Obstacle = [[0 for j in range (2)] for o in range (nbr)]
    for m in range (5):
        Obstacle[m][0],Obstacle[m][1] = int(n/2)-3,m
        Obstacle[m+5][0],Obstacle[m+5][1] = int(n/2)+3,m
        Obstacle[m+10][0],Obstacle[m+10][1] = int(n/2)-3,n-m-1
        Obstacle[m+15][0],Obstacle[m+15][1] = int(n/2)+3,n-m-1
        Obstacle[m+20][0],Obstacle[m+20][1] = int(n/2)-3-m, 5
        Obstacle[m+25][0],Obstacle[m+25][1] = int(n/2)-3-m, n-5-1
        Obstacle[m+30][0],Obstacle[m+30][1] = int(n/2)-3-m-5, 5
        Obstacle[m+35][0],Obstacle[m+35][1] = int(n/2)-3-m-5, n-5-1
        Obstacle[m+40][0],Obstacle[m+40][1] = int(n/2)+3+5, 5+m+5
        Obstacle[m+45][0],Obstacle[m+45][1] = int(n/2)+3+5, n-5-1-m-5
        Obstacle[m+50][0],Obstacle[m+50][1] = int(n/2)+3+m, 5+m
        Obstacle[m+55][0],Obstacle[m+55][1] = int(n/2)+3+m, n-5-1-m
        Obstacle[m+160][0],Obstacle[m+160][1] = int(n/2)-2+1-13, 5+4+m+2
        Obstacle[m+165][0],Obstacle[m+165][1] = int(n/2)-2+1-13, n-5-1-4-m-2
    for m in range (13):
        Obstacle[m+90][0],Obstacle[m+90][1] = int(n/2)-m+1, 5+4
        Obstacle[m+106][0],Obstacle[m+106][1] = int(n/2)-m+1, n-5-1-4
    for m in range (4):
        Obstacle[m+70][0],Obstacle[m+70][1] = int(n/2)+3, 5+m+6
        Obstacle[m+75][0],Obstacle[m+75][1] = int(n/2)+3, n-5-1-m-6
    for m in range (3):
        Obstacle[m+60][0],Obstacle[m+60][1] = int(n/2)-3-10-m, n-6-m
        Obstacle[m+65][0],Obstacle[m+65][1] = int(n/2)-3-10-m, 5+m
    for m in range (2):
        Obstacle[m+80][0],Obstacle[m+80][1] = int(n/2)+m+1, 5+m+4
        Obstacle[m+85][0],Obstacle[m+85][1] = int(n/2)+m+1, n-5-1-m-4
        Obstacle[m+150][0],Obstacle[m+150][1] = int(n/2)-m+1-13, 5+4+m
        Obstacle[m+155][0],Obstacle[m+155][1] = int(n/2)-m+1-13, n-5-1-4-m
    for o in range (nbr):
        M[Obstacle[o][0]][Obstacle[o][1]]=20
    Mbis[i][j] = 30
    Mbis[k][l] = -4
    M[k][l] = 1
    Visuel([M,0,Mbis],0)
    Position = [[k,l] for p in range (z)]
    return M, Position, Mbis,z



def Initialisation(n,m,nbr):
    M = [[0 for i in range (n)] for j in range (n)]
    Mbis = [[0 for i in range (n)] for j in range (n)]
    i,j = random.randint(0,n-1), random.randint(0,n-1)
    k,l = random.randint(0,n-1), random.randint(0,n-1)
    Obstacle = [[random.randint(0,n-1) for j in range (2)] for o in range (nbr)]        #Virgule remplacé par deux éléments
    while k==i and l==j:
        k, l = random.randint(0,n-1), random.randint(0,n-1)
    for o in range (nbr):
        while Obstacle[o][0]==i or Obstacle[o][0]==k or Obstacle[o][1]==j or Obstacle[o][1]==l:
            Obstacle[o] = [random.randint(0,n-1),random.randint(0,n-1)]
        M[Obstacle[o][0]][Obstacle[o][1]]=20
    Random = 1
    for elts in Obstacle:
        M[elts[0]][elts[1]]=20
    for q in range (nbr):
        Random = random.randint(0,1)
        Autour = [[0,1],[-1,0],[0,-1],[1,0]]
        for elt in Autour:
            Random = random.randint(0,1)
            while Random>=1:
                Random = random.randint(0,1)
                try:
                    if Mbis[Obstacle[q][0]+elt[0]][Obstacle[q][1]+elt[1]]==0:
                        M[Obstacle[q][0]+elt[0]][Obstacle[q][1]+elt[1]]=20
                        if elt[0]==1:
                            elt[0]+=1
                        else:
                            elt[1]+=1
                except IndexError:
                    pass
    Mbis[i][j] = 30
    Mbis[k][l] = -4
    M[k][l] = 1
    Position = [[k,l] for p in range (m)]
    return M,Position,Mbis,m



def deplacementAlt(monde, nbr,MODE):                                            #Dépend du type d emouvement qu'on veut au départ
    mode = [0 for i in range (nbr)]                                             #Défini les mouvements : 0 recherche, 1 a trouvé (et retourne base), 2 va source
    k = [0 for i in range(nbr)]
    nbr_robot=monde[3]
    n = len(monde[0])
    M = monde[0]
    Mbis = monde[2]
    Position = monde[1]
    if MODE ==0:
        Orientation = [[random.randint(1,4)] for i in range (nbr_robot)]            ## 1 = D, 2 = H, 3 = G, 4 = B
    else:
        Orientation = [[1] for i in range (nbr_robot)]
    chemin = [[[Position[i][0],Position[i][1]]] for i in range (nbr_robot)]
    for j in range(nbr):
        Visuel([M,0,Mbis],j)
        for i in range (nbr_robot):
            if mode[i] ==0:
                Rotation = random.randint(-4,4)
                if Rotation<=-2 or Rotation>=2:
                    Rotation = 0
                if not(Rotation==0):
                    Orientation[i].append((Orientation[i][-1]+Rotation)%4)
                else:
                    if Orientation[i][-1] == 1:
                        if n>Position[i][1]+1 and not(M[Position[i][0]][Position[i][1]+1]==20):
                            M[Position[i][0]][Position[i][1]] = 0
                            M[Position[i][0]][Position[i][1]+1] = 1
                            chemin[i].append([Position[i][0],Position[i][1]+1])
                            Position[i][1]+=1
                        elif n>Position[i][1]+1:
                            Orientation[i].append(random.choice([2,3,3,4]))
                        else:
                            Orientation[i].append(random.choice([2,4]))           #On le biaise pas pour aller en arrière (encourage l'explo)
                    elif Orientation[i][-1] == 2:
                        if n>Position[i][0]+1 and not(M[Position[i][0]+1][Position[i][1]]==20):
                            M[Position[i][0]][Position[i][1]] = 0
                            M[Position[i][0]+1][Position[i][1]] = 1
                            chemin[i].append([Position[i][0]+1,Position[i][1]])
                            Position[i][0]+=1
                        elif n>Position[i][0]+1:
                            Orientation[i].append(random.choice([1,4,3,4]))
                        else:
                            Orientation[i].append(random.choice([1,4]))
                    elif Orientation[i][-1] == 3:
                        if 0<Position[i][1]-1 and not(M[Position[i][0]][Position[i][1]-1]==20):
                            M[Position[i][0]][Position[i][1]] = 0
                            M[Position[i][0]][Position[i][1]-1] = 1
                            chemin[i].append([Position[i][0],Position[i][1]-1])
                            Position[i][1]-=1
                        elif 0<Position[i][1]-1:
                            Orientation[i].append(random.choice([2,1,1,4]))
                        else:
                            Orientation[i].append(random.choice([2,4]))
                    elif Orientation[i][-1] == 4:
                        if 0<Position[i][0]-1 and not(M[Position[i][0]-1][Position[i][1]]==20):
                            M[Position[i][0]][Position[i][1]] = 0
                            M[Position[i][0]-1][Position[i][1]] = 1
                            chemin[i].append([Position[i][0]-1,Position[i][1]])
                            Position[i][0]-=1
                        elif 0<Position[i][0]-1:
                            Orientation[i].append(random.choice([2,1,2,3]))
                        else:
                            Orientation[i].append(random.choice([1,3]))
                    if entourage(Position[i][0],Position[i][1],monde[2])[0]:
                        if entourage(Position[i][0],Position[i][1],Mbis)[1]==30:
                            mode[i]=1
                            k[i] = len(chemin[i])-1
                        elif entourage(Position[i][0],Position[i][1],monde[2])[1]==-4:
                            nada ="nada"          #Si repasse par base, on reset son chemin (pose problème pour mode 3 plus est inutile)
                        else:
                            mode[i] = 2
                    if len(chemin[i])>1:
                        if Mbis[Position[i][0]][Position[i][1]]==-4:
                            chemin[i] = [[Position[0][0],Position[0][1]]]
            elif mode[i] == 1:
                if k[i]==0:
                    mode[i]=2
                else:
                    if Mbis[chemin[i][k[i]][0]][chemin[i][k[i]][1]]==0:
                        Mbis[chemin[i][k[i]][0]][chemin[i][k[i]][1]] = log((atan(5*k[i]+pi/2)/pi)+1)
                    Position[i][0] = chemin[i][k[i]][0]
                    Position[i][1] = chemin[i][k[i]][1]
                    M[chemin[i][k[i]][0]][chemin[i][k[i]][1]] = 0
                    print("mouv1")
                    k[i]-=1
                    M[chemin[i][k[i]][0]][chemin[i][k[i]][1]] = 1
            elif mode[i]==2:
                max = -1
                Mouvement=[0,0]
                if Position[i][1]<n-1:                                                 #Reste ne sera jamais négatif, bon !
                    if Mbis[Position[i][0]][Position[i][1]+1]>max:
                        max = Mbis[Position[i][0]][Position[i][1]+1]
                        Mouvement = [0,1]
                if Position[i][0]<n-1:
                    if Mbis[Position[i][0]+1][Position[i][1]]>max:
                        max = Mbis[Position[i][0]+1][Position[i][1]]
                        Mouvement = [1,0]
                if Position[i][0]>0:
                    if Mbis[Position[i][0]-1][Position[i][1]]>max:
                        max = Mbis[Position[i][0]-1][Position[i][1]]
                        Mouvement = [-1,0]
                if Position[i][1]>0:
                    if Mbis[Position[i][0]][Position[i][1]-1]>max:
                        max = Mbis[Position[i][0]][Position[i][1]-1]
                        Mouvement = [0,-1]
                try:
                    if Mbis[Position[i][0]][Position[i][1]]==30:
                        mode[i]=3
                except IndexError:
                    pass
                try:
                    if Mbis[Position[i][0]+1][Position[i][1]]==30:
                        mode[i]=3
                except IndexError:
                    pass
                try:
                    if Mbis[Position[i][0]-1][Position[i][1]]==30:
                        mode[i]=3
                except IndexError:
                    pass
                try:
                    if Mbis[Position[i][0]][Position[i][1]+1]==30:
                        mode[i]=3
                except IndexError:
                    pass
                try:
                    if Mbis[Position[i][0]][Position[i][1]-1]==30:
                        mode[i]=3
                except IndexError:
                    pass

                if mode[i]==2:
                    M[Position[i][0]][Position[i][1]] = 0                             #Valeur de départ pour la fonction qui calcule l'intensité des phéromones
                    Position[i][0]+=Mouvement[0]
                    Position[i][1]+=Mouvement[1]
                    M[Position[i][0]][Position[i][1]] = 1
            elif mode[i]==3:
                Mouvement=[0,0]
                Mbis[Position[i][0]][Position[i][1]]=log(exp(Mbis[Position[i][0]][Position[i][1]])+(atan(5*k[i]+pi/2)/pi)+1)
                min = 35000                                                     #Ne devrait jamais être aussi grand (inshalla)
                if Position[i][1]<n-1:
                    if Mbis[Position[i][0]][Position[i][1]+1]<min and not(Mbis[Position[i][0]][Position[i][1]+1]==0):
                        min = Mbis[Position[i][0]][Position[i][1]+1]
                        Mouvement = [0,1]
                if Position[i][0]<n-1:
                    if Mbis[Position[i][0]+1][Position[i][1]]<min and not(Mbis[Position[i][0]+1][Position[i][1]]==0):
                        min = Mbis[Position[i][0]+1][Position[i][1]]
                        Mouvement = [1,0]
                if Position[i][0]>0:
                    if Mbis[Position[i][0]-1][Position[i][1]]<min and not(Mbis[Position[i][0]-1][Position[i][1]]==0):
                        min = Mbis[Position[i][0]-1][Position[i][1]]
                        Mouvement = [-1,0]
                if Position[i][1]>0:
                    if Mbis[Position[i][0]][Position[i][1]-1]<min and not(Mbis[Position[i][0]][Position[i][1]-1]==0):
                        min = Mbis[Position[i][0]][Position[i][1]-1]
                        Mouvement = [0,-1]
                try:
                    if Mbis[Position[i][0]][Position[i][1]]==-4:
                        mode[i]=2
                except IndexError:
                    pass
                try:
                    if Mbis[Position[i][0]+1][Position[i][1]]==-4:
                        mode[i]=2
                except IndexError:
                    pass
                try:
                    if Mbis[Position[i][0]-1][Position[i][1]]==-4:
                        mode[i]=2
                except IndexError:
                    pass
                try:
                    if Mbis[Position[i][0]][Position[i][1]+1]==-4:
                        mode[i]=2
                except IndexError:
                    pass
                try:
                    if Mbis[Position[i][0]][Position[i][1]-1]==-4:
                        mode[i]=2
                except IndexError:
                    pass
                if mode[i]==3:
                    M[Position[i][0]][Position[i][1]] = 0
                    Position[i][0]+=Mouvement[0]
                    Position[i][1]+=Mouvement[1]
                    M[Position[i][0]][Position[i][1]] = 1
    Visuel([M,0,Mbis],nbr)



                                                                             #k note où le robot (i) en est sur son itinéraire retour (ou aller)
def Visuel(monde,m):
    Timg = np.zeros((len(monde[0]),len(monde[0][0]),3))
    for i in range (len(monde[0])):
        for j in range (len(monde[0][0])):
            if monde[0][i][j]==0:
                Timg[i][j][0],Timg[i][j][1],Timg[i][j][2] = 255,255,255
            if not(10*monde[2][i][j]-10*int(monde[2][i][j])==0):
                Timg[i][j][0],Timg[i][j][1],Timg[i][j][2] = 0,0.4*monde[2][i][j],226
            if monde[0][i][j]==1:
                Timg[i][j][0],Timg[i][j][1],Timg[i][j][2] = 0,0,0
            if monde[2][i][j]==30:
                Timg[i][j][0],Timg[i][j][1],Timg[i][j][2] = 138,43,226
            if monde[2][i][j]==-4:
                Timg[i][j][0],Timg[i][j][1],Timg[i][j][2] = 255,0,226
            if monde[0][i][j]==20:
                Timg[i][j][0],Timg[i][j][1],Timg[i][j][2] = 130,103,77
    Img = Image.fromarray(Timg.astype(np.uint8))
    Img = Img.resize((Timg.shape[0]*50,Timg.shape[1]*50))
    image = "Image"+str(m)
    Img.save("E:/TIPE BIS/Image/%s.png"%image)



def entourage(i,j,Mbi):
    n = len(Mbi)
    pos = [[-1,0],[0,-1],[0,1],[1,0]]
    for k in range (4):
        if i+pos[k][0]>n-1 or 1>i+pos[k][0]:
            pos[k][0]=0
        if j+pos[k][1]>n-1 or 1>j+pos[k][1]:
            pos[k][1]=0
        if not(Mbi[i+pos[k][0]][j+pos[k][1]]==0):
            return True, Mbi[i+pos[k][0]][j+pos[k][1]]
    return False,0