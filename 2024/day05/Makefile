classname = utils

main: main.o $(classname).o
		g++ main.o $(classname).o -o main

main.o: main.cpp
		g++ -c main.cpp

$(classname).o: $(classname).h $(classname).cpp
		g++ -c $(classname).h $(classname).cpp

clean:
		rm main *.o *.gch
