import mesa_reader as mr
import matplotlib.pyplot as plt

# A simple plotting script for MESA data with mesa_reader
# mesa_reader offers a lot of functionality!
# Check out the documentation at:
# https://billwolf.space/py_mesa_reader/

# Specify the directory containing MESA logs
logs = mr.MesaLogDir("LOGS")

# Read the history and profile data
history = logs.history
profile = logs.profile_data(model_number=-1)  # -1 for the last model

# Make an HR diagram from the history data
plt.figure()
plt.plot(history.log_Teff, history.log_L)
plt.xlabel(r"$\log_{10}(T_{\mathrm{eff}})\ \mathrm{[K]}$")
plt.ylabel(r"$\log_{10}(L)\ [L_\odot]$")
plt.gca().invert_xaxis()
plt.savefig('log_Teff-log_L')

# Plot the density profile as a function of the mass coordinate
plt.figure()
plt.plot(profile.mass, profile.Rho)
plt.xlabel(r"$M(r)\ [M_\odot]$")
plt.ylabel(r"$\rho\ [\mathrm{g/cm}^3]$")
plt.yscale("log")
plt.savefig('Mass-density')

plt.figure()
plt.plot(profile.Rho, profile.T)
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r"$\rho\ [\mathrm{g/cm}^3]$")
plt.ylabel(r"$\log_{10}(T_{\mathrm{eff}})\ \mathrm{[K]}$")
plt.savefig('density-temperature')

plt.figure()
plt.plot(profile.Rho,profile.P)
plt.xlabel(r"$\rho\ [\mathrm{g/cm}^3]$")
plt.ylabel(r"$P\ [\mathrm{dyn/cm^2}]$")
plt.savefig('density-pressure')

fig,ax=plt.subplots(1,3,figsize=(12,4))
ax[0].plot(history.log_Teff,history.log_L)
ax[0].set_xlabel(r"$\log_{10}(T_{\mathrm{eff}})\ \mathrm{[K]}$")
ax[0].set_ylabel(r"$\log_{10}(L)\ [L_\odot]$")
ax[0].set_title('HR diagram')
ax[0].grid()
ax[0].invert_xaxis()
ax[1].plot(profile.Rho, profile.T)
ax[1].set_xlabel(r"$\rho\ [\mathrm{g/cm}^3]$")
ax[1].set_ylabel(r"$T\ \mathrm{[K]}$")
ax[1].set_title(r'$T(\rho)$')
ax[1].grid()
ax[2].plot(profile.Rho, profile.P)
ax[2].set_xlabel(r"$\rho\ [\mathrm{g/cm}^3]$")
ax[2].set_ylabel(r"$P\ [\mathrm{dyn/cm^2}]$")
ax[2].set_title(r"$P(\rho)$")
ax[2].grid()
plt.tight_layout()
plt.savefig('mixing_length=2')
# Show plots
plt.show()
