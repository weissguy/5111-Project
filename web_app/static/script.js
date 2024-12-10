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
// document.getElementById('submit-btn').addEventListener('click', () => {
//     const selectedMolecule = document.getElementById('molecule').value;

//     // Fetch visualization
//     fetch('/api/generate', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ molecule: selectedMolecule })
//     })
//     .then(response => {
//         if (!response.ok) {
//             throw new Error('Failed to generate visualization');
//         }
//         return response.blob();
//     })
//     .then(imageBlob => {
//         const imageUrl = URL.createObjectURL(imageBlob);
//         const imgElement = document.getElementById('molecule-image');
//         imgElement.src = imageUrl;
//         imgElement.style.display = 'block';
//     })
//     .catch(error => console.error('Error generating visualization:', error));

//     // Fetch audio (sonification)
//     fetch('/api/generate', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ molecule: selectedMolecule })
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.audio_url) {
//             const audio = new Audio(data.audio_url);
//             audio.play();
//         } else {
//             console.error('Error:', data.error);
//         }
//     })
//     .catch(error => console.error('Error generating audio:', error));
// });
