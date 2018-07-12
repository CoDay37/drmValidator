
blobtoData('blob:https://www.discovery.com/1b06ca34-2229-450f-9bcb-7700a3e2dad3')

function blobtoData(blob, callback){
    var a = new window.FileReader();
    a.onload = function(e) {callback(e.target.result);}
    a.readAsDataURL(blob)
}

function dataToBlob(dataurl){
    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
        while(n--){
            u8arr[n] = bstr.charCodeAt(n);
        }
        return new Blob([u8arr], {type:mime})
}

var blob = dataToBlob('data:text/plain;base64,YWFhYWFhYQ==')