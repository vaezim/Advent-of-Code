
main: main.o wire.o
		g++ main.o wire.o -o main

main.o: main.cpp
		g++ -c main.cpp

wire.o: wire.cpp
		g++ -c wire.h wire.cpp

clean:
		rm *.o main *.gch
