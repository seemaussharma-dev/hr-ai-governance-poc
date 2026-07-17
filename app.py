from pathlib import Path

import streamlit as st

from audit import log_event
from config import AI_DISCLOSURE, APP_NAME, APP_VERSION, PRIVACY_NOTICE, SYSTEM_TYPE
from guardrails import evaluate_question
from policy_search import PolicySearchEngine
from response_builder import build_response


st.set_page_config(
    page_title="HR AI Governance POC",
    page_icon="🛡️",
    layout="centered",
)


@st.cache_resource
def load_engine() -> PolicySearchEngine:
    return PolicySearchEngine.from_directory(Path(__file__).parent / "policies")


engine = load_engine()

st.title("🛡️ HR AI Governance POC")
st.subheader("Stage 1: Offline governed policy retrieval")

st.info(AI_DISCLOSURE)
st.warning(PRIVACY_NOTICE)

with st.sidebar:
    st.header("System information")
    st.write(f"**Application:** {APP_NAME}")
    st.write(f"**Version:** {APP_VERSION}")
    st.write(f"**Type:** {SYSTEM_TYPE}")
    st.write("**Data:** Synthetic policies only")
    st.write("**External model/API:** None")
    st.write("**Raw question logging:** Disabled")

    st.header("Approved scope")
    st.write("- Vacation and leave")
    st.write("- Remote work")
    st.write("- Expense reimbursement")
    st.write("- Equal employment opportunity and non-discrimination")

    st.header("Prohibited scope")
    st.write("- Personal employee records")
    st.write("- Salary and payroll records")
    st.write("- Medical or disability information")
    st.write("- Performance and disciplinary records")
    st.write("- Hiring, ranking, promotion, or termination decisions")

question = st.text_area(
    "Ask a general HR policy question",
    max_chars=500,
    placeholder="Example: How many vacation days do employees receive?",
)

if st.button("Submit question", type="primary"):
    decision = evaluate_question(question)

    if not decision.allowed:
        if decision.reason == "human_escalation_required":
            st.warning(decision.user_message)
            st.write(
                "**Control outcome:** Human HR escalation before policy retrieval."
            )
            audit_decision = "escalated"
        else:
            st.error(decision.user_message)
            st.write(
                "**Control outcome:** Request blocked before policy retrieval."
            )
            audit_decision = "blocked"

        st.write(
            "**Detected categories:** "
            + ", ".join(decision.categories)
        )
        st.write(
            "**Controls applied:** "
            + ", ".join(decision.controls)
        )

        log_event(
            event_type="question_evaluated",
            decision=audit_decision,
            controls=decision.controls,
            categories=decision.categories,
        )
    else:
        response = build_response(question, engine.search(question))

        if response.status == "answered":
            st.success(response.answer)
            st.markdown(
                f"**Source:** {response.source_title}, "
                f"Section: {response.source_section}, "
                f"Version: {response.source_version}"
            )
            st.caption(
                f"Retrieval assessment: {response.confidence_label}. "
                "This is general policy information, not an employment decision."
            )
            with st.expander("Governance controls applied"):
                for control in response.applied_controls:
                    st.write(f"- {control}")
            log_event(
                event_type="question_evaluated",
                decision="answered",
                controls=response.applied_controls,
                categories=decision.categories,
                source_document=response.source_title,
            )
        else:
            st.warning(response.answer)
            st.write("**Control outcome:** Human HR escalation.")
            with st.expander("Governance controls applied"):
                for control in response.applied_controls:
                    st.write(f"- {control}")
            log_event(
                event_type="question_evaluated",
                decision="escalated",
                controls=response.applied_controls,
                categories=decision.categories,
            )

st.divider()
st.caption(
    "Educational portfolio prototype. It is not legal advice, regulatory "
    "certification, or a production HR system."
)
