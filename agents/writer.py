from pydantic.v1 import BaseModel
from langchain.tools import tool


class WriterInput(BaseModel):
    content: str


class WriterTools:

    @tool("Report Writer")
    def generate_report(content: str) -> str:
        """
        Generate a structured research report from provided content.
        """

        report = f"""
Research Report
=====================

Summary
-------
{content}

Conclusion
----------
The above research findings have been organized into a structured report.
Further analysis and citations can be added to strengthen the study.
"""

        return report.strip()