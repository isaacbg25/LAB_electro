set terminal pngcairo size 800,600 font "Helvetica, 18"
set output 'RvsVa.png'

# Títols i etiquetes
#set title "R^2 en funció de Va"
set xlabel "Va (V)"
set ylabel "R^2 (m^2)"
set key top left

# Defineix la funció lineal f(x) = a*x + b
f(x) = a*x + b

# Ajusta la regressió lineal
fit f(x) "taulaRvsVa.txt" using 1:2 via a, b

# Dibuixa la gràfica
plot "taulaRvsVa.txt" using 1:2:3:4 with xyerrorbars title "Dades amb error", \
     f(x) with lines title "Regressió Lineal"
