# ============================================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# MAIN AUTONOMOUS PIPELINE
# ============================================================

from planner_agent import create_plan
from architect_agent import create_architecture
from coder_agent import create_project_structure
from testing_agent import run_tests
from review_agent import review_project
from repair_agent import repair_project
from security_agent import scan_project
from verification_agent import verify_project

from pipeline_state import PipelineState


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
    # CREATE PIPELINE STATE
    # --------------------------------------------------------

    state = PipelineState(
        requirement
    )

    state.final_status = "Running"
    state.save()

    # --------------------------------------------------------
    # 1. PLANNER
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("1️⃣ PLANNER AGENT")
    print("=" * 70)

    state.update_agent(
        "Planner",
        "Running"
    )

    try:

        plan = create_plan(
            requirement
        )

        state.plan = plan

        state.update_agent(
            "Planner",
            "Completed",
            plan
        )

        print(
            "✅ Development plan created."
        )

    except Exception as error:

        state.update_agent(
            "Planner",
            "Failed",
            str(error)
        )

        state.set_final_status(
            "Failed"
        )

        print(
            f"❌ Planner failed: {error}"
        )

        return {
            "final_status": False,
            "error": str(error)
        }

    # --------------------------------------------------------
    # 2. ARCHITECT
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("2️⃣ ARCHITECT AGENT")
    print("=" * 70)

    state.update_agent(
        "Architect",
        "Running"
    )

    try:

        architecture = create_architecture(
            plan
        )

        state.architecture = architecture

        state.update_agent(
            "Architect",
            "Completed",
            architecture
        )

        print(
            "✅ System architecture created."
        )

    except Exception as error:

        state.update_agent(
            "Architect",
            "Failed",
            str(error)
        )

        state.set_final_status(
            "Failed"
        )

        print(
            f"❌ Architect failed: {error}"
        )

        return {
            "final_status": False,
            "error": str(error)
        }

    # --------------------------------------------------------
    # 3. CODER
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("3️⃣ CODING AGENT")
    print("=" * 70)

    state.update_agent(
        "Coder",
        "Running"
    )

    project_name = (
        requirement
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "")
        .replace("?", "")
    )

    try:

        project_path = create_project_structure(
            project_name,
            architecture
        )

        state.project_name = project_name
        state.project_path = project_path

        state.update_agent(
            "Coder",
            "Completed",
            project_path
        )

        print(
            f"✅ Project created at: {project_path}"
        )

    except Exception as error:

        state.update_agent(
            "Coder",
            "Failed",
            str(error)
        )

        state.set_final_status(
            "Failed"
        )

        print(
            f"❌ Coder failed: {error}"
        )

        return {
            "final_status": False,
            "error": str(error)
        }

    # --------------------------------------------------------
    # 4. TESTING
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("4️⃣ TESTING AGENT")
    print("=" * 70)

    state.update_agent(
        "Tester",
        "Running"
    )

    try:

        test_result = run_tests(
            project_path
        )

        state.test_result = test_result

        if test_result["success"]:

            state.update_agent(
                "Tester",
                "Passed",
                test_result
            )

            print(
                "✅ All tests passed."
            )

        else:

            state.update_agent(
                "Tester",
                "Failed",
                test_result
            )

            print(
                "❌ Tests failed."
            )

    except Exception as error:

        state.update_agent(
            "Tester",
            "Failed",
            str(error)
        )

        print(
            f"❌ Testing failed: {error}"
        )

    # --------------------------------------------------------
    # 5. REVIEW
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("5️⃣ REVIEW AGENT")
    print("=" * 70)

    state.update_agent(
        "Reviewer",
        "Running"
    )

    try:

        review_report = review_project(
            project_path
        )

        state.review_report = review_report

        total_review_issues = sum(
            len(issues)
            for issues in review_report.values()
        )

        if total_review_issues == 0:

            state.update_agent(
                "Reviewer",
                "Passed",
                review_report
            )

            print(
                "✅ Code review passed."
            )

        else:

            state.update_agent(
                "Reviewer",
                "Completed",
                review_report
            )

            print(
                f"⚠️ {total_review_issues} "
                f"review issue(s) detected."
            )

    except Exception as error:

        state.update_agent(
            "Reviewer",
            "Failed",
            str(error)
        )

        print(
            f"❌ Review failed: {error}"
        )

    # --------------------------------------------------------
    # 6. REPAIR
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("6️⃣ REPAIR AGENT")
    print("=" * 70)

    state.update_agent(
        "Repairer",
        "Running"
    )

    try:

        repair_result = repair_project(
            project_path,
            review_report
        )

        state.repair_result = repair_result

        state.update_agent(
            "Repairer",
            "Completed",
            repair_result
        )

        print(
            "✅ Repair stage completed."
        )

    except Exception as error:

        state.update_agent(
            "Repairer",
            "Failed",
            str(error)
        )

        print(
            f"❌ Repair failed: {error}"
        )

    # --------------------------------------------------------
    # 7. SECURITY
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("7️⃣ SECURITY AGENT")
    print("=" * 70)

    state.update_agent(
        "Security",
        "Running"
    )

    try:

        security_report = scan_project(
            project_path
        )

        state.security_report = security_report

        total_security_issues = sum(
            len(issues)
            for issues in security_report.values()
        )

        if total_security_issues == 0:

            state.update_agent(
                "Security",
                "Passed",
                security_report
            )

            print(
                "✅ No obvious security issues detected."
            )

        else:

            state.update_agent(
                "Security",
                "Completed",
                security_report
            )

            print(
                f"🚨 {total_security_issues} "
                f"security issue(s) detected."
            )

    except Exception as error:

        state.update_agent(
            "Security",
            "Failed",
            str(error)
        )

        print(
            f"❌ Security scan failed: {error}"
        )

    # --------------------------------------------------------
    # 8. VERIFICATION
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("8️⃣ VERIFICATION AGENT")
    print("=" * 70)

    state.update_agent(
        "Verification",
        "Running"
    )

    try:

        verification_result = verify_project(
            project_path,
            test_result,
            review_report,
            security_report
        )

        state.verification_result = (
            verification_result
        )

        if verification_result["final_status"]:

            state.update_agent(
                "Verification",
                "Passed",
                verification_result
            )

            state.set_final_status(
                "Verified"
            )

        else:

            state.update_agent(
                "Verification",
                "Failed",
                verification_result
            )

            state.set_final_status(
                "Failed"
            )

    except Exception as error:

        state.update_agent(
            "Verification",
            "Failed",
            str(error)
        )

        state.set_final_status(
            "Failed"
        )

        verification_result = {
            "final_status": False,
            "error": str(error)
        }

        print(
            f"❌ Verification failed: {error}"
        )

    # --------------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("📦 FINAL RESULT")
    print("=" * 70)

    if state.final_status == "Verified":

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