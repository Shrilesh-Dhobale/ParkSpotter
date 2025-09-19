document.getElementById('vehicleEntryform').addEventListener('submit', function(e) {
    e.preventDefault();
    const plateNumber = document.getElementById('plateNumber').value;
    const entryTime = document.getElementById('entryTime').value;
    const isPaid = document.getElementById('isPaid').checked;
    const selectedVehicle = document.querySelector('input[name="vehicleType"]:checked');
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    // Frontend validation
    if (!plateNumber.trim()) {
        alert('Please enter a plate number');
        return;
    }

    if (!selectedVehicle) {
        alert('Please select a vehicle type');
        return;
    }

    if (!entryTime) {
        alert('Please select an entry time');
        return;
    }

    const formData = {
        plateNumber: plateNumber.trim(),
        vehicleType: selectedVehicle.value,
        entryTime: entryTime,
        isPaid: isPaid
    };

    fetch('new_entry/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.entry_id) {
            window.location.href = `/recipt/${data.entry_id}/`;
        } else {
            alert('Error creating entry');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while creating the entry.');
    });
});