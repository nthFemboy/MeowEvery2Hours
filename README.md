# MeowEvery2Hours Bot

This Python script automates logging into Twitter (X), generating a random number of "meow" words, and posting them as a tweet. It uses Selenium for web automation and the Chrome WebDriver to interact with the browser.

## Features

- Logs into Twitter (X) using provided username and password.
- Generates a random tweet consisting of the word "meow" repeated a random number of times.
- Automatically posts the generated tweet to the user's profile.
- Takes screenshots for debugging (e.g., when elements are not found).

## Requirements

- Python 3.x
- `selenium` Python package
- `webdriver_manager` Python package
- Google Chrome (latest version)
- ChromeDriver (automatically managed by `webdriver_manager`)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/nthFemboy/MeowEvery2Hours.git
   cd MeowEvery2Hours
