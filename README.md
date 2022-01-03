# Web Scraping Toolkit

Web scraping in Python is a very powerful tool to have as a web developer or security researcher. This repository holds some of the scripts I've written in Python for various tasks related to web scraping.

NOTE: Webscraping can be illegal depending on the nature of the data you are collecting, among other things. I am not responsible for anything you do with these tools, nor is any of this legal advice.

## Clear

This repository is currently split into two folders. 

Normal holds scripts to facilitate the scraping of the "clearweb". For this I used BeautifulSoup. 

This collection of scripts was originally developed to collect the addresses of open IP cameras from various websites that collect them, so while only one script (scraper.py) does the actual scraping, the other four do various post-processing on the data. 

Note that while the filenames used here are about IP addresses, these scripts will work for any type of data with some modifications. 

Here is the pipeline:

scraper.py -> ips_raw.txt -> cleaner.py -> ips_cleaned.txt -> extractor.py -> ips_extracted.txt -> locator.py -> ips_located.json -> formatter.py -> ips_formatted.json

In other words, scraper.py gets a bunch of IP addresses from a website, and then the next two clean up what scraper.py collected using regex, and then the IPs are geolocated and formatted in a JSON for later use. This same process can be used to get any other form of data from a webpage, you just likely will not need to include the geolocator script in the pipeline.

## Hidden

Hidden services are websites that can only be visited through The Onion Router (Tor). These websites will have a .onion TLD, and one must use the Tor browser to access them. 

Since there are many forums and marketplaces on the deep web where threat actors trade/sell information, I thought a hidden service web crawler might be useful for threat intelligence research. As such, the Hidden folder contains the Hidden Spider. 

To be able to access Tor through a Python script, some extra steps are required.

First, we are using Selenium this time, as we may need to interact with pages. Selenium requires a driver to be able to automate a browser, and since Tor runs on Firefox, we use Mozilla's Geckodriver, downloadable at https://github.com/mozilla/geckodriver/releases. Move the driver to your ~/.local/bin folder.

We will also need the location of the Tor browser's Firefox binary. This can be found by right-clicking on the Tor browser in whatever folder it was installed in and clicking 'show contents'. Find the Firefox binary in there and copy the path. This goes in line 6, where specified.

Finally, we set the url variable to the .onion that we would like to scrape.

Hidden services are understandably very security-conscious. This sometimes creates some problems for our spider. The two biggest are Captchas and anti-crawling measures. 

Captchas on hidden services are often much different from those you encounter in the clearweb. They are more complex and harder to automate through. A simple workaround currently implemented in spider.py is to use the implicit wait function to wait until an action can be performed. 

Anti-crawling measures will attempt to detect unusual traffic. If we are scraping a large website in one go, that may get red-flagged. One solution is to scrape the website in smaller chunks and combine them later using combine.py.

Hidden services are by their very nature hard to find. For a threat intelligence researcher, it could be useful to have a sort of map of the hidden service landscape. This can be achieved with some extensions to spider.py. Given a starting point that is a sort of hub of hidden service links, such as a forum or a directory, the spider can be set to pull all .onion urls from the page. Then, the spider can go through each pulled url and repeat the process at each site. The spider can continue to repeat this process until there are no new urls to scrape. At that point you'll have a large amount of .onion urls. From there, it would be useful if the spider could do some basic classification based off the other elements on the pages to give a likely category to each .onion, such as marketplace or forum. This would give you a decent map of a certain subset of the hidden service landscape. Note that visiting certain hidden services may be illegal, so do this at your own risk. Right now it is purely an interesting though experiment for me.
