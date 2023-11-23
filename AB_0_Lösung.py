import numpy as np

#Aufgabe 2.1
rand_uni = np.array(1)
rand_norm = np.random.rand(100)

sum_uni = np.sum(rand_uni) #Summe
sum_norm = np.sum(rand_norm) #Summe

mean_uni = np.mean(rand_uni) #Mittelwert
mean_norm = np.mean(rand_norm) #Mittelwert

var_uni = np.var(rand_uni) #Varianz 
var_norm = np.var(rand_norm) #Varianz

rand_mat = np.array([rand_uni, rand_norm])
rand_arr = np.append(rand_uni, rand_norm)

print(rand_mat)
print(rand_arr)