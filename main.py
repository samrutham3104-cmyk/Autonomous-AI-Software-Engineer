# ============================================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# MAIN AUTONOMOUS PIPELINE
# ============================================================

import os

from planner_agent import create_plan
from architect_agent import create_architecture
from coder_agent import create_project_structure
from testing_agent import run_tests
from review_agent import review_project
from repair_agent import repair_project
from security_agent import scan_project
from verification_agent import verify_project


# ============================================================
# DISPLAY HEADER
# ============================================================

def display_header():

    print("=" * 70)
    print("🤖 AUTONOMOUS AI SOFTWARE ENGINEER")
    print("=" * 70)

    print(
        "\nThe system will automatically run:"
    )

    print(
        """
🧠 Planner
🏗️ Architect
💻 Coder
🧪 Tester
🔍 Reviewer
🔧 Repairer
🛡️ Security
✅ Verification
"""
    )


# ============================================================
# MAIN PIPELINE
# ============================================================

def run_pipeline(requirement):

    # --------------------------------------------------------
    # 1. PLANNER
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("1️⃣ PLANNER AGENT")
    print("=" * 70)

    plan = create_plan(
        requirement
    )

    print("✅ Development plan created.")

    # --------------------------------------------------------
    # 2. ARCHITECT
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("2️⃣ ARCHITECT AGENT")
    print("=" * 70)

    architecture = create_architecture(
        plan
    )

    print("✅ System architecture created.")

    # --------------------------------------------------------
    # 3. CODER
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("3️⃣ CODING AGENT")
    print("=" * 70)

    project_name = (
        requirement
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "")
        .replace("?", "")
    )

    project_path = create_project_structure(
        project_name,
        architecture
    )

    print(
        f"✅ Project created at: {project_path}"
    )

    # --------------------------------------------------------
    # 4. TESTING
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("4️⃣ TESTING AGENT")
    print("=" * 70)

    test_result = run_tests(
        project_path
    )

    if test_result["success"]:

        print("✅ All tests passed.")

    else:

        print("❌ Tests failed.")

    # --------------------------------------------------------
    # 5. REVIEW
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("5️⃣ REVIEW AGENT")
    print("=" * 70)

    review_report = review_project(
        project_path
    )

    total_review_issues = sum(
        len(issues)
        for issues in review_report.values()
    )

    if total_review_issues == 0:

        print("✅ Code review passed.")

    else:

        print(
            f"⚠️ {total_review_issues} "
            f"review issue(s) detected."
        )

    # --------------------------------------------------------
    # 6. REPAIR
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("6️⃣ REPAIR AGENT")
    print("=" * 70)

    repair_result = repair_project(
        project_path,
        review_report
    )

    print(
        f"✅ Repair stage completed."
    )

    # --------------------------------------------------------
    # 7. SECURITY
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("7️⃣ SECURITY AGENT")
    print("=" * 70)

    security_report = scan_project(
        project_path
    )

    total_security_issues = sum(
        len(issues)
        for issues in security_report.values()
    )

    if total_security_issues == 0:

        print(
            "✅ No obvious security issues detected."
        )

    else:

        print(
            f"🚨 {total_security_issues} "
            f"security issue(s) detected."
        )

    # --------------------------------------------------------
    # 8. VERIFICATION
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("8️⃣ VERIFICATION AGENT")
    print("=" * 70)

    verification_result = verify_project(
        project_path,
        test_result,
        review_report,
        security_report
    )

    # --------------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("📦 FINAL RESULT")
    print("=" * 70)

    if verification_result["final_status"]:

        print(
            "\n🎉 PROJECT VERIFIED SUCCESSFULLY!"
        )

        print(
            f"\n📁 Project:"
        )

        print(
            f"   {project_path}"
        )

    else:

        print(
            "\n⚠️ PROJECT NOT VERIFIED."
        )

        print(
            "\nAdditional work is required."
        )

    print("\n" + "=" * 70)

    return verification_result


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    display_header()

    requirement = input(
        "\nWhat software do you want to build?\n> "
    ).strip()

    if not requirement:

        print(
            "\n❌ Requirement cannot be empty."
        )

    else:

        run_pipeline(
            requirement
        )