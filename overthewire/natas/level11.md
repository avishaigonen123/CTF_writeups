# Natas Level 11 Solution

```
<?
$defaultData = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$jsonEncodedData = json_encode($defaultData);

$defDecoded = 'HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=';
$decodedDef = base64_decode($defDecoded);

$outText = '';
for($i=0;$i<min(strlen($jsonEncodedData),strlen($decodedDef));$i++) {
    $outText .= $jsonEncodedData[$i] ^ $decodedDef[$i];
}

echo ($outText);
?>
```

by running this code i can find the key, which is `eDWo`

now, we will create the payload with yes in the key `showpassword`

```
<?
$defaultdata = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = 'eDWo';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

echo base64_encode(xor_encrypt(json_encode($defaultdata)));
?>
```

this give us `HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5`

and then, all left is to put it in the cookie `data`

**Flag:** ***`yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB`*** 