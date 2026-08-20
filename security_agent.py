# ============================================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# PHASE 7 - SECURITY AGENT
# ============================================================

import os
import re


# ============================================================
# FIND PYTHON FILES
# ============================================================

def find_python_files(project_path):

    python_files = []

    for root, directories, files in os.walk(project_path):

        # Ignore cache and virtual-environment folders
        directories[:] = [
            directory
            for directory in directories
            if directory not in ["venv", "__pycache__"]
        ]

        for file in files:

            if file.endswith(".py"):

                python_files.append(
                    os.path.join(root, file)
                )

    return python_files


# ============================================================
# SECURITY SCAN
# ============================================================

def scan_file(file_path):

    vulnerabilities = []

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            source_code = file.read()

    except Exception as error:

        return [
            f"Could not read file: {error}"
        ]

    # Convert to lowercase for easier detection
    code_lower = source_code.lower()

    # --------------------------------------------------------
    # 1. Hardcoded API keys / secrets
    # --------------------------------------------------------

    secret_patterns = [
        r"api[_-]?key\s*=\s*['\"][^'\"]+['\"]",
        r"secret[_-]?key\s*=\s*['\"][^'\"]+['\"]",
        r"password\s*=\s*['\"][^'\"]+['\"]",
        r"token\s*=\s*['\"][^'\"]+['\"]"
    ]

    for pattern in secret_patterns:

        if re.search(pattern, source_code, re.IGNORECASE):

            vulnerabilities.append(
                "Possible hardcoded secret detected."
            )

            break

    # --------------------------------------------------------
    # 2. eval()
    # --------------------------------------------------------

    if re.search(
        r"\beval\s*\(",
        source_code
    ):

        vulnerabilities.append(
            "Dangerous eval() usage detected."
        )

    # --------------------------------------------------------
    # 3. exec()
    # --------------------------------------------------------

    if re.search(
        r"\bexec\s*\(",
        source_code
    ):

        vulnerabilities.append(
            "Dangerous exec() usage detected."
        )

    # --------------------------------------------------------
    # 4. os.system()
    # --------------------------------------------------------

    if re.search(
        r"os\.system\s*\(",
        source_code
    ):

        vulnerabilities.append(
            "Potentially unsafe os.system() usage detected."
        )

    # --------------------------------------------------------
    # 5. subprocess shell=True
    # --------------------------------------------------------

    if re.search(
        r"subprocess\.[a-zA-Z_]+\s*\([^)]*shell\s*=\s*True",
        source_code,
        re.IGNORECASE
    ):

        vulnerabilities.append(
            "subprocess with shell=True detected."
        )

    # --------------------------------------------------------
    # 6. SQL string construction
    # --------------------------------------------------------

    sql_patterns = [
        r"SELECT\s+.*\+",
        r"INSERT\s+.*\+",
        r"UPDATE\s+.*\+",
        r"DELETE\s+.*\+"
    ]

    for pattern in sql_patterns:

        if re.search(
            pattern,
            source_code,
            re.IGNORECASE
        ):

            vulnerabilities.append(
                "Possible unsafe SQL string construction detected."
            )

            break

    # --------------------------------------------------------
    # 7. HTTP without HTTPS
    # --------------------------------------------------------

    if "http://" in code_lower:

        vulnerabilities.append(
            "Unencrypted HTTP URL detected."
        )

    return vulnerabilities


# ============================================================
# SCAN PROJECT
# ============================================================

def scan_project(project_path):

    print("\n🛡️ Security Agent is scanning the project...\n")

    python_files = find_python_files(
        project_path
    )

    report = {}

    for file_path in python_files:

        relative_path = os.path.relpath(
            file_path,
            project_path
        )

        vulnerabilities = scan_file(
            file_path
        )

        report[relative_path] = vulnerabilities

    return report


# ============================================================
# DISPLAY SECURITY REPORT
# ============================================================

def display_security_report(report):

    print("=" * 70)
    print("🛡️ SECURITY REPORT")
    print("=" * 70)

    total_files = len(report)

    total_vulnerabilities = sum(
        len(vulnerabilities)
        for vulnerabilities in report.values()
    )

    print(f"\nPython files scanned: {total_files}")
    print(
        f"Potential security issues: "
        f"{total_vulnerabilities}"
    )

    for file_path, vulnerabilities in report.items():

        print("\n" + "-" * 70)

        print(f"📄 {file_path}")

        if not vulnerabilities:

            print("  ✅ No obvious security issues detected.")

        else:

            for vulnerability in vulnerabilities:

                print(
                    f"  🚨 {vulnerability}"
                )

    print("\n" + "=" * 70)


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

        report = scan_project(
            project_path
        )

        display_security_report(
            report
        )