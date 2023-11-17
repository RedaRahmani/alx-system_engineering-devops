# Postmortem: Unexpected Downtime on Payment Gateway


## Issue Summary

- **Duration:**
  - Start Time: November 10, 2023, 14:00 (UTC)
  - End Time: November 10, 2023, 15:30 (UTC)
- **Impact:**
  - The payment gateway experienced unexpected downtime, leading to transaction failures for users.
  - Approximately 20% of users were affected during the outage.
  - The core payment service was unavailable, resulting in failed transactions and payment processing issues.
- **Root cause:**
  - A recent update to the payment gateway API resulted in compatibility issues with our system, causing the service to go down.

## Timeline

- **Detection:**
  - The issue was detected on November 10, 2023, 14:00 (UTC) through automated monitoring alerts indicating a spike in failed transactions.
- **Actions Taken:**
  - Investigated server logs for any unusual activity or errors related to payment processes.
  - Assumed the issue might be related to recent updates in the payment gateway API.
- **Misleading Paths:**
  - Initially explored server performance, suspecting issues with server load affecting payment processing.
  - Checked for recent code changes and deployment logs.
- **Escalation:**
  - The incident was escalated to the Development team after initial investigation suggested a potential API-related issue.
- **Resolution:**
  - Rolled back to the previous stable version of the payment gateway API, restoring compatibility with our system.
  - Restarted the necessary services to apply the rollback.

## Root Cause and Resolution

- **Root Cause:**
  - The recent update to the payment gateway API was not compatible with our system, causing the service to fail during payment processing.
- **Resolution:**
  - Rolled back to the previous version, ensuring the correct API version was in place.
  - Implemented additional checks in the deployment process to verify API compatibility.

## Corrective and Preventative Measures

- **Improvements/Fixes:**
  - Enhance automated testing procedures to include specific tests for API compatibility.
  - Strengthen monitoring for payment-related errors and failed transactions.
  - Implement a checklist in the deployment process to validate and confirm the correctness of API versions.
- **Tasks:**
  - Conduct a thorough review of the payment gateway’s API setup to identify and rectify potential compatibility issues.
  - Schedule regular audits of payment logs to proactively identify and address potential issues.
  - Implement a post-deployment validation step to verify the stability of the payment service after each release.

*In conclusion, the unexpected downtime in the payment gateway was promptly addressed by rolling back to a stable API version and implementing additional testing measures. This incident highlights the critical role of proper API compatibility and underscores the need for vigilant monitoring and testing in the deployment process. The outlined corrective and preventative measures aim to enhance the resilience of the payment gateway, ensuring a more dependable user payment experience.*

