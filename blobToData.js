url = document.getElementsByTagName('video');
var a = document.createElement('a');
document.body.appendChild(a);
a.style = 'display: none';
a.href = url;
a.setAttribute("Download","button");
a.click();
window.URL.revokeObjectURL(url);