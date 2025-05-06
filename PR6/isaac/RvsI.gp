set terminal pngcairo size 800,600 font "Helvetica, 18"
set output 'regressio_1.png'

# Títols i etiquetes
#set title "Regressió lineal de x^2+y^2 vs 2y per diferents intencitats"
set xlabel "2y(m)"
set ylabel "x^2+y^2 (m²)"
set key top left  # Posició de la llegenda
set xrange [0:0.055]

# Defineix la funció lineal f(x) = a*x + b
f1(x) = a*x + b
f2(x) = c*x + d
f3(x)= a3*x + b3
f4(x)= a4*x + b4
f5(x)= a5*x + b5
f6(x)= a6*x + b6
f7(x)= a7*x + b7
f8(x)= a8*x + b8


# Ajusta la regressió lineal
fit f1(x) "RvsI.txt" index 0 using 1:2 via a, b
fit f2(x) "RvsI.txt" index 1 using 1:2 via c, d
fit f3(x) "RvsI.txt" index 2 using 1:2 via a3, b3
fit f4(x) "RvsI.txt" index 3 using 1:2 via a4, b4
fit f5(x) "RvsI.txt" index 4 using 1:2 via a5, b5
fit f6(x) "RvsI.txt" index 5 using 1:2 via a6, b6
fit f7(x) "RvsI.txt" index 6 using 1:2 via a7, b7
fit f8(x) "RvsI.txt" index 7 using 1:2 via a8, b8

#set label sprintf("Pendent 1: %.2f", a) at graph 0.70, 0.85 textcolor rgb "red"
#set label sprintf("Pendent 2: %.2f", c) at graph 0.70, 0.80 textcolor rgb "blue"

# Dibuixa la gràfica
plot "RvsI.txt" index 0 using 1:2 notitle, \
     "RvsI.txt" index 1 using 1:2 notitle, \
     "RvsI.txt" index 2 using 1:2 notitle, \
     "RvsI.txt" index 3 using 1:2 notitle, \
     "RvsI.txt" index 5 using 1:2 notitle, \
     "RvsI.txt" index 7 using 1:2 notitle, \
     f1(x) with lines title sprintf("I=0.1A, R= %.2fm", a),\
     f2(x) with lines title sprintf("I=0.2A, R= %.2fm", c),\
     f3(x) with lines title sprintf("I=0.3A, R= %.2fm", a3),\
     f4(x) with lines title sprintf("I=0.4A, R= %.2fm", a4),\
     f6(x) with lines title sprintf("I=0.6A, R= %.2fm", a6),\
     f8(x) with lines title sprintf("I=0.8A, R= %.2fm", a8)
     
     
