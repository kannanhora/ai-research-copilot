from langchain.tools import tool
from langchain_groq import ChatGroq


class ReviewerTools:

    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )

    @tool("Report Reviewer")
    def critique_report(report: str) -> str:
        """
        Review the generated research report and provide feedback.
        """

        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )

        prompt = f"""
Review the following research report.

Check for:
- clarity
- correctness
- completeness

Provide short feedback.

Report:
{report}
"""

        response = llm.invoke(prompt)

        return response.content