hw01-q5-application: src/hw01-q5-application.o
	g++ src/hw01-q5-application.o -o hw01-q5-application 

hw01-q5-application.o: src/hw01-q5-application.cpp
	g++ -c src/hw01-q5-application.cpp src/hw01-q5-application.o

clean:
	rm *.o


