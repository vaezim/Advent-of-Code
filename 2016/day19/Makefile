filename = linked_elves

main: main.o $(filename).o
		g++ main.o $(filename).o -o main

main.o: main.cpp
		g++ -c main.cpp

$(filename).o: $(filename).cpp
		g++ -c $(filename).h $(filename).cpp

clean:
		rm *.o main *.gch
