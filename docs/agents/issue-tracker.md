## Issue Title Format
GitHub issue titles must follow this format:
````
ID <number>: <issue description>
````

Example:
* ID 2: Update system

## Reading GitHub Issues
When retrieving GitHub issues:
1. Read the issue title.
2. Extract the numeric issue ID from the beginning of the title.
3. Extract the issue description after the colon.
4. Read the issue body for additional requirements and context.
5. Use the GitHub issue number as the authoritative reference when linking back to the issue.

## Parsing Rules
Use this pattern to identify issue titles:
^ID\s+(\d+)\s*:\s*(.+)$

## Issue Processing
For each GitHub issue:
1. Retrieve the issue title and body.
2. Validate that the title follows the expected format.
3. Extract the ID and description.
4. Review the issue requirements.
5. Determine if work required deals with documentation.
6. Implement requested changes.
7. Update the issue with progress and completion details.

## Handling Invalid Titles
If a title does not match the expected format:
* Do not assume an ID from the title.
* Use the actual GitHub issue number as the reference.
* Flag the title as non-standard.
* Continue processing if the issue requirements are clear.