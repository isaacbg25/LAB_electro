set terminal pngcairo size 800,600
set output 'FvsI_amb_errors.png'

# Títols i etiquetes
set xlabel "I (A^2)"
set ylabel "F (kg)"
set key bottom right

# Defineix la funció lineal f(x) = a*x + b
f(x) = a*x + b

# Ajusta la regressió lineal
fit f(x) "FvsI.txt" using 1:2 via a, b

# Dibuixa la gràfica
plot "I2vsm.txt" using 1:2:3:4 with xyerrorbars title "Barres d'error", \
     f(x) with lines title "Regressió Lineal", \
     "I2vsm.txt" using 1:2 with points pt 7 ps 1 lc rgb 'blue' title "Massa en funció de I al quadrat"
