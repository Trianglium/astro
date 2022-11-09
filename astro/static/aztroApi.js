

function getHoroscope(sign_name) {
    const URL = `https://aztro.sameerkumar.website/?sign=${sign_name}&day=today`;
    fetch(URL, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(json => {
        const date = json.current_date;
        const description = json.description;
        console.log(date, description);
    });

    return description
}