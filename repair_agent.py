# ============================================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# PHASE 6 - REPAIR AGENT
# ============================================================

import os
import re


# ============================================================
# REPAIR RESULT
# ============================================================

def repair_project(project_path, review_report):

    print("\n🔧 Repair Agent is analyzing detected issues...\n")

    repaired_files = []
    remaining_issues = []

    for relative_path, issues in review_report.items():

        if not issues:
            continue

        file_path = os.path.join(
            project_path,
            relative_path
        )

        if not os.path.exists(file_path):
            remaining_issues.extend(
                [f"{relative_path}: file not found"]
            )
            continue

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:
                source_code = file.read()

            original_code = source_code

            # ------------------------------------------------
            # Repair TODO comments
            # ------------------------------------------------

            if "TODO" in source_code:

                source_code = re.sub(
                    r"#\s*TODO.*",
                    "# TODO item reviewed by Repair Agent",
                    source_code
                )

            # ------------------------------------------------
            # Repair bare except
            # ------------------------------------------------

            if re.search(
                r"except\s*:",
                source_code
            ):

                source_code = re.sub(
                    r"except\s*:",
                    "except Exception:",
                    source_code
                )

            # ------------------------------------------------
            # Check whether anything changed
            # ------------------------------------------------

            if source_code != original_code:

                with open(
                    file_path,
                    "w",
                    encoding="utf-8"
                ) as file:

                    file.write(source_code)

                repaired_files.append(
                    relative_path
                )

            else:

                remaining_issues.extend(
                    [
                        f"{relative_path}: {issue}"
                        for issue in issues
                    ]
                )

        except Exception as error:

            remaining_issues.append(
                f"{relative_path}: Repair failed - {error}"
            )

    return {
        "repaired_files": repaired_files,
        "remaining_issues": remaining_issues
    }


# ============================================================
# DISPLAY REPAIR RESULT
# ============================================================

def display_repair_result(result):

    print("=" * 70)
    print("🔧 REPAIR RESULTS")
    print("=" * 70)

    if result["repaired_files"]:

        print("\n✅ Files repaired:")

        for file_path in result["repaired_files"]:

            print(f"  • {file_path}")

    else:

        print("\nℹ️ No automatic repairs were necessary.")

    if result["remaining_issues"]:

        print("\n⚠️ Issues requiring further review:")

        for issue in result["remaining_issues"]:

            print(f"  • {issue}")

    else:

        print("\n✅ No unresolved repair issues.")

    print("\n" + "=" * 70)


# ============================================================
# DEMO REVIEW REPORT
# ============================================================

def create_demo_review_report():

    """
    Temporary demo report.

    Later the Review Agent will provide this
    automatically.
    """

    return {
        "app/main.py": [
            "Example issue for repair testing."
        ]
    }


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("🤖 AUTONOMOUS AI SOFTWARE ENGINEER")
    print("=" * 70)

    project_path = input(
        "\nEnter generated project path:\n> "
    ).strip()

    if not os.path.exists(project_path):

        print("\n❌ Project path does not exist.")

    else:

        review_report = create_demo_review_report()

        result = repair_project(
            project_path,
            review_report
        )

        display_repair_result(result)