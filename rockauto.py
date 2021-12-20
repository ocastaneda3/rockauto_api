import sys
import time
import random
import json

from selenium import webdriver

# from selenium.webdriver.chrome import options
# from selenium.webdriver.common.by import By

# from bs4 import BeautifulSoup
# import lxml

CHROMEDRIVER_PATH = 'chromedriver.exe'
WINDOW_SIZE = '1920,1080'

def main( ):
    driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH )

    driver.get('http://www.google.com/')

    time.sleep(5) # Let the user actually see something!

    driver.quit()
    # try:
    #     options = Options()
    #     # options.add_argument( '--headless' )
    #     # options.add_argument( '--disable-gpu' )
    #     options.add_argument( '--window-size=%s' % WINDOW_SIZE )

    #     # User-Agent
    #     options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    #     # Suppress Unwanted Warnings
    #     options.add_experimental_option('excludeSwitches', ['enable-logging'])

    #     # Establish Driverpip3
    #     # driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, options=options )
    #     # Delete Cookies
    #     driver.delete_all_cookies()
    #     # Pause
    #     driver.implicitly_wait( 15 )
    #     # Get Page
    #     driver.get('https://www.rockauto.com/en/catalog/')
    #     # Sleep to load page
    #     time.sleep( random.randint( 5, 10 ) )

    #     for index_1, val_1 in enumerate( driver.find_elements( By.CLASS_NAME, 'ranavnode' ) ):
    #         print( 'Make Layer' )
    #         make_button = val_1.find_element( By.CLASS_NAME, 'nlabel' )
            
    #         # Open Make Drop Down
    #         make_button.click()
    #         time.sleep( 2 )
            
    #         # Check 
    #         if not 'ra-hide' in val_1.find_element( By.CLASS_NAME, 'nchildren' ).find_element( By.CLASS_NAME, 'ranavnode' ).find_element( By.CLASS_NAME, 'nchildren' ).get_attribute( 'class' ).split( ' ' ):
    #             print( 'Bad' )

    #         for index_2, val_2 in enumerate( val_1.find_element( By.CLASS_NAME, 'nchildren' ).find_elements( By.CLASS_NAME, 'ranavnode' ) ):
    #             print( 'Year Layer' )
    #             year_button = val_2.find_element( By.CLASS_NAME, 'nlabel' )

    #             # Open Make Drop Down
    #             year_button.click()
    #             time.sleep( 2 )
    #             if not 'ra-hide' in val_2.find_element( By.CLASS_NAME, 'nchildren' ).find_element( By.CLASS_NAME, 'ranavnode' ).find_element( By.CLASS_NAME, 'nchildren' ).get_attribute( 'class' ).split( ' ' ):
    #                 print( 'Bad' )

    #             for index_3, val_3 in enumerate( val_2.find_element( By.CLASS_NAME, 'nchildren' ).find_elements( By.CLASS_NAME, 'ranavnode' ) ):
    #                 print( 'Model Layer' )
    #                 mdoel_button = val_3.find_element( By.CLASS_NAME, 'nlabel' )
                    
    #                 # Open Make Drop Down
    #                 mdoel_button.click()
    #                 time.sleep( 2 )

    #                 # Collapse Single Items
    #                 if not 'ra-hide' in val_3.find_element( By.CLASS_NAME, 'nchildren' ).find_element( By.CLASS_NAME, 'ranavnode' ).find_element( By.CLASS_NAME, 'nchildren' ).get_attribute( 'class' ).split( ' ' ):
    #                     val_3.find_element( By.CLASS_NAME, 'nchildren' ).find_element( By.CLASS_NAME, 'ranavnode' ).find_element( By.CLASS_NAME, 'nlabel' ).click()
    #                     time.sleep( 2 )
    #                     # input( 'Press any key to continue . . .' )
                    
    #                 # Close Make Drop Down
    #                 mdoel_button.click()
    #                 time.sleep( 1 )

    #                 if index_3 == 0: 
    #                     break
    #             # Close Make Drop Down
    #             year_button.click()
    #             time.sleep( 1 )

    #             if index_2 == 0:
    #                 break

    #         # Close Make Drop Down
    #         make_button.click()
    #         time.sleep( 1 )

    #         if index_1 == 0:
    #             break

    # except Exception as e:
    #     print( e )
    # finally:
    #     driver.quit()

if __name__ == '__main__':
    sys.exit( main( ) )

# Tips & Tricks
# https://levelup.gitconnected.com/8-tips-to-master-web-control-with-selenium-ab120004753a
# https://towardsdatascience.com/how-to-setup-selenium-on-a-linux-vm-cd19ee47d922