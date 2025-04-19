set terminal pngcairo size 800,600
set output 'thetavsr_amb_errors.png'

# Títols i etiquetes
set xlabel "1/r (m^(-1))"
set ylabel "Angle (θ)"
set key bottom right

# Defineix la funció lineal f(x) = a*x + b
f(x) = a*x + b

# Ajusta la regressió lineal
fit f(x) "thetavsr.txt" using 1:2 via a, b

# Dibuixa la gràfica
plot "thetavsr.txt" using 1:2:3:4 with xyerrorbars title "Barres d'error", \
     f(x) with lines title "Regressió Lineal", \
     "thetavsr.txt" using 1:2 with points pt 7 ps 1 lc rgb 'blue' title "Angle en funció de la inversa de la distància de separació"
