set terminal pngcairo size 800,600
set output 'regressio_amb_errors.png'

# Títols i etiquetes
set title "Regressió Lineal amb Barres d'Error"
set xlabel "X"
set ylabel "Y"

# Defineix la funció lineal f(x) = a*x + b
f(x) = a*x + b

# Ajusta la regressió lineal
fit f(x) "dades.txt" using 1:2:3 via a, b

# Dibuixa la gràfica
plot "dades.txt" using 1:2:3 with yerrorbars title "Dades amb error", \
     f(x) with lines title "Regressió Lineal"
