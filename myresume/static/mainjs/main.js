
    // Get all dropdown elements
    var dropdowns = document.getElementsByClassName("dropdown");

    // Loop through all dropdowns to bind click event
    for (let i = 0; i < dropdowns.length; i++) {
        dropdowns[i].addEventListener('click', function() {
            var dropdownContent = this.children[1]; // The dropdown-content is the second child of dropdown
            if (dropdownContent.style.display === "none") {
                dropdownContent.style.display = "block";
            } else {
                dropdownContent.style.display = "none";
            }
        });
    }

