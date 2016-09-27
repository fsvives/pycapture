import pyscreenshot
import sys
from sendkeys import SendInput
from sendkeys import Keyboard
from sendkeys import VK_NEXT
from time import sleep

__author__ = "Facundo Vives"
__copyright__ = "Copyright 2016"
__license__ = "GPL"
__version__ = "1.0.0"
__stauts__ = "Testing"

if __name__ == "__main__":
    number_of_pages = int(input("Enter number of pages to capture: "))
    start_page = int(input("Enter page where capture will start: "))
    print("Starting to capture in 3 seconds...")
    sleep(3)
    for page in range(start_page,number_of_pages+1):
        im=pyscreenshot.grab(bbox=(590,90,1325,1050)) #Left, Top, Right, Bot
        page_filename = "page" + str(page) + ".png" #Change extension to desired format
        im.save(page_filename) #Save image in the same folder the script executes
        print("Saving page number",page)
        SendInput(Keyboard(VK_NEXT)) #Simulate Page Down key pressed. Could simulate alt+tab or any other desired combination
        sleep(0.2)
#-#
