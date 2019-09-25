let is_updating = false;
let submit_form = function () {
    let keyword_form = document.getElementById('keyword_form');
    if (is_updating === false) {
        is_updating = true;
        console.log(is_updating);
        keyword_form.submit()
    }
    else(
        alert('請勿重複操作')
    )
};