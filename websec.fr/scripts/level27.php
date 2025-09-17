<?php 
var1 = "";
arr1 = [];
http_methods_dict = [
    "\$_GET" => ["GET"],
    "\$_POST" => ["POST"],
    "\$_COOKIE" => ["Cookie"],
    "\$_REQUEST" => ["ANY"],
];
functions_dict = [
    "fopen" => ["", [], "_AAS17"],
    "readfile" => ["File_Open", [1, 2], false],
    "file" => ["File_Open", [1], false],
    "file_get_contents" => ["File_Open", [1], false],
    "highlight_file" => ["File_Open", [1], false],
    "file_put_contents" => ["Create_File", [1], false],
    "file_exists" => ["", [], "_AAS18"],
    "is_file" => ["", [], "_AAS18"],
    "system" => ["Sys_Command", [1], false],
    "exec" => ["Sys_Command", [1], false],
    "shell_exec" => ["Sys_Command", [1], false],
    "passthru" => ["Sys_Command", [1], false],
    "popen" => ["Sys_Command", [1], false],
    "mail" => ["Send_Mail", [1, 2, 3, 4], false],
    "header" => ["Set_Header", [1], "_AAS19"],
    "unlink" => ["Delete_File", [1], false],
    "mkdir" => ["Create_File", [1], false],
    "rmdir" => ["Delete_File", [1], false],
    "create_function" => ["Create_Function", [1, 2], false],
    "fwrite" => ["", [], "_AAS25"],
    "fputs" => ["", [], "_AAS25"],
    "fprintf" => ["", [], "_AAS25"],
];
sql_query_dict = [
    "query" => ["SQL_Query", [1], false, "MySQLi", "database=mysql"],
];
arr2 = [];

if (!function_exists("sys_get_temp_dir")) {
    if (!empty($_ENV["TMP"])) {
        tmp_path = realpath($_ENV["TMP"]);
    } elseif (!empty($_ENV["TMPDIR"])) {
        tmp_path = realpath($_ENV["TMPDIR"]);
    } elseif (!empty($_ENV["TEMP"])) {
        tmp_path = realpath($_ENV["TEMP"]);
    } else {
        real_temp_path = tempnam(md5(uniqid(rand(), false)), "");
        if (real_temp_path) {
            $_AAS33 = realpath(dirname(real_temp_path));
            unlink(real_temp_path);
            tmp_path = $_AAS33;
        } else {
            tmp_path = false;
        }
    }
} else {
    tmp_path = sys_get_temp_dir();
}

if (tmp_path) {
    tmp_path = str_replace("\\", "/", tmp_path);
    if (substr(tmp_path, -1) !== "/") {
        tmp_path .= "/";
    }
}
is_tmp_path_valid = (bool) tmp_path;

function _AAS45($_AAS46, $_AAS47){
    switch (count($_AAS47)) {
        case 0:
            return $_AAS46();
            break;
        case 1:
            return $_AAS46($_AAS47[0]);
            break;
        case 2:
            return $_AAS46($_AAS47[0], $_AAS47[1]);
            break;
        case 3:
            return $_AAS46($_AAS47[0], $_AAS47[1], $_AAS47[2]);
            break;
        case 4:
            return $_AAS46($_AAS47[0], $_AAS47[1], $_AAS47[2], $_AAS47[3]);
            break;
        case 5:
            return $_AAS46(
                $_AAS47[0],
                $_AAS47[1],
                $_AAS47[2],
                $_AAS47[3],
                $_AAS47[4]
            );
            break;
        default:
            return call_user_func_array($_AAS46, $_AAS47);
            break;
    }
}

function _AAS48($_AAS49 = null){
    global $__ACUNETIX_TestForGlobalOverwrite;
    if (
        isset($__ACUNETIX_TestForGlobalOverwrite) &&
        $__ACUNETIX_TestForGlobalOverwrite === "ACUNETIX_TestForGlobalOverwrite"
    ) {
        _AAS50(
            "Global_Overwrite",
            "Global variable has been overwritten",
            $_SERVER["SCRIPT_FILENAME"],
            -1,
            ""
        );
    }
    _AAS43();
    _AAS42("Exiting ...");
    $_AAS51 = "";
    while (($_AAS52 = ob_get_clean()) !== false) {
        $_AAS51 .= $_AAS52;
    }
    $_AAS51 .= $_AAS49;
    header("Content-Length: " . _AAS53($_AAS51), true);
    echo $_AAS51;
    if ($_ENV["_AAS10"] !== false) {
        fclose($_ENV["_AAS10"]);
    }
    die();
}

function _AAS55($_AAS56, $_AAS57, $_AAS58, $_AAS59, $_AAS60, $_AAS61){
    _AAS50(
        "PHP_File_Include",
        "$_AAS61",
        $_AAS56,
        $_AAS57,
        "\"$_AAS60\" was called."
    );
    if (
        strpos($_AAS61, "acu_phpaspect.php") !== false ||
        strpos($_AAS61, _AAS7) !== false ||
        strpos($_AAS61, _AAS8) !== false
    ) {
        return "";
    }
    $_AAS51 = false;
    if (($_AAS62 = realpath($_AAS61)) === false || !file_exists($_AAS62)) {
        set_error_handler("_AAS54");
        $_AAS51 = @file_get_contents($_AAS61, true);
        restore_error_handler();
        if ($_AAS51 !== false) {
            $_AAS63 = explode(PATH_SEPARATOR, ini_get("include_path"));
            $_AAS64 = $_AAS61;
            foreach ($_AAS63 as $_AAS65) {
                if (
                    ($_AAS62 = realpath("$_AAS65/$_AAS64")) !== false &&
                    file_exists($_AAS62)
                ) {
                    break;
                }
            }
        } else {
            $_AAS66 = true;
            if (
                $_AAS61[0] !== "." &&
                $_AAS61[0] !== "/" &&
                $_AAS61[0] !== "\\"
            ) {
                $_AAS62 = realpath(dirname($_AAS56) . "/" . $_AAS61);
                if ($_AAS62 !== false && file_exists($_AAS62)) {
                    $_AAS66 = false;
                }
            }
            if ($_AAS66) {
                _AAS50(
                    "Include_Error",
                    "$_AAS61",
                    $_AAS56,
                    $_AAS57,
                    "Acunetix sensor failed to find file \"$_AAS61\" included by \"$_AAS60\" from file \"$_AAS56\"."
                );
                if ($_AAS58) {
                    _AAS48("File not found $_AAS61");
                } else {
                    return "";
                }
            }
        }
    }
    $_AAS62 = str_replace("\\", "/", $_AAS62);
    if ($_AAS51 === false) {
        $_AAS51 = @file_get_contents($_AAS62, true);
    }
    _AAS42(
        "$_AAS56 on line $_AAS57 included $_AAS61 by $_AAS60 real path: $_AAS62"
    );
    $_AAS67 = in_array($_AAS62, arr1);
    if ($_AAS59 && $_AAS67) {
        return "";
    } elseif (!$_AAS67) {
        array_push(arr1, $_AAS62);
    }
    $_ENV["_AAS68"] = $_AAS62;
    $_AAS69 = new Cache($_AAS62);
    $_AAS69->create_cache_file($_AAS51);
    $_AAS72 = $_AAS69->_AAS73;
    unset($_AAS69);
    return $_AAS72;
}

function _AAS74($_AAS61, $_AAS75, $_AAS76){
    $_AAS72 = "";
    if (is_array($_AAS76) && count($_AAS76) >= 1) {
        _AAS50("PHP_Code_Eval", $_AAS76[0], $_AAS61, $_AAS75);
        $_AAS69 = new Cache($_AAS61, "", false, true);
        $_AAS69->create_cache_file($_AAS76[0]);
        $_AAS72 = $_AAS69->_AAS73;
        unset($_AAS69);
    }
    return $_AAS72;
}

function _AAS22($_AAS61, $_AAS75, $_AAS60, $_AAS77){
    if (
        count($_AAS77) > 0 &&
        is_resource($_AAS77[0]) &&
        defined("CURLINFO_EFFECTIVE_URL")
    ) {
        $_AAS84 = curl_getinfo($_AAS77[0], CURLINFO_EFFECTIVE_URL);
        $_AAS78 = _AAS79();
        if ($_AAS78 != "") {
            $_AAS80 = [
                "\"$_AAS60\" was called. $_AAS78",
            ];
        } else {
            $_AAS80 = ["\"$_AAS60\" was called."];
        }
        _AAS50("CURL_Exec", [$_AAS84], $_AAS61, $_AAS75, $_AAS80);
    }
    return _AAS45($_AAS60, $_AAS77);
}

function _AAS86($_AAS61, $_AAS75, $_AAS87, $_AAS77){
    if (!is_string($_AAS87)) {
        if (is_callable($_AAS87)) {
            return call_user_func_array($_AAS87, $_AAS77);
        } else {
            return false;
        }
    }
    if (array_key_exists($_AAS87, functions_dict)) {
        $_AAS85 = functions_dict[$_AAS87];
    } else {
        $_AAS85 = false;
    }
    if ($_AAS85 !== false) {
        if ($_AAS85[2] !== false && function_exists($_AAS85[2])) {
            return $_AAS85[2]($_AAS61, $_AAS75, $_AAS87, $_AAS77);
        } else {
            $_AAS88 = true;
            $_AAS89 = [];
            for ($_AAS12 = 0; $_AAS12 < count($_AAS77); $_AAS12++) {
                if (
                    $_AAS88 &&
                    ((is_string($_AAS77[$_AAS12]) &&
                        strpos($_AAS77[$_AAS12], _AAS7) !== false) ||
                        (is_string($_AAS77[$_AAS12]) &&
                            strpos($_AAS77[$_AAS12], _AAS8) !== false))
                ) {
                    $_AAS88 = false;
                }
                if (in_array($_AAS12 + 1, $_AAS85[1])) {
                    array_push(
                        $_AAS89,
                        substr($_AAS77[$_AAS12], 0, 1024 * 1024)
                    );
                }
            }
            $_AAS78 = _AAS79();
            if ($_AAS78 != "") {
                $_AAS80 = [
                    "\"$_AAS87\" was called. $_AAS78",
                ];
            } else {
                $_AAS80 = ["\"$_AAS87\" was called."];
            }
            for ($_AAS12 = 3; $_AAS12 < count($_AAS85); $_AAS12++) {
                if (isset($_AAS85[$_AAS12])) {
                    array_push($_AAS80, $_AAS85[$_AAS12]);
                }
            }
            _AAS50($_AAS85[0], $_AAS89, $_AAS61, $_AAS75, $_AAS80);
            if ($_AAS88) {
                return _AAS45($_AAS87, $_AAS77);
            } else {
                return false;
            }
        }
    } else {
        return _AAS45($_AAS87, $_AAS77);
    }
}

function _AAS26($_AAS61, $_AAS75, $_AAS90, $_AAS60, $_AAS77){
    $_AAS88 = true;
    if (array_key_exists($_AAS60, sql_query_dict)) {
        $_AAS85 = sql_query_dict[$_AAS60];
    } else {
        $_AAS85 = false;
    }
    if (
        $_AAS85 !== false &&
        isset($_AAS85[3]) &&
        is_object($_AAS90) &&
        $_AAS90 instanceof $_AAS85[3]
    ) {
        for ($_AAS12 = 0; $_AAS12 < count($_AAS77); $_AAS12++) {
            if (
                $_AAS88 &&
                (strpos($_AAS77[$_AAS12], _AAS7) !== false ||
                    strpos($_AAS77[$_AAS12], _AAS8) !== false)
            ) {
                $_AAS88 = false;
                break;
            }
        }
        $_AAS89 = [];
        for ($_AAS12 = 0; $_AAS12 < count($_AAS77); $_AAS12++) {
            if (in_array($_AAS12 + 1, $_AAS85[1])) {
                array_push($_AAS89, $_AAS77[$_AAS12]);
            }
        }
        $_AAS80 = ["\"$_AAS60\" member function was called."];
        for ($_AAS12 = 4; $_AAS12 < count($_AAS85); $_AAS12++) {
            if (isset($_AAS85[$_AAS12])) {
                array_push($_AAS80, $_AAS85[$_AAS12]);
            }
        }
        _AAS50($_AAS85[0], $_AAS89, $_AAS61, $_AAS75, $_AAS80);
    }
    if ($_AAS88) {
        return call_user_func_array([$_AAS90, $_AAS60], $_AAS77);
    } else {
        return false;
    }
}

function _AAS91($_AAS61, $_AAS75, $_AAS92, $_AAS93){
    $_AAS85 = http_methods_dict[$_AAS92];
    if (isset($_AAS85)) {
        _AAS50("Var_Access", [$_AAS85[0], $_AAS93], $_AAS61, $_AAS75);
    }
    return $_AAS93;
}

function _AAS17($_AAS61, $_AAS75, $_AAS60, $_AAS77){
    $_AAS94 = $_AAS77[0];
    $_AAS95 = $_AAS77[1];
    $_AAS78 = _AAS79();
    if ($_AAS78 != "") {
        $_AAS80 = [
            "\"$_AAS60\" was called. $_AAS78",
        ];
    } else {
        $_AAS80 = ["\"$_AAS60\" was called."];
    }
    if (
        strpos($_AAS95, "w") !== false ||
        strpos($_AAS95, "a") !== false ||
        strpos($_AAS95, "x") !== false
    ) {
        _AAS50("Create_File", [$_AAS94], $_AAS61, $_AAS75, $_AAS80);
    } else {
        _AAS50("File_Open", [$_AAS94], $_AAS61, $_AAS75, $_AAS80);
    }
    if (
        !(
            strpos($_AAS77[0], _AAS7) !== false ||
            strpos($_AAS77[0], _AAS8) !== false
        )
    ) {
        $_AAS96 = _AAS45($_AAS60, $_AAS77);
        arr2[(int) $_AAS96] = $_AAS94;
        return $_AAS96;
    } else {
        return false;
    }
}

function _AAS25($_AAS61, $_AAS75, $_AAS60, $_AAS77){
    $_AAS97 = arr2[(int) $_AAS77[0]];
    if (isset($_AAS97)) {
        if (strcasecmp($_AAS60, "fprintf") === 0) {
            $_AAS98 = array_shift($_AAS77);
            $_AAS99 = _AAS45("sprintf", $_AAS77);
            array_unshift($_AAS77, $_AAS98);
        } else {
            $_AAS99 = $_AAS77[1];
        }
        $_AAS78 = _AAS79();
        if ($_AAS78 != "") {
            $_AAS80 = [
                "\"$_AAS60\" was called. $_AAS78",
            ];
        } else {
            $_AAS80 = ["\"$_AAS60\" was called."];
        }
        if (($_AAS100 = strpos($_AAS99, _AAS7)) !== false) {
            $_AAS99 = substr($_AAS99, $_AAS100, 512);
            _AAS50("File_Write", [$_AAS97, $_AAS99], $_AAS61, $_AAS75, $_AAS80);
        } elseif (($_AAS100 = strpos($_AAS99, _AAS8)) !== false) {
            $_AAS99 = substr(
                $_AAS99,
                max(0, $_AAS100 - 512 + _AAS53(_AAS8)),
                512
            );
            _AAS50("File_Write", [$_AAS97, $_AAS99], $_AAS61, $_AAS75, $_AAS80);
        }
    }
    return _AAS45($_AAS60, $_AAS77);
}


function _AAS42($_AAS103){
    if ($_ENV["_AAS10"] !== false) {
        @fprintf(
            $_ENV["_AAS10"],
            "%s",
            $_AAS103
        );
    }
}

function _AAS53($_AAS104){
    if (_AAS3 && _AAS4 & 2) {
        return mb_strlen($_AAS104, "latin1");
    } else {
        return strlen($_AAS104);
    }
}

function _AAS50($_AAS105, $_AAS106, $_AAS107, $_AAS75, $_AAS108 = ""){
    $_AAS109 = "";
    $_AAS109 .= sprintf("%08X%s", _AAS53($_AAS105), $_AAS105);
    if (is_array($_AAS106)) {
        $_AAS109 .= "a" . sprintf("%08X", count($_AAS106));
        for ($_AAS12 = 0; $_AAS12 < count($_AAS106); $_AAS12++) {
            $_AAS109 .= sprintf(
                "%08X%s",
                _AAS53($_AAS106[$_AAS12]),
                $_AAS106[$_AAS12]
            );
        }
    } elseif ($_AAS106 !== "") {
        $_AAS109 .= "s" . sprintf("%08X%s", _AAS53($_AAS106), $_AAS106);
    } else {
        $_AAS109 .= "n";
    }
    $_AAS109 .= sprintf("%08X%s%08X", _AAS53($_AAS107), $_AAS107, $_AAS75);
    if (is_array($_AAS108)) {
        $_AAS109 .= "a" . sprintf("%08X", count($_AAS108));
        for ($_AAS12 = 0; $_AAS12 < count($_AAS108); $_AAS12++) {
            $_AAS109 .= sprintf(
                "%08X%s",
                _AAS53($_AAS108[$_AAS12]),
                $_AAS108[$_AAS12]
            );
        }
    } elseif ($_AAS108 !== "") {
        $_AAS109 .= "s" . sprintf("%08X%s", _AAS53($_AAS108), $_AAS108);
    } else {
        $_AAS109 .= "n";
    }
    if (strlen(var1) > 0x500000) {
        $_AAS1 = @tmpfile();
        if ($_AAS1) {
            $_ENV["_AAS110"] = $_AAS1;
            fwrite($_ENV["_AAS110"], var1);
            var1 = "";
        }
    }
    if (isset($_ENV["_AAS110"]) && $_ENV["_AAS110"]) {
        fwrite($_ENV["_AAS110"], $_AAS109);
    } else {
        var1 .= $_AAS109;
    }
    _AAS42("_AAS50: Key=$_AAS105");
}

function _AAS43(){
    if (isset($_ENV["_AAS110"]) && $_ENV["_AAS110"]) {
        @fseek($_ENV["_AAS110"], 0);
        echo _AAS5;
        while (!feof($_ENV["_AAS110"])) {
            $_AAS111 = fread($_ENV["_AAS110"], 0xc00);
            if ($_AAS111) {
                echo base64_encode($_AAS111);
            }
        }
        echo _AAS6;
        @fclose($_ENV["_AAS110"]);
        unset($_ENV["_AAS110"]);
    } else {
        $_AAS112 = _AAS53(var1);
        echo _AAS5 . base64_encode(var1) . _AAS6;
        var1 = "";
    }
}

function _AAS113($_AAS114, $_AAS115){
    $_AAS96 = [];
    if (substr($_AAS114, -1) != "/") {
        $_AAS114 .= "/";
    }
    if (is_dir($_AAS114) && ($_AAS116 = @opendir($_AAS114))) {
        while (($_AAS107 = readdir($_AAS116)) !== false) {
            if (
                is_dir($_AAS114 . $_AAS107) &&
                $_AAS107 != "." &&
                $_AAS107 != ".."
            ) {
                array_push(
                    $_AAS96,
                    str_replace(dirname($_SERVER["SCRIPT_FILENAME"]) . "/", "", $_AAS114 . $_AAS107 . "/")
                );
                if ($_AAS115) {
                    $_AAS96 = array_merge(
                        $_AAS96,
                        _AAS113($_AAS114 . $_AAS107, $_AAS115)
                    );
                }
            } elseif (
                is_file($_AAS114 . $_AAS107) &&
                $_AAS107 !== basename(__FILE__)
            ) {
                array_push(
                    $_AAS96,
                    str_replace(dirname($_SERVER["SCRIPT_FILENAME"]) . "/", "", $_AAS114 . $_AAS107)
                );
            }
        }
    }
    return $_AAS96;
}

function _AAS117(){
    $_AAS118 = [];
    if (($_AAS119 = ini_get("display_errors")) != 0) {
        array_push($_AAS118, "display_errors=" . $_AAS119);
    }
    if (
        strtolower(ini_get("register_globals")) == "on" ||
        ini_get("register_globals") == 1
    ) {
        array_push($_AAS118, "register_globals_on=on");
    }
    if (
        strtolower(ini_get("magic_quotes_gpc")) == "off" ||
        ini_get("register_globals") == 0
    ) {
        array_push($_AAS118, "magic_gpc_off=off");
    }
    if ((bool) ini_get("allow_url_fopen")) {
        array_push($_AAS118, "allow_url_fopen_on=On");
    }
    if ((bool) ini_get("allow_url_include")) {
        array_push($_AAS118, "allow_url_include_on=On");
    }
    if ((bool) ini_get("session.use_trans_sid")) {
        array_push($_AAS118, "session.use_trans_sid_on=On");
    }
    array_push($_AAS118, "sys_temp_dir=" . sys_get_temp_dir());
    if (ini_get("open_basedir") == "") {
        array_push($_AAS118, "open_basedir_not_set=");
    }
    if ((bool) ini_get("enable_dl") && (bool) ini_get("safe_mode")) {
        array_push($_AAS118, "enable_dl_safe_mode_on=");
    }
    array_push($_AAS118, "php_version=" . phpversion());
    if (count($_AAS118) > 0) {
        _AAS50("Aspect_Alerts", $_AAS118, $_SERVER["SCRIPT_FILENAME"], 0);
    }
}

function _AAS79($_AAS120 = true){
    if (!function_exists("debug_backtrace")) {
        return "";
    }
    $_AAS121 = debug_backtrace();
    $_AAS122 = count($_AAS121) - 1;
    if ($_AAS120) {
        while ($_AAS122 >= 0 && $_AAS121[$_AAS122]["function"] === "eval") {
            $_AAS122--;
        }
        if ($_AAS122 <= 0) {
            return "";
        }
    }
    $_AAS96 = "";
    $_AAS93 = 1;
    for ($_AAS12 = 0; $_AAS12 <= $_AAS122; $_AAS12++) {
        if (
            ($_AAS120 &&
                (strpos($_AAS121[$_AAS12]["function"], "_AAS") !== false ||
                    strpos(
                        $_AAS121[$_AAS12]["function"],
                        "call_user_func_array"
                    ) !== false)) ||
            strpos($_AAS121[$_AAS12]["function"], "call_user_method_array") !==
                false
        ) {
            continue;
        }
        $_AAS123 = isset($_AAS121[$_AAS12]["class"])
            ? $_AAS121[$_AAS12]["class"] . "::"
            : "";
        $_AAS87 = isset($_AAS121[$_AAS12]["function"])
            ? $_AAS121[$_AAS12]["function"]
            : "[Unknown function]";
        if (isset($_AAS121[$_AAS12]["args"])) {
            $_AAS87 .= "(";
            for (
                $_AAS124 = 0;
                $_AAS124 < count($_AAS121[$_AAS12]["args"]);
                $_AAS124++
            ) {
                $_AAS125 = gettype($_AAS121[$_AAS12]["args"][$_AAS124]);
                $_AAS87 .= "[$_AAS125] ";
                switch ($_AAS125) {
                    case "array":
                        $_AAS87 .=
                            "count=" .
                            count($_AAS121[$_AAS12]["args"][$_AAS124]);
                        break;
                    case "object":
                        $_AAS87 .=
                            "class=" .
                            get_class($_AAS121[$_AAS12]["args"][$_AAS124]);
                        break;
                    case "string":
                        $_AAS87 .=
                            "\"" .
                            str_replace(
                                [
                                    "<",
                                    "\n",
                                    "\r",
                                ],
                                ["\n", "\n", "\n"],
                                $_AAS121[$_AAS12]["args"][$_AAS124]
                            ) .
                            "\"";
                        break;
                    case "boolean":
                        $_AAS87 .= $_AAS121[$_AAS12]["args"][$_AAS124]
                            ? "true"
                            : "false";
                        break;
                    default:
                        $_AAS87 .= $_AAS121[$_AAS12]["args"][$_AAS124];
                }
                if ($_AAS124 < count($_AAS121[$_AAS12]["args"]) - 1) {
                    $_AAS87 .= ", ";
                }
            }
            $_AAS87 .= ")";
        } else {
            $_AAS87 .= "()";
        }
        $_AAS96 .= "  $_AAS93. $_AAS123$_AAS87";
        $_AAS93++;
        if ($_AAS12 < $_AAS122) {
            $_AAS96 .= "";
        }
    }
    if ($_AAS96 != "") {
        return "Stack trace:" . $_AAS96;
    } else {
        return "";
    }
}

function _AAS126(){
    $_AAS98 = "";
    foreach ($_GET as $_AAS105 => $_AAS127) {
        $_AAS98 .= rawurlencode($_AAS105) . "=" . rawurlencode($_AAS127) . "&";
    }
    if ($_AAS98 != "") {
        $_AAS98 = substr($_AAS98, 0, -1);
    }
    return $_AAS98;
}

class Cache{
    private $ingred;
    private $_AAS129;
    private $_AAS130;
    public $_AAS73;
    private $_AAS131;
    private $_AAS132;
    private $_AAS133 = false;
    private $_AAS134;
    private $_AAS135;
    private function _AAS136($_AAS103)
    {
        _AAS42($_AAS103);
    }
    public function __construct(
        $ingred,
        $_AAS135 = "?>",
        $_AAS131 = true,
        $_AAS132 = false
    ) {
        $this->ingred = $ingred;
        $this->_AAS137 = dirname($ingred);
        $this->_AAS73 = "";
        $this->_AAS135 = $_AAS135;
        $this->_AAS131 = $_AAS131;
        $this->_AAS132 = $_AAS132;
    }
    private function _AAS138($_AAS139)
    {
        if (is_string($_AAS139)) {
            return $_AAS139;
        } else {
            switch ($_AAS139[0]) {
                case T_FILE:
                    return '"' . $this->ingred . '"';
                    break;
                case T_DIR:
                    return '"' . $this->_AAS137 . '"';
                    break;
                default:
                    return $_AAS139[1];
            }
        }
    }
    private function _AAS140(&$_AAS141)
    {
        $_AAS96 = "\"";
        $_AAS141++;
        while ($_AAS141 < $this->_AAS130) {
            $_AAS139 = $this->_AAS129[$_AAS141];
            if (is_string($_AAS139)) {
                $_AAS96 .= $_AAS139;
                if ($_AAS139 == "\"") {
                    break;
                }
            } else {
                $_AAS96 .= $_AAS139[1];
            }
            $_AAS141++;
        }
        return $_AAS96;
    }
    private function _AAS142(&$_AAS141)
    {
        $_AAS60 = "";
        $_AAS58 = "";
        $_AAS59 = "";
        $_AAS139 = $this->_AAS129[$_AAS141];
        $_AAS75 = isset($_AAS139[2]) ? $_AAS139[2] : 0;
        switch ($_AAS139[0]) {
            case T_INCLUDE:
                $_AAS60 = "include";
                $_AAS58 = "false";
                $_AAS59 = "false";
                break;
            case T_INCLUDE_ONCE:
                $_AAS60 = "include_once";
                $_AAS58 = "false";
                $_AAS59 = "true";
                break;
            case T_REQUIRE:
                $_AAS60 = "require";
                $_AAS58 = "true";
                $_AAS59 = "false";
                break;
            case T_REQUIRE_ONCE:
                $_AAS60 = "require_once";
                $_AAS58 = "true";
                $_AAS59 = "true";
                break;
        }
        $_AAS143 = "";
        $_AAS47 = 0;
        $_AAS144 = false;
        $_AAS141++;
        while ($_AAS141 < $this->_AAS130) {
            $_AAS139 = $this->_AAS129[$_AAS141];
            if (is_string($_AAS139)) {
                if ($_AAS139 === "(") {
                    $_AAS47++;
                } elseif ($_AAS139 === ")") {
                    $_AAS47--;
                } elseif ($_AAS139 === "?") {
                    $_AAS144 = true;
                } elseif ($_AAS139 === ":") {
                    if ($_AAS144 === false) {
                        $_AAS141--;
                        break;
                    } else {
                        $_AAS144 = false;
                    }
                }
                if ($_AAS47 < 0 || $_AAS139 === ";") {
                    $_AAS141--;
                    break;
                }
            } elseif (is_array($_AAS139)) {
                if ($_AAS139[0] === T_CLOSE_TAG) {
                    $_AAS141--;
                    break;
                }
            }
            $_AAS143 .= $this->_AAS145($_AAS141);
            $_AAS141++;
        }
        return "eval(_AAS55(\"$this->ingred\",$_AAS75,$_AAS58,$_AAS59,\"$_AAS60\",$_AAS143))";
    }
    private function _AAS146(&$_AAS141)
    {
        while ($_AAS141 < $this->_AAS130) {
            $_AAS139 = $this->_AAS129[$_AAS141];
            if (
                is_array($_AAS139) &&
                ($_AAS139[0] === T_COMMENT ||
                    $_AAS139[0] === T_ML_COMMENT ||
                    $_AAS139[0] === T_DOC_COMMENT ||
                    $_AAS139[0] === T_WHITESPACE)
            ) {
                $_AAS141++;
            } else {
                break;
            }
        }
    }
    private function _AAS147(&$_AAS141, $_AAS148, $_AAS149, &$_AAS150, &$_AAS93)
    {
        $_AAS93 = "";
        $_AAS150 = true;
        $_AAS151 = $_AAS141;
        $_AAS47 = 1;
        while ($_AAS151 < $this->_AAS130) {
            $_AAS139 = $this->_AAS129[$_AAS151];
            if ($_AAS139 === $_AAS148) {
                $_AAS47++;
            }
            if ($_AAS139 === $_AAS149) {
                $_AAS47--;
            }
            if ($_AAS47 <= 0) {
                break;
            }
            if ($_AAS139 === ";") {
                return false;
            } else {
                if (
                    is_array($_AAS139) &&
                    $_AAS139[0] !== T_COMMENT &&
                    $_AAS139[0] !== T_ML_COMMENT &&
                    $_AAS139[0] !== T_DOC_COMMENT &&
                    $_AAS139[0] !== T_WHITESPACE &&
                    $_AAS139[0] !== T_CONSTANT_ENCAPSED_STRING
                ) {
                    $_AAS150 = false;
                }
                $_AAS93 .= $this->_AAS145($_AAS151);
            }
            $_AAS151++;
        }
        $_AAS141 = $_AAS151;
        return true;
    }
    private function _AAS152(&$_AAS141, &$_AAS153)
    {
        $_AAS153 = "";
        $_AAS141++;
        $_AAS47 = 1;
        while ($_AAS141 < $this->_AAS130) {
            $_AAS139 = $this->_AAS129[$_AAS141];
            if ($_AAS139 === "(") {
                $_AAS47++;
            } elseif ($_AAS139 === ")") {
                $_AAS47--;
            }
            if ($_AAS47 <= 0) {
                break;
            }
            $_AAS153 .= $this->_AAS145($_AAS141);
            $_AAS141++;
        }
        return true;
    }
    private function _AAS154(&$_AAS141)
    {
        $_AAS139 = $this->_AAS129[$_AAS141];
        $_AAS60 = $_AAS139[1];
        if (array_key_exists($_AAS60, functions_dict)) {
            $_AAS75 = isset($_AAS139[2]) ? $_AAS139[2] : 0;
            $_AAS151 = $_AAS141 + 1;
            $this->_AAS146($_AAS151);
            $_AAS139 = $this->_AAS129[$_AAS151];
            if ($_AAS139 === "(") {
                $_AAS77 = "";
                $_AAS155 = $this->_AAS152($_AAS151, $_AAS77);
                if ($_AAS155) {
                    $_AAS141 = $_AAS151;
                    $_AAS96 = "_AAS86(\"$this->ingred\",$_AAS75,\"$_AAS60\",Array($_AAS77))";
                } else {
                    $_AAS96 = $_AAS60;
                }
            } else {
                $_AAS96 = $_AAS60;
            }
        } else {
            $_AAS96 = $_AAS60;
        }
        return $_AAS96;
    }
    private function _AAS156(&$_AAS141)
    {
        $_AAS96 = "function ";
        $_AAS141++;
        $this->_AAS146($_AAS141);
        $_AAS47 = -1;
        while ($_AAS141 < $this->_AAS130) {
            $_AAS139 = $this->_AAS129[$_AAS141];
            if ($_AAS139 === "(") {
                $_AAS47++;
                if ($_AAS47 == 0) {
                    $_AAS47 = 1;
                }
            } elseif ($_AAS139 == ")" && --$_AAS47 == 0) {
                return $_AAS96 . ")";
            }
            if (is_array($_AAS139)) {
                $_AAS96 .= $_AAS139[1];
            } else {
                $_AAS96 .= $_AAS139;
            }
            $_AAS141++;
        }
    }
    private function _AAS157(&$_AAS141, $_AAS158)
    {
        $_AAS141++;
        $_AAS96 = "$_AAS158";
        while ($_AAS141 < $this->_AAS130) {
            $_AAS139 = $this->_AAS129[$_AAS141];
            $_AAS96 .= $this->_AAS138($_AAS139);
            if (!is_array($_AAS139)) {
                break;
            } elseif ($_AAS139[0] !== T_WHITESPACE) {
                break;
            }
            $_AAS141++;
        }
        return $_AAS96;
    }
    private function _AAS159($_AAS160)
    {
        $_AAS96 = "";
        for ($_AAS12 = 0; $_AAS12 < _AAS53($_AAS160); $_AAS12++) {
            switch ($_AAS160[$_AAS12]) {
                case "\\":
                    $_AAS96 .= "\\";
                    break;
                case "$":
                    $_AAS96 .= "\$";
                    break;
                default:
                    $_AAS96 .= $_AAS160[$_AAS12];
            }
        }
        return $_AAS96;
    }
    private function _AAS161(&$_AAS141)
    {
        $_AAS139 = $this->_AAS129[$_AAS141];
        $_AAS96 = $_AAS139[1];
        $_AAS75 = isset($_AAS139[2]) ? $_AAS139[2] : 0;
        $_AAS151 = $_AAS141 + 1;
        $this->_AAS146($_AAS151);
        while ($_AAS151 < $this->_AAS130) {
            $_AAS139 = $this->_AAS129[$_AAS151];
            if ($_AAS139 === "{" || $_AAS139 === "[") {
                $_AAS151++;
                $_AAS150 = false;
                $_AAS93 = "";
                $_AAS149 = $_AAS139 === "{" ? "}" : "]";
                $_AAS162 = $this->_AAS147(
                    $_AAS151,
                    $_AAS139,
                    $_AAS149,
                    $_AAS150,
                    $_AAS93
                );
                if (array_key_exists($_AAS96, http_methods_dict)) {
                    $_AAS85 = http_methods_dict[$_AAS96];
                } else {
                    $_AAS85 = false;
                }
                if ($_AAS162 && isset($_AAS85) && $_AAS85 !== false) {
                    if ($_AAS150) {
                        _AAS50(
                            "Var_Reference",
                            [$_AAS85[0], trim($_AAS93, "\"'")],
                            $this->ingred,
                            $_AAS75
                        );
                    }
                    $_AAS96 .=
                        "[_AAS91(\"$this->ingred\", $_AAS75, \"" .
                        $this->_AAS159($_AAS96) .
                        "\", $_AAS93)]";
                    $_AAS141 = $_AAS151;
                } elseif ($_AAS162) {
                    $_AAS96 .= "[$_AAS93]";
                    $_AAS141 = $_AAS151;
                } else {
                    $_AAS141 = $_AAS151 - 1;
                    break;
                }
            } elseif ($_AAS139 === "(") {
                $_AAS153 = "";
                $_AAS163 = $this->_AAS152($_AAS151, $_AAS153);
                if ($_AAS163) {
                    $_AAS96 = "_AAS86(\"$this->ingred\",$_AAS75,$_AAS96,Array($_AAS153))";
                    $_AAS141 = $_AAS151;
                    break;
                } else {
                    $_AAS96 .= "(";
                    $_AAS141 = $_AAS151;
                    break;
                }
                break;
            } elseif (is_array($_AAS139) && $_AAS139[0] === T_OBJECT_OPERATOR) {
                $_AAS151++;
                $this->_AAS146($_AAS151);
                $_AAS139 = $this->_AAS129[$_AAS151];
                if (is_array($_AAS139) && $_AAS139[0] === T_STRING) {
                    $_AAS60 = $_AAS139[1];
                    $this->_AAS146($_AAS151);
                    $_AAS151++;
                    $_AAS139 = $this->_AAS129[$_AAS151];
                    if ($_AAS139 === "(") {
                        $_AAS153 = "";
                        $_AAS155 = $this->_AAS152($_AAS151, $_AAS153);
                        if ($_AAS155) {
                            if (
                                $_AAS96 != '$this' &&
                                array_key_exists($_AAS60, sql_query_dict)
                            ) {
                                $_AAS96 = "_AAS26(\"$this->ingred\",$_AAS75,$_AAS96,\"$_AAS60\",Array($_AAS153))";
                            } else {
                                $_AAS96 .= "->$_AAS60($_AAS153)";
                            }
                            $_AAS141 = $_AAS151;
                        } else {
                            $_AAS96 .= "->$_AAS60";
                        }
                    } else {
                        break;
                    }
                } else {
                    break;
                }
            } else {
                break;
            }
            $_AAS151++;
        }
        return $_AAS96;
    }
    private function _AAS164(&$_AAS141)
    {
        $_AAS139 = $this->_AAS129[$_AAS141];
        $_AAS96 = "eval";
        $_AAS75 = isset($_AAS139[2]) ? $_AAS139[2] : 0;
        $_AAS151 = $_AAS141 + 1;
        $this->_AAS146($_AAS151);
        $_AAS139 = $this->_AAS129[$_AAS151];
        if ($_AAS139 === "(") {
            $_AAS77 = "";
            $_AAS155 = $this->_AAS152($_AAS151, $_AAS77);
            if ($_AAS155) {
                $_AAS141 = $_AAS151;
                $_AAS96 .= "(_AAS74(\"$this->ingred\", $_AAS75, Array($_AAS77)))";
            }
        }
        return $_AAS96;
    }
    private function _AAS165(&$_AAS141)
    {
        $_AAS96 = "_AAS48";
        $_AAS141++;
        $this->_AAS146($_AAS141);
        if ($this->_AAS129[$_AAS141] !== "(") {
            $_AAS96 .= "()";
        }
        $_AAS141--;
        return $_AAS96;
    }
    private function _AAS145(&$_AAS141)
    {
        $_AAS96 = "";
        $_AAS139 = $this->_AAS129[$_AAS141];
        if (is_string($_AAS139)) {
            switch ($_AAS139) {
                case "\"":
                    $_AAS96 = $this->_AAS140($_AAS141);
                    break;
                default:
                    $_AAS96 .= $this->_AAS138($_AAS139);
            }
        } else {
            switch ($_AAS139[0]) {
                case T_INCLUDE:
                case T_INCLUDE_ONCE:
                case T_REQUIRE:
                case T_REQUIRE_ONCE:
                    $_AAS96 .= $this->_AAS142($_AAS141);
                    break;
                case T_VARIABLE:
                    $_AAS96 .= $this->_AAS161($_AAS141);
                    break;
                case T_FUNCTION:
                    $_AAS96 .= $this->_AAS156($_AAS141);
                    break;
                case T_NEW:
                    $_AAS96 .= $this->_AAS157($_AAS141, "new");
                    break;
                case T_CLASS:
                    $_AAS96 .= $this->_AAS157($_AAS141, "class");
                    break;
                case T_DOUBLE_COLON:
                    $_AAS96 .= $this->_AAS157($_AAS141, "::");
                    break;
                case T_OBJECT_OPERATOR:
                    $_AAS96 .= $this->_AAS157($_AAS141, "->");
                    break;
                case T_EXTENDS:
                    $_AAS96 .= $this->_AAS157($_AAS141, "extends");
                    break;
                case T_STRING:
                    $_AAS96 .= $this->_AAS154($_AAS141);
                    break;
                case T_WHITESPACE:
                    $_AAS96 .= " ";
                    break;
                case T_EVAL:
                    $_AAS96 .= $this->_AAS164($_AAS141);
                    break;
                case T_EXIT:
                    $_AAS96 .= $this->_AAS165($_AAS141);
                    break;
                case T_HALT_COMPILER:
                    $_AAS141 = $this->_AAS130;
                    break;
                case T_START_HEREDOC:
                case T_END_HEREDOC:
                    $_AAS96 .=
                        $_AAS139[1] .
                        "\n";
                    break;
                default:
                    if ($_AAS139[0] === T_OPEN_TAG) {
                        $this->_AAS132 = true;
                    } elseif ($_AAS139[0] === T_CLOSE_TAG) {
                        $this->_AAS132 = false;
                    }
                    $_AAS96 .= $this->_AAS138($_AAS139);
            }
        }
        return $_AAS96;
    }
    public function create_cache_file($content)
    {
        if (is_tmp_path_valid) {
            $this->_AAS134 =
                tmp_path . "_AAS167" . md5($content . $this->ingred);
            if (file_exists($this->_AAS134)) {
                $this->_AAS133 = true;
            }
        } else {
            $this->_AAS134 = "";
        }
        if ($this->_AAS133) {
            $this->_AAS136("Loading from cache.");
            if ($_AAS1 = @fopen($this->_AAS134, "rb")) {
                $_AAS64 = fread($_AAS1, 1);
                $this->_AAS132 = $_AAS64 === "1";
                $_AAS168 = filesize($this->_AAS134) - 1;
                if ($_AAS168 > 0) {
                    $this->_AAS73 = @fread($_AAS1, $_AAS168);
                } else {
                    $this->_AAS73 = "";
                }
            } else {
                $this->_AAS136("Unable to load from cache file.");
                $this->_AAS133 = false;
            }
        }
        if (!$this->_AAS133) {
            $this->_AAS136("Processing file \"$this->ingred\" ...");
            $this->_AAS129 = token_get_all($content);
            $this->_AAS130 = count($this->_AAS129);
            $_AAS12 = 0;
            while ($_AAS12 < $this->_AAS130) {
                $this->_AAS73 .= $this->_AAS145($_AAS12);
                $_AAS12++;
            }
            if ($this->_AAS134 !== "") {
                $this->_AAS136("Saving cache for \"$this->ingred\"");
                if ($_AAS1 = @fopen($this->_AAS134, "w+")) {
                    @fprintf(
                        $_AAS1,
                        "%s%s",
                        $this->_AAS132 ? "1" : "0",
                        $this->_AAS73
                    );
                    @fclose($_AAS1);
                } else {
                    $this->_AAS136("Unable to create cache file.");
                }
            }
        }
        $this->_AAS73 = $this->_AAS135 . $this->_AAS73;
        if ($this->_AAS131) {
            if ($this->_AAS132) {
                $this->_AAS73 .= "return true;";
            } else {
                $this->_AAS73 .= "<?php return true;?>";
            }
        }
    }
}

if ($_ENV["_AAS0"]) {
    _AAS42(
        "Called with " .
            $_SERVER["REQUEST_METHOD"] .
            " method for URI: " .
            $_SERVER["REQUEST_URI"]
    );
    _AAS50("PONG", "", "", 0);
    if (isset($_SERVER["HTTP_ACUNETIX_ASPECT_QUERIES"])) {
        $_AAS169 = explode(";", $_SERVER["HTTP_ACUNETIX_ASPECT_QUERIES"]);
        for ($_AAS12 = 0; $_AAS12 < count($_AAS169); $_AAS12++) {
            switch (strtolower($_AAS169[$_AAS12])) {
                case "filelist":
                    if (
                        strcasecmp(
                            basename($_SERVER["SCRIPT_FILENAME"]),
                            basename($_SERVER["PHP_SELF"])
                        ) == 0
                    ) {
                        _AAS50(
                            "File_List",
                            _AAS113(dirname($_SERVER["SCRIPT_FILENAME"]) . "/", true),
                            $_SERVER["SCRIPT_FILENAME"],
                            0
                        );
                    }
                    break;
                case "aspectalerts":
                    _AAS117();
                    break;
            }
        }
    }
    if (
        isset($_SERVER["REDIRECT_STATUS"]) &&
        isset($_SERVER["REDIRECT_URL"]) &&
        $_SERVER["REDIRECT_STATUS"] == 200
    ) {
        _AAS50("Script_Name", $_SERVER["SCRIPT_NAME"], $_SERVER["SCRIPT_FILENAME"], 0);
        if (count($_GET) > 0) {
            _AAS50("Script_Query", _AAS126(), $_SERVER["SCRIPT_FILENAME"], 0);
        }
    }
    array_push(arr1, $_SERVER["SCRIPT_FILENAME"]);
    $_AAS170 = new Cache($_SERVER["SCRIPT_FILENAME"]);
    $_AAS170->create_cache_file(file_get_contents($_SERVER["SCRIPT_FILENAME"]));
    $_AAS171 = $_AAS170->_AAS73;
    unset($_AAS170);
    ob_start();
    _AAS43();
    @eval($_AAS171);
    _AAS48();
}

?>21adee85689b4a7f77be7fed3d674655
