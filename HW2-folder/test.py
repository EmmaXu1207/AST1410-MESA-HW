import numpy as np
import matplotlib.pyplot as plt
import mesa_reader as mr


logs1 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/HW2-1/LOGS")
logs2 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/tutorial/LOGS")
logs4 = mr.MesaLogDir("/Users/emmaxu/Desktop/AST1410/mesa-25.12.1/HW2-4/LOGS")
history1 = logs1.history
history2 = logs2.history
history4 = logs4.history

profile1 = logs1.profile_data(model_number=-1)
profile2 = logs2.profile_data(model_number=-1)
profile4 = logs4.profile_data(model_number=-1)

Teff1 = history1.log_Teff
Lum1  = history1.log_L
density1 = profile1.Rho
pressure1 = profile1.P
central_temp1 = profile1.T

Teff2 = history2.log_Teff
Lum2  = history2.log_L
density2 = profile2.Rho
pressure2 = profile2.P
central_temp2 = profile2.T

Teff4 = history4.log_Teff
Lum4  = history4.log_L
density4 = profile4.Rho
pressure4 = profile4.P
central_temp4 = profile4.T

# print(pressure1 == pressure2)

# HR diagram
plt.figure(figsize=(7,6))
plt.plot(Teff1, Lum1, label="alpha=1", color='blue')
plt.plot(Teff2, Lum2, label="alpha=2", color='orange')
plt.plot(Teff4, Lum4, label="alpha=4", color='red')
plt.gca().invert_xaxis()  # HR diagram Teff 从高到低
plt.xlabel("log(Teff) [K]")
plt.ylabel("log(L/Lsun)")
plt.title("HR diagram: effect of mixing length alpha")
plt.legend()
plt.grid(True)
plt.savefig('comparison')

#density vs. tempature
plt.figure()
plt.plot(density1, central_temp1,label='alpha=1',color='blue')
plt.plot(density2, central_temp2,label='alpha=2',color='orange')
plt.plot(density4, central_temp4,label='alpha=4',color='red')
# plt.plot(density1, central_temp1,label='alpha=1',color='blue')
# plt.yscale('log')
# plt.xscale('log')
plt.xlabel(r"$\rho\ [\mathrm{g/cm}^3]$")
plt.ylabel(r"$\log_{10}(T_{\mathrm{eff}})\ \mathrm{[K]}$")
plt.legend()
plt.savefig('density-temperature')

#density vs. pressure
plt.figure()
plt.plot(density1,pressure1,label='alpha=1',color='blue')
plt.plot(density2,pressure2,label='alpha=2',color='orange')
plt.plot(density4,pressure4,label='alpha=4',color='red')
plt.xlabel(r"$\rho\ [\mathrm{g/cm}^3]$")
plt.ylabel(r"$P\ [\mathrm{dyn/cm^2}]$")
plt.legend()
plt.savefig('density-pressure')






fig,ax = plt.subplots(1,3,figsize=(12,4))
ax[0].plot(Teff1, Lum1, label="alpha=1", color='blue')
ax[0].plot(Teff2, Lum2, label="alpha=2", color='orange')
ax[0].plot(Teff4, Lum4, label="alpha=4", color='red')
ax[0].invert_xaxis()
ax[0].set_xlabel(r"$\log_{10}(T_{\mathrm{eff}})\ \mathrm{[K]}$")
ax[0].set_ylabel(r"$\log_{10}(L)\ [L_\odot]$")
ax[0].set_title("HR diagram")
ax[0].legend()
ax[0].grid(True)

ax[1].plot(density1, central_temp1,label='alpha=1',color='blue')
ax[1].plot(density2, central_temp2,label='alpha=2',color='orange')
ax[1].plot(density4, central_temp4,label='alpha=4',color='red')
# ax[1].set_yscale('log')
# ax[1].set_xscale('log')
ax[1].set_xlabel(r"$\rho\ [\mathrm{g/cm}^3]$")
ax[1].set_ylabel(r"$T_{\mathrm{eff}}\ \mathrm{[K]}$")
ax[1].set_title(r"$T_{\mathrm{eff}} (\rho)$")
ax[1].grid()
ax[1].legend()

ax[2].plot(density1,pressure1,label='alpha=1',color='blue')
ax[2].plot(density2,pressure2,label='alpha=2',color='orange')
ax[2].plot(density4,pressure4,label='alpha=4',color='red')
ax[2].set_xlabel(r"$\rho\ [\mathrm{g/cm}^3]$")
ax[2].set_ylabel(r"$P\ [\mathrm{dyn/cm^2}]$")
ax[2].set_title(r"$P(\rho)$")
ax[2].grid()
ax[2].legend()
plt.tight_layout()
plt.savefig('mixing_length_alpha')

plt.show()
