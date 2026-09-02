import os
import subprocess
import sys
from openai import OpenAI

PAGES_REPO_DIR = os.environ["PAGES_REPO_DIR"]
AI_API_KEY = os.environ["RAKUTEN_AI_API_KEY"]
AI_MODEL = os.environ["RAKUTEN_AI_MODEL"]

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


def main():
    changed_files = sys.argv[1:]
    if not changed_files:
        print("No changed files provided.")
        return

    # Deduplicate targets — a target may be listed by multiple source files
    seen_targets = set()

    for source_file in changed_files:
        source_file = source_file.strip()
        targets = MAPPING.get(source_file)
        if not targets:
            print(f"No mapping for: {source_file} — skipping")
            continue
        print(f"Processing: {source_file}")
        for target in targets:
            if target in seen_targets:
                print(f"  already updated: {target}")
                continue
            seen_targets.add(target)
            update_page(source_file, target)


if __name__ == "__main__":
    main()
