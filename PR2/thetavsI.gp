set terminal pngcairo size 800,600
set output 'thetavsI_amb_errors.png'

# Títols i etiquetes
set xlabel "Intensitat (A)"
set ylabel "Angle (θ)"
set key bottom right

# Defineix la funció lineal f(x) = a*x + b
f(x) = a*x + b

# Ajusta la regressió lineal
fit f(x) "thetavsI.txt" using 1:2 via a, b

# Dibuixa la gràfica
plot "thetavsI.txt" using 1:2:3:4 with xyerrorbars title "Barres d'error", \
     f(x) with lines title "Regressió Lineal", \
     "thetavsI.txt" using 1:2 with points pt 7 ps 1 lc rgb 'blue' title "Angle en funció de la Intensitat de corrent"
