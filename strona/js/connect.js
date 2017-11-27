{
  const sendButton = document.getElementById('sendButton');
  const answers = document.getElementById('answers');
  const fleetOne = {};
  const fleetTwo = {};

  const emptyFleetTest = (fleet) => {
    let result = false;
    for (let [key, value] of Object.entries(fleet)) {
      if (parseInt(value, 10) != NaN && parseInt(value, 10) > 0) {
        return true;
      }
    }
    return false;
  }

  const testFleets = (inputs) => {
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
    testFleets(inputs);
    if (emptyFleetTest(fleetOne) && emptyFleetTest(fleetTwo)) {
      console.log(fleetOne, fleetTwo);
      answers.innerHTML = "Waiting for answer"
    } else {
      answers.innerHTML = "<span class=\"buttonError\">To run simulation you must write ship numbers!</span>"
    }
  }

  // sendFleetbyPostRequest() {
  //   var headers = new Headers();
  //   headers.append('Accept', 'application/json'); // This one is enough for GET requests
  //   headers.append('Content-Type', 'application/json'); // This one sends body
  //
  //   return fetch('localhost:8080/post/fleet', {
  //     method: 'POST',
  //     mode: 'same-origin',
  //     credentials: 'include',
  //     redirect: 'follow',
  //     headers: headers,
  //     body: JSON.stringify(fleetOne, fleetTwo)
  //   }).then(resp => {
  //     ...
  //   }).catch(err => {
  //     ...
  //   })
  // }
  sendButton.addEventListener('click', btnClick, false);
}
