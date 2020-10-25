# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:50:04 2020

@author: Clément P
"""

from random import randint
comp = [[0,1,2],
        [2,1,0]]
d = []
wow = "wow"
def draft(l):
    global d
    
    for p in l:
        if 6 in p:
            d.append(6)
        elif 3 in p:
            d.append(3)
        elif 2 in p:
            d.append(2)
        elif 16 in p:
            d.append(16)
        elif 7 in p:
            d.append(7)
        else:
            d.append(p[0])
    return d
        


def tour_de_jeu(etat, memo):
    perso = etat.doitJouer.pid
    life =  [etat.equipes[0][i].vie  for i in range(len(etat.equipes[0])) if etat.equipes[0][i]]
    lifeA = [etat.equipes[1][i].vie for i in range(len(etat.equipes[1]))  if etat.equipes[1][i]]

    cibleA = lifeA.index(min(lifeA))
    spell = 0
    cible = 0
    
    if min(life) <= 1500:
        if perso in [2,6,8,16]: #Healers
            cible = life.index(min(life))
            spell = 1 * (perso == 2) + 1 * (perso == 16) + 1 * (perso == 16 and min(life) <= 1000)
            
            
    
        
        
    return cibleA,cible,spell,None


def prio(cap, tab):
    for i in tab:
        if cap[i].attente == 0:
            return i
    return 0
    

def PrStrydan(etat):
    tab = [2,1,0]
    cap = etat.doitJouer.capacites
    
    return prio(cap, tab), 2 #a définir entre 1,2,3

def CPE(etat):
    tab = [2,1,0]
    cap = etat.doitJouer.capacites
    return prio(cap, tab), None
            
def Proviseur(etat):
    tab = [1,2,0]
    cap = etat.doitJouer.capacites
    return prio(cap, tab), None

def Surdoue(etat):
    #tab = [1,2,0]
    cap = etat.doitJouer.capacites
    life =  [etat.equipes[0][i].vie  for i in range(len(etat.equipes[0])) if etat.equipes[0][i]]
    if min(life) > 1500 and cap[2].attente == 0:
        return 2, None
    else: #TODO /!\ les effets ne se cumulent pas
        return 1, None
        
    
def Cancre(etat):
    tab = [1,0,2]
    cap = etat.doitJouer.capacites
    return prio(cap, tab), None
    
def Geek(etat):
    tab = [1,2,0]
    cap = etat.doitJouer.capacites
    return prio(cap, tab), None  #cible de cap 2 a revoir 
    
def Matheux(etat):
    tab = [2,0,1]
    cap = etat.doitJouer.capacites
    return prio(cap, tab), None
    
def Chimiste(etat):
    tab = [2,0,1]
    cap = etat.doitJouer.capacites
    return prio(cap, tab), None  #Cible a revoir pour ne pas heal dans le vide
 
def Physicien(etat):
    return 0, None
    
def Machine(etat):
    tab = [2,1,0]
    cap = etat.doitJouer.capacites
    return prio(cap, tab)
   
def Sportif(etat):
    tab = [2,1,0]
    cap = etat.doitJouer.capacites
    return prio(cap, tab)
    
def Delegue(etat):
    tab = [2,1,0]
    cap = etat.doitJouer.capacites
    return prio(cap, tab) 

def PrLacience(etat):
    tab = [2,1,0]
    cap = etat.doitJouer.capacites
    return prio(cap, tab)
    
def PrDuspord(etat):
    tab = [2,1,0]
    cap = etat.doitJouer.capacites
    return prio(cap, tab)
    
def PrPhylou(etat):
    tab = [2,1,0]
    cap = etat.doitJouer.capacites
    return prio(cap, tab)

def Infirmier(etat): 
    tab = [2,1,0]
    cap = etat.doitJouer.capacites
    return prio(cap, tab)
 

    
    
# Penser a achever si possible plutot que de Heal
    
    
    
    
    
    
    
    
    
    


        
#res = Reseau()
#res.addNv(FCNiv(1,10))
#res.addNv(NiveauActivation(tanh, tanhp))
#res.addNv(FCNiv(3,1))
#res.addNv(NiveauActivation(tanh, tanhp))
#
#data = np.array([[[2]], [[3]], [[5]], [[4]], [[0]]])
#obj = np.array([[[4]], [[9]], [[25]], [[16]], [[0]]])
#
#res.perte(score, scoreP)
#res.train(data, obj, 10000, 0.1)
#
#out = res.pred(data)
#print(out)

        
    
        
