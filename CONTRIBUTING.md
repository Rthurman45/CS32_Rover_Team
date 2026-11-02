Contributing to the Rover Project

This document outlines our setup steps, dual-repository workflow, physical testing protocols, code review standards, and contribution norms. Because our software interacts directly with rover hardware and relies heavily on physical verification, we follow a structured workflow tailored to our hardware setup.

1. Codebase Audit & Project Context

Before writing code or modifying features in an existing codebase, all contributors must understand its current state, physical constraints, and known technical debt. Our audit findings and architectural constraints are documented across our living documentation:

Constraints & Requirements: Documented in docs/requirements.md. Look here for system boundaries, pinouts, power limits, and hardware constraints.

Design Decisions & Trade-offs: Documented in docs/design.md. Includes decisions to keep or replace legacy modules, submodules, drivers, or control logic.

Conventions & Pitfalls: Maintained in this file (CONTRIBUTING.md) and project AI context files.

Audit Summary Checklist

When onboarding or taking over legacy code, review the following:

Execution & Hardware: What runs on the physical rover, how it runs, microcontrollers/drivers involved, and what currently fails or is broken.

Hardware & Script State: The operational state of existing manual verification scripts and pin mappings.

Dependencies & Toolchain: Required compilers, ROS2 Jazzy packages, SDKs, firmware versions, or external libraries.

Risks & Debt: Known physical/software debt, unhandled edge cases in sensor readouts, or inherited hardware risks.

2. Dual-Repository Structure & Workflow

We maintain two separate Git repositories:

CS32_Rover_Team: Our active development space where team members branch, build, and test features.

DAM Robotics GitHub Repository: The official, stable repository. Code is only merged here after thorough physical verification.

Contribution Norms

Active Workspace: Each member’s work lives in the Group GitHub repository during development.

Target Integration: Code will eventually be merged into the main DAM Robotics GitHub repository after it has been fully tested and verified.

Clean Pushes: Code that does not compile or overwrites someone else's active development work must never be pushed to the repository. Ensure you pull and resolve merge conflicts locally first.

Saturday Testing Rhythm: Code pushed to the Group GitHub throughout the week is queued for physical integration and hardware testing on the following Saturday.

3. Getting Started & Setup Steps

Follow the environment setup instructions from the project README to configure your local workspace for ROS2 Jazzy and related tools (such as MoveIt2, Nav2, and RealSense SDKs):

Clone the Group Repository:

git clone <git@github.com:Rthurman45/CS32_Rover_Team.git>

Clone the main Rover Repository:

git clone <git@github.com:OSURoboticsClub/Rover_2026_2027.git>


Configure Environment & Toolchain:

Ensure ROS2 Jazzy is installed and sourced:

source /opt/ros/jazzy/setup.bash


Install missing ROS dependencies using rosdep:

rosdep update
rosdep install --from-paths src --ignore-src -r -y


Build the Project Locally: Build your workspace using colcon:

colcon build --symlink-install
source install/setup.bash


4. Local Development & Validation Commands

Even without automated remote CI, all code must pass local build and compilation checks before hardware deployment:

Workspace Build & Compilation Check:

colcon build --symlink-install


Network / Middleware Check (Zenoh): Verify your environment variables (RMW_IMPLEMENTATION=rmw_zenoh_cpp) and Zenoh router configuration in ~/.profile are correctly set up to communicate with the rover.

5. Branching & PR Workflow

Branch Naming: Create feature branches off main in the Group GitHub using descriptive names:

feature/<short-description>

fix/<short-description>

refactor/<short-description>

Development & Commit: Commit clean, atomic changes with clear messages.

Pull Request to Group Repo: Submit a PR on the Group GitHub repository for peer review before Saturday testing.

6. Code Review Expectations

Peer Review: At least one team member must review the code for logic, readability, and compliance with project constraints.

Conflict Prevention: Reviewers will verify that the incoming code does not clobber concurrent active development work.

7. Definition of Done (DoD)

Before code may be merged into the main DAM Robotics GitHub Repository, it must satisfy all of the following criteria:

[ ] Compiles Successfully: Code builds cleanly locally via colcon build without errors.

[ ] Physically Tested on Rover: The code has been physically deployed and tested in-person on the actual Rover hardware. (This process cannot be automated with a CI/CD pipeline because it must be physically tested in person on the rover).

[ ] Works Correctly & Safely: Physical hardware execution produces expected outputs without causing mechanical, electrical, or software instability.

[ ] Review Approval: Received peer review approval from team lead.

[ ] Documentation Updated: Pinout changes, hardware configurations, or operational steps are fully documented in docs/ or relevant README files.

8. Where to Ask for Help

Discord/Email: Reach out on our primary team messaging channel for quick software or hardware questions.

Saturday Physical Syncs: Bring hardware integration questions and bench testing setups to our Saturday test sessions.

Design & Hardware Conflicts: Check docs/requirements.md and docs/design.md first, or tag module leads in your GitHub PR comments.