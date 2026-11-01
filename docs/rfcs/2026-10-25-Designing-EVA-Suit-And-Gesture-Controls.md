# RFC: [EVA Suit and Astronaut Follow Command]
| Field | Value |
| --- | --- |
| Author | Zion Moreau |
| Date | 2026-10-24 |
| Status | Proposed |
| Decision Date | (fill when decided) |
| Deciders | (who agreed to the outcome) |
| Superseded By | (link, if applicable) |
## Problem and Context
For the Mars Rover Autonomous Capstone project a requirement is to add software that
enables a challenge where the rover must work with an "astronaut" in an EVA suit (which must
be built by the team) who will use gestures to issue commands to the rover. The Rover has a
series of cameras in all directions, but these cameras may be subject to weather and elemental
conditions.
Specifically the Rover must see the Astronaut perform a gesture and after recognizing it
it must begin following the Astronaut and stop when it reaches within 3 meters of them.
Completing this task is worth 15 points in the URC (University Rover Competition)
## Options
### Option A: Use Existing Cameras and Create a computer vision model
This option involves using the existing cameras on the rover and training a model using
openCV to be able to detect a human figure and understand what gesture they are performing.
The benefit of this option is that no additional hardware on the rover is necessary, just work
implementing the software and training the computer vision model to handle this. However the
downside of this is that the performance of this majorly depends on both how well trained the
computer vision model is, and how clear the weather and camera view is during the competition.
Using the existing cameras with no modification means that the results of detecting the
Astronaut might be wildly dependent on the weather conditions of the environment as well as
the lighting.
### Option B: Retroreflective Tape on EVA Suit and Additional Front-Facing Flashlight
This option involves putting retroreflective tape on the EVA suit in certain known parts
(for example on the wrists and arms), and mounting a forward-facing flashlight onto the rover
itself. This would allow the EVA suit to appear to be extremely bright from the front facing
camera on the rover whenever the astronaut is in front of the rover, which we know it will be for
this challenge. The Astronaut appearing to be extremely bright would allow for our computer
vision model to use brightness to filter out objects from their surroundings to isolate the
Astronaut’s silhouette. Because there are no other sources of light on mars other than the sun
(no man made lights) This would work extremely well since the only thing that appears as bright
as the retroreflective tape should be the sun itself. However the downside and cost of this option
is that we must physically buy retroreflective tape when making the EVA suit, and a powerful
flashlight to attach to the rover. However this option would likely reduce the time taken to
implement the computer vision model, and would reduce the dependence on clear weather as
the retroreflective glow would make finding the astronaut easier in bad conditions.
### Option C: Do Nothing
Doing nothing means that this functionality is not implemented and we will miss out on the 15
points for the URC. But it also means that there is no cost, both in actual money and in
development time.
## Analysis
The tradeoffs that matter for this decision are cost, effort, and performance. The ideal solution
would be as cheap as possible, requiring as little effort as possible, but perfectly able to detect
the Astronaut’s gesture and follow them within 3 meters until they stop regardless of
weather/lighting conditions. The source for this analysis of tradeoffs comes from the URC 2027
rulebook and discussions with the OSU Robotics Club
## Recommendation and Verification Plan
The decision above that I suggest is to go with option B, and use the retroreflective tape and the
flashlight. Though this is the only option that requires external spending, both the tape and the
flashlight should be very inexpensive, but this option should make the computer vision model
significantly easier to implement, because it can start with a simple brightness mask. The
information that led me to this conclusion is looking up the cost of simple retroreflective tape
which ranges from $10-$30. I also believe this would allow for us to score much better when at
the URC event, because if the lighting is poor (such as overcast and dim, or even foggy) then
the flashlight and tape would allow the Astronaut to stand out much more from its surroundings,
allowing the rover to find it.
## Constraints
The only constraint that applies to this decision is if the Rover Club has enough budget to
allocate approximately $40 to us for us to be able to buy retroreflective tape and a flashlight.
## Delegation and Validation
Nothing is given to AI tools for this assignment. For our project there is no CI/CD pipeline
implementation, because all tests must be physically done on the rover. To test the decision that
is made for this assignment, we will have to prepare a mock EVA suit and observe how well the
cameras are able to detect and understand the Astronaut’s gestures. We will have to devise a
method to simulate poor conditions, for example testing in different light levels.
What is assessed is in the [AI
policy](https://capstone.alexulbrich.com/assignments/introduction/#ai-policy-applies-to-every-as
signment).
No AI was used in any part of this assignment.
## Decision
Proposed.