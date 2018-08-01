var video = document.getElementsByName('edge-player-content-element');

blobUtil.imgSrcToBlob(video.src).then(function(blob) {
    var blobUrl = blobUtil.createObjectURL(blob);
    var newVid = document.createElement('video');
    newVid.src = blobURL;
    video.parentNode.appendChild(newVid)
})
//Web uses xhr.send() and xhr.response
//Dom using URL.createobjectURL and fr.readAsDataUrl()
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function(){
    if(this.readyState == 4 && this.status == 200){
        document.getElementsByClassName('edge-player-content-element').innerHTML = xttp.responseText;
    }
};
xhttp.open('GET',url)
var reader = new FileReader();
reader.addEventListener('loadend',function(){
})
//Fetching a blob and converting to base24
export const fetchAsBlob = url => fetch(url)
    .then(response => response.blob())
export const convertBlobToBase64 = blob => new Promise((resolve,reject)=>{
    const reader = new FileReader;
    reader.onerror = reject;
    reader.onload = () =>{
        resolve(reader.result);
    };
    reader.readAsDataURL(blob);
});