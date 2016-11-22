# import drivers
from selenium import webdriver

# creates and open browser to be driven
browser = webdriver.Firefox()
browser.get('https://web.whatsapp.com/')

# saves in name the name of the contact to 'atack'
name = raw_input("insira o nome da vitima: ")
# path to the chat button
xpath_target = "//div[@class='chat-title']/span[@title='" + name + "']"
# finds an element in the page and click it
element = browser.find_element_by_xpath(xpath_target)
element.click()

# finds the text box to input the text
msgBox = browser.find_element_by_xpath("//div[@class='input']")

# saves the xpath to the send button
xpath_send_btn = "//button[@class='icon btn-icon icon-send send-container']"
# declare how many msgs you want to spam
numMax = input("Num de msgs: ")
num = 0  # instantiete couter
while (num <= numMax):
    # create the message, finds the send button and click it
    msg = 'Num de msgs restantes: ' + str(int(numMax - num))
    msgBox.send_keys(msg)
    sendBtn = browser.find_element_by_xpath(xpath_send_btn)
    sendBtn.click()
    num = num + 1  # increment couter

msgBox.send_keys("The flood has been planted")
sendBtn = browser.find_element_by_xpath(xpath_send_btn)
sendBtn.click()
