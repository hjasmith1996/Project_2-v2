from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from common_functions import *

month_number_match = [{'Month': 'January', 'Number': '1'},
                      {'Month': 'February', 'Number': '2'}, 
                      {'Month': 'March', 'Number': '3'}, 
                      {'Month': 'April', 'Number': '4'}, 
                      {'Month': 'May', 'Number': '5'}, 
                      {'Month': 'June', 'Number': '6'},
                      {'Month': 'July', 'Number': '7'},
                      {'Month': 'August', 'Number': '8'},
                      {'Month': 'September', 'Number': '9'},
                      {'Month': 'October', 'Number': '10'},
                      {'Month': 'November', 'Number': '11'},
                      {'Month': 'December', 'Number': '12'},]

#TD make it so that the code works without the above variable(s) and function(s)



#TD make sure there are no unused imports here. 

class Wikipedia_Xpath_selection():
    """
    This is where the user can change certain xpaths easily without having to find all the usages in the code. 

    These cover the xpaths from wikipeeida. The function title normally contains the name of the usual variable name making it easy to type in and refer to. 
    These all return strings 

    TD: Make this a subclass of some sort of all encompassing variable selector. 

    """
    def get_five_hundred_button():
        """
        This is the button that changes the amount of edit histories displayed from 50 to 500, a better page to scrape from
        """
        return '/html/body/div[3]/div[3]/div[4]/a[7]'
        
    def get_full_edit_list():
        return '//*[@id="pagehistory"]'
    def get_table_header():
        return '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[1]'
    def get_page_table_unchanged_format():
        """
        At some point the format of the list changes. Different xpaths are needed depending on this. 
        """
        return '/html/body/div[3]/div[3]/div[5]/div[1]/table[2]/tbody'
    def get_page_table_changed_format():
        """
        At some point the format of the list changes. Different xpaths are needed depending on this. 
        """
        return '/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/tbody'
wikipedia_xpaths = Wikipedia_Xpath_selection



class Non_duplicate_lists():
    """
    This class is for lists that we wouldn't to have duplicates unless very specifically allowed. 

    TD (generally). thoroughly make sure weather some of these lists would be better off as dictionaries as they 
    """
    def __init__(self,input_list):
        self.input_list = input_list

    def reset_list(self, inout_list):
        """
        Empties the list

        output: list
        """
        input_list = []
    
    def add_if_no_duplication(self, new_entry):
        """
        This function adds a new entry to the list only if it is not existing inside already. 


        input: List, List_entry (any acceptable list variable)
        output: List
        """
        item_found = False
        for items in self.input_list:
            if items == new_entry:
                item_found = True
        if item_found == False:
            self.input_list.append(new_entry)        

    def alphabetise(self):
        """
        Orders the list. this means alphabetised list for strings.  

        input, output: list of strings  (optional)

        TD: incorpate this into searching algorithms. 
        """
        self.input_list.sort
            

class Weather_Xpath_Selection():
    """
    This is where the user can change certain xpaths easily without having to find all the usages in the code. 

    These cover the xpaths on the weather website. The function title normally contains the name of the usual variable name making it easy to type in and refer to. 
    These all return strings 

    TD: Make this a subclass of some sort of all encompassing variable selector. 

    """
    def get_search_button():
        return '/html/body/app-root/app-history-search/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div/div/div/div/form/lib-date-selector/div/input'
    def get_high_temp():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[1]/td[1]'
    def get_low_temp():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[2]/td[1]'
    def get_temp_average():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[3]/td[1]'
    def get_precipitation_number():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[2]/tr/td[1]'
    def get_dew_point():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[3]/tr[1]/td[1]'
    def get_dew_high():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[3]/tr[2]/td[1]'
    def get_dew_low():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[3]/tr[3]/td[1]'
    def get_dew_average():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[3]/tr[4]/td[1]'
    def get_max_wind_speed():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[4]/tr[1]/td[1]'
    def get_visibility():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[4]/tr[2]/td[1]'
    def get_day_length():
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[6]/tr[1]/td[1]'

    def get_observations_body():
        """
        This Xpath refers to the table where the timely specific variables occur agaisnt their time of day. 
        """
        return '/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table/tbody'

#TD This ideally should not be needed here but code wouldn't work without it. Find out how to improve this.  
weather_xpaths = Weather_Xpath_Selection






class Rigid_Parameters_Selection():
    """
    These variables should never be changed. 

    For example there will very likely never be a different list of months.

    TD Implement this properly so it is private
    
    """
    def return_list_of_month_names():
        """
        return a list of all the months

        output: list
        """
        return ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    def return_month_number_match():
        """
        returns a dictionary matching the month with the position it has in a year.

        outputs: Dictionary with string key and integer output. 
        """
        return [{'Month': 'January', 'Number': '1'},
                      {'Month': 'February', 'Number': '2'}, 
                      {'Month': 'March', 'Number': '3'}, 
                      {'Month': 'April', 'Number': '4'}, 
                      {'Month': 'May', 'Number': '5'}, 
                      {'Month': 'June', 'Number': '6'},
                      {'Month': 'July', 'Number': '7'},
                      {'Month': 'August', 'Number': '8'},
                      {'Month': 'September', 'Number': '9'},
                      {'Month': 'October', 'Number': '10'},
                      {'Month': 'November', 'Number': '11'},
                      {'Month': 'December', 'Number': '12'},] 

#TD This ideally should not be needed here but code wouldn't work without it. Find out how to improve this.         
rigid_parameters = Rigid_Parameters_Selection

class Parameters_selection():
    """
    These parameters are likely to be changed. They can all be found here without digging through the code.

    The function names usually contatin the name of the variable being used.  

    outputs vary. 
    """
    def return_amount_of_ranks():
        return 16
    def return_date_text_identifier():
        return 'mw-changeslist-date'
    def return_end_date():
        return ['16:08, 6 August 2020']
    def return_exchange_URL():
        return 'https://en.wikipedia.org/w/index.php?title=List_of_stock_exchanges&action=history'
    def return_format_change_dates():
        return ['02:17, 22 April 2021']
    def return_history_name():
        return 'historySearch'
    def return_skipped_dates():
        return ['07:40, 24 January 2021']
    def return_weather_URL():
        return 'https://www.wunderground.com/history' 
    def return_URL_sleeping_list():
        return [4, 4, 1, 2, 2]
    def return_weather_sleeping_list():
        return [3, 2]
    def return_diff_name_dict():
        return {'Hong Kong' : 'Kowloon', 'Mexico City': 'IMEXICOC52'}
    def return_correct_link_length():
        return 36

    def return_desired_scraped_months():
        return [(2021, 'September'),(2021, 'August'),(2021, 'July'),
            (2021, 'June'),(2021, 'May'),(2021, 'April'),
            (2021, 'March'),(2021, 'February'),(2021, 'January'),
            (2020, 'December'), (2020, 'November'),(2020, 'October'),
            (2020, 'September'),(2020, 'August') ]

#TD This ideally should not be needed here but code wouldn't work without it. Find out how to improve this.  
our_parameters = Parameters_selection    
                










class Scraping_Space():
    """
    General scraping mechanism. 
    
    This includes functions common to different scrapers. 
    """
    def __init__(self, sleeping_amounts):
        self.sleeping_amounts = sleeping_amounts
    @staticmethod


    def get_all_children(driver, xpath):
        """
        This is for tables and such. It creates a list of the xpaths of a table (or over encompassing web object).

        input: xpath
        output: list of xpaths 
        """
        dummy_var = driver.find_element_by_xpath(xpath)
        dummy_list = dummy_var.find_elements_by_xpath("*")
        return dummy_list


    @staticmethod
    def outputting_dict(list_of_keys, list_of_data):
        """
        Outputs a dictionary created from two lists resembelming the keys and values specifically. 

        TD. Incorporate this into code. 
        """
        output_dict = {}
        for i in list_of_keys:
            output_dict[{list_of_keys[i]}] = list_of_data[i]
        
    def go_to_link(self, driver, link):
        """
        Make the driver go to the inputted link. 
        """
        driver.get(link)

    def close_driver(driver):
        """
        closes the driver.

        TD: Check this is unused then delete, redundant.
        """
        driver.close

            
            
#TD This ideally should not be needed here but code wouldn't work without it. Find out how to improve this.              
wikipedia_xpaths = Wikipedia_Xpath_selection

















class Stock_Scraping_Space(Scraping_Space):
    """
    This is the scraping mechnism for the stock exchange, the wikipedia pages, specifically. 
    """
    def __init__(self, sleeping_amounts, written_date_text):
        """

        """
        super().__init__()
        self.sleeping_amounts = sleeping_amounts


    def go_to_home(exchange_URL, driver):
        driver.get(exchange_URL)
        fivehundred_link = Wikipedia_Xpath_selection().get_five_hundred_button()
        fivehundred_link.click()


   # def check_format_change(change_of_format, second_driver):
    #        if  change_of_format == False:
     #           page_table = second_driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/table[2]/tbody')
      #      else:
       #         page_table = second_driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/table[1]/tbody')

    def check_format_change(written_date_text, self):
        if written_date_text in our_parameters.return_format_change_dates():
            return True
        else:
            return False

    def check_end_date(written_date_text, self):
        if written_date_text in our_parameters.return_end_date():
            return True
        else:
            return False
    



    def return_edit_list(self, driver):
        return self.get_all_children(driver, wikipedia_xpaths.get_full_edit_list())
    
    def return_page_table(second_driver, change_of_format):
        if change_of_format == False:
            return second_driver.find_element_by_xpath(wikipedia_xpaths.get_page_table_unchanged_format())
        else:
            return second_driver.find_element_by_xpath(wikipedia_xpaths.get_page_table_changed_format())

    def complete_stock_scrape(self):
        change_of_format = False
        #edit_list = get_all_children('//*[@id="pagehistory"]')
    
    def get_month_and_year_from_text(written_date_text = '12:07, 27 August 2021'):
        current_year =  written_date_text[-4:]
        for month in rigid_parameters.return_list_of_month_names():
            if month in written_date_text:
                current_month = month
        return (current_year, current_month)

    def scrape_through_rows_of_table(list_of_rows, this_months_dictionary):
        for row_elements in list_of_rows:
            list_of_row_elements = row_elements.find_elements_by_xpath("*")
            k = 1   #This k indicates which column we are concerned with

            if len(list_of_row_elements) == our_parameters.return_amount_of_ranks:  #This is the correct amount of elements in a row. Any other number than this makes it difficult to scrape from. 
                if k == 1:  #This column corresponds to the rank of the exchange. 
                    this_months_dictionary['months_rank_list'].append(row_elements.text)

                if k ==3: #This column corresponds to the name of the exchange.
                    this_months_dictionary['months_exchange_list'].append(row_elements.text)

                if k == 6:
                    split_locations = row_elements.text.split('\n')
                    this_months_dictionary['months_location_list'].append(split_locations)

                if k == 7:  #This column corresponds to the market's market cap. 
                    this_months_dictionary['months_market_cap_list'].append(row_elements.text)

                if k ==8: # This column corresponds to the market's trade volume
                    this_months_dictionary['months_trade_volume_list'].append(row_elements.text)



                k += 1 #  Move to the next column 


    def scrape_current_month(self,  change_of_format, written_date_text = '12:07, 27 August 2021', this_months_dictionary = {'months_rank_list' : [], 'months_exchange_list' : [], 'months_location_list' : [], 'months_market_cap_list' : [], 'months_trade_volume_list' : [], 'current_column' : [], 'table_header_children' : []}):
        global months_rank_list, months_exchange_list, months_location_list, months_market_cap_list, months_trade_volume_list, current_column, table_header_children
        months_exchange_list = []
        months_location_list = []
        months_market_cap_list = []
        months_trade_volume_list = []
        #this_months_dictionary = create_dict("months_rank_list", "months_exchange_list", "months_location_list", "months_market_cap_list", "months_trade_volume_list")

        current_column = 0
                 
        second_driver = webdriver.Chrome('chromedriver.exe') # It makes it easier if we use a second driver to open links to a new window. 
        self.go_to_link(second_driver, written_date_text)

        table_header_children = self.get_all_children(second_driver, wikipedia_xpaths.get_table_header())

        page_table = self.return_page_table(second_driver, change_of_format)
        list_of_rows = page_table.find_elements_by_xpath("*")
        
        self.scrape_through_rows_of_table(list_of_rows, this_months_dictionary)

        self.rename_keys(this_months_dictionary)

        second_driver.quit()
        return this_months_dictionary



    def rename_keys(this_months_dictionary):
        #!!!It is convient to change the keys as they are less specific going forward.
        this_months_dictionary['Rank'] = this_months_dictionary.pop('months_rank_list')
        this_months_dictionary['Name of exchange'] = this_months_dictionary.pop('months_exchange_list')
        this_months_dictionary['Locations'] = this_months_dictionary.pop('months_location_list')
        this_months_dictionary['Market Cap'] = this_months_dictionary.pop('months_market_cap_list')
        this_months_dictionary['Trade Voume'] = this_months_dictionary.pop('months_trade_volume_list')


    def add_locations_to_distinct_list(list_of_locations, this_months_dictionary):
        for location in this_months_dictionary['Locations']:
            if location not in list_of_locations:
                list_of_locations.append(location)

    def create_month_location_match(month_and_year, month_location_list):
        month_and_year = month_location_list
        return create_dict("month_and_year")

    def return_last_scraped_month_data(complete_list, last_scraped_month):
        for month in complete_list:
            if month[0] == last_scraped_month:
                return month[1]

    def scrape_through_edit_list(self, edit_list, driver, complete_list, list_of_locations):
        month_and_year = []
        completed_months_and_years = []
        last_scraped_month = ''
        for link in edit_list:
            reset_variable(month_and_year)
            written_date = link.find_element_by_class_name(our_parameters.return_date_text_identifier()) # The text here gives us the date
            written_date_link = written_date.get_attribute('href')
            written_date_text = written_date.text


            if self.skip_date(written_date_text) == True:
                continue
            
            month_and_year = self.get_month_and_year_from_text(written_date_text)
            

            if self.check_shall_month_be_scraped(month_and_year) == True:
                this_months_dictionary = self.scrape_current_month(written_date_text, change_of_format = self.check_format_change(written_date_text))
                complete_list.append([month_and_year, this_months_dictionary])                        
                completed_months_and_years.append(month_and_year)
                self.add_locations_to_distinct_list(list_of_locations, this_months_dictionary)
                self.create_month_location_match(month_and_year, this_months_dictionary['Locations'])

                self.copy_data_to_skipped_month(self, complete_list, this_months_dictionary, completed_months_and_years, list_of_locations, month_and_year)

                last_scraped_month = month_and_year


            if self.check_end_date(written_date_text) == True:
                self.copy_data_to_skipped_month(complete_list,completed_months_and_years, list_of_locations, month_and_year, this_months_dictionary = self.return_last_scraped_month_data(complete_list, last_scraped_month))
                break

    def copy_data_to_skipped_month(self, complete_list, this_months_dictionary, completed_months_and_years, list_of_locations, month_and_year):           
        for skipped_month in our_parameters.return_desired_scraped_months:
            if our_parameters.return_desired_scraped_months.index(skipped_month) < our_parameters.return_desired_scraped_months.index(month_and_year) and skipped_month not in completed_months_and_years:
                complete_list.append([skipped_month, this_months_dictionary])                        
                completed_months_and_years.append(skipped_month)
                self.add_locations_to_distinct_list(list_of_locations, this_months_dictionary)
                self.create_month_location_match(month_and_year = skipped_month, location_list = this_months_dictionary['Locations'])       


    def check_if_month_is_desired(month_and_year):
        if month_and_year in our_parameters.return_desired_scraped_months:
            return True
        else:
            return False

    def check_shall_month_be_scraped(self, month_and_year, completed_months_and_years):
        if month_and_year in completed_months_and_years:
            return False
        else:
            if month_and_year in self.check_if_month_is_desired:
                return True
            else: 
                return False


    def find_next_desired_month(month_and_year):
        index = our_parameters.return_desired_scraped_months.index(month_and_year)
        return our_parameters.return_desired_scraped_months[index + 1]
                
    
    def skip_date(written_date_text, self):
        if written_date_text in our_parameters.return_skipped_dates:
            return True
        else:
            return False

























class Location_Url_Scrape(Scraping_Space):
    def __init__(self, sleeping_amounts):
        self.sleeping_amounts = sleeping_amounts
    def reset_location_urls(location_urls):
        location_urls = []

    def location_scrape(self, driver, location, location_urls):
        driver.get(our_parameters.return_weather_URL())
        time.sleep(self.sleeping_amounts[0])
        search_bar = driver.find_element_by_name(our_parameters.return_history_name())   #This is the search bar
        search_bar.click()

        self.location_name_matcher(location)

        search_bar.send_keys(location)  #Type the location in. 
        time.sleep(self.sleeping_amounts[1])
        search_bar.send_keys(Keys.RETURN) #Pressing enter after a delay will send you to a page regarding that location. 
        view_button = driver.find_element_by_xpath(weather_xpaths.get_search_button())
        view_button.click()
        view_button.click()  #This activate button needs to be clicked twice
        time.sleep(self.sleeping_amounts[2])  #The code does not scrape properly without these periods of waiting. 
        current_url = driver.current_url
        #if len(current_url) == our_parameters.return_correct_link_length():
        time.sleep(self.sleeping_amounts[3])
        location_urls.append(current_url)  #Add the url to the list of urls. These are inputted in the exact same order as the locations in the locations list. 

        time.sleep(self.sleeping_amounts[4])
        driver.get(our_parameters.return_weather_URL())  #Return to searchpage            



        current_url = driver.current_url
        


    
    def complete_url_scrape(self, driver, list_of_locations, location_urls):
        for location in list_of_locations:
            self.location_scrape(driver,  location, location_urls)
        driver.quit()
        print(location_urls)
        return location_urls
    
    @staticmethod
    def location_name_matcher(location):
        diff_name_dict = our_parameters.return_diff_name_dict
        if location in diff_name_dict():
            location = diff_name_dict[location]
        return location









































class Weather_Scrape(Scraping_Space):
    def __init__(self):
        super().__init__()
    def reset_dataset():
        Giant_dataset = []
    
    def trying_scraping(current_date_dict, driver, xpath, key_name):  # This function tries scraping from the locations on the weather website. These are try statements so if a page has no info, no info is added.
    #These functions can be functions inside functions with two variables. One for xpath another for xpath. 
        try:      
            dummy = driver.find_element_by_xpath(xpath)
            current_date_dict[key_name] = dummy.text
        except:
            current_date_dict[key_name] = 'Null'

    def complete_weather_scrape(self, month_location_match, Giant_dataset):
        for months in month_location_match:
            self.month_year_weather_scrape(months, Giant_dataset)


    def month_year_weather_scrape(self,month_and_year, months, Giant_dataset):
        current_month_dict = {}
        current_month, current_year = seperate_month_and_year(month_and_year)
        month_info = Month_And_Year(month = current_month, year = current_year)
        month_number = month_info.get_month_number
        amount_of_days = month_info.get_amount_of_days


        current_month_dict['Month'] = (current_month, current_year) #These last two enteries correspond to the month of the year and the year. 
        current_month_dict['Data'] = [] 


        for locations in months['Locations']:  #We are finding the key for each location here.
            self.location_and_month_scrape()

            
            
        Giant_dataset.append(current_month_dict)  #Add the month's data to the giant dataset. 

    def find_current_code(self, enteries, dictionary, locations):
        if enteries['Location Name'] == locations:
            current_key = enteries['key']    #The key is found.
            return current_key
    def location_and_month_scrape(self, location_key_match, locations, amount_of_days):
        current_key = ''
        
        #Good use for a search function here. 
        for enteries in location_key_match:  
            self.find_current_code(enteries, locations, dictionary = location_key_match)

    
        for i in range(1, amount_of_days + 1):  #This range means for every day of the month
            self.day_scrape()

    def get_day_url(self, current_key, current_year, month_number):
        return f"https://www.wunderground.com/history/daily/{current_key}/date/{current_year}-{month_number}-{i}"




    def try_daily_observations_scraping(self, current_date_dict, driver):  # This is a fucntion which scrapes from the table in the weather section.
        time_data = []
        try:
            self.daily_observation_scraping_attempt

       
        except:
            current_date_dict['Time_Data'] = time_data


    def daily_observation_scraping_attempt(self, current_date_dict, driver):

        list_of_rows = self.get_all_children(weather_xpaths.get_observations_body)
        time_data = []

        for row in list_of_rows:
            self.get_time_of_day_weather_information(row)


        current_date_dict['Time_Data'] = time_data


    def get_time_of_day_weather_information(self, row, time_data):
        time_condition = {} # A dictionary recording data for each time in the day in the table. 
        column_number = 1 # Start with the leftmost column. 

        row_elements = row.find_elements_by_xpath("*")

        for column in row_elements:
            self.time_of_day_column_scrape(column, column_number)



        time_data.append(time_condition)       #collect all the time data together and add them to the dictionary. 

    def time_of_day_column_scrape(column, column_number, time_condition):
        if column_number == 1:
            time_condition['Time'] = column.text # This column is the time column. 
        if column_number == 5: 
            time_condition['Wind_Direction'] = column.text #This column is the wind direction column. 
        if column_number == 10:
            time_condition['Rain_Condition'] = column.text   #This column is the worded rain column. 
        column_number += 1

    def day_scrape(self, i, locations, current_key, current_year, month_number, current_month_dict):
        time.sleep(our_parameters.return_weather_sleeping_list[0]) 

        driver = start_driver
        current_date_dict = {}
        current_date_dict['day_and_location'] = {'day': i,'location': locations}  #Input the independent variables into the dictionary


        desired_url = get_day_url(current_key, current_year, month_number)             
        driver.get(desired_url)

        time.sleep(our_parameters.return_weather_sleeping_list[1])


        self.trying_scraping(current_date_dict, driver)   #We are using the two previous functions for scraping these pages
        self.try_daily_observations_scraping(current_date_dict, driver)

            
        current_month_dict['Data'].append(current_date_dict)   #Add all this date to the data value of this month   















































class Matching_Dictionary():
    """
    Unused class for future incorportion.  Dictionaries where key and value are very strongly linked and used to identify eachother. 

    Would have been used several times in project. 

    TD incorporate this into code. 
    """
    def __init__(self, left_key, right_key, input_list):
        self.left_key = left_key
        self.right_key = right_key
        self.input_list = input_list
    def add_list(self, input_list):
        self.input_list = input_list
    def add_key():
        pass
    @classmethod
    def __iter__(self):
        return self

    def get_rightvalue_from_leftvalue(self,  left_value):
        for dictionaries in self.input_list:
            if dictionaries[self.left_key] == left_value:
                return dictionaries[self.right_key]

    @classmethod
    def alphatbetise_by_left_key(cls):
        pass


class Column_Condition_Matcher(Matching_Dictionary):
    def __init__(self):
        super().__init__()
    """
    Unused class which would have given values in a table a place in a dictonary with the column header as key name. 
    """
    def __init__(self, input_list):
        self.left_key = 'Coloumn number'
        self.right_key = 'Property'
        self.input_list = input_list
    def return_new_dict(self):
        output_dict = {}
        for dicts in self.input_list:
            pass
        return output_dict
    

class Saved_Data():
    pass

class Unusual_Locations_For_Searching():
    pass

class Leaf_Xpath_Match(Matching_Dictionary):
    """ 
    another unused class in which the children with no descendants in a webpage match with their xpath. 

    The hope for this was to make a DPS algorithm to search through all xpaths in a webpage. 
    """
    def __init__(self):
        super().__init__()
    def __init__(self, input_list):
        self.left_key = 'Property'
        self.right_key = 'Xpath'
        self.input_list = input_list
    def create_new_dict_from_scrape(self, driver):
        scraped_data = {}
        for item in self.input_list:
            print(item[self.left_key])
            print(item[self.right_key])
            a =  driver.find_element_by_xpath({item[self.right_key]})
            scraped_data[{item[self.left_key]}] = a.text
            print(item[self.left_key])
            print(item[self.right_key])
        return scraped_data




#month_number_matcher = Matching_Dictionary(left_key = 'Month', right_key = 'Number', input_list = month_number_match)

#print(month_number_matcher.get_rightvalue_from_leftvalue( left_value = 'September'))
class Month_And_Year():
    def __init__(self, month, year):
        self.month = month
        self.year = year
    def get_month_number(self):
        month_number_matcher = Matching_Dictionary(left_key = 'Month', right_key = 'Number', input_list = month_number_match)
        return month_number_matcher.get_rightvalue_from_leftvalue( left_value = self.month)
    def get_amount_of_days(self):
        if self.month in ('July', 'May', 'March', 'January', 'December', 'October','August'):  #These months have 31 days
            amount_of_days = 31
        elif self.month in ('June', 'April', 'November', 'September'): #These months have 30 days
            amount_of_days = 30
        elif int(self.year) %4 == 0: #A test for whether the year is a leap year or not. This is sufficient logic in the span of dates we are looking at. 
            amount_of_days = 29
        else:
            amount_of_days = 28
        return amount_of_days