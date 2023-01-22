# webscrapers
This repository contains webs-crapers and crawlers I created while learning.

Content

1) ICC world cup indian world cup data
    
    -This scrapper scraps the last 10 years of the data bowlers that have been a part of indian world cup cricket team.
      And store the data in the CSV file
      
      link to the file :-
      https://github.com/sachin-kansal/webscrapers/blob/main/icc_worldcup_scrapper/iccdata_bowlers.py
      
      url scrapped :-
      https://stats.espncricinfo.com/ci/engine/records/averages/bowling.html?id=89;team=6;type=trophy
2) Weather data scrappper/crawler
    -This crawler crawls the website for each month data 
    And scraps the data for each day of that month
    Then Stores the data inside a DataFrame
    
    link to the file :-
    https://github.com/sachin-kansal/webscrapers/blob/main/weather_crawler_scrapper.py
    
    url crawled :-
    https://www.estesparkweather.net/archive_reports.php?date=200901
    
    200901 --> represent code for year and month (yyyymm) which is used for crawling
    
    so for ex december 2018 will be represented as 201812
    and link will be https://www.estesparkweather.net/archive_reports.php?date=201812
