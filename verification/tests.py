"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["678"],
            "answer": True,
        },
        {
            "input": ["hi"],
            "answer": False,
        }
    ],
    "Extra": [
        {
            "input": ["6", "3"],
            "answer": True,
        },
        {
            "input": ["hello", "list"],
            "answer": False,
        }
    ]
}
