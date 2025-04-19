set terminal pngcairo size 800,600
set output 'I2vsm_amb_errors.png'

# Títols i etiquetes
set xlabel "I2"
set ylabel "m"

# Defineix la funció lineal f(x) = a*x + b
f(x) = a*x + b

# Ajusta la regressió lineal
fit f(x) "I2vsm.txt" using 1:2 via a, b

# Dibuixa la gràfica
plot "I2vsm.txt" using 1:2:3:4 with xyerrorbars title "I2vsm", \
     f(x) with lines title "Regressió Lineal de I2vsm", \
     "I2vsm.txt" using 1:2 with points

