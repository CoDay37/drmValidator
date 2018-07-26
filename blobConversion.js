var video = document.getElementsByName('edge-player-content-element');

blobUtil.imgSrcToBlob(video.src).then(function(blob) {
    var blobUrl = blobUtil.createObjectURL(blob);

    var newVid = document.createElement('video');
    newVid.src = blobURL;

    video.parentNode.appendChild(newVid)
})

//Downloading a blob: 
function getBlob(url, cb){
    var r = new XMLHttpRequest();
    r.open('GET', url);
    //or use array buffer
    r.responseType = 'blob' 
    r.send(null);
    r.onload = function(){
        if (cb) cb(r.response);
    }
}

//Web uses xhr.send() and xhr.response
//Dom using URL.createobjectURL and fr.readAsDataUrl()