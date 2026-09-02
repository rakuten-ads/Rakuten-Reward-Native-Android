import os
import re
import subprocess
import sys
from openai import OpenAI

PAGES_REPO_DIR = os.environ["PAGES_REPO_DIR"]
AI_API_KEY = os.environ["RAKUTEN_AI_API_KEY"]
AI_MODEL = os.environ["RAKUTEN_AI_MODEL"]
CONFLUENCE_PAT = os.environ.get("CONFLUENCE_PAT", "")
CONFLUENCE_BASE_URL = "https://confluence.rakuten-it.com/confluence"
CONFLUENCE_REPORT_PARENT_ID = "6893456549"

client = OpenAI(
    api_key=AI_API_KEY,
    base_url="https://api.ai.public.rakuten-it.com/rakutenllms/v1/",
)

# Maps source file (relative to repo root) -> list of target paths (relative to pages repo root)
MAPPING = {
    # EN
    "README.md": [
        "docs/android/integration.md",
    ],
    "doc/basic/README.md": [
        "docs/android/index.md",
    ],
    "doc/basic/LOGIN.md": [
        "docs/android/login.md",
    ],
    "doc/basic/MissionAchivement.md": [
        "docs/android/mission.md",
    ],
    "doc/basic/SdkPortal.md": [
        "docs/android/ui.md",
    ],
    "doc/basic/UserInfo.md": [
        "docs/android/index.md",
    ],
    "doc/consent/README.md": [
        "docs/android/consent.md",
    ],
    "doc/faq/README.md": [
        "docs/android/faq.md",
    ],
    "doc/migration/README.md": [
        "docs/android/migration.md",
    ],
    "doc/migration/v8-migration.md": [
        "docs/android/migration.md",
    ],
    "doc/migration/migrate-from-v1.md": [
        "docs/android/migration.md",
    ],
    "doc/extension/README.md": [
        "docs/android/js-extension.md",
    ],
    "doc/core/README.md": [
        "docs/android/reward-config.md",
        "docs/android/app-locale.md",
        "docs/android/debugging.md",
    ],
    "doc/core/RakutenReward.md": [
        "docs/android/api-rakuten-reward.md",
        "docs/android/api-rakuten-reward-coroutine.md",
    ],
    "doc/apiData/README.md": [
        "docs/android/api-rakuten-reward.md",
    ],
    # JA
    "doc/ja/README.md": [
        "docs/ja/android/integration.md",
    ],
    "doc/ja/basic/README.md": [
        "docs/ja/android/index.md",
    ],
    "doc/ja/basic/LOGIN.md": [
        "docs/ja/android/login.md",
    ],
    "doc/ja/basic/MissionAchivement.md": [
        "docs/ja/android/mission.md",
    ],
    "doc/ja/basic/SdkPortal.md": [
        "docs/ja/android/ui.md",
    ],
    "doc/ja/basic/UserInfo.md": [
        "docs/ja/android/index.md",
    ],
    "doc/ja/consent/README.md": [
        "docs/ja/android/consent.md",
    ],
    "doc/ja/faq/README.md": [
        "docs/ja/android/faq.md",
    ],
    "doc/ja/extension/README.md": [
        "docs/ja/android/js-extension.md",
    ],
    "doc/ja/core/README.md": [
        "docs/ja/android/reward-config.md",
        "docs/ja/android/app-locale.md",
        "docs/ja/android/debugging.md",
    ],
    "doc/ja/core/RakutenReward.md": [
        "docs/ja/android/api-rakuten-reward.md",
        "docs/ja/android/api-rakuten-reward-coroutine.md",
    ],
    "doc/ja/apiData/README.md": [
        "docs/ja/android/api-rakuten-reward.md",
    ],
}

# Maps source file -> list of Confluence Android page dicts {id, title}
CONFLUENCE_MAPPING = {
    "README.md": [
        {"id": "6863539179", "title": "1 - Introduction (Android)"},
        {"id": "6863539182", "title": "3 - Setup (Android)"},
        {"id": "6863539186", "title": "4 - Initialization (Android)"},
    ],
    "doc/basic/LOGIN.md": [
        {"id": "6863539190", "title": "5 - Authentication (Android)"},
    ],
    "doc/basic/MissionAchivement.md": [
        {"id": "6863539194", "title": "6 - Missions and Points (Android)"},
    ],
    "doc/consent/README.md": [
        {"id": "6863539202", "title": "7 - Consent (Android)"},
    ],
    "doc/basic/SdkPortal.md": [
        {"id": "6863539213", "title": "8 - Portal UI (Android)"},
    ],
    "doc/sps/README.md": [
        {"id": "6863539236", "title": "9 - SPS Ads (Android)"},
    ],
    "doc/extension/README.md": [
        {"id": "6863539157", "title": "10 - JavaScript Extension (Android)"},
    ],
    "doc/core/README.md": [
        {"id": "6863539161", "title": "11 - Configuration (Android)"},
    ],
    "doc/apiData/README.md": [
        {"id": "6863539172", "title": "12 - API Data (Android)"},
    ],
    "doc/APIReference/README.md": [
        {"id": "6863539176", "title": "13 - API Reference (Android)"},
    ],
    "doc/core/RakutenReward.md": [
        {"id": "6863539176", "title": "13 - API Reference (Android)"},
    ],
}

SYSTEM_PROMPT = """You are a technical documentation editor for the Rakuten Reward Android SDK.

You will receive:
- DIFF: a git diff showing exactly what changed in a source documentation file from the SDK repository
- TARGET: the corresponding public-facing documentation page on the GitHub Pages site

Your task:
1. Read the DIFF carefully — lines starting with + were added, lines starting with - were removed.
2. Apply only those specific changes to TARGET, adapting them to match TARGET's tone, formatting, and style.
3. Do not rewrite or restructure sections that were not touched by the diff.
4. Skip any changes related to RID token, RAE token, or internal Rakuten authentication mechanisms — these are internal details that must not be disclosed publicly.
5. Return ONLY the complete updated TARGET file content with no explanation or commentary."""

CONFLUENCE_REVIEW_PROMPT = """You are a technical documentation editor for the Rakuten Reward Android SDK.

You will receive:
- DIFF: a git diff showing exactly what changed in a source documentation file
- CURRENT_PAGE: the current HTML content of the corresponding Confluence page

Your task: produce a concise HTML review summary listing what needs to change in the Confluence page.

Rules:
1. Only describe changes derived from the DIFF.
2. Skip any changes related to RID token, RAE token, or internal Rakuten authentication mechanisms — do not include these.
3. For each change needed, identify the section and provide the current text and proposed replacement.
4. Use this HTML structure for each change item:
   <ul><li><strong>Section:</strong> ...<br/><strong>Current:</strong> <code>...</code><br/><strong>Proposed:</strong> <code>...</code></li></ul>
5. If no changes are needed for this page, return exactly: <p>No changes needed.</p>
6. Return ONLY the HTML content, no prose explanation."""


def get_diff(source_path):
    result = subprocess.run(
        ["git", "diff", "HEAD~1", "HEAD", "--", source_path],
        capture_output=True, text=True
    )
    return result.stdout.strip()


def update_page(source_path, target_rel_path):
    target_abs_path = os.path.join(PAGES_REPO_DIR, target_rel_path)

    if not os.path.exists(target_abs_path):
        print(f"  SKIP: target not found: {target_abs_path}")
        return

    diff = get_diff(source_path)
    if not diff:
        print(f"  SKIP: no diff found for {source_path}")
        return

    target_content = open(target_abs_path, encoding="utf-8").read()

    response = client.chat.completions.create(
        model=AI_MODEL,
        temperature=0.0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"DIFF:\n{diff}\n\nTARGET:\n{target_content}",
            },
        ],
    )

    updated = response.choices[0].message.content
    with open(target_abs_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"  updated: {target_rel_path}")


def update_kdoc_link():
    readme = open("README.md", encoding="utf-8").read()
    match = re.search(r'https://rakuten-ads\.github\.io/products/mission/android/kdoc/[^\s\)\"\']+', readme)
    if not match:
        print("  SKIP: KDoc URL not found in README.md")
        return

    new_url = match.group(0)
    config_path = os.path.join(PAGES_REPO_DIR, "docs/.vitepress/config.mjs")
    if not os.path.exists(config_path):
        print(f"  SKIP: config.mjs not found at {config_path}")
        return

    config = open(config_path, encoding="utf-8").read()
    updated = re.sub(
        r'https://rakuten-ads\.github\.io/products/mission/android/kdoc/[^\s\)\"\']+',
        new_url,
        config
    )

    if updated == config:
        print("  KDoc link already up to date in config.mjs")
        return

    with open(config_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"  updated: docs/.vitepress/config.mjs (KDoc → {new_url})")


# --- Confluence review report ---

def get_latest_version():
    readme = open("README.md", encoding="utf-8").read()
    match = re.search(r'^\|\s*(\d+\.\d+\.\d+)\s*\|', readme, re.MULTILINE)
    return match.group(1) if match else "unknown"


def get_confluence_page(page_id):
    import requests
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content/{page_id}?expand=body.storage,version,title"
    resp = requests.get(
        url,
        headers={"Authorization": f"Bearer {CONFLUENCE_PAT}", "Accept": "application/json"},
    )
    resp.raise_for_status()
    return resp.json()


def build_confluence_review_section(source_path, page_info):
    diff = get_diff(source_path)
    if not diff:
        return None

    page_id = page_info["id"]
    page_title = page_info["title"]
    page_url = f"{CONFLUENCE_BASE_URL}/pages/viewpage.action?pageId={page_id}"

    try:
        page_data = get_confluence_page(page_id)
        current_html = page_data["body"]["storage"]["value"]
    except Exception as e:
        print(f"  WARN: could not fetch Confluence page {page_id}: {e}")
        return None

    response = client.chat.completions.create(
        model=AI_MODEL,
        temperature=0.0,
        messages=[
            {"role": "system", "content": CONFLUENCE_REVIEW_PROMPT},
            {"role": "user", "content": f"DIFF:\n{diff}\n\nCURRENT_PAGE:\n{current_html}"},
        ],
    )
    proposed = response.choices[0].message.content.strip()

    if "<p>No changes needed.</p>" in proposed:
        print(f"  no changes needed: {page_title}")
        return None

    print(f"  changes found: {page_title}")
    return f'<h2><a href="{page_url}">{page_title}</a></h2>\n{proposed}'


def create_confluence_report_page(version, sections_html):
    import requests
    title = f"Android {version} Guide Update"
    body = (
        "<p>Proposed changes generated from the latest commit. "
        "Review each section below and apply the changes manually to the linked pages.</p>\n"
        + "\n<hr/>\n".join(sections_html)
    )
    payload = {
        "type": "page",
        "title": title,
        "ancestors": [{"id": CONFLUENCE_REPORT_PARENT_ID}],
        "space": {"key": "RADS"},
        "body": {
            "storage": {
                "value": body,
                "representation": "storage",
            }
        },
    }
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content"
    resp = requests.post(
        url,
        json=payload,
        headers={
            "Authorization": f"Bearer {CONFLUENCE_PAT}",
            "Content-Type": "application/json",
        },
    )
    resp.raise_for_status()
    created = resp.json()
    page_url = f"{CONFLUENCE_BASE_URL}/pages/viewpage.action?pageId={created['id']}"
    print(f"  report page created: {page_url}")
    return page_url


def sync_confluence_review(changed_files):
    if not CONFLUENCE_PAT:
        print("CONFLUENCE_PAT not set — skipping Confluence review.")
        return

    print("\nGenerating Confluence review report...")
    version = get_latest_version()
    seen_pages = set()
    sections = []

    for source_file in changed_files:
        cf_pages = CONFLUENCE_MAPPING.get(source_file)
        if not cf_pages:
            continue
        for page_info in cf_pages:
            pid = page_info["id"]
            if pid in seen_pages:
                continue
            seen_pages.add(pid)
            print(f"  Analysing: {page_info['title']}")
            section = build_confluence_review_section(source_file, page_info)
            if section:
                sections.append(section)

    if sections:
        create_confluence_report_page(version, sections)
    else:
        print("  No Confluence changes needed.")


def main():
    changed_files = [f.strip() for f in sys.argv[1:] if f.strip()]
    if not changed_files:
        print("No changed files provided.")
        return

    # GitHub Pages sync
    seen_targets = set()
    for source_file in changed_files:
        targets = MAPPING.get(source_file)
        if not targets:
            print(f"No mapping for: {source_file} — skipping")
            continue
        print(f"Processing: {source_file}")
        if source_file == "README.md":
            update_kdoc_link()
        for target in targets:
            if target in seen_targets:
                print(f"  already updated: {target}")
                continue
            seen_targets.add(target)
            update_page(source_file, target)

    # Confluence review report
    sync_confluence_review(changed_files)


if __name__ == "__main__":
    main()
