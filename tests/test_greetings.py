import subprocess
import pytest
import os

#AI Declaration:
# I used AI to create compilation so that pytest may run properly during the build
# I also used AI to format this file when I copy-paste it from the instructions PDF
# so that I did not have to manually remove individual spaces created during the copy-paste.

# Begin AI Function

@pytest.fixture(scope="module", autouse=True)
def build_and_cleanup():
    """Compile greeter.cpp before tests and delete after."""
    # Compile
    os.system("g++ src/*.cpp -o greeter -std=c++17")

    yield  # run the tests

    # Cleanup
    if os.path.exists("greeter"):
        os.remove("greeter")

# End of AI Function

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

def test_greeting_no_spaces():
    """Test the greeting with a name that includes no spaces."""
    name = "First"
    expected_output = f"Hello, {name}!"
    actual_output = run_greeter(name)
    assert actual_output == expected_output

def test_greeting_with_symbols():
    """Test the greeting with a name that includes lots of symbols."""
    name = "A*A(G*UA(GYUHIAJKにちはNG8_ a7dg*gak éé€éñ"
    expected_output = f"Hello, {name}!"
    actual_output = run_greeter(name)
    assert actual_output == expected_output

def test_long_name():
    """Test the greeting with a name that includes a really long name."""
    name = "Aladdin the First Princess Jasmine Lover Prince of Ababwa"
    expected_output = f"Hello, {name}!"
    actual_output = run_greeter(name)
    assert actual_output == expected_output

def test_with_spaces():
    """Test the greeting with a name that includes a really long name."""
    name = " A l a d d i n "
    expected_output = f"Hello, {name}!"
    actual_output = run_greeter(name)
    assert actual_output == expected_output
