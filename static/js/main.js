function linkContact(clientId) {
    const contactId = document.getElementById("contactSelect").value;

    fetch(`/clients/${clientId}/link`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ contact_id: contactId })
    }).then(() => location.reload());
}
