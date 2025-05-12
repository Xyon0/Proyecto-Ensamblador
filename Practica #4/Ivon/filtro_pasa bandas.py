#parte 4 del código
# Función para aplicar el filtro pasa bandas
def apply_bandpass_filter(signal, lowcut=0.01, highcut=0.1, fs=1, order=4):
    b, a = butter(N=order, Wn=[lowcut, highcut], btype='band')
    return filtfilt(b, a, signal)

# Señales originales
viento = viento_df['Velocidad_Viento_mps'].values
temperatura = temperatura_df['Temperatura_C'].values
humedad = humedad_df['Humedad_Relativa_%'].values
tiempo = viento_df['Tiempo'].values  # Asumimos que todas tienen el mismo tiempo

# Filtrado
viento_filtrado = apply_bandpass_filter(viento)
temperatura_filtrada = apply_bandpass_filter(temperatura)
humedad_filtrada = apply_bandpass_filter(humedad)

# Graficar las tres señales
fig, axs = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

axs[0].plot(tiempo, viento, label='Original', alpha=0.5)
axs[0].plot(tiempo, viento_filtrado, label='Filtrada', linewidth=2)
axs[0].set_title('Velocidad del Viento')
axs[0].set_ylabel('m/s')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(tiempo, temperatura, label='Original', alpha=0.5)
axs[1].plot(tiempo, temperatura_filtrada, label='Filtrada', linewidth=2)
axs[1].set_title('Temperatura')
axs[1].set_ylabel('°C')
axs[1].legend()
axs[1].grid(True)

axs[2].plot(tiempo, humedad, label='Original', alpha=0.5)
axs[2].plot(tiempo, humedad_filtrada, label='Filtrada', linewidth=2)
axs[2].set_title('Humedad Relativa')
axs[2].set_ylabel('%')
axs[2].set_xlabel('Tiempo')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()
