let changeImage = function (event, targetImage) {
    let image = document.getElementById(targetImage);
    let img3 = document.getElementById('img3'); // img tags
    let img2 = document.getElementById('img2');
    let img1 = document.getElementById('img1');

    let image1 = document.getElementById('image-1'); // file input form
    let image2 = document.getElementById('image-2');
    let image3 = document.getElementById('image-3');

    let temp1 = image1.files;
    let temp2 = image2.files;
    let temp3 = image3.files;

    console.log(image1.files, image2.files, image3.files);

    closeDelete = document.createElement('span');
    closeDelete.className = 'closeDelete';
    closeDelete.textContent = 'x';
    if (targetImage === 'img3'){
        if (img1.className==='image-input'){
            img1.src = URL.createObjectURL(event.target.files[0]);
            img1.className = 'image-input-active';
            document.getElementById('image-1').files=document.getElementById('image-3').files;
            document.getElementById('image-form-3').value = '';
            // clearFileInput('image-3');
        }
        else if (img2.className==='image-input'){
            img2.src = URL.createObjectURL(event.target.files[0]);
            img2.className = 'image-input-active';
            img2.innerHTML = '<span class="deleteClose">&times;</span>'
            image2.files=image3.files;
            // event.target.value = null;
            // clearFileInput('image-2');
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
            image1.files=image2.files;
            // event.target.value = null;
            // clearFileInput('image-2');
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

function clearFileInput(id)
{
    var oldInput = document.getElementById(id);

    var newInput = document.createElement("input");

    newInput.type = "file";
    newInput.id = oldInput.id;
    newInput.name = oldInput.name;
    newInput.className = oldInput.className;
    newInput.style.cssText = oldInput.style.cssText;
    // TODO: copy any other relevant attributes

    oldInput.parentNode.replaceChild(newInput, oldInput);
}