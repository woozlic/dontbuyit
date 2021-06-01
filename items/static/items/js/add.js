let changeImage = function (event, targetImage) {
    let img3 = document.getElementById('img3'); // img tags
    let img2 = document.getElementById('img2');
    let img1 = document.getElementById('img1');
    let image1 = document.getElementById('image-1'); // file input form
    let image2 = document.getElementById('image-2');
    let image3 = document.getElementById('image-3');

    if (targetImage === 'img3'){
        if (img1.className==='image-input'){
            img1.src = URL.createObjectURL(event.target.files[0]);
            img1.className = 'image-input-active';
            document.getElementById('image-1').files=document.getElementById('image-3').cloneNode().files
            clearFileInput(image3);
        }
        else if (img2.className==='image-input'){
            img2.src = URL.createObjectURL(event.target.files[0]);
            img2.className = 'image-input-active';
            img2.innerHTML = '<span class="deleteClose">&times;</span>'
            document.getElementById('image-2').files=document.getElementById('image-3').cloneNode().files
            clearFileInput(image3);
        }
        else {
            img3.src = URL.createObjectURL(event.target.files[0]);
            img3.className = 'image-input-active';
            img3.innerHTML = '<span class="deleteClose">&times;</span>'
        }
    }
    else if (targetImage === 'img2'){
        if (img1.className==='image-input'){
            img1.src = URL.createObjectURL(event.target.files[0]);
            img1.className = 'image-input-active';
            document.getElementById('image-1').files=document.getElementById('image-2').cloneNode().files
            clearFileInput(image2);
        }
        else {
            img2.src = URL.createObjectURL(event.target.files[0]);
            img2.className = 'image-input-active';
        }
    }
    else {
        img1.src = URL.createObjectURL(event.target.files[0]);
        img1.className = 'image-input-active';
    }
    console.log(image1.files, image2.files, image3.files);
}
function clearFileInput(f)
{
    if(f.value){
        try{
            f.value = '';
        }catch(err){
        }
        if(f.value){
            let form = document.createElement('form'), ref = f.nextSibling;
            form.appendChild(f);
            form.reset();
            ref.parentNode.insertBefore(f,ref);
        }
    }
}