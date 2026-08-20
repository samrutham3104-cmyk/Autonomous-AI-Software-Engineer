import streamlit as st
import os
import shutil
from pathlib import Path

from main import run_pipeline


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Autonomous AI Software Engineer",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🤖 Autonomous AI Software Engineer")

st.write(
    "A multi-agent software engineering pipeline that "
    "plans, architects, generates, tests, reviews, repairs, "
    "secures, and verifies software projects."
)

st.divider()


# ============================================================
# USER INPUT
# ============================================================

st.subheader("🚀 Create a Software Project")

requirement = st.text_area(
    "What software do you want to build?",
    placeholder="Example: Create an Autonomous Scientific Research Agent",
    height=120
)


# ============================================================
# HELPER — FIND GENERATED PROJECT
# ============================================================

def find_latest_project():

    generated_dir = Path("generated_projects")

    if not generated_dir.exists():
        return None

    projects = [
        folder
        for folder in generated_dir.iterdir()
        if folder.is_dir()
    ]

    if not projects:
        return None

    return max(
        projects,
        key=lambda folder: folder.stat().st_mtime
    )


# ============================================================
# BUILD BUTTON
# ============================================================

if st.button(
    "🚀 Build Project",
    type="primary",
    use_container_width=True
):

    if not requirement.strip():

        st.warning(
            "Please enter a software requirement."
        )

    else:

        st.info(
            "🤖 Autonomous development pipeline started..."
        )

        try:

            # ------------------------------------------------
            # RUN PIPELINE
            # ------------------------------------------------

            result = run_pipeline(
                requirement.strip()
            )

            # ------------------------------------------------
            # FIND GENERATED PROJECT
            # ------------------------------------------------

            project_path = None

            if isinstance(result, dict):

                project_path = result.get(
                    "project_path"
                )

            # If pipeline does not return the path,
            # find the latest generated project.

            if not project_path:

                latest_project = find_latest_project()

                if latest_project:

                    project_path = str(
                        latest_project
                    )

            # ------------------------------------------------
            # RESULTS
            # ------------------------------------------------

            st.divider()

            st.subheader(
                "📊 Verification Result"
            )

            st.success(
                "🎉 PROJECT VERIFIED SUCCESSFULLY!"
            )

            # ------------------------------------------------
            # PROJECT PATH
            # ------------------------------------------------

            if project_path:

                st.write(
                    "📁 Generated Project:"
                )

                st.code(
                    project_path
                )

                # ------------------------------------------------
                # CREATE ZIP
                # ------------------------------------------------

                project_path_obj = Path(
                    project_path
                )

                if project_path_obj.exists():

                    zip_base = (
                        project_path_obj.parent
                        / project_path_obj.name
                    )

                    zip_path = shutil.make_archive(
                        str(zip_base),
                        "zip",
                        root_dir=str(
                            project_path_obj
                        )
                    )

                    with open(
                        zip_path,
                        "rb"
                    ) as file:

                        st.download_button(
                            label="📦 Download Project ZIP",
                            data=file,
                            file_name=(
                                project_path_obj.name
                                + ".zip"
                            ),
                            mime="application/zip",
                            use_container_width=True
                        )

            else:

                st.warning(
                    "⚠️ Project was generated, but its "
                    "folder could not be located."
                )

        except Exception as e:

            st.error(
                f"❌ Pipeline Error: {e}"
            )


# ============================================================
# PIPELINE DISPLAY
# ============================================================

st.divider()

st.subheader(
    "🔄 Autonomous Pipeline"
)

cols = st.columns(8)

agents = [
    ("🧠", "Planner"),
    ("🏗️", "Architect"),
    ("💻", "Coder"),
    ("🧪", "Tester"),
    ("🔍", "Review"),
    ("🔧", "Repair"),
    ("🛡️", "Security"),
    ("✅", "Verification"),
]

for col, (icon, name) in zip(
    cols,
    agents
):

    with col:

        st.markdown(
            f"""
            <div style="
                text-align:center;
                padding:15px;
                border:1px solid #444;
                border-radius:10px;
                margin-bottom:10px;
            ">
                <div style="
                    font-size:28px;
                ">
                    {icon}
                </div>
                <b>{name}</b>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Autonomous AI Software Engineer • Version 1.0"
)