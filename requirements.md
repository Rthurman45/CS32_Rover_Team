# Requirements


## Problem statement
    The given problem is to update a rovers navigation stack written in ROS2 to prepare for the upcoming University Rover Competition (URC) that takes place in spring of 2027. The goal is to update the existing navigation stack from ROS2 version "humble" to ROS2 "jazzy" and add new features such as gesture controls, computer vision and object recognition, and voice controls. Additionally we must create a UI within unity that displays a map to the user with the rover's position and orientation that allows the user to input gps waypoints that the rover will navigate to.

## Functional requirements
    - FR-1: (Must: cannot work on anything else until this is complete): Existing code must be updated to new ROS2 version successfully and must be able to build and run on the rover without errors. Acceptance: Colcon build succeeeds on the rover with zero package failures.

    - FR-2: (Must: Most essential part of project and URC, worth the most points): Must update existing Nav Stack code to ensure it is fully functional and remove all existing bugs. Acceptance: Rover should be able to successfully navigate to given GPS coordinates and avoids collisions with obstacles with Nav2, stopping within 3 meters of the AruCo tags at the given waypoints.

    - FR-3: (Must: Essential for presentation video, due during February 2027): Must create a Unity UI that shows the rovers position and allows for a user to give GPS coordinates to navigate to. Acceptance: UI should display rover's current position and orientation and succesfully show it moving towards the given GPS points.

    - FR-4: (Must: Essential for full points at URC competition): Must implement a YOLO computer vision model to detect a specific hammer that the robot must find and navigate to, positioning itself within the arm's workspace. Acceptance: Model must be able to detect the hammer in harsh sunlight as the competition will take place in Utah desert, and the rover must be able to position the hammer within a 1 foot by 2 foot area that is the arms workspace once it is located.

## Non-functional requirements
    - NFR-1: (Must: URC has a limited amount of time for autonomous tasks, so it must complete all tasks within 1 hour): The rover navigates at a safe but reasonable speed, and the computer vision model is not set to training mode.


## Constraints
    - Must dual boot using Ubuntu version 24.04 and use ROS2 Jazzy.
    - Must communicate with groundstation and arm capstone teams to ensure full competition points.
    - Team members limited to the expected 9 hours per week of work for a capstone project.

## Success metrics
    - Rover can autonomously navigate to 3 different GPS waypoints at varying elevations and successfully find and stop within 3 meters of ARuCo tags
    - The YOLO model successfully detects the specific hammer in strong sunlight from different angles at least 9/10 tests.
    - Gestures are recognized from the EVA astronaut and the rover follows within 3 meters
    - Unity UI shows live rover position with minimal delay and properly accepts GPS waypoint inputs.

## Non-goals
    - Arm autonomy. That is part of a different capstone, we must just get the object into the arm's workspace

## Open questions
    - Will we have new club members coming to help work on the more difficult in scope parts of the project.