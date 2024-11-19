# Workflow Diagram

```mermaid
flowchart TD
    A[Inputs] --> B[Fetch PR Data from GitHub]
    B --> C[Validate PR Titles]
    C --> D[Verify Associated Jira Tickets]
    D --> E[Track Modified Repositories]
    E --> F[Generate Compliance Report]

    %% Inputs
    A --> A1[App ID]
    A --> A2[GitHub Token]
    A --> A3[Jira Token]
    A --> A4[Jira Project]

    %% Outputs
    F --> F1[Invalid PR Details]
    F --> F2[List of Modified Repositories]