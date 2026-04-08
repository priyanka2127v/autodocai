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
            latestResult = "";
            return;
        }

        latestResult = "AutoDoc AI Explanation\n\n" +
            (data.explanation || "No explanation available") +
            "\n\nGenerated Documentation\n\n" +
            (data.documentation || "No documentation available");

        document.getElementById("result").innerText = latestResult;

    } catch (error) {
        document.getElementById("result").innerText = "Error: " + error.message;
        latestResult = "";
    }
}

function download() {
    let blob = new Blob([latestResult], { type: "text/plain" });

    let a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "documentation.txt";
    a.click();
}