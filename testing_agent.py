# ============================================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# PHASE 4 - TESTING AGENT
# ============================================================

import os
import subprocess
import sys


def run_tests(project_path):

    print("\n🧪 Testing Agent is running tests...\n")

    # --------------------------------------------------------
    # Check whether tests directory exists
    # --------------------------------------------------------

    tests_path = os.path.join(
        project_path,
        "tests"
    )

    if not os.path.exists(tests_path):

        return {
            "success": False,
            "return_code": -1,
            "output": "❌ No tests directory found."
        }

    # --------------------------------------------------------
    # Run pytest using the SAME Python environment
    # --------------------------------------------------------

    try:

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "tests"
            ],
            cwd=project_path,
            capture_output=True,
            text=True
        )

        output = result.stdout + "\n" + result.stderr

        return {
            "success": result.returncode == 0,
            "return_code": result.returncode,
            "output": output
        }

    except Exception as error:

        return {
            "success": False,
            "return_code": -1,
            "output": str(error)
        }


# ============================================================
# DISPLAY TEST RESULT
# ============================================================

def display_test_result(result):

    print("=" * 70)
    print("🧪 TEST RESULTS")
    print("=" * 70)

    if result["success"]:

        print("\n✅ ALL TESTS PASSED")

    else:

        print("\n❌ TESTS FAILED")

    print("\nTest output:")
    print("-" * 70)

    print(result["output"])

    print("-" * 70)

    print(f"\nReturn code: {result['return_code']}")

    print("=" * 70)


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("🤖 AUTONOMOUS AI SOFTWARE ENGINEER")
    print("=" * 70)

    project_path = input(
        "\nEnter generated project path:\n> "
    )

    project_path = project_path.strip()

    # --------------------------------------------------------
    # Check project path
    # --------------------------------------------------------

    if not os.path.exists(project_path):

        print("\n❌ Project path does not exist.")

    else:

        result = run_tests(project_path)

        display_test_result(result)