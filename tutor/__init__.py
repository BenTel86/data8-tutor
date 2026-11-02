"""Local Data 8 tutor over md_corpus.

Platform bots should import `answer` rather than talking to Slack or Discord here.
"""

from .engine import TutorReply, answer

__all__ = ["TutorReply", "answer"]
