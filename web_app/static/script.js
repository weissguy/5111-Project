const audioVersions = {
    h2o: [0, 1, 2], // Water has 3 audio versions
    h2: [0],      // Hydrogen has 2 audio versions
    co2: [0, 1, 2,3],  // Carbon Dioxide has 3 audio versions
    c2h4: [0, 1,2,3,4,5,6,7,8,9,10,11]     // Ethene has 2 audio versions
};

// Function to update the audio version dropdown based on selected molecule
function updateAudioVersionOptions(molecule) {
    const audioVersionDropdown = document.getElementById('audio-version');
    // Clear existing options
    audioVersionDropdown.innerHTML = '';

    // Get the list of available versions for the selected molecule
    const availableVersions = audioVersions[molecule] || [];

    // Add new options to the dropdown
    availableVersions.forEach(version => {
        const option = document.createElement('option');
        option.value = version;
        option.textContent = `Vibration ${version + 1}`; // Display as Version 1, 2, 3, etc.
        audioVersionDropdown.appendChild(option);
    });
}

// Event listener for the Submit button
document.getElementById('submit-btn').addEventListener('click', () => {
    const selectedMolecule = document.getElementById('molecule').value;

    if (!selectedMolecule) {
        alert('Please select a molecule before proceeding.');
        return;
    }

<<<<<<< HEAD
    // Update the audio version options based on the selected molecule
    updateAudioVersionOptions(selectedMolecule);

    // Display the audio version selector
    const audioSelector = document.getElementById('audio-selector');
    audioSelector.style.display = 'block';

    // Store the selected molecule for later use
    sessionStorage.setItem('selectedMolecule', selectedMolecule);
});

// Add event listener for the 'Play Audio' button
document.getElementById('play-btn').addEventListener('click', () => {
    const selectedMolecule = sessionStorage.getItem('selectedMolecule');

    // Get the selected version from the dropdown
    const selectedVersion = document.getElementById('audio-version').value;

    if (!selectedMolecule) {
        alert('Please select a molecule first.');
        return;
    }

    // Construct the image path
    const imagePath = `../static/gifs/${selectedMolecule}_${selectedVersion}.gif`; // Adjust according to your file names
=======
    //const imagePath = `../static/pngs/${selectedMolecule}.png`
    const imagePath = `../static/gifs/${selectedMolecule}_0.gif`
>>>>>>> 4dfe7031c3be9797978a7160523121b50ab6f912
    const imageElement = document.getElementById('molecule-image');
    imageElement.src = imagePath;
    imageElement.style.display = 'block';

    // Construct the audio file path based on selected molecule and version
    const audioPath = `../static/mp3_files/${selectedMolecule}_${selectedVersion}.mp3`;
    console.log(`Playing audio from: ${audioPath}`);

    // Play the selected audio version
    const audioElement = new Audio(audioPath);
    audioElement.load();
    audioElement.play().catch(error => {
        console.error('Error playing the audio:', error);
    });
});

// // Function to update the audio version dropdown based on selected molecule
// function updateAudioVersionOptions(molecule) {
//     const audioVersionDropdown = document.getElementById('audio-version');
//     // Clear existing options
//     audioVersionDropdown.innerHTML = '';

//     // Get the list of available versions for the selected molecule
//     const availableVersions = audioVersions[molecule] || [];

//     // Add new options to the dropdown
//     availableVersions.forEach(version => {
//         const option = document.createElement('option');
//         option.value = version;
//         option.textContent = `Vibration ${version + 1}`; // Display as Version 1, 2, 3, etc.
//         audioVersionDropdown.appendChild(option);
//     });
// }


// document.getElementById('submit-btn').addEventListener('click', () => {

//     const selectedMolecule = document.getElementById('molecule').value;

//     if (!selectedMolecule) {
//         alert('Please select a molecule before loading the image.');
//         return;
//     }

//     updateAudioVersionOptions(selectedMolecule);

//     // Display the audio version selector
//     const audioSelector = document.getElementById('audio-selector');
//     audioSelector.style.display = 'block';

//     // Store the selected molecule for later use
//     sessionStorage.setItem('selectedMolecule', selectedMolecule);
// });

//     //const imagePath = `../static/pngs/${selectedMolecule}.png`
//     const imagePath = `../static/gifs/${selectedMolecule}_1.gif`;
//     const imageElement = document.getElementById('molecule-image');
//     const audioPath = `../static/mp3_files/${selectedMolecule}_0.mp3`;
//     console.log(audioPath);
//     imageElement.src = imagePath;
//     imageElement.style.display = 'block';

//     const audioElement = new Audio(audioPath);
//     audioElement.load();
//     audioElement.play().catch(error => {
//         console.error('Error playing the audio:', error);
//     });
// });
