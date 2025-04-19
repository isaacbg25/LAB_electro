set terminal pngcairo size 800,600
set output 'I^2vsm_amb_errors.png'

# Títols i etiquetes
set xlabel "I^2"
set ylabel "m"

# Defineix la funció lineal f(x) = a*x + b
f(x) = a*x + b

# Ajusta la regressió lineal
fit f(x) "I^2vsm20.txt" using 1:2 via a, b

# Dibuixa la gràfica
plot "I^2vsm.txt" using 1:2:3:4 with yerrorbars title "I^2vsm", \
     f(x) with lines title "Regressió Lineal de I^2vsm"
