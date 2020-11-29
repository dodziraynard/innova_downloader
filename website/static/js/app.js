const linksDiv = document.querySelector("#download-links")
const loading = document.querySelector("#link-loading")


document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault();
    const params = new FormData(e.target);
    url = e.target.getAttribute("action")
    loading.style.display = "block";
    linksDiv.innerHTML = "";

    fetch(url, {
        method: 'post',
        body: params,
    })
        .then(res => {
            loading.style.display = "none";
            res.text().then(function (text) {
                linksDiv.innerHTML = text;
            });
        }).catch(err => {
            loading.style.display = "none";
            alert(err.message)
            console.log(err)
        })
})

function submitForm() {
    if (document.querySelector("form").checkValidity()) {
        document.querySelector("#get_link").click()
    }
}