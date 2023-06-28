classname = program

main: main.o $(classname).o
		g++ main.o $(classname).o -o main

main.o: main.cpp
		g++ -c main.cpp

$(classname).o: $(classname).cpp
		g++ -c $(classname).h $(classname).cpp

clean:
		rm *.o main *.gch
