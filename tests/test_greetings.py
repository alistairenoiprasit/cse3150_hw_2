import subprocess
import pytest
import os


@pytest.fixture(scope="module", autouse=True)
def build_and_cleanup():
    """Compile greeter.cpp before tests and delete after."""
    # Compile
    os.system("g++ src/*.cpp -o greeter -std=c++17")

    yield  # run the tests

    # Cleanup
    if os.path.exists("greeter"):
        os.remove("greeter")


def run_greeter(input_text):
    """Helper function to run the compiled C++ greeter with input."""
    # The input_text needs a newline, as if the user pressed Enter
    input_with_newline = input_text + "\n"

    result = subprocess.run(
        ["./greeter"],
        input=input_with_newline,
        capture_output=True,
        text=True,
        check=True
    )
    # The output from the C++ program includes the prompt and the final message.
    lines = result.stdout.strip().splitlines()
    return lines[-1] if lines else ""


def test_greeting_with_spaces():
    """Test the greeting with a name that includes spaces."""
    name = "First Last"
    expected_output = f"Hello, {name}!"
    actual_output = run_greeter(name)
    assert actual_output == expected_output
