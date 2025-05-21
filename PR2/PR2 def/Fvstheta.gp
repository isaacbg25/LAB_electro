set terminal pngcairo size 800,600
set output 'Fvstheta_amb_errors.png'

# Títols i etiquetes
set xlabel "Angle (θ)"
set ylabel "Força (N)"
set key bottom right

# Establir els límits per als eixos
set xrange [10:80]
set yrange [0:0.0003]

# Defineix la funció lineal f(x) = a*x + b
f(x) = a*x + b

# Ajusta la regressió lineal
fit f(x) "Fvstheta.txt" using 1:2 via a, b

# Dibuixa la gràfica
plot "Fvstheta.txt" using 1:2:3:4 with xyerrorbars title "Barres d'error", \
     f(x) with lines title "Regressió Lineal", \
     "Fvstheta.txt" using 1:2 with points pt 7 ps 1 lc rgb 'blue' title "Força en funció de l'angle"
