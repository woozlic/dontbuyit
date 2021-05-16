function toggle_visibility(id) {
    let categories = document.getElementsByClassName('dropdown-shift');
    let e = document.getElementById(id);
    for (let category of categories){
        if (category === e)
            continue;
        else
            category.style.display = 'none'
    }
    if (e.style.display === 'block')
        e.style.display = 'none';
    else
        e.style.display = 'block'
}