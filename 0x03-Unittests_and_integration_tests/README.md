# Unittests and Integration Tests

## Description

This project contains unit tests and integration tests for various functionalities. The goal is to ensure that individual units of code work correctly (unit tests) and that different pieces of the application work together as expected (integration tests).

## Requirements

- Python 3.4.3 or later
- Ubuntu 20.04 LTS
- PEP 8 style guide (version 2.5)
- `unittest` module
- `parameterized` module

## Installation

1. Ensure you have Python 3.4.3 or later installed on your system.
2. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/your_username/unittests-integrationtests.git
    cd unittests-integrationtests
    ```

3. Ensure your files are executable:

    ```sh
    chmod +x test_client.py
    ```

4. Install the required modules:

    ```sh
    pip install parameterized
    ```

## Usage

### Running Unit Tests

Unit tests are designed to test individual units of code to ensure they work as expected. To run the unit tests, use the following command:

```sh
python3 -m unittest discover -s tests/unit -p "*.py"

