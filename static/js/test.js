const openedClass = 'glyphicon-minus-sign';
const closedClass = 'glyphicon-plus-sign';

function clickHandler(e){
    if (this === e.target) {
        console.log(e.target)
        if($(this).has('ul').length){
            console.log(url)
            $(this).find('i').toggleClass(openedClass + " " + closedClass);
            $(this).children().children().toggle();
        }
        else{
            const fetch_url = `${url}/${this.getAttribute('emp_id')}`;
            console.log(fetch_url)
            $(this).find('i').toggleClass(openedClass + " " + closedClass);
            fetch(fetch_url)
                .then(response => response.text())
                .then(res => {
                    if(res === "<ul id=\"tree\">\n    \n</ul>"){
                        console.log('empty')
                        $(this).find('i').remove()
                        $(this).append(document.createElement('ul'));
                    }
                    const temp = document.createElement("div");
                    temp.innerHTML = res;
                    const node = temp.firstElementChild;
                    $(this).append(node);
                    for(let t of node.childNodes){
                        t.addEventListener('click', clickHandler)
                    }
                })
        }
    }
}

$('#tree').find('li').each(function () {
    $(this).on('click', clickHandler)
});