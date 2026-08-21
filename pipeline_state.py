# ============================================================
# PIPELINE STATE MANAGER
# AUTONOMOUS AI SOFTWARE ENGINEER
# ============================================================

import json
import os


STATE_FILE = "pipeline_state.json"


class PipelineState:

    def __init__(self, requirement=""):

        self.requirement = requirement

        self.project_name = ""
        self.project_path = ""

        self.agents = {
            "Planner": {
                "status": "Waiting",
                "result": None
            },
            "Architect": {
                "status": "Waiting",
                "result": None
            },
            "Coder": {
                "status": "Waiting",
                "result": None
            },
            "Tester": {
                "status": "Waiting",
                "result": None
            },
            "Reviewer": {
                "status": "Waiting",
                "result": None
            },
            "Repairer": {
                "status": "Waiting",
                "result": None
            },
            "Security": {
                "status": "Waiting",
                "result": None
            },
            "Verification": {
                "status": "Waiting",
                "result": None
            }
        }

        self.plan = None
        self.architecture = None
        self.test_result = None
        self.review_report = None
        self.repair_result = None
        self.security_report = None
        self.verification_result = None

        self.current_agent = "None"
        self.progress = 0
        self.final_status = "Not Started"

    # ========================================================
    # UPDATE AGENT
    # ========================================================

    def update_agent(
        self,
        agent_name,
        status,
        result=None
    ):

        if agent_name not in self.agents:
            return

        self.agents[agent_name]["status"] = status

        if result is not None:
            self.agents[agent_name]["result"] = result

        self.current_agent = agent_name

        self.calculate_progress()

        self.save()

    # ========================================================
    # CALCULATE PROGRESS
    # ========================================================

    def calculate_progress(self):

        completed = 0

        for agent in self.agents.values():

            if agent["status"] in [
                "Completed",
                "Passed"
            ]:
                completed += 1

        total_agents = len(self.agents)

        self.progress = int(
            (completed / total_agents) * 100
        )

    # ========================================================
    # FINAL STATUS
    # ========================================================

    def set_final_status(self, status):

        self.final_status = status

        self.save()

    # ========================================================
    # SAVE STATE
    # ========================================================

    def save(self):

        data = {
            "requirement": self.requirement,
            "project_name": self.project_name,
            "project_path": self.project_path,
            "agents": self.agents,
            "plan": self.plan,
            "architecture": self.architecture,
            "test_result": self.test_result,
            "review_report": self.review_report,
            "repair_result": self.repair_result,
            "security_report": self.security_report,
            "verification_result": self.verification_result,
            "current_agent": self.current_agent,
            "progress": self.progress,
            "final_status": self.final_status
        }

        try:

            with open(
                STATE_FILE,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4,
                    default=str
                )

        except Exception as error:

            print(
                f"⚠️ Could not save pipeline state: {error}"
            )

    # ========================================================
    # LOAD STATE
    # ========================================================

    @classmethod
    def load(cls):

        if not os.path.exists(STATE_FILE):

            return cls()

        try:

            with open(
                STATE_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            state = cls(
                data.get("requirement", "")
            )

            state.project_name = data.get(
                "project_name",
                ""
            )

            state.project_path = data.get(
                "project_path",
                ""
            )

            state.agents = data.get(
                "agents",
                state.agents
            )

            state.plan = data.get(
                "plan"
            )

            state.architecture = data.get(
                "architecture"
            )

            state.test_result = data.get(
                "test_result"
            )

            state.review_report = data.get(
                "review_report"
            )

            state.repair_result = data.get(
                "repair_result"
            )

            state.security_report = data.get(
                "security_report"
            )

            state.verification_result = data.get(
                "verification_result"
            )

            state.current_agent = data.get(
                "current_agent",
                "None"
            )

            state.progress = data.get(
                "progress",
                0
            )

            state.final_status = data.get(
                "final_status",
                "Not Started"
            )

            return state

        except Exception as error:

            print(
                f"⚠️ Could not load pipeline state: {error}"
            )

            return cls()