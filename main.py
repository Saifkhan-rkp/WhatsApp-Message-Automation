import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# reading csv file using pandas
df = pd.read_csv("Chess_Registrations.csv", header=None)

# converting data frame into multidimensional list[[name,phone]]
recipients = df.values.tolist()

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("Please scan the QR code and press enter")

# stopping forward action till browser page loads
time.sleep(30)


# Loop through the recipients and send the message
for name, phone in recipients:
    # Click on the new chat button
    new_chat_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[3]/header/div[2]/div/span/div[5]/div')
    new_chat_button.click()
    
    # Search for the recipient
    search_box = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]')
    search_box.click()
    driver.implicitly_wait(2)
    search_box.send_keys("+91"+str(phone))
    time.sleep(4)
    search_box.send_keys(Keys.RETURN)

    # Wait for the chat to load
    time.sleep(4)

    # Type and send the message
    message_box = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
    message_box.click()
    driver.implicitly_wait(4)
    message_box.send_keys(f"Hey {name}! Join our exclusive Respawn Chess WhatsApp group for epic chess action! Let's strategize and have fun together!  #RespawnChess  Group Link: [Link] Note: If the link isn't clickable, save the contact and try again. Feel free to text back if needed!")
    message_box.send_keys(Keys.RETURN)

    time.sleep(2)

    print(f"Message sent to {phone}")

print("All messages sent successfully!")

# Close the browser after a few seconds
time.sleep(5)
driver.quit()
