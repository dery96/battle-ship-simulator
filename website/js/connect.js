{
  const sendButton = document.getElementById('sendButton');
  const answers = document.getElementById('answers');
  const fleetOne = {};
  const fleetTwo = {};

  const emptyFleetTest = (fleet) => {
    // if
    for (let [key, value] of Object.entries(fleet)) {
      if (!isNaN(value) && parseInt(value) > 0) {
        return false;
      }
    }
    return true;
  }

  const fleetFormToArray = (inputs) => {
    inputs.forEach((object) => {
      if (object.name.includes('one')) {
        fleetOne[object.name] = object.value;
      } else {
        fleetTwo[object.name] = object.value
      }
    })
  }

  const btnClick = () => {
    inputs = document.querySelectorAll("input");
    fleetFormToArray(inputs);
    if (!emptyFleetTest(fleetOne) && !emptyFleetTest(fleetTwo)) {
      data = new Object();
      data.fleetOne = fleetOne;
      data.fleetTwo = fleetTwo;
      sendFleetbyPostRequest(data);
    } else {
      answers.innerHTML = "<span class=\"buttonError\">To run simulation you must write ship numbers!</span>"
    }
  }

  const sendFleetbyPostRequest = (data) => {
    var headers = new Headers();
    headers.append('Accept', 'application/json');
    headers.append('Content-Type', 'application/json');
    fetch('http://localhost:5000/battle', {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      method: 'POST',
      body: JSON.stringify(data)
    }).then(resp => {
      answers.innerHTML = "Waiting for answer"
      return resp.json();
    }).then(resp => {
      resp.log = resp.log.replace(/\n/g,"<br>")
      resp.log = resp.log.replace(/> Round/g,"<span style='font-weight: bold;'> > Round </span>")
      resp.log = resp.log.replace(/One:/g,"<span style='color: #a92b29;font-weight: bold;'> One: </span>")
      resp.log = resp.log.replace(/Two:/g,"<span style='color: #283A4F;font-weight: bold;'> Two: </span>")
      answers.innerHTML = resp.log;
      console.log(resp);
    }).catch(err => {
      console.log(err);
    })
  }
  sendButton.addEventListener('click', btnClick, false);
}
