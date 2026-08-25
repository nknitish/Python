
# Global Import
import os

# import from PIP
import requests

from dotenv import load_dotenv

# Import from Modules 
from utils.calculator import add, sub


def demonstrate_calculator():
    """Demonstrate functions imported from the utils package."""

    # Call and display calculator functions.
    print(f"Addition: {add(5, 10)}")
    print(f"Subtraction: {sub(30, 4)}")
    print(f"Addition: {add(10, 23)}")


def check_github_status():
    """Check whether the GitHub API is available."""

    try:
        # Send a GET request to GitHub with a ten-second timeout.
        response = requests.get("https://api.github.com", timeout=10)

        # Raise an error if the request was unsuccessful.
        response.raise_for_status()

        print(f"GitHub status: {response.status_code}")

    except requests.RequestException as error:
        # Handle network and HTTP-related errors.
        print(f"Request failed: {error}")


def display_name():
    """Read and display the NAME value from the .env file."""

    # Read environment variables from the .env file.
    load_dotenv()

    # Use "Guest" if NAME is not defined.
    name = os.getenv("NAME", "Guest")

    print(f"Name: {name}")


def main():
    """Run all application demonstrations."""

    demonstrate_calculator()
    check_github_status()
    display_name()


# Run main() only when this file is executed directly.
if __name__ == "__main__":
    main()



