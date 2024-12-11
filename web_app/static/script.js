document.getElementById('submit-btn').addEventListener('click', () => {

    const selectedMolecule = document.getElementById('molecule').value;

    if (!selectedMolecule) {
        alert('Please select a molecule before loading the image.');
        return;
    }

    //const imagePath = `../static/pngs/${selectedMolecule}.png`
    const imagePath = `../static/gifs/${selectedMolecule}_0.gif`
    const imageElement = document.getElementById('molecule-image');
    imageElement.src = imagePath;
    imageElement.style.display = 'block';

});
