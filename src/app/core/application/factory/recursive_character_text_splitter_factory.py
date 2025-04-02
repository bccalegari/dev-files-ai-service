from langchain_text_splitters import RecursiveCharacterTextSplitter


class RecursiveCharacterTextSplitterFactory:
    @staticmethod
    def execute() -> RecursiveCharacterTextSplitter:
        return RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=80,
            length_function=len,
            is_separator_regex=False
        )
