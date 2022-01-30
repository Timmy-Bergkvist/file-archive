const file = document.getElementById("iconstyle");

var filename = args.get_fileName(file);
var type = filename.split(".")[1];
var row = args.get_row();
var span = $(row).find(".ruFileWrap .ruUploadProgress");
if (type == "jpg") {
    span.text("").append("<img class='iconstyle' src='../Images/Pic1.png' />" + filename);
}
else if (type == "pdf") {
    span.text("").append("<img class='iconstyle' src='../Images/Pic2.png' />" + filename);
}
else if (type == "xml") {
    span.text("").append("<img class='iconstyle' src='../Images/Pic3.png' />" + filename);
}
