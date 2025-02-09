from unittest.mock import Mock

import bs4

from sec_parser.processing_engine.html_tag import HtmlTag
from sec_parser.semantic_elements.composite_semantic_element import (
    CompositeSemanticElement,
)

MockHtmlTag = Mock()


def test_to_dict():
    # Arrange
    tag = bs4.Tag(name="span")
    tag.string = "A" * 60

    # Act
    actual = CompositeSemanticElement(
        HtmlTag(tag),
        (),
        inner_elements=[Mock(), Mock()],
    ).to_dict()

    # Assert
    assert actual["inner_elements"] == 2
