# B2B Email Finder & Live SMTP/MX Verifier 🚀

[![Apify Actor](https://img.shields.io/badge/Apify-Actor%20Store-blue?style=for-the-badge&logo=apify)](https://apify.com/haktelaren/b2b-email-finder-verifier)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://github.com/celaltokmak61/b2b-email-finder-verifier)

> Discover corporate business emails, resolve DNS MX infrastructure, detect catch-all mailboxes, and perform live socket-level SMTP deliverability verification.

---

## ⚡ Instant Cloud Execution (No Code / No Proxies Required)

Run it in the browser. No install.

👉 **[Run B2B Email Finder on Apify](https://apify.com/haktelaren/b2b-email-finder-verifier)** — **\.005 per result**

On Apify Cloud, outbound **port 25 is blocked**. A cloud run returns name permutations, MX hosts, and the mail provider (Microsoft 365, Google Workspace, and others). Live mailbox SMTP needs erifier_api_url on a server you control that can open port 25. This actor does not use residential proxies.

* JSON, CSV, Excel, or Google Sheets export
* Schedule runs and send results to Make, n8n, or Zapier

---

## 🌟 Key Features

- 🧠 **Pattern Permutations:** Generates standard corporate combinations (`{first}.{last}`, `{first}`, `{f}{last}`, etc.).
- 🛡️ **Catch-All Detection:** Probes random addresses to detect catch-all servers, protecting your sender domain reputation.
- ⚡ **Live Socket SMTP Handshake:** RFC-compliant `EHLO`, `MAIL FROM`, `RCPT TO` checks on port 25 without sending messages.
- 🏢 **MX Provider Fingerprinting:** Instantly identifies Google Workspace, Microsoft 365, Proofpoint, Mimecast, etc.
- 📦 **Single & Bulk Mode:** Verify individual prospects or batch upload thousands of leads.

---

## 🚀 Quickstart: Python Client

This repository provides an official, lightweight Python automation client for the [B2B Email Finder & Live SMTP/MX Verifier Actor](https://apify.com/haktelaren/b2b-email-finder-verifier).

### 1. Installation

```bash
git clone https://github.com/celaltokmak61/b2b-email-finder-verifier.git
cd b2b-email-finder-verifier
pip install -r requirements.txt
```

### 2. Set Your Apify API Token

Get your free API token from [Apify Console -> Settings -> Integrations](https://console.apify.com/account/integrations).

```bash
# Windows (PowerShell)
$env:APIFY_TOKEN = "your_apify_api_token_here"

# Linux / macOS
export APIFY_TOKEN="your_apify_api_token_here"
```

### 3. Run the Automation Client

```bash
python run_actor.py
```

You can customize your parameters directly in `sample_input.json`:

```json
{
  "first_name": "Satya",
  "last_name": "Nadella",
  "domain": "microsoft.com",
  "deep_smtp_check": true,
  "timeout_seconds": 10
}
```

The script will trigger the cloud Actor, wait for execution to complete, and automatically save the scraped records to `output_dataset.json` and `output_dataset.csv`.

---

## 📦 Sample Output

```json
[
  {
    "input_first_name": "Satya",
    "input_last_name": "Nadella",
    "input_domain": "microsoft.com",
    "status": "VALID",
    "best_guess_email": "satya.nadella@microsoft.com",
    "is_deliverable": true,
    "is_catch_all": false,
    "confidence_score": 98,
    "mx_provider": "Microsoft 365 / Exchange Online",
    "primary_mx": "microsoft-com.mail.protection.outlook.com",
    "smtp_response_code": 250,
    "smtp_message": "2.1.5 Recipient OK",
    "verified_at": "2026-09-17T12:00:00.000Z"
  },
  {
    "input_first_name": "Sam",
    "input_last_name": "Altman",
    "input_domain": "openai.com",
    "status": "VALID",
    "best_guess_email": "sam.altman@openai.com",
    "is_deliverable": true,
    "is_catch_all": false,
    "confidence_score": 95,
    "mx_provider": "Google Workspace",
    "primary_mx": "aspmx.l.google.com",
    "smtp_response_code": 250,
    "smtp_message": "2.1.5 Recipient OK",
    "verified_at": "2026-09-17T12:01:00.000Z"
  }
]
```

Full sample records are available in [`sample_output.json`](sample_output.json) and [`sample_output.csv`](sample_output.csv).

---

## 🌐 API & Integration Examples

You can easily trigger this Actor from any language or workflow tool:

### cURL

```bash
curl "https://api.apify.com/v2/acts/haktelaren~b2b-email-finder-verifier/runs?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
  "first_name": "Satya",
  "last_name": "Nadella",
  "domain": "microsoft.com",
  "deep_smtp_check": true,
  "timeout_seconds": 10
}'
```

### Node.js / JavaScript

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('haktelaren/b2b-email-finder-verifier').call({
  "first_name": "Satya",
  "last_name": "Nadella",
  "domain": "microsoft.com",
  "deep_smtp_check": true,
  "timeout_seconds": 10
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

---

## 👤 Author & Custom Development

* **Author:** Celal Tokmak
* **Apify Profile:** [@haktelaren](https://apify.com/haktelaren)
* **GitHub:** [@celaltokmak61](https://github.com/celaltokmak61)

### 💼 Need Custom Scrapers or Enterprise Data Pipelines?
Need bespoke scraping solutions, specialized B2B data extractors, or custom workflow integrations? Feel free to open an Issue or contact me via my [Apify Profile](https://apify.com/haktelaren/b2b-email-finder-verifier).

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
