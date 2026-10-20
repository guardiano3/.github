# Contributing

Thank you for helping improve GuardianO3. This guide applies to every
repository in the organisation that does not carry its own.

Everyone taking part is expected to follow our
[code of conduct](CODE_OF_CONDUCT.md).

## Issues: always welcome

Bug reports, documentation fixes and feature requests are welcome as issues.
Use the templates; they ask for the SDK, its version and the `X-Request-Id`
of a failing request, which is usually enough for us to find the cause.

**Never paste API keys, session audio, transcripts or personal data** into an
issue, a pull request or a log excerpt. Remove them, or replace them with
placeholders, before you post. If you have already posted a key, revoke it in
the developer console.

Security problems are not issues: follow [SECURITY.md](SECURITY.md).

## Pull requests: hand-written code only

Each SDK has two halves:

- **Generated code** (models and operations) is rebuilt from the GuardianO3
  API's OpenAPI contract. It is never edited by hand, so we close pull requests
  that change it. If generated code is wrong, open an issue: the fix belongs in
  the contract, and the next regeneration carries it to every SDK.
- **Hand-written code** (transport, retries, errors, pagination, live-session
  helpers, tests and docs) is where pull requests are welcome. Each SDK's
  README says which directories are which.

For anything larger than a small fix, open an issue first so we can agree on
the approach before you spend time on it.

## Sign your commits (DCO)

We use the [Developer Certificate of Origin](https://developercertificate.org/)
instead of a contributor licence agreement. By adding a `Signed-off-by` line to
a commit, you certify that you wrote the change or otherwise have the right to
submit it under the repository's licence.

```bash
git commit -s -m "Fix retry delay when Retry-After is a date"
```

Every commit in a pull request needs the line, and CI checks it. To sign off
commits you already made: `git rebase --signoff main`, then force-push your
branch.

## Licence

Contributions are accepted under the licence of the repository you contribute
to (Apache-2.0 for the SDKs). No other agreement is needed.
