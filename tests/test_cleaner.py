from comment_cleaner.cleaner import clean


def test_cleaner_removes_lines_starting_with_hash():
    INPUT = "# This is a comment"
    assert clean(INPUT) == ""


def test_cleaner_removes_comments_with_leading_whitespace():
    INPUT = "       # This is a comment"
    assert clean(INPUT) == ""


def test_cleaner_does_not_remove_normal_lines():
    INPUT = """
    def main():
        pass
    """
    assert clean(INPUT) == INPUT