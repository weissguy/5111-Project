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
    })
    .catch(error => console.error('Error:', error));
});
