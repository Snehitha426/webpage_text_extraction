# Web Content Extractor using Selenium

This project extracts text content from a webpage (including dynamically loaded content via JavaScript) and saves it to a `.txt` file using Selenium and ChromeDriver.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- `pip` (Python package installer)
- Google Chrome (latest version)
- ChromeDriver (matching your Chrome version)

### Install Required Libraries

You need to install the following Python packages:

```bash
pip install selenium
```

## Setup

### 1. Download ChromeDriver

1. Find out your Chrome version by going to `chrome://settings/help` in the browser.
2. Go to the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/) and download the version that matches your Chrome browser version.
3. Extract the downloaded file and note the path to `chromedriver.exe`.

### 2. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Snehitha426/web-content-extractor.git
```

### 3. Update `driver_path`

In the Python script, update the `driver_path` variable to point to the location of `chromedriver.exe` on your machine. For example:

```python
driver_path = r"C:\path\to\chromedriver.exe"
```

### 4. Run the Script

Navigate to the directory where the script is located and run the script:

```bash
python extract_text_selenium.py
```

When prompted, enter the URL you want to extract text from, for example:

```
https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BIRYANI
```

The extracted text content will be saved to `output.txt`.

## Usage

1. Run the script from the terminal.
2. Enter the URL of the webpage you want to extract the content from.
3. The script will open a browser using Selenium, load the page, and extract the content.
4. The text content will be saved in an `output.txt` file in the same directory.

## Example

```bash
Enter the URL: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BIRYANI
Text content successfully written to output.txt
```

## Troubleshooting

1. **ChromeDriver Path Issues**: Make sure the `chromedriver.exe` path is correctly set in the script.
2. **Version Mismatch**: Ensure that your ChromeDriver version matches your Chrome browser version.
3. **Page Load Time**: If the page is not loading fully, increase the wait time in the script (`time.sleep(5)`).

## Contributing

Feel free to open issues or submit pull requests for improvements or new features.

## License

This project is licensed under the MIT License.


### Instructions:
1. Replace `https://github.com/Snehitha426/web-content-extractor.git` with the actual URL of your GitHub repository.
2. Save this content in a file named `README.md` and upload it to your repository.

This file includes installation, usage instructions, troubleshooting tips, and a basic structure for contributing to the project.
