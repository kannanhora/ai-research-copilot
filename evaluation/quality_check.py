from langchain_groq import ChatGroq


class ReportEvaluator:

    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0
        )

    def evaluate(self, report: str) -> dict:
        """
        Evaluate quality of generated research report.
        """

        prompt = f"""
Evaluate the following research report on three metrics:
1. Clarity
2. Completeness
3. Accuracy

Return scores from 1–10 and a short comment.

Report:
{report}
"""

        response = self.llm.invoke(prompt)

        return {
            "evaluation": response.content
        }