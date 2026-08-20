# ============================================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# PHASE 5 - REVIEW AGENT
# ============================================================

import os
import ast


# ============================================================
# FIND PYTHON FILES
# ============================================================

def find_python_files(project_path):

    python_files = []

    for root, directories, files in os.walk(project_path):

        # Ignore virtual environments and cache folders
        directories[:] = [
            directory
            for directory in directories
            if directory not in ["venv", "__pycache__"]
        ]

        for file in files:

            if file.endswith(".py"):

                full_path = os.path.join(
                    root,
                    file
                )

                python_files.append(full_path)

    return python_files


# ============================================================
# ANALYZE PYTHON FILE
# ============================================================

def analyze_python_file(file_path):

    issues = []

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            source_code = file.read()

        # ----------------------------------------------------
        # Check whether Python syntax is valid
        # ----------------------------------------------------

        try:

            tree = ast.parse(source_code)

        except SyntaxError as error:

            issues.append(
                f"Syntax error at line {error.lineno}: "
                f"{error.msg}"
            )

            return issues

        # ----------------------------------------------------
        # Check for functions
        # ----------------------------------------------------

        functions = [
            node
            for node in ast.walk(tree)
            if isinstance(
                node,
                (ast.FunctionDef, ast.AsyncFunctionDef)
            )
        ]

        if len(functions) == 0:

            issues.append(
                "No functions found."
            )

        # ----------------------------------------------------
        # Check for classes
        # ----------------------------------------------------

        classes = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
        ]

        # ----------------------------------------------------
        # Check for TODO comments
        # ----------------------------------------------------

        if "TODO" in source_code:

            issues.append(
                "TODO item found."
            )

        # ----------------------------------------------------
        # Check for print statements
        # ----------------------------------------------------

        print_statements = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "print"
        ]

        if len(print_statements) > 5:

            issues.append(
                "Large number of print statements detected."
            )

        # ----------------------------------------------------
        # Check for very long functions
        # ----------------------------------------------------

        for function in functions:

            function_length = (
                function.end_lineno -
                function.lineno
            )

            if function_length > 80:

                issues.append(
                    f"Function '{function.name}' "
                    f"is very long ({function_length} lines)."
                )

        # ----------------------------------------------------
        # Check for broad exception handling
        # ----------------------------------------------------

        broad_exceptions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.ExceptHandler)
            and node.type is None
        ]

        if broad_exceptions:

            issues.append(
                "Bare 'except' detected."
            )

        # ----------------------------------------------------
        # Check for hardcoded secrets
        # ----------------------------------------------------

        secret_words = [
            "password=",
            "api_key=",
            "secret_key=",
            "token="
        ]

        lowercase_source = source_code.lower()

        for word in secret_words:

            if word in lowercase_source:

                issues.append(
                    f"Possible hardcoded secret: {word}"
                )

        return issues

    except Exception as error:

        return [
            f"Could not analyze file: {error}"
        ]


# ============================================================
# REVIEW PROJECT
# ============================================================

def review_project(project_path):

    print("\n🔍 Review Agent is analyzing the project...\n")

    python_files = find_python_files(
        project_path
    )

    report = {}

    for file_path in python_files:

        relative_path = os.path.relpath(
            file_path,
            project_path
        )

        issues = analyze_python_file(
            file_path
        )

        report[relative_path] = issues

    return report


# ============================================================
# DISPLAY REVIEW
# ============================================================

def display_review(report):

    print("=" * 70)
    print("🔍 CODE REVIEW REPORT")
    print("=" * 70)

    total_files = len(report)

    total_issues = sum(
        len(issues)
        for issues in report.values()
    )

    print(f"\nPython files analyzed: {total_files}")
    print(f"Issues detected: {total_issues}")

    for file_path, issues in report.items():

        print("\n" + "-" * 70)

        print(f"📄 {file_path}")

        if not issues:

            print("  ✅ No issues detected")

        else:

            for issue in issues:

                print(f"  ⚠️ {issue}")

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

        report = review_project(
            project_path
        )

        display_review(
            report
        )