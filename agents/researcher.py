from langchain.tools import tool
from langchain_community.utilities.arxiv import ArxivAPIWrapper


class ResearcherTools:

    @tool("arXiv Search")
    def search_arxiv(query: str) -> str:
        """Search arXiv for research papers related to a query."""

        arxiv = ArxivAPIWrapper(
            top_k_results=3,
            load_max_docs=3
        )

        results = arxiv.run(query)

        return results