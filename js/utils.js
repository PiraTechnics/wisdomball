async function loadWisdom() {
    
    let textFile = await fetch("wisdom.txt");
    let wisdomLines = await (await textFile.text()).split("\n");

    let randomIndex = Math.floor(Math.random() * wisdomLines.length);

    document.getElementById("wisdom").innerHTML = wisdomLines[randomIndex];
  }