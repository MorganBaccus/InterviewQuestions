import React from "react"

function Time() {
  const date = new Date(2018, 6, 31, 15)
  const hours = date.getHours()
  let timeOfDay
  const styles = {
    fontSize: '25px'
  }
  
  if (hours < 12) {
    timeOfDay = "morning"
    styles.backgroundColor = "yellow"
  } else if (hours >= 12 && hours < 17) {
    timeOfDay = "afternoon"
    styles.backgroundColor = "blue"
  } else {
    timeOfDay = "night"
    styles.backgroundColor = "darkblue"
  }
  
  return (
    <h1 style={styles}>Good {timeOfDay}!</h1>
    )
  }

  export default Time