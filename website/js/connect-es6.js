{
  const sendButton = document.getElementById('sendButton');
  const answers = document.getElementById('answers');
  sendButton.addEventlistener('click', buttonClick, false);

  const btnClick = (fleetOne, fleetTwo) => {
   if (!fleetOne.isEmpty() && !fleetTwo.isEmpty()) {
     // fetch().
     console.log("Fetch ja?");
   } else {
     answers.innerHTML = 'To run simulation you must write ship numbers!'
   }

 }

}()
