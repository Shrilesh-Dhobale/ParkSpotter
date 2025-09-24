document.getElementById('vehicleEntryform').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // --- This part is the same ---
    const plateNumber = document.getElementById('plateNumber').value;
    const entryTime = document.getElementById('entryTime').value;
    const isPaid = document.getElementById('isPaid').checked;
    const selectedVehicle = document.querySelector('input[name="vehicleType"]:checked');
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    if (!plateNumber.trim() || !selectedVehicle || !entryTime) {
        alert('Please fill out all required fields.');
        return;
    }

    const formData = {
        plateNumber: plateNumber.trim(),
        vehicleType: selectedVehicle.value,
        entryTime: entryTime,
        isPaid: isPaid
    };
    
    // --- This fetch block is NEW and IMPROVED ---
    fetch('/new_entry/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        // Check if the response from the server is an error (like 403, 404, 500)
        if (!response.ok) {
            // If it's an error, we'll try to get the error message from Django's response
            // and then throw an error to be caught by the .catch() block below.
            return response.json().then(errorData => {
                throw new Error(errorData.error || `Server responded with status ${response.status}`);
            });
        }
        // If the response is OK (200-299), parse the JSON as normal
        return response.json();
    })
    .then(data => {
        // This part runs only on a successful response
        if (data.entry_id) {
            // Paid entry, redirect to receipt
            window.location.href = `/receipt/${data.entry_id}/`;
        } else if (data.success) {
            // Unpaid entry, show success message and reload
            alert(data.message);
            window.location.reload();
        } else {
            // Handle other success cases if any
            alert('Entry added, but an issue occurred.');
        }
    })
    .catch(error => {
        // This .catch() block will now display the SPECIFIC error
        console.error('Error:', error);
        alert(`Request Failed: ${error.message}`);
    });
});