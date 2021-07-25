# PortSwigger Labs 

## Lab: SQL injection UNION attack, determining the number of columns returned by the query


### Hints: 

### Use Burp Suite to intercept and modify the request that sets the product category filter.
### Modify the category parameter, giving it the value '+UNION+SELECT+NULL--. Observe that an error occurs.
### Modify the category parameter to add an additional column containing a null value: '+UNION+SELECT+NULL,NULL--
### Continue adding null values until the error disappears and the response includes additional content containing the null values.


The Lab has been expoited using many programming languages.
