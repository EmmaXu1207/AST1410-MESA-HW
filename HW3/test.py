import numpy as np
import matplotlib.pyplot as plt
import mesa_reader as mr

#read in the files
logs02 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/0.2mass/LOGS")
logs05= mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/0.5mass/LOGS")
logs1 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/1mass/LOGS")
logs3 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/3mass/LOGS")
logs5 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/5mass/LOGS")
logs10 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/10mass/LOGS")
logs15 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/15mass/LOGS")
logs30 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/30mass/LOGS")
logs70 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/70mass/LOGS")

#select detailed data
history02 = logs02.history
history05 = logs05.history
history1 = logs1.history
history3 = logs3.history
history5 = logs5.history
history10 = logs10.history
history15 = logs15.history
history30 = logs30.history
history70 = logs70.history

cmap = plt.get_cmap('plasma')
color = [cmap(i) for i in np.linspace(0, 1, 9)]
plt.plot(history02.log_Teff,history02.log_L,label='0.2$M_\odot$',color=color[0])
plt.plot(history05.log_Teff,history05.log_L,label='0.5$M_\odot$',color=color[1])
plt.plot(history1.log_Teff,history1.log_L,label='1$M_\odot$',color=color[2])
plt.plot(history3.log_Teff,history3.log_L,label='3$M_\odot$',color=color[3])
plt.plot(history5.log_Teff,history5.log_L,label='5$M_\odot$',color=color[4])
plt.plot(history10.log_Teff,history10.log_L,label='10$M_\odot$',color=color[5])
plt.plot(history15.log_Teff,history15.log_L,label='15$M_\odot$',color=color[6])
plt.plot(history30.log_Teff,history30.log_L,label='30$M_\odot$',color=color[7])
plt.plot(history70.log_Teff,history70.log_L,label='70$M_\odot$',color=color[8])

iso_teff = []
iso_L = []
target_age = 1e8
all_histories = [history02,history05,history1,history3,history5,history10,history15,history30,history70,]
for history in all_histories:
    ages = history.star_age
    idx = np.argmin(np.abs(ages - target_age))
    iso_teff.append(history.log_Teff[idx])
    iso_L.append(history.log_L[idx])

plt.plot(iso_teff, iso_L, 'o-',color='red',alpha=0.3,zorder=-1,label='age=1e8yr')
plt.gca().invert_xaxis()
plt.xlabel("log(Teff) [K]")
plt.ylabel("log(L/Lsun)")
plt.title("HR diagram: isochrones")
plt.legend()
plt.grid(True)
plt.savefig('comparison')



plt.figure()
age = [history02.star_age[-1],history05.star_age[-1],history1.star_age[-1],history3.star_age[-1],
       history5.star_age[-1],history10.star_age[-1],history15.star_age[-1],history30.star_age[-1],history70.star_age[-1]]

turn_off_mass = [0.2,0.5,1,3,5,10,15,30,70]
plt.scatter(age,turn_off_mass)
log_age = np.log10(age[1:])
log_mass = np.log10(turn_off_mass[1:])
coeff = np.polyfit(log_age, log_mass ,1)
# coeff = np.polyfit(age, turn_off_mass ,1)
a = coeff[0]
b = coeff[1]
print("log(M) =", a, "* log(age) +", b)
log_age1 = np.log10(age)
print(log_age1)
fit_mass = 10**(a*log_age1 + b)
# fit_mass = 10**(a*np.array(age) + b)
plt.plot(age,fit_mass,linestyle='--',label=fr'$M \propto age^{{{a:.3f}}}$')
plt.ylabel('Turn off mass [$M_\odot$]')
plt.xlabel('Age')
plt.xscale('log')
plt.title('Turn off mass as a function of age')
plt.grid(True)
plt.legend()
plt.savefig('age-mass')


plt.show()