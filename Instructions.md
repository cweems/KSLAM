#Welcome to the first section of our KSLAM!

Today's work will consist of three sections:

* 1. Retrieving and Processing Data From an API
* 2. Making visualizations from your data

Side note: The document you are reading is posted on Github. You can think of Github as Dropbox or GoogleDocs for code. In more technical terms, it's a version control system based on a computer language known as git. It allows developers to collaboratively create and edit code.

#Section 1: Retrieving Data

We're going to start off the section by going through a simple lesson on Codecademy. Codecademy is a website that allows you to learn how to code in various languages in an online environment.

##Getting Started with APIs

1. Go to: http://www.codecademy.com
2. If you think you might like to use Codecademy yourself, create an account by logging in via Google. Otherwise, have Charlie give you his login info.
3. We'll be using the Sunlight Foundation's Capitol Words API to learn the basics of accessing data via API. Once that's complete, Charlie will demonstrate how you can use the same code to access other API's such as the USAID Development Credit Authority Database. **Navigate to the course by clicking this link:** http://www.codecademy.com/courses/python-intermediate-en-D56TP/0/1?curriculum_id=50ecbb00306689057a000188
4. Charlie and Mari will help lead you through the tutorial and explain what is happening.

##Takeaways from the Capitol Words API:

1. An API has an endpoint which is the main URL that we call to receive data.
2. APIs take "parameters" which allow us to filter data.
3. Sometimes APIs take a "Key" – this allows the API administrators to regulate use of the API.
4. Most APIs return JSON, a data format that works well for data transfers. We can convert JSON into Comma Separated Values (CSV) at websites like this one: http://www.danmandle.com/blog/json-to-csv-conversion-utility/
5. Using these principals, Charlie will demonstrate how to access the USAID Development Credit Authority Loan Database via API. Don't worry about following along yourself, but do pull up the code that Charlie is using here: https://github.com/cweems/KSLAM/blob/master/Code/apicaller.py. You can run this on your computer later if you would like to experiment, but unfortunately Python takes a little effort to setup on some computers so we'll just observe for now.

##Converting API Data from JSON to CSV

This isn't something that's normally done, because Python is very good at processing JSON. However, for our purposes it would be nice to open this data in something like excel.

Here's a website that we can copy and paste our JSON into:
* http://www.danmandle.com/blog/json-to-csv-conversion-utility/
* http://jsfiddle.net/sturtevant/vUnF9/



