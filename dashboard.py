# ============================================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# PROJECT DASHBOARD
# ============================================================

import os
import zipfile

import streamlit as st

from pipeline_state import PipelineState


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Autonomous AI Software Engineer",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# CREATE PROJECT ZIP
# ============================================================

def create_project_zip(project_path):

    if not project_path:
        return None

    if not os.path.exists(project_path):
        return None

    if not os.path.isdir(project_path):
        return None

    zip_path = os.path.join(
        os.path.dirname(project_path),
        os.path.basename(project_path) + ".zip"
    )

    try:

        with zipfile.ZipFile(
            zip_path,
            "w",
            zipfile.ZIP_DEFLATED
        ) as zip_file:

            for root, dirs, files in os.walk(
                project_path
            ):

                for file in files:

                    file_path = os.path.join(
                        root,
                        file
                    )

                    archive_path = os.path.relpath(
                        file_path,
                        os.path.dirname(project_path)
                    )

                    zip_file.write(
                        file_path,
                        archive_path
                    )

        return zip_path

    except Exception as error:

        st.error(
            f"Error creating ZIP: {error}"
        )

        return None


# ============================================================
# LOAD PIPELINE STATE
# ============================================================

state = PipelineState.load()


# ============================================================
# HEADER
# ============================================================

st.title(
    "🤖 Autonomous AI Software Engineer"
)

st.caption(
    "Multi-Agent Software Development and Verification Platform"
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header(
        "⚙️ Project Configuration"
    )

    requirement = st.text_area(
        "Software Requirement",
        value=state.requirement,
        placeholder=(
            "Example: Build a student management system"
        ),
        height=120
    )

    if st.button(
        "🚀 Initialize Pipeline",
        use_container_width=True
    ):

        if not requirement.strip():

            st.error(
                "Requirement cannot be empty."
            )

        else:

            new_state = PipelineState(
                requirement.strip()
            )

            new_state.save()

            st.success(
                "Pipeline initialized!"
            )

            st.rerun()

    st.divider()

    st.subheader(
        "Pipeline Information"
    )

    st.write(
        f"**Current Agent:** {state.current_agent}"
    )

    st.write(
        f"**Progress:** {state.progress}%"
    )

    st.write(
        f"**Final Status:** {state.final_status}"
    )


# ============================================================
# SOFTWARE REQUIREMENT
# ============================================================

st.subheader(
    "📋 Software Requirement"
)

if state.requirement:

    st.info(
        state.requirement
    )

else:

    st.warning(
        "Enter a software requirement from the sidebar."
    )


# ============================================================
# OVERALL PROGRESS
# ============================================================

st.subheader(
    "📊 Overall Progress"
)

st.progress(
    state.progress / 100
)

st.write(
    f"**{state.progress}% completed**"
)


# ============================================================
# AGENT DISPLAY FUNCTION
# ============================================================

def display_agent(icon, name):

    status = state.agents[name]["status"]

    if status in [
        "Completed",
        "Passed"
    ]:

        indicator = "🟢"

    elif status == "Running":

        indicator = "🟡"

    elif status == "Failed":

        indicator = "🔴"

    else:

        indicator = "⚪"

    st.markdown(
        f"### {icon} {name}"
    )

    st.write(
        f"{indicator} **{status}**"
    )


# ============================================================
# AGENT PIPELINE
# ============================================================

st.subheader(
    "🔄 Agent Pipeline"
)


# ============================================================
# FIRST ROW
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    display_agent(
        "🧠",
        "Planner"
    )


with col2:

    display_agent(
        "🏗️",
        "Architect"
    )


with col3:

    display_agent(
        "💻",
        "Coder"
    )


with col4:

    display_agent(
        "🧪",
        "Tester"
    )


# ============================================================
# SECOND ROW
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    display_agent(
        "🔍",
        "Reviewer"
    )


with col2:

    display_agent(
        "🔧",
        "Repairer"
    )


with col3:

    display_agent(
        "🛡️",
        "Security"
    )


with col4:

    display_agent(
        "✅",
        "Verification"
    )


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.divider()

st.subheader(
    "📁 Project Information"
)


col1, col2 = st.columns(2)


with col1:

    st.write(
        "**Project Name**"
    )

    if state.project_name:

        st.code(
            state.project_name
        )

    else:

        st.code(
            "Not generated"
        )


with col2:

    st.write(
        "**Project Path**"
    )

    if state.project_path:

        st.code(
            state.project_path
        )

    else:

        st.code(
            "Not generated"
        )


# ============================================================
# PIPELINE RESULTS
# ============================================================

st.divider()

st.subheader(
    "📊 Pipeline Results"
)


col1, col2, col3 = st.columns(3)


# ============================================================
# TEST RESULTS
# ============================================================

with col1:

    st.write(
        "**🧪 Tests**"
    )

    if state.test_result:

        if state.test_result.get(
            "success",
            False
        ):

            st.success(
                "Tests Passed"
            )

        else:

            st.error(
                "Tests Failed"
            )

    else:

        st.info(
            "Not executed"
        )


# ============================================================
# REVIEW RESULTS
# ============================================================

with col2:

    st.write(
        "**🔍 Code Review**"
    )

    if state.review_report is not None:

        try:

            total_issues = sum(
                len(issues)
                for issues in state.review_report.values()
            )

        except Exception:

            total_issues = 0

        if total_issues == 0:

            st.success(
                "No Issues"
            )

        else:

            st.warning(
                f"{total_issues} issue(s)"
            )

    else:

        st.info(
            "Not executed"
        )


# ============================================================
# SECURITY RESULTS
# ============================================================

with col3:

    st.write(
        "**🛡️ Security**"
    )

    if state.security_report is not None:

        try:

            total_security_issues = sum(
                len(issues)
                for issues in state.security_report.values()
            )

        except Exception:

            total_security_issues = 0

        if total_security_issues == 0:

            st.success(
                "No Issues"
            )

        else:

            st.error(
                f"{total_security_issues} issue(s)"
            )

    else:

        st.info(
            "Not executed"
        )


# ============================================================
# PROJECT DOWNLOAD
# ============================================================

st.divider()

st.subheader(
    "📦 Project Download"
)


if state.project_path:

    if os.path.exists(
        state.project_path
    ):

        st.write(
            "Your generated project is ready."
        )

        verification_passed = (
            state.final_status == "Verified"
        )

        if verification_passed:

            st.success(
                "✅ Project verified and ready for download."
            )

        else:

            st.warning(
                "⚠️ Project has not been verified yet."
            )


        # ----------------------------------------------------
        # CREATE ZIP
        # ----------------------------------------------------

        if st.button(
            "📦 Prepare Project ZIP",
            use_container_width=True
        ):

            with st.spinner(
                "Creating project package..."
            ):

                zip_path = create_project_zip(
                    state.project_path
                )


            if zip_path:

                st.success(
                    "Project ZIP created successfully!"
                )

                try:

                    with open(
                        zip_path,
                        "rb"
                    ) as zip_file:

                        zip_data = zip_file.read()


                    st.download_button(
                        label="📥 Download Project ZIP",
                        data=zip_data,
                        file_name=os.path.basename(
                            zip_path
                        ),
                        mime="application/zip",
                        use_container_width=True
                    )

                except Exception as error:

                    st.error(
                        f"Unable to prepare download: {error}"
                    )

            else:

                st.error(
                    "Unable to create project ZIP."
                )

    else:

        st.warning(
            "Project folder could not be found."
        )

else:

    st.info(
        "No project has been generated yet."
    )


# ============================================================
# FINAL STATUS
# ============================================================

st.divider()

st.subheader(
    "🎯 Final Status"
)


if state.final_status == "Verified":

    st.success(
        "🎉 PROJECT VERIFIED SUCCESSFULLY!"
    )


elif state.final_status == "Failed":

    st.error(
        "❌ PROJECT VERIFICATION FAILED."
    )


elif state.final_status == "Running":

    st.warning(
        "🔄 PROJECT PIPELINE IS RUNNING..."
    )


else:

    st.info(
        state.final_status
    )


# ============================================================
# REFRESH
# ============================================================

st.divider()

if st.button(
    "🔄 Refresh Dashboard",
    use_container_width=True
):

    st.rerun()