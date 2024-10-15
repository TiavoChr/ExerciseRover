# ExerciseRover

## Class

Pattern Builder ?

### RoverState
- x: entier
- y: entier
- orientation: NORD|SUD|EST|WEST

### CircularOrientationInterface
+ rotateLeft
+ rotateRight

### LinearMoveInterface
+ moveForward
+ moveBackward

### RoverOrientation < CircularOrientationInterface
+ rotateLeft
+ rotateRight

### RoverMove < LinearMoveInterface
+ moveForward
+ moveBackward

### Rover < 