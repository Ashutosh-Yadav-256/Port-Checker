document.getElementById("scanForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let targetIp = document.getElementById("targetIp").value;
    let startPort = document.getElementById("startPort").value;
    let endPort = document.getElementById("endPort").value;

    fetch("/scan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ targetIp, startPort, endPort })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("scanResults").innerHTML = 
            data.open_ports.length > 0
            ? `<p>Open Ports: ${data.open_ports.join(", ")}</p>`
            : "<p>No open ports found.</p>";
    })
    .catch(error => console.error("Error:", error));
});
