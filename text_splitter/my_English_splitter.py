import re
from typing import List, Optional, Any

class My_English_splitter:
    def __init__(
        self,
        separators: Optional[List[str]] = None,
        keep_separator: bool = True,
        is_separator_regex: bool = True,
        **kwargs: Any,
    ) -> None:
        """Create a new English TextSplitter."""
        self.keep_separator = keep_separator
        self.separators = separators or [
            "\n\n",
            "\n",
            r"\.\s|\!\s|\?\s",
            ";|:\s",
            ",|\s"
        ]
        self.is_separator_regex = is_separator_regex
        self.chunk_size = kwargs.get('chunk_size', 100)  # Default chunk size
        self.length_function = kwargs.get('length_function', len)  # Default length function

    def _split_text(self, text: str, separators: List[str]) -> List[str]:
        """Split incoming text and return chunks."""
        final_chunks = []
        separator = separators[-1]
        new_separators = []

        for i, _s in enumerate(separators):
            _separator = _s if self.is_separator_regex else re.escape(_s)
            if _s == "":
                separator = _s
                break
            if re.search(_separator, text):
                separator = _s
                new_separators = separators[i + 1:]
                break

        _separator = separator if self.is_separator_regex else re.escape(separator)
        splits = self._split_text_with_regex(text, _separator)

        _good_splits = []
        _separator = "" if self.keep_separator else separator
        for s in splits:
            if self.length_function(s) < self.chunk_size:
                _good_splits.append(s)
            else:
                if _good_splits:
                    merged_text = self._merge_splits(_good_splits, _separator)
                    final_chunks.extend(merged_text)
                    _good_splits = []
                if not new_separators:
                    final_chunks.append(s)
                else:
                    other_info = self._split_text(s, new_separators)
                    final_chunks.extend(other_info)
        if _good_splits:
            merged_text = self._merge_splits(_good_splits, _separator)
            final_chunks.extend(merged_text)

        return [re.sub(r"\n{2,}", "\n", chunk.strip()) for chunk in final_chunks if chunk.strip() != ""]

    def _split_text_with_regex(self, text: str, separator: str) -> List[str]:
        """Split text using the given regex separator."""
        if self.keep_separator:
            splits = re.split(f"({separator})", text)
            return [s for s in splits if s]
        else:
            return re.split(separator, text)

    def segment_text(self, text: str) -> List[str]:
        """Segment the text into words."""
        return text.split()

    def _merge_splits(self, splits: List[str], separator: str) -> List[str]:
        """Merge splits to fit within the chunk size."""
        merged_texts = []
        current_text = ""
        for split in splits:
            if len(current_text) + len(split) + len(separator) <= self.chunk_size:
                current_text += split + separator
            else:
                merged_texts.append(current_text.strip(separator))
                current_text = split + separator
        if current_text:
            merged_texts.append(current_text.strip(separator))
        return merged_texts
