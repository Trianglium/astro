

function getHoroscope(sign_name) {
    const URL = `https://aztro.sameerkumar.website/?sign=${sign_name}&day=today`;

    console.log(sign_name);
    console.log(URL);
    fetch(URL, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(json => {
        const date = json.current_date;
        const description = json.description;
        console.log(date, description);
    });
    console.log(json);
    return json;
}