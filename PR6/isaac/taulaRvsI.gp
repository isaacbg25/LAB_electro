set terminal pngcairo size 800,600 font "Helvetica, 18"
set output 'RvsI.png'

# Títols i etiquetes
#set title "R en funció de 1/I"
set xlabel "1/I (1/A)"
set ylabel "R (m)"
set key top left

# Defineix la funció lineal f(x) = a*x + b
f(x) = a*x + b

# Ajusta la regressió lineal
fit f(x) "taulaRvsI.txt" using 1:2 via a, b

# Dibuixa la gràfica
plot "taulaRvsI.txt" using 1:2:3:4 with xyerrorbars title "Dades amb error", \
     f(x) with lines title "Regressió Lineal"
