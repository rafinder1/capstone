document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#btn-compose-project').addEventListener('click', empty_layout_create);

    //  "More Information"
    const btnsMoreInfo = document.querySelectorAll('.btn-more-info');
    btnsMoreInfo.forEach((btn) => {
    btn.addEventListener('click', () => {
        const projectDiv = btn.closest('.modal-body');

        const additionalInfo = projectDiv.querySelector('.additional-info');

        if (additionalInfo.style.display === 'none') {
            additionalInfo.style.display = 'block';
        } else {
            additionalInfo.style.display = 'none';
        }
    });
});
});
function display_details () {

}

function empty_layout_create() {
    formContainer = document.querySelector('#form-container-compose-project');

    var formHTML = `

        <div class="container" id="add-form">
            <form>
                <hr>
                <div class="form-group">
                    <input class="form-control" id="title" placeholder="Title">
                </div>
                <div class="form-group">
                    <input class="form-control" id="author" placeholder="Author">
                </div>
                <div class="form-group">
                    <input class="form-control" id="description" placeholder="Description">
                </div>
                <div class="form-group">
                    <input class="form-control" id="requirements" placeholder="Requirements">
                </div>
                <div class="form-group">
                    <input class="form-control" id="technology" placeholder="Technology">
                </div>
                <div class="form-group">
                    <input class="form-control" id="video" placeholder="Video">
                </div>
                <hr>
                <div>
                    <button type='button' class='btn btn-success' id='save-project'>Save Project</button>
                    <button type='button' class='btn btn-danger' id='break-add-project'>Close</button>
                </div>
            </form>
        </div>
    `;

    formContainer.innerHTML = formHTML;

    document.querySelector('#save-project').onclick = () => {
        save_project();
    };

    document.querySelector('#break-add-project').onclick = () => {
        close_element("#add-form");
    };

}

function save_project() {
    const title = document.querySelector('#title').value;
    const author = document.querySelector('#author').value;
    const description = document.querySelector('#description').value;
    const requirements = document.querySelector('#requirements').value;
    const technology = document.querySelector('#technology').value;
    const video = document.querySelector('#video').value;

    const csrfToken = getCookie('csrftoken');

    fetch(`create`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            title: title,
            author: author,
            description: description,
            requirements: requirements,
            technology: technology,
            video: video,
        })
    })
    .then(response => {
        formContainer.innerHTML = `
        <div class="alert alert-success" id="success-alert" style="display: block">
            Project added successfully!
        <button id="btn-close" type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true"><i class="lni lni-cross-circle"></i></span>
        </button>
        </div>`;

        document.querySelector(`#btn-close`).onclick = () => {
            close_element("#success-alert");
    };
    })
    .catch(error => {
        console.error('Error:', error);
    });


}

function close_element(id) {
    const element = document.querySelector(id);
    element.style.display = 'none';
}

// Function to retrieve the CSRF token from the cookie
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
}