
main: main.o planet.o
		g++ main.o planet.o -o main

main.o: main.cpp
		g++ -c main.cpp

planet.o: planet.cpp
		g++ -c planet.cpp

clean:
		rm *.o main
