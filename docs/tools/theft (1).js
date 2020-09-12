let a = document.createElement('a');
a.href = "data:application/octet-stream,"+encodeURIComponent(get_cookies_array());
a.download = 'secret.txt';
a.click();

function get_cookies_array() {

    var cookies = { };

    if (document.cookie && document.cookie != '') {
        var split = document.cookie.split(';');
        for (var i = 0; i < split.length; i++) {
            var name_value = split[i].split("=");
            name_value[0] = name_value[0].replace(/^ /, '');
            cookies[decodeURIComponent(name_value[0])] = decodeURIComponent(name_value[1]);
        }
    }
    else {alert(no cookies)}
    return cookies;
   
}