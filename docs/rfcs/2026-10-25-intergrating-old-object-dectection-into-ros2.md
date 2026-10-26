
# RFC: [intergrating old objet detection into ros2]


| Field | Value |
| --- | --- |
| Author |Robert Thurman |
| Date | 2026-10-25 |
| Status | Proposed |
| Decision Date | TBD |
| Deciders | Jared, Zion, Noah |
| Superseded By | N/A |

## Problem and Context

The current object detection software works, but it is not very maintainable on the old system that was used. The rover team/project is updating its software to Ubuntu 24.04 and switching to Jazzy.

We need to update the old system to work on the new software and get it into a more stable state so that adding new features and objects is an easier task. The decisions we need to make are what to keep of the old software and how to make it more sustainable for future work. If we don’t make these decisions, the object detection will be faulty and extremely difficult to maintain in the future.
## Options


### Option A: [Keep as much of the old system as we can while improving the maintainability ]

Description: The old system is in a state of “it works,” but only on the old software. We want to convert the old code to work with the new dependencies and keep the main structure that we know works, while also improving its maintainability.

Benefits: This should save time and leave us mostly testing and editing the code to work with the new software. With improved maintainability, it should also allow future work to be done faster.

Costs (Low): It shouldn’t take much to convert the old code, so the cost should be low, especially in time. That leaves us more time to build and test new features.

### Option B: [Rebuild the entire object detection from scratch]

Description: The old code is too far into the unworkable zone with the new software and is too costly to reuse while also making it maintainable.

Benefits: This will give us a new code base built on the new software from the start. It will also be clean and far more sustainable, since we will build it step by step.

Costs (Medium): Time consumption will be heavy, leaving us less time to test the new features. We would have to develop, test, and train a model to detect objects and tell the rest of the bot what action is needed.

### Option C: Do Nothing

The cost is heavy, because the code does not work on the new software that the rest of the rover’s code is running on. This would leave the rover unable to compete, or, if it does compete, unable to meet all of its requirements.

## Analysis

Option A keeps the model and structure we already know work, so performance is known and only needs re-measuring after the port. Its complexity is moderate (fix what breaks, then clean up step by step) and its time cost is lowest. Option B has unknown performance until a new model is trained, high complexity, and a medium-to-high time cost, but the best long-term maintainability. Option C is simple today but doesn’t run on Jazzy and leaves us on unsupported software. Both A and B move us to Ubuntu 24.04 and Jazzy, which is a long-term-support release [link the ROS 2 Jazzy release page and migration notes]. We are uncertain how tightly the old code depends on old APIs, and our time estimates for A and B are guesses until we try building it [add results of a quick test build if you run one].

## Recommendation and Verification Plan

I recommend Option A. It keeps what we know works and spends our time on what is actually broken, leaving more time for new objects and features. Option B risks using most of our time redoing existing work, and Option C fails outright. If the old code still can’t build and run one detection on Jazzy, we will revisit Option B. Before changing anything, we will record the old system’s accuracy and speed as a baseline. We will know it worked when it builds cleanly on Ubuntu 24.04 with Jazzy, publishes detections from recorded test data.

## Constraints

None apply to this decision. All of the code is open source and freely available, so there are no licensing or IP restrictions on reusing or modifying it. The only data we will use is collected by our own hardware and provided by the competition hosts, and all of it is free to use with no conditions attached.

## Delegation and Validation

- **AI Tools Usage:** AI tools haven't been used yet. The coding environment doesn't have a good way to support the use of built in tools. We do plan on using it for answering questions. Mainly about conceptual topics that will then be researched as well as formatting for libraries, function calls, and debugging.

- **Automatic Checks:** We use a separate branch that only gets merged to main when everything performs on the actual hardware.  Right now we don't have any existing review gates besides our terms. The practice environment is used to simulate what the rover does before moving the real rover. The rollback path would be going back to main branch or moving back in commits.

- **Personal Checks:** I haven't done a personal check on the decision yet since we are just in the proposal stage.

## Decision

There are no decisions yet as we are still doing the proposals