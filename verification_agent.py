# ============================================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# PHASE 8 - VERIFICATION AGENT
# ============================================================

import os


# ============================================================
# VERIFY PROJECT STRUCTURE
# ============================================================

def verify_project_structure(project_path):

    required_items = [
        "app",
        "tests",
        "requirements.txt",
        "README.md"
    ]

    missing_items = []

    for item in required_items:

        item_path = os.path.join(
            project_path,
            item
        )

        if not os.path.exists(item_path):

            missing_items.append(item)

    return missing_items


# ============================================================
# VERIFY TEST RESULTS
# ============================================================

def verify_tests(test_result):

    if not test_result:
        return False

    return test_result.get("success", False)


# ============================================================
# VERIFY REVIEW
# ============================================================

def verify_review(review_report):

    if not review_report:
        return False

    total_issues = sum(
        len(issues)
        for issues in review_report.values()
    )

    return total_issues == 0


# ============================================================
# VERIFY SECURITY
# ============================================================

def verify_security(security_report):

    if not security_report:
        return False

    total_vulnerabilities = sum(
        len(vulnerabilities)
        for vulnerabilities
        in security_report.values()
    )

    return total_vulnerabilities == 0


# ============================================================
# FINAL VERIFICATION
# ============================================================

def verify_project(
    project_path,
    test_result,
    review_report,
    security_report
):

    print("\n🔄 Verification Agent is performing final verification...\n")

    missing_items = verify_project_structure(
        project_path
    )

    tests_passed = verify_tests(
        test_result
    )

    review_passed = verify_review(
        review_report
    )

    security_passed = verify_security(
        security_report
    )

    structure_passed = len(missing_items) == 0

    final_status = (
        structure_passed
        and tests_passed
        and review_passed
        and security_passed
    )

    return {
        "structure_passed": structure_passed,
        "tests_passed": tests_passed,
        "review_passed": review_passed,
        "security_passed": security_passed,
        "missing_items": missing_items,
        "final_status": final_status
    }


# ============================================================
# DISPLAY FINAL RESULT
# ============================================================

def display_verification(result):

    print("=" * 70)
    print("✅ FINAL VERIFICATION")
    print("=" * 70)

    print("\n📁 Project Structure:",
          "PASS" if result["structure_passed"] else "FAIL")

    print("🧪 Tests:",
          "PASS" if result["tests_passed"] else "FAIL")

    print("🔍 Code Review:",
          "PASS" if result["review_passed"] else "FAIL")

    print("🛡️ Security:",
          "PASS" if result["security_passed"] else "FAIL")

    if result["missing_items"]:

        print("\n⚠️ Missing project items:")

        for item in result["missing_items"]:

            print(f"  • {item}")

    print("\n" + "-" * 70)

    if result["final_status"]:

        print("🎉 FINAL STATUS: ✅ VERIFIED")

        print(
            "\n🚀 Project passed all verification checks."
        )

    else:

        print("❌ FINAL STATUS: NOT VERIFIED")

        print(
            "\n⚠️ Project requires additional work."
        )

    print("=" * 70)


# ============================================================
# DEMO MODE
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

        print(
            "\n⚠️ Verification Agent requires "
            "test, review, and security results."
        )

        print(
            "\nThis standalone version only checks "
            "the project structure."
        )

        missing_items = verify_project_structure(
            project_path
        )

        if not missing_items:

            print(
                "\n📁 Project Structure: ✅ PASS"
            )

        else:

            print(
                "\n📁 Project Structure: ❌ FAIL"
            )

            for item in missing_items:

                print(f"  • Missing: {item}")