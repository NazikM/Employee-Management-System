const openedClass = 'glyphicon-minus-sign';
const closedClass = 'glyphicon-plus-sign';

function clickHandler(e){
    if (this === e.target) {
        console.log(e.target)
        if($(this).has('ul').length){
            $(this).find('i').toggleClass(openedClass + " " + closedClass);
            $(this).children().children().toggle();
        }
        else{
            const fetch_url = `${url}/${this.getAttribute('emp_id')}`;
            $(this).find('i').toggleClass(openedClass + " " + closedClass);
            fetch(fetch_url)
                .then(response => response.text())
                .then(res => {
                    const temp = document.createElement("div");
                    temp.innerHTML = res;
                    const node = temp.firstElementChild;
                    if(!$(node).has('li').length){
                        console.log('empty')
                        $(this).find('i').remove()
                        $(this).append(document.createElement('ul'));
                    }
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