# Then obfuscation is more secure Solution

using online deobfuscation tools i got this code:
```
$(".c_submit").click(function () {
  var _0xf382x1 = $("#cpass").val();
  if (_0xf382x1 == "02l1alk3") {
    if (document.location.href.indexOf("?p=") == -1) {
      document.location = document.location.href + "?p=" + _0xf382x1;
    }
    ;
  } else {
    $("#cresponse").html("<div class='error'>Wrong password sorry.</div>");
  }
  ;
});
```
so, this is the password: `02l1alk3`

**Flag:** ***`FLAG-5PJne3T8d73UGv4SCqN44DXj`***
