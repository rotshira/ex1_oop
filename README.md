# ex1_oop-Assignment

//a background exlenation
in this assignment we are going to create an off-line algorithm for smart elevators.
the system is assign elevator to a call in the same way of the call.
that how we will save some time for each call till it will complete.'

//Smart elevator:
The computer centralizes all the readings and decides which elevator will reach which reading in the shortest time.
(Perhaps on the basis of calculating the average time for an elevator to rise from floor to floor).
Maybe go to the nearest floor (very short waiting time). It is important that every customer would answer at the end.
Another way is to walk to the nearest floor at a time and walk in the same direction to make sure all the passenger calls are completed.
The algorithm can be improved by stopping it on the highest floor that has a reading. (Then going down instead of going up to the top).
You can set preferred floors for stopping or analyze which floor has the most average entrances and set it as preferred.
You can set an algorithm that the computer determines (and improves while moving)
(Based on preferred floors for example or based on time of arrival to the floor and customer care).

//Literature survey for the problem:
1) the science behind elevators-
https://www.youtube.com/watch?v=xOayymoIl8U
2) the elevator optimization problem by Brendan Ferris- 
https://towardsdatascience.com/elevator-optimization-in-python-73cab894ad30
3) project idea-smart elevator by Sri Harsha- https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup/
4) Smart Elevators: A Faster Way Up and Down-
https://www.npr.org/templates/story/story.php?storyId=6799860
5) The Hidden Science of Elevators-
 https://www.popularmechanics.com/technology/infrastructure/a20986/the-hidden-science-of-elevators/

//An Explenation about the diffrent between offline algorithm and online algorithm.
first we will try to understand the diffrents between online algorithm and offline algorithm.
in offline algorithm we get all the input from the start. in the other hand in online algorithm we get update input throuth the running of the program.

//Off-line algorithm
Offline #
A) Given the list of inputs, a call is received on a particular floor - if there is an elevator available on the current floor then it receives the call, at the end of the call ,the Elevator stops on the floor it has reached.
B) Otherwise, the elevator closest to the call goes up / down to take the call and make the trip (if there are several elevators then we will prefer the elevator with the best stop time, start time, and speed).
C) If there are passengers on the travel route of the call the elevator picks them up (lets say the elevator goes up and there is another passenger who wants to go up).
D) If there is a unused elevator it will take the new call.
E) If another call is subsequently received (in the existing output) to the route against the direction of elevator and there is another unused elevator it answers the call according to the algorithm we described, in case not we wait for the first available elevator to complete its route and then pick up passengers for the new call.
F) This algorithm goes on and on until the readings from the given input are finished. 



//A simple Junit tests

a)Check how long it takes for the elevator to reach each passenger-
According to the function of travel time per passenger.

B)Check how many times an elevator has visited each floor -
According to the functions in the elevator class of destination floor and source floor.

C) Check if there is a forgotten passenger-
According to a check in how many uncomleted calls there is in the test result.

D) How many times does an elevator complete all the floors-
According to an inspection in the elevator class (src and dest floor) of the travel.

E) Check how long it takes for the elevator to open a door-
According to inspection by the elevator door function and opening times of the elevator door.

F) Check how long it takes for the elevator to close a door-
According to an inspection by the elevator door function and the closing times of the elevator door.

G) How long does it take to allocate an elevator-
According to a check by the allocate an elevator in algorithm class and a check waiting time for the elevator.

H) Average length of elevator route-
According to an inspection in the elevator department of travel time function.

I) Number of stops of the elevator-
According to an examination in the elevator class , the amount of use of a stop function at a given output.

J) How many elevators are not used at a given time-
According to an inspection of an elevator class at a given time and an examination of the condition of all the existing elevator condition.

L) Checking the number of times the elevator stopped while traveling on route-
By the function of stopping an elevator and opening a door.

M) The most requested floor inspection in which the elevator visited the most-
By functions in the elevator class of destination floor and source floor.

N) Check how many times the elevator is unused (level).
   -Count the number of times this function is activated. isEmpty by function

O) Checking average speed for an elevator.
By Elevator speed function in elevator class and by number of elevators in the input. 
