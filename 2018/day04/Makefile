
main: main.o Date.o Guard.o
		g++ main.o Date.o Guard.o -o main

main.o: main.cpp
		g++ -c main.cpp

Date.o: Date.cpp Date.h
		g++ -c Date.cpp

Guard.o: Guard.cpp Guard.h
		g++ -c Guard.cpp

clean:
		rm *.o main
