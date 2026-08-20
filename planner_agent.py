# ============================================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# PHASE 1 - PLANNER AGENT
# ============================================================

def create_plan(requirement):

    print("\n🧠 Planner Agent is analyzing the requirement...\n")

    # --------------------------------------------------------
    # Temporary local AI simulation
    # --------------------------------------------------------
    plan = {
        "project": requirement,

        "objective": (
            "Analyze the user's software requirement and "
            "produce a structured development plan."
        ),

        "requirements": [
            "Understand the user's objective",
            "Identify required features",
            "Identify technical requirements",
            "Define system components",
            "Define testing requirements",
            "Define security requirements"
        ],

        "technology_stack": [
            "Python",
            "FastAPI",
            "PostgreSQL",
            "REST API",
            "Automated Testing"
        ],

        "components": [
            "User Interface",
            "Backend API",
            "Database",
            "Business Logic",
            "Authentication",
            "Testing System"
        ],

        "development_tasks": [
            "Analyze requirements",
            "Design system architecture",
            "Design database",
            "Implement backend",
            "Implement business logic",
            "Implement authentication",
            "Create automated tests",
            "Perform security checks",
            "Verify final system"
        ],

        "testing": [
            "Unit testing",
            "Integration testing",
            "API testing",
            "Error handling testing"
        ],

        "security": [
            "Authentication",
            "Authorization",
            "Input validation",
            "Secret management",
            "Dependency security"
        ]
    }

    return plan


# ============================================================
# DISPLAY PLAN
# ============================================================

def display_plan(plan):

    print("=" * 70)
    print("📋 SOFTWARE DEVELOPMENT PLAN")
    print("=" * 70)

    print(f"\n📌 PROJECT:\n{plan['project']}")

    print("\n🎯 OBJECTIVE:")
    print(plan["objective"])

    print("\n📋 REQUIREMENTS:")

    for item in plan["requirements"]:
        print(f"  • {item}")

    print("\n🛠️ TECHNOLOGY STACK:")

    for item in plan["technology_stack"]:
        print(f"  • {item}")

    print("\n🏗️ SYSTEM COMPONENTS:")

    for item in plan["components"]:
        print(f"  • {item}")

    print("\n⚙️ DEVELOPMENT TASKS:")

    for number, task in enumerate(plan["development_tasks"], 1):
        print(f"  {number}. {task}")

    print("\n🧪 TESTING:")

    for item in plan["testing"]:
        print(f"  • {item}")

    print("\n🛡️ SECURITY:")

    for item in plan["security"]:
        print(f"  • {item}")

    print("\n" + "=" * 70)


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("🤖 AUTONOMOUS AI SOFTWARE ENGINEER")
    print("=" * 70)

    requirement = input(
        "\nWhat software do you want to build?\n> "
    )

    plan = create_plan(requirement)

    display_plan(plan)