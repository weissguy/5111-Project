document.getElementById('submit-btn').addEventListener('click', () => {
    const selectedMolecule = document.getElementById('molecule').value;

    fetch('/api/data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ molecule: selectedMolecule })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').textContent = data.message;
        Jmol.setDocument(false);
        var myJmol = Jmol.getApplet("myJmol", {
            width: 400,
            height: 400,
            use: "HTML5",
            j2sPath: "https://chemapps.stolaf.edu/jmol/jsmol/j2s",
            script: "load file.cub;"
        });
    })
    .catch(error => console.error('Error:', error));
});
