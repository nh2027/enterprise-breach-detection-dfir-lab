# False Positive Notes

Use this file to document what normal behaviour could trigger each detection and how the rule could be tuned.

## DET-001 Multiple failed logons
Possible false positives:
- User forgot password.
- Service account password changed.
- Misconfigured scheduled task.

Tuning ideas:
- Exclude known service accounts after validation.
- Add threshold and time window.
- Correlate failed logons followed by success.

## DET-005 Suspicious PowerShell encoded command
Possible false positives:
- Admin automation.
- Software deployment tools.

Tuning ideas:
- Review parent process.
- Check user and host.
- Check whether command reached external network.
