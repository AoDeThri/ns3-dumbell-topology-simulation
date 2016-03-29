set terminal png size 1200,1000
set output 'cwnd.png'
plot 'cwnd.dat' using 1:2 title 'Congestion Window' with linespoints
exit
