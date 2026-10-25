# RFC-001:  Adding Elevation Maps into Autonomous Routing

| Field | Value |
| --- | --- |
| Author | Noah West |
| Date | 2026-10-24 |
| Status | Proposed |
| Decision Date | TBD |
| Deciders | Zion, Robert, Jared |
| Superseded By | N/A |

## Problem and Context

The current autonomous routing system uses a depth camera to determine object distance. The distances are then used to make cost estimates for how long it would take the rover to route to different areas. The rover will be used in bright and dusty environments where camera accuracy could be limited.

We need to provide a baseline for how the environment looks based on elevation maps so that the routing system can use that information when the conditions don't permit accurate camera images. The specific decision we need to make is how to incorporate the elevation maps into the existing routing system's cost analysis. If we don't make decision, the routing system will be faulty to poor camera conditions.

## Options

### Option A: Preprocess to Occupancy Grid

Converting elevation maps into an occupancy grid before launching Nav2. When given a DEM elevation map, the program could perform slope and roughness analysis beforehand. The benefits are that it provides a simpler setup, uses standard Nav2 components, and is easy to debug since cost values can be directly compared beforehand.

The cost of this option is relatively low since a lot of the functionality is already provided by built in Nav2 components. This option would be the right choice when we would want to simply mark unsafe slopes or terrain as obstacles and treat everything else as traversable.

### Option B: Preprocess to Graded Costs

Converting elevation maps into a 0-100 cost grid and then using a custom cost map layer. When given a DEM elevation map, the program could convert the slope and roughness of different sections into a 0-100 cost value. The cost value for all the sections could then be given to a custom cost map layer which informs the Nav2 stack of areas with the lowest cost. The benefits are that it allows the planner to specifically prefer gentle slopes instead of avoiding all steep terrain.

The cost of this option is medium since it requires developing and tuning a custom conversion mechanism that maps slop/roughness values from an elevation map to a 0-100 cost value. This option also requires developing a custom cost map layer that then utilizes the cost values to inform the Nav2 stack. This option would be the right choice when we want to grade costs based on steepness rather than simply mark slopes as obstacles.

### Option C: Do Nothing

Doing nothing means that we would retain the existing Nav stack that relies on only the camera images for informing routing decisions. This option has the cost of making our route faulty for poor lighting or dust conditions which we are likely to encounter during the competition. This cost would arrive during the competition and likely during our testing phase.

## Analysis

The technical tradeoffs that matter for this decision are performance, complexity, and maintainability. We need our Nav2 routing system to be efficient since the rover will constantly be receiving new route information from the astronaut it is following. We also need the system to be maintainable and not too complex so that we can finish our implementation on time and so future teams can build upon it.

### Option A: Preprocess to Occupancy Grid
It is unknown at this point what the exact performance of this option is since we can't test it. I can estimate that it would perform better and be a little slower than the existing system, but not that much slower since everything is pre-computed on static terrain. The complexity would be higher, but not by too much. The maintainability will be fine as long as we thoroughly document and communicate everything.

### Option B: Preprocess to Graded Costs
It is unknown at this point what the exact performance of this option is since we can't test it. I can again estimate that it would perform better and be a bit slower than the existing system, but not too much slower since everything is pre-computed on static terrain. It will likely be slower than option A, however, since at run time it has to use a custom translation layer that goes from the graded costs to route recommendations. The complexity would be higher with the addition of a cost grader and a translation layer. The maintainability will be fine as long as we thoroughly document and communicate everything.

### Option C: Do Nothing
It is unknown at this point what the exact performance of the previous system is since we are still working on getting the old system running on the new ROS2 version. We have been told that it worked well enough but had a hard time with poor lighting and weather conditions. For complexity, the existing system is at the lowest level, so it isn't very complex. For maintainability, the existing system doesn't work on the new ROS2 version so if it isn't updated, then it won't be able to be used. I have relied on our group mentor Jared for this information and the current code base.

## Recommendation and Verification Plan

Based on our current knowledge of the existing system's functionality, I would propose adopting Option A. The competition specifically requires being able to determine what hills are passable and which aren't. I believe the specific cost analysis would allow us to fine tune those decisions more than Option A, where we arbitrarily pick certain terrain as obstacles. The performance would be better, because of the tuning allowed by the cost analysis. The complexity would be higher, but I think that is good since our routing algorithm will have more data to work with. The maintainability would be good as long as we thoroughly document and communicate everything.

We will know that Option A worked by testing the system in a simulation and physically on the rover. If the rover successfully reaches the goal post and navigates around hazardous terrain, then we will know that the cost analysis is working and informing the routing decisions correctly. This will be checked as soon as we have a proof of concept running. We don't have any specific metrics besides reaching the goal. Failure would mean stopping early, going out of bounds, running out of time (30 min), or flipping the rover.

## Constraints

There are no licensing, IP, or partner confidentiality boundaries. All the code is open source and freely available. The only data we will be using is collected by our hardware and provided by the competition hosts. All data is free use and doesn't come with any constraints.


## Delegation and Validation

- **AI Tools Usage:** We haven't given anything to AI tools yet. The mentor's coding environment doesn't have a good way of supporting a built in tool, but we do plan on using it for answering specific questions. We will specifically ask it about conceptual topics that we can then research as well as formatting for libraries and function calls.

- **Automatic Checks:** We are using a separate branch that only gets merged to main when everything performs on the actual hardware. We don't have any existing hard-coded review gates besides our agreed terms. The staging/practice environment is the simulation where we simulate the rover navigating before moving the real rover. The rollback path would be going back to main branch or moving back in commits.

- **Personal Checks:** I haven't performed personal checks on the decision yet since we are just in the proposal stage.

## Decision

There is no decision at the moment since this is just the proposal.