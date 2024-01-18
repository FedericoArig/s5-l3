#!/usr/bin/env python
# coding: utf-8

# In[1]:


nome_scuola = "Epicode"

for carattere in nome_scuola:
    print(carattere)


# In[ ]:


# Inizializza la variabile numero
numero = 0

# Utilizza un ciclo while per stampare i numeri da 0 a 20
while numero <= 20:
    print(numero)
    numero += 1


# In[3]:


# Utilizza un ciclo for per stampare i numeri da 0 a 20

numero = 0

for numero in range(21):
    print(numero)
    


# In[6]:


#Utilizza un ciclo for per calcolare e stampare le prime 10 potenze di 2

for esponente in range(11):
    risultato = 2** esponente
    print(f"2^{esponente}={risultato}")
    


# In[10]:


dizionario_auto ={
    "Ada":"Punto",
    "Ben":"Multipla",
    "Charlie":"Golf",
    "Debbie":"107"
}

print(dizionario_auto)
auto_Debbie=dizionario_auto["Debbie"]
print("\nauto_Debbie", "è la",auto_Debbie)


# In[20]:


dizionario_auto ={
    "Ada":"Punto",
    "Ben":"Multipla",
    "Charlie":"Golf",
    "Debbie":"107"
}
valore_da_escludere = "Multipla"
chiavi_da_escludere = [chiave for chiave,valore in dizionario_auto.items()if valore ==valore_da_escludere] #approfondire listcomprhension

for chiave in chiavi_da_escludere:
    del dizionario_auto[chiave]
    

print("Non sono una Multipla", dizionario_auto.values())


# In[23]:


dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"}
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"}#nuovi dati
dizionario_auto.update({"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"})#utilizziamo la funzione .update() per aggiornare il dizionario
print(dizionario_auto)#stampa del dizionario


# In[38]:


def trova_minimo_massimo(lista_numeri):
    if not lista_numeri:
        return None, None
#inizializzazione della funzione dal primo numero della lista, identificato con 0
minimo = massimo = lista_numeri[0]
#attraverso la funzione if in iteriamo gli elementi della lista per trovare il minimo e il massimo
for numero in "lista_numeri":
    if numero<minimo:
        minimo = numero
    elif numero> massimo:
        massimo = numero
return minimo, massimo
lista_numeri = [12,13,14,15,16,17,18]
minimo, massimo = trova_minimo_massimo(lista_di_numeri)
    print("Minimo:", minimo)
    print("Massimo:", massimo)



# In[ ]:




