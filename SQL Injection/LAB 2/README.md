# PortSwigger Labs 

## Lab: SQL injection UNION attack, finding a column containing text


### Hints: 

#### Use Burp Suite to intercept and modify the request that sets the product category filter.
#### Determine the number of columns that are being returned by the query. Verify that the query is returning three columns, using the following payload in the category parameter: '+UNION+SELECT+NULL,NULL,NULL--
#### Try replacing each null with the random value provided by the lab, for example: '+UNION+SELECT+'abcdef',NULL,NULL--
#### If an error occurs, move on to the next null and try that instead.

The Lab has been expoited using many programming languages.
