set terminal pngcairo size 800,600
set output 'I2vsF_amb_errors.png'

# Títols i etiquetes
set ylabel "I^2 (A^2)"
set xlabel "Força (N)"
set key bottom right

# Establir els límits per als eixos
set xrange [0:0.0003]
# set yrange [10:80]
 

# Defineix la funció lineal f(x) = a*x + b
f(x) = a*x + b

# Ajusta la regressió lineal
fit f(x) "I2vsF.txt" using 1:2 via a, b

# Dibuixa la gràfica
plot "I2vsF.txt" using 1:2:3:4 with xyerrorbars title "Barres d'error", \
     f(x) with lines title "Regressió Lineal", \
     "I2vsF.txt" using 1:2 with points pt 7 ps 1 lc rgb 'blue' title "Intensitat al quadrat en funció de la força"
