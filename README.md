<h1>OVERVIEW</h1>

<p>For this assesment I have been provided with code and a scenario to create a test plan and carry out tests for.</p>

<h2>ASSESMENT INSTRUCTIONS</h2>
<h3>Scenario</h3>

<p>You work for a software development company that specialises in educational software for high school age students. The project is developing a 10pin bowling game prototype that can be used to teach a variety of subjects. The source code has been developed and your role is to test this prototype using the provided source code.</p>

<p>Your course tutor will provide you with code for the back end of the program. There is not yet any GUI, and no system for receiving input data from files or a database. Once the backend has been tested, these parts will be developed. The bowling game source code file shows example usage of the system. Activities for this project assessment are:</p>

<ul>
<li>Create a Test Plan</li>
<li>Design a suite of unit tests</li>
<li>Debug and refactor an application</li>Debug and refactor an application
<li>Create Pythondoc and associated documentation</li>
<li>Use git</li>
<li>Report findings</li>
</ul>

 

<h2>Business Rules</h2>
<p>How the program works is largely defined by the business rules developed with the client at the beginning of the project.</p>

<h2>Rules of Play</h2>
<p>Each game of bowling consists of ten frames. In each frame, the bowler will have two chances to knock down as many pins as possible with their bowling ball. In games with more than one bowler, as is common, every bowler will take their frame in a predetermined order before the next frame begins. If a bowler knocks down all ten pins with their first ball, he is awarded a strike. If the bowler knocks down all 10 pins with the two balls of a frame, it is known as a spare. Bonus points are awarded for both a strike and a spare. The bonus points awarded depend on what is scored in the next 2 balls (for a strike) or 1 ball (for a spare). If the bowler knocks down all 10 pins in the tenth frame, the bowler is allowed to throw 3 balls for that frame. This allows for a potential of 12 strikes in a single game, and a maximum score of 300 points, a perfect game. </p>

<h2>Scoring</h2>
<p>In general, one point is scored for each pin that is knocked over. For example, if a player bowls over three pins with the first shot, then six with the second, the player would receive a total of nine points for that frame. If a player knocks down nine pins with the first shot, but misses with the second, the player would also score nine. When a player fails to knock down all ten pins after their second ball it is known as an open frame. In the event that all ten pins are knocked over by a player in a single frame, bonuses are awarded.</p>

 

A ten-pin bowling score sheet showing how a strike is scored: Bowlstrike.png

Strike: When all ten pins are knocked down with the first ball (called a strike and typically rendered as an “X” on a score sheet), a player is awarded ten points, plus a bonus of whatever is scored with the next two balls. In this way, the points scored for the two balls after the strike are counted twice.

Frame 1, ball 1: 10 pins (strike) Frame 2, ball 1: 3 pins
Frame 2, ball 2: 6 pins

The total score from these throws is:

Frame one: 10 + (3 + 6) = 19 Frame two: 3 + 6 = 9
TOTAL = 28

A player who scores multiple strikes in succession would score like so:

Frame 1, ball 1: 10 pins (strike) Frame 2, ball 1: 10 pins (strike) Frame 3, ball 1: 4 pins
Frame 3, ball 2: 2 pins

The score from these throws are:

Frame one: 10 + (10 + 4) = 24 Frame two: 10 + (4 + 2) = 16 Frame three: 4 + 2 = 6
TOTAL = 46

The most points that can be scored in a single frame are 30 points (10 for the original strike, plus strikes in the two subsequent frames).

A player who bowls a strike in the tenth (final) frame is awarded two extra balls allowing the playing to gain bonus points. If both these balls also result in strikes, a total of 30 points (10 + 10 + 10) is awarded for the frame. These bonus points do not count on their own; they only count as the bonus for the strike.
