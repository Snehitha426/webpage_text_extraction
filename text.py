from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Function to extract text from a URL using Selenium
def extract_text_from_url_selenium(url, output_file, driver_path):
    # Set up the WebDriver (Chrome in this case)
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        # Open the URL
        driver.get(url)

        # Wait for the page to fully load
        time.sleep(5)  # Adjust if necessary (increase for slow-loading pages)

        # Extract the full text of the page
        text = driver.find_element(By.TAG_NAME, "body").text

        # Write the extracted text to a file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"Text content successfully written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the browser
        driver.quit()

# Main execution
if __name__ == "__main__":
    url = input("Enter the URL: ")
    output_file = "output.txt"  # Name of the output file
    driver_path = r"C:\Users\Bairi Snehitha\Downloads\chromedrivers\chromedriver.exe"  # Correct path to chromedriver

    extract_text_from_url_selenium(url, output_file, driver_path)

