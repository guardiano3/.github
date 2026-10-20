<p align="center">
  <img src="https://raw.githubusercontent.com/guardiano3/.github/main/profile/banner.jpg" alt="GuardianO3 — Observe · Orient · Override" width="100%">
</p>

<h2 align="center">GuardianO3</h2>

<p align="center">
  <b>Scam-risk decisions for live customer sessions, delivered as an API.</b><br>
  Send a session's text or audio. Get a risk decision back while the session is still live.
</p>

<p align="center">
  <a href="https://guardiano3.com"><img src="https://raw.githubusercontent.com/guardiano3/.github/main/profile/assets/btn-website.svg" alt="Website" height="44"></a>&nbsp;
  <a href="https://guardiano3.com"><img src="https://raw.githubusercontent.com/guardiano3/.github/main/profile/assets/btn-console.svg" alt="Get an API key" height="44"></a>&nbsp;
  <a href="mailto:support@guardiano3.com"><img src="https://raw.githubusercontent.com/guardiano3/.github/main/profile/assets/btn-contact.svg" alt="Contact us" height="44"></a>
</p>

<img src="https://raw.githubusercontent.com/guardiano3/.github/main/profile/assets/divider.svg" alt="" width="100%">

### Scams are decided in the conversation

The most damaging scams don't break into an account. They talk the account holder into acting: sharing a one-time code, installing a remote-access app, or approving a transfer while someone posing as the bank or the police keeps up the pressure.

Transaction monitoring sees the payment, but not the conversation that led to it. **GuardianO3 gives banks, payment platforms, telcos and contact centres a risk decision during the customer session itself**, while there's still time to pause, check and reach out.

<img src="https://raw.githubusercontent.com/guardiano3/.github/main/profile/assets/features.svg" alt="Why GuardianO3: decisions while the session is live, every score explained, built for scam pressure, API-first, you own the action" width="100%">

<img src="https://raw.githubusercontent.com/guardiano3/.github/main/profile/assets/divider.svg" alt="" width="100%">

### ⚡ Quick start

Create an API key in the developer console at [guardiano3.com](https://guardiano3.com), then score a piece of text:

```bash
curl https://api.guardiano3.com/v1/analyze/text \
  -H "Authorization: Bearer $GUARDIANO3_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "There is an arrest warrant in your name. Transfer your savings now."}'
```

<details>
<summary><b>Example response</b> (abridged)</summary>

```json
{
  "riskScore": 92,
  "riskLevel": "critical",
  "fraudType": "Law Enforcement Impersonation",
  "explanation": [
    "Asks the listener to share a secret or send money."
  ]
}
```

</details>

For live audio, start a session with `POST /v1/sessions`, stream audio over the session's WebSocket, and read a decision for each chunk.

### 📦 SDKs

| Language | Install | Repository |
|---|---|---|
| Python 3.10+ | `pip install guardiano3` | [guardiano3-python](https://github.com/guardiano3/guardiano3-python) |
| TypeScript / JavaScript (Node 22+) | `npm install @guardiano3/sdk` | [guardiano3-node](https://github.com/guardiano3/guardiano3-node) |
| Java 11+ | `com.guardiano3:guardiano3-sdk-core:0.1.0` | [guardiano3-java](https://github.com/guardiano3/guardiano3-java) |
| Go 1.23+ | `go get github.com/guardiano3/guardiano3-go@v0.1.0` | [guardiano3-go](https://github.com/guardiano3/guardiano3-go) |

The SDKs are open source under Apache-2.0. They add typed errors, safe retries, idempotency keys, pagination and live sessions on top of the `/v1` API.

### 🧩 The API at a glance

| | Capability | Endpoint |
|:-:|---|---|
| 📝 | Score text | `POST /v1/analyze/text` |
| 🎧 | Score an audio clip | `POST /v1/analyze/audio` |
| 🟢 | Start a live session | `POST /v1/sessions` |
| 📡 | Stream session audio and receive live decisions | WebSocket `/v1/sessions/{id}/audio` · `/v1/sessions/{id}/stream` |
| ⏹️ | Finalise a session | `POST /v1/sessions/{id}/stop` |
| 🏷️ | Label an outcome (scam / not scam) | `POST /v1/sessions/{id}/feedback` |
| 🔑 | Manage API keys | `/v1/api-keys` |
| 👥 | Manage your organisation's members | `/v1/org` |

Every response is camelCase JSON. Errors share one envelope, so branch on `error.code`. Every response carries an `X-Request-Id` to quote in support requests.

### 🗺️ Coming to this organisation

- [x] Official SDKs: Python, TypeScript, Java and Go
- [ ] Developer documentation and integration guides
- [ ] Sample integrations and quick-start projects
- [ ] Changelog for the `/v1` API

<img src="https://raw.githubusercontent.com/guardiano3/.github/main/profile/assets/footer.svg" alt="Observe · Orient · Override" width="100%">

<p align="center">
  <a href="https://guardiano3.com">guardiano3.com</a> · <a href="mailto:support@guardiano3.com">support@guardiano3.com</a><br>
  <sub>© 2026 Proneuronet Solutions Private Limited. The SDKs are open source (Apache-2.0); the GuardianO3 service is proprietary.</sub>
</p>
