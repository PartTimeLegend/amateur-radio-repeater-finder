# Amateur Radio Repeater Finder

The Amateur Radio Repeater Finder is a Python script that allows users to find amateur radio repeaters based on a Maidenhead locator. It interacts with the RepeaterBook API to retrieve repeater information and provides options to save the data to CSV files compatible with various programming software used in amateur radio transceivers.

## Features

- Retrieve amateur radio repeaters by providing a Maidenhead locator.
- Sort repeaters by mode and distance.
- Export repeater data to CSV files compatible with CHIRP, Icom programming software, and Yaesu programming software.

## Prerequisites

- Python 3 installed on your system.
- A RepeaterBook API key. You can sign up for a free account at [RepeaterBook](https://www.repeaterbook.com/) to obtain your API key.
- Necessary Python packages installed, which are listed in `requirements.txt`.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/parttimelegend/amateur-radio-repeater-finder.git
```

2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Set the `REPEATERBOOK_API_KEY` environment variable with your RepeaterBook API key.

2. Run the script `main.py`:

```bash
python main.py
```

3. Follow the prompts to enter the Maidenhead locator and choose the export format for the repeater data.

4. Provide the filename to save the CSV file.

## Export Formats

The script supports exporting repeater data to the following formats:

- **CHIRP**: CSV format compatible with CHIRP radio programming software.
- **Icom**: CSV format compatible with Icom radio programming software (e.g., CS-7100, CS-5100).
- **Yaesu**: CSV format compatible with Yaesu radio programming software (e.g., ADMS-4B, ADMS-7B).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
