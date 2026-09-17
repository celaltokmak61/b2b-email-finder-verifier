#!/usr/bin/env python3
"""
Official Python Client & Automation Runner for B2B Email Finder & Live SMTP/MX Verifier
Apify Store: https://apify.com/haktelaren/b2b-email-finder-verifier
"""

import os
import sys
import json
import csv
from apify_client import ApifyClient

def main():
    print("=" * 60)
    print("  🚀 B2B Email Finder & Live SMTP/MX Verifier - Runner")
    print("  Store: https://apify.com/haktelaren/b2b-email-finder-verifier")
    print("=" * 60)

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        print("\n❌ Error: APIFY_TOKEN environment variable is not set.")
        print("Please set your Apify API token:")
        print("  Windows: $env:APIFY_TOKEN = 'your_token'")
        print("  Linux/Mac: export APIFY_TOKEN='your_token'")
        print("Get your token at: https://console.apify.com/account/integrations\n")
        sys.exit(1)

    client = ApifyClient(token)

    # Load input config
    input_file = "sample_input.json"
    if os.path.exists(input_file):
        with open(input_file, "r", encoding="utf-8") as f:
            actor_input = json.load(f)
        print(f"\n📄 Loaded input configuration from '{input_file}'")
    else:
        actor_input = {
        "first_name": "Satya",
        "last_name": "Nadella",
        "domain": "microsoft.com",
        "deep_smtp_check": true,
        "timeout_seconds": 10
}
        print("\n📄 Using default input configuration")

    print("\n⏳ Starting cloud run on Apify...")
    run = client.actor("haktelaren/b2b-email-finder-verifier").call(run_input=actor_input)

    status = run.get("status")
    run_id = run.get("id")
    dataset_id = run.get("defaultDatasetId")
    console_url = f"https://console.apify.com/actors/{run.get('actId')}/runs/{run_id}"

    print(f"\n✅ Run Finished with status: {status}")
    print(f"🔗 Console Run URL: {console_url}")
    print(f"📦 Default Dataset ID: {dataset_id}")

    # Fetch dataset items
    dataset_client = client.dataset(dataset_id)
    items = dataset_client.list_items().items
    print(f"📊 Total items extracted: {len(items)}")

    # Save to JSON
    with open("output_dataset.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    print("💾 Saved results to 'output_dataset.json'")

    # Save to CSV if items exist
    if items:
        keys = list(items[0].keys())
        with open("output_dataset.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for row in items:
                # Format nested lists/dicts for clean CSV
                clean_row = {k: (json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v) for k, v in row.items()}
                writer.writerow(clean_row)
        print("💾 Saved results to 'output_dataset.csv'")

    print("\n🎉 Done! Check 'output_dataset.json' for full data.\n")

if __name__ == "__main__":
    main()
