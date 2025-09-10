import subprocess
import pytest
import os
import tracemalloc
#AI Declaration:
# I used AI to create compilation so that pytest may run properly during the build
# I also used AI to format this file when I copy-paste it from the instructions PDF
# so that I did not have to manually remove individual spaces created during the copy-paste.

# I also used an AI function to detect memory leaks because I had no idea how to test that,
# usually I use valgrind however, this isn't  ideal.

# Begin AI Functions

@pytest.fixture(scope="module", autouse=True)
def build_and_cleanup():
    """Compile greeter.cpp before tests and delete after."""
    # Compile
    os.system("g++ src/*.cpp -o greeter -std=c++17")

    yield  # run the tests

    # Cleanup
    if os.path.exists("greeter"):
        os.remove("greeter")

# End of AI Functions

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

# AI Function
# This function is completely optional and I've used AI to create it so I may trace memory leaks
# However, it has not found any and this is not part of the main component or testing suite for my assignment.
# It is for my personal testing.
def test_greeter_no_memory_leak():
    """Test that running the greeter repeatedly does not leak memory in Python."""
    tracemalloc.start()
    snapshot1 = tracemalloc.take_snapshot()

    # Run the greeter multiple times
    for _ in range(100):
        run_greeter("John Doe")

    snapshot2 = tracemalloc.take_snapshot()
    stats = snapshot2.compare_to(snapshot1, 'lineno')
    total_diff = sum(stat.size_diff for stat in stats)

    # Allow small fluctuations, fail if memory grows too much
    assert total_diff < 1024 * 10, f"Potential memory leak detected: {total_diff} bytes"
# End of AI Function

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
