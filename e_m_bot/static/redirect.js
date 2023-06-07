function redirectWithParams() {
    // Get the data and information you want to pass to the new page
    var data1 = 'Hello';
    var data2 = 'World';

    // Construct the URL with the parameters
    var url = 'lessons.html?param1=' + encodeURIComponent(data1) + '&param2=' + encodeURIComponent(data2);

    // Redirect to the new page
    window.location.href = url;
}