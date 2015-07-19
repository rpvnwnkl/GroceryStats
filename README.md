This is a tool to conduct analysis on our regular grocery purchases. 

* Assembles .csv files into a dict of objects
* Conducts analysis on the collection of objects
* Plots results of Analysis 

Would eventually like to build a UI to call and clear plots on demand, as well as choose scope, etc. 

-MM

##Ultimate Goal:

A tool to provide pricing information for grocery purchases

##Requires:
* Accessibility from desktops and mobile phones
* Provide accurate information on grocery prices 
* Provide relevant information on grocery purchasing trends 
* Be easy and enjoyable to use

##How:
* Records past grocery purchases via user input or scanning receipts
* Formats and logs raw data
* Computes pricing and trend information
* Displays information via interactive graphical interface

###Records Grocery Purchases

This is currently being accomplished via the use of spreadsheets saved in a `.csv` format. 
It would be desirable to automate this process, but it's not clear how that would best be done.
__*Possible Ideas:*__
* Use a computer vision library like opencv as seen here: https://www.youtube.com/watch?v=B1d9dpqBDVA
    This would involve photographing or scanning receipts and then interpreting the information into a usable format.
    *Obstacles*: 
        Receipts do not always include the weight/volume of a product. This means either the weight/volume must be gathered via another method, automated or not; or that the analytics performed by this tool would not be relying on information beyond what is garnered from a receipt. The latter is a less desirable alternative and the focus will be on attaining the weight/volume data with the intention of calculating 'value'.

* Have a web/gui form which can be used either standalone to enter product or receipt information, or have a form populated by a receipt scan which is then further completed by an interested user. 
    *Obstacles*:
         Still a lot of work for the user, but less if the starting info can be prepopulated. I can see the process being gamified.

* As an alternative to human intervention in the data logging process, a function could be developed to source elsewhere the information not gathered from the scanning process itself. This could take the form of a dictionary of information on different products. This dictionary/database could be compiled either from web scraping, past data inputs, or both. An automated process could be held for user review before being accepted as a valid item input.
    *Obstacles*: 
        Using past data to find new data is problematic because it requires an initial input of data, and then may be no more accurate then the data initially given. A solution to this might be the use of web scrapers, past data inputs, and a machine learning algorithm. I will have to learn more about machine learning in order to even further consider implementing this method, not to mention actually putting it into practice.

* The last choice would be to simply keep recording basic information in a spreadsheet with each grocery purchase.
    *Obstacles*:
        This takes time and is a little boring

###Formats and Logs Raw Data

*This is functionally implemented in the current code.*
This is a straightforward step in the process, depending upon what demands there are on the data. 
The basic process should receive the data accurately, and store it in a type of database for easy access.
 *Currently the process uses objects to store and interact with the data*. 
All data is disc saved as .csv files. Additional data fields could be created depending upon the demands of the analysis, such as cost/unit information or deviation from average product price. 

###Computes Pricing and Trend Information:

This can be done either automatically as data is entered into the system, or on demand as specific queries are executed on the data. Most likely it will involve both. Pricing information should be calculated via the Cost and Amount category values, however that data is sourced. Trends are more difficult, and some basic ones, like monthly averages and totals, are already implemented. Further analysis will have to be intoroduced as I go back to look at some more statistical methods.

There is an argument the the queries should be able to be automatically constructed, as like a SQL database. This could introduce unnecessary complications to the building of the tool. It would be far easier to determine a set of analysis to conduct and serve that as a set of options. Really we just want to know if the food is a good buy or not, and then to know what we've been spending our money on, and how much money we've been spending. What other information can be garnered from the purchase history of these products? That needs to be established.

###Displays information via graphical user interface

This will most likely manifest as a web app. Perhaps it will just be something hosted in dropbox or elsewhere. But the gist is that it will ve accessed in the browser. I'm looking into using Django down the road to get that up and going. 

