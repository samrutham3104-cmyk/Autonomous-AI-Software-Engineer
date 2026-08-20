# ============================================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# PHASE 2 - ARCHITECT AGENT
# ============================================================

from planner_agent import create_plan


def create_architecture(plan):

    print("\n🏗️ Architect Agent is designing the system...\n")

    architecture = {
        "architecture_style": "Modular Layered Architecture",

        "backend": {
            "framework": "FastAPI",
            "language": "Python"
        },

        "database": {
            "type": "PostgreSQL",
            "purpose": "Store application data"
        },

        "modules": [
            "API Layer",
            "Business Logic Layer",
            "Database Layer",
            "Authentication Module",
            "Validation Module",
            "Testing Module",
            "Security Module"
        ],

        "project_structure": [
            "app/",
            "app/api/",
            "app/services/",
            "app/models/",
            "app/database/",
            "app/security/",
            "tests/",
            "requirements.txt",
            "README.md",
            ".env"
        ],

        "data_flow": [
            "User sends request",
            "API validates request",
            "Business logic processes request",
            "Database performs required operation",
            "Response is returned to user"
        ]
    }

    return architecture


def display_architecture(architecture):

    print("=" * 70)
    print("🏗️ SYSTEM ARCHITECTURE")
    print("=" * 70)

    print("\n📐 ARCHITECTURE STYLE:")
    print(architecture["architecture_style"])

    print("\n⚙️ BACKEND:")

    for key, value in architecture["backend"].items():
        print(f"  • {key}: {value}")

    print("\n🗄️ DATABASE:")

    for key, value in architecture["database"].items():
        print(f"  • {key}: {value}")

    print("\n🧩 MODULES:")

    for module in architecture["modules"]:
        print(f"  • {module}")

    print("\n📁 PROJECT STRUCTURE:")

    for item in architecture["project_structure"]:
        print(f"  • {item}")

    print("\n🔄 DATA FLOW:")

    for number, step in enumerate(architecture["data_flow"], 1):
        print(f"  {number}. {step}")

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

    # Planner Agent
    plan = create_plan(requirement)

    # Architect Agent
    architecture = create_architecture(plan)

    # Display architecture
    display_architecture(architecture)