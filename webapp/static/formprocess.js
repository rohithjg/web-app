/*function output() {
    alert('Get it sooner, read well')
    var x;
    x = document.getElementById("myform");
    a = x.elements["firstname"].value;
    b = x.elements["lastname"].value;
    c = x.elements["companyname"].value;
    d = x.elements["notes"].value;
    document.write("Firstname: ",a);
    document.write(b);
    document.write(c);
    document.write(d);
}
function cancel(){
    alert('Cancelled')
}*/

function output() {
    var get_field = document.getElementById("myform");
    var data = {Firstname:get_field.elements["firstname"].value, Lastname:get_field.elements["lastname"].value,Companyname:get_field.elements["companyname"].value,Notes:get_field.elements["notes"].value};
    document.write(data.Firstname,data.Lastname,data.Companyname,data.Notes);
    console.log(data);
}
function cancel(){
    alert('Cancelled')
}



