var saveData = (function () {
    console.log("YEHOW")
    var a = document.createElement('a');
    document.body.appendChild(a);
    a.style = "display: none";
    return function (data, fileName){
        var json = JSON.stringify(data),
            blob = new Blob([json], {type: 'octet/stream'}),
            url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = fileName;
        a.name = dwBlob;
        a.click();
        window.URL.revokeObjectURL(url);
    };
}());

var data = { x: 42, s: "hello, world", d: new Date() },
    fileName = "downloady2.json";

saveData(data,fileName)