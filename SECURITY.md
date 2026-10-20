# Security policy

This policy covers every repository in the GuardianO3 organisation, including
the official SDKs, and the GuardianO3 API they talk to.

GuardianO3 processes live session audio and transcripts, which is sensitive
personal data. Please report vulnerabilities privately.

## Reporting a vulnerability

**Do not open a public issue, and do not put a working exploit in the first
message.**

| | |
|---|---|
| Where | **Security → Report a vulnerability** on the affected repository, or email **security@guardiano3.com** |
| Acknowledgement | within **2 business days** |
| Initial assessment | within **5 business days**, with a severity and a plan |
| Fix target | Critical: **7 days** · High: **30 days** · Medium: **90 days** |

A useful report says what an attacker gains, gives the smallest set of steps
that shows it, names the affected SDK and version (or API endpoint), and
includes the `X-Request-Id` of a request that shows the behaviour.

**Please do not** run automated scanners against the production API, access
data that is not yours, or degrade the service for other users.

We will keep you informed, credit you in the advisory if you want to be
credited, and tell you when the fix ships. There is no bounty programme.

## Never send us secrets

Do not include API keys, session audio, transcripts or personal data in a report,
an issue or a pull request. If a key has been exposed, revoke it in the
developer console first, then tell us.

## Supported versions

The SDKs are pre-1.0. Fixes land in the latest release only.
