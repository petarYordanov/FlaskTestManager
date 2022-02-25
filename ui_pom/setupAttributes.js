
var table = document.getElementsByClassName("table")[0];
for (var i = 0, row; row = table.rows[i]; i++) {
    for (var j = 0, col; col = row.cells[j]; j++) {
        var userDetails = row.innerText.split('	');
        console.log(userDetails);
        row.setAttribute("firstName", userDetails[0]);
        row.setAttribute("lastName", userDetails[1]);
        row.setAttribute("date", userDetails[2]);
        if (col.hasChildNodes()) {
            var elem = col.firstChild;
            var sibling = elem.nextElementSibling;
            if (sibling) {
                var oncatrr = sibling.getAttribute('onclick');
                if (oncatrr != null) {
                    var id = oncatrr.match(/(\d+)/);
                    row.setAttribute("id", id[0]);
                    console.log(id[0]);
                }
            }
        }
    }
}
