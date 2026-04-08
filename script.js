let latestResult = "";

async function analyze() {
    let code = document.getElementById("code").value;

    try {
        let res = await fetch("http://127.0.0.1:8001/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ code: code })
        });

        let data = await res.json();

        if (data.error) {
            document.getElementById("result").innerText = "Error: " + data.error;
            return;
        }

        latestResult = "AutoDoc AI Documentation\n\n" +
            "Functions:\n" + (data.functions || []).join("\n") +
            "\n\nExplanation:\n" + (data.explanation || "No explanation available");

        document.getElementById("result").innerText = latestResult;

    } catch (error) {
        document.getElementById("result").innerText = "Error: " + error.message;
    }
}

function download() {
    let blob = new Blob([latestResult], { type: "text/plain" });

    let a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "documentation.txt";
    a.click();
}